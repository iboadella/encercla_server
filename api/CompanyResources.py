from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models import UserModel,QuestionModel,SurveyModel,CompanyModel,SurveyCompanyModel,AnswerModel
from run import db
from flask import Flask, jsonify, request
from datetime import datetime
from pytz import timezone
import pytz
from run import app
import os
from shutil import copyfile
class Company(Resource):
     @jwt_required
     def get(self):
        user_id=request.args.get('user_id')

        user= UserModel.find_by_username(email=get_jwt_identity())
        if (user_id!=None and user.type_user!=1):
           return {'message': 'not authorized'}, 500
        if (user_id!=None):
            user=UserModel.find_by_id(id=user_id)

        results=[]

        company= CompanyModel.find_by_id(id=user.id_company)
        if (company==None):
            return {'id':''}
        else:
             #return jsonify(json_list = questions)
             return {
             "id":company.id,
            "sector": company.sector,
            "subsector" : company.subsector,
            "commercial_name" : company.commercial_name,
            "fiscal_name" : company.fiscal_name,
            "nif": company.nif,
            "number_survey":company.number_survey,
            "duplication_survey":company.duplication_survey,
            "name_surname":company.name_surname,
            "telephone_number":company.telephone_number,
            "description":company.description,
            "comarca":company.comarca,
            "territori_leader":company.territori_leader,
            "number_workers":company.number_workers}

class CompanyAll(Resource):
     @jwt_required
     def get(self):
        

        user= UserModel.find_by_username(email=get_jwt_identity())
        if (user.type_user!=1):
           return {'message': 'not authorized'}, 500


        results=[]

        items= CompanyModel.find_all()
        if (len(items)==0):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             for company in items:
                 results.append({
                    "id":company.id,
                    "sector": company.sector,
                    "subsector" : company.subsector,
                    "commercial_name" : company.commercial_name,
                    "fiscal_name" : company.fiscal_name,
                    "nif": company.nif,
                    "number_survey":company.number_survey,
                    "duplication_survey":company.duplication_survey,
                    "name_surname":company.name_surname,
                    "telephone_number":company.telephone_number,
                    "description":company.description,
                    "comarca":company.comarca,
                    "territori_leader":company.territori_leader,
                    "number_workers":company.number_workers})
             return results 


class SurveyCompanyAll(Resource):
    @jwt_required
    def get(self):
        user= UserModel.find_by_username(email=get_jwt_identity())
        if (request.args.get('type')!=None and user.type_user!=1):
            return {'message':'not authorized'},500

        results=[]
        company= CompanyModel.find_by_id(id=user.id_company)
        items=SurveyCompanyModel.find_by_company_id(id_company=user.id_company)

        if (request.args.get('type')=='all'):
            items=SurveyCompanyModel.find_all()
        
        if (len(items)==0):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             for item in items:
                 pub_date=''
                 if (item.pub_date!=None):
                       pub_date=item.pub_date.strftime('%Y')
                 results.append({
"id":item.id,
"id_survey": item.id_survey ,
"name_survey":item.name_survey,
"id_company":item.id_company,
"status":item.status,
"score":item.score,
"score_future":item.score_future,
"last_modified":item.last_date.strftime('%d/%m/%Y %H:%M'),
"pub_date":pub_date,
"version":item.version,
"year":item.convocatoria_year})
             return results
    
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_survey', help = 'This field cannot be blank', required = True)
        parser.add_argument('id_company', help = 'This field cannot be blank', required = True)
        parser.add_argument('file_dari', help = 'This field cannot be blank', required = False)
        parser.add_argument('convocatoria', help = 'This field cannot be blank', required = True)
        parser.add_argument('convocatoria_year', help = 'This field cannot be blank', required = False)      
        data = parser.parse_args()

        items=SurveyCompanyModel.find_by_company_id(id_company=data['id_company'])
        company=CompanyModel.find_by_id(id=data['id_company']) 
        #len(items)
        #if len>1
        #items[len(items)-1].version+1
        #else version=1
        
        convocatoria=False
        if (data['convocatoria']=='True'):
            convocatoria=True

        version=len(items)+1
        new_surveycompany = SurveyCompanyModel(
            id_survey = data['id_survey'],
            name_survey = company.commercial_name+".v"+str(version)+'-'+datetime.utcnow().strftime('%Y'),
            id_company = data['id_company'],
            version=version,
            status = 'created',
            start_date = datetime.now(pytz.timezone('Europe/Amsterdam')),
            last_date = datetime.now(pytz.timezone('Europe/Amsterdam')),
            score=0,
            score_future=0,
            file_dari=data['file_dari'],
            convocatoria=convocatoria,
            convocatoria_year=data['convocatoria_year']
        )
        try:
            survey = SurveyModel.find_by_id(id=data['id_survey'])
            questions= [int(s) for s in survey.questions.split(',')]
            answers_id=[]
            for question in questions:
                answer=AnswerModel(id_question=question,
                            score=-1,
                            score_future=0,
                            future=False,
                            id_option=-1,
                            justification_text='',
                            future_justification_text='',
                            justification_file='')
                answer.save_to_db()
                answers_id.append(answer.id)
            new_surveycompany.answers=','.join([str(i) for i in answers_id])
                     
            new_surveycompany.save_to_db()
            return {
                'message': 'Survey company '+str(new_surveycompany.id)+' was created'
            }
        except Exception as e:
           print(e)
           return {'message': 'Something went wrong '+str(e)}, 500


class DuplicateSurveyCompany(Resource):
    @jwt_required
    def get(self,id):
        
        item=SurveyCompanyModel.find_by_id(id=id)
        if (item==None):
            return {'message':'the survey was not found'}
        #if (item.status!="created"):
        #    return {'message':'survey already submitted'}
        user= UserModel.find_by_username(email=get_jwt_identity())
        if (item.id_company!= user.id_company):
            return {'message':'not authorized'},500


        items=SurveyCompanyModel.find_by_company_id(id_company=user.id_company)
        version=len(items)+1
        
        company=CompanyModel.find_by_id(id=user.id_company) 

        if (company.duplication_survey==False):
            return {'message':'No es pot duplicar el qüestionari'},500   
        new_surveycompany = SurveyCompanyModel(
            id_survey = item.id_survey,
            name_survey = company.commercial_name+".v"+str(version)+'-'+datetime.utcnow().strftime('%Y'),
            id_company = company.id,
            version=version,
            status = 'created',
            start_date = datetime.now(pytz.timezone('Europe/Amsterdam')),
            last_date = datetime.now(pytz.timezone('Europe/Amsterdam')),
            score=0,
            score_future=0,
            file_dari=item.file_dari
        )
        try:
            
            answers= [int(s) for s in item.answers.split(',')]
            answers_id=[]
            
            for answer in answers:
                answerDone=AnswerModel.find_by_id(id=answer)
                
                new_answer=AnswerModel(id_question=answerDone.id_question,
                            score=answerDone.score,
                            score_future=answerDone.score_future,
                            future=answerDone.future,
                            id_option=answerDone.id_option,
                            justification_text=answerDone.justification_text,
                            future_justification_text=answerDone.future_justification_text,
                            justification_file=answerDone.justification_file)
                new_answer.save_to_db()
                if (answerDone.justification_file!=None and answerDone.justification_file!=''):
                    filename = app.config['UPLOAD_FOLDER'] + '/answers/' + str(answerDone.id) +'/'+ answerDone.justification_file
                    new_filename = app.config['UPLOAD_FOLDER'] + '/answers/' + str(new_answer.id) +'/'+ new_answer.justification_file
                    if not os.path.exists(os.path.dirname(new_filename)):
                        try:
                            os.makedirs(os.path.dirname(new_filename))
                        except OSError as exc:
                            return {'message': 'Something went wrong '+str(exc)}, 500

                    copyfile(filename,new_filename)
                answers_id.append(new_answer.id)
            new_surveycompany.answers=','.join([str(i) for i in answers_id])
                     
            new_surveycompany.save_to_db()
            return {
                'message': 'Survey company '+str(new_surveycompany.id)+' was created'
            }
        except Exception as e:
           print(e)
           return {'message': 'Something went wrong '+str(e)}, 500

class SurveyCompany(Resource):
    @jwt_required
    def get(self,id):
        results=[]
        
        item=SurveyCompanyModel.find_by_id(id=id)

        if (item==None):
            return {'message':'the survey was not found'}
        else:
             #return jsonify(json_list = questions)
             survey=SurveyModel.find_by_id(id=item.id_survey)
             company=CompanyModel.find_by_id(id=item.id_company)
             if (item.pub_date!=None):
                pub_date=item.pub_date.strftime('%d/%m/%Y')
             else:
                pub_date=''
             return {
"id":item.id,
"id_survey": item.id_survey ,
"name_survey":item.name_survey,
"id_company":item.id_company,
"company":company.commercial_name,
"status":item.status,
"score":item.score,
"score_future":item.score_future,
"pub_date":pub_date,
"version":item.version,
"questions":survey.questions,
"answers":item.answers}
             
             return {'data':results}
    @jwt_required
    def put(self,id):
        item=SurveyCompanyModel.find_by_id(id=id)
        if (item==None):
            return {'data':[]}
        else:
             data= request.json['company_survey']
             if (data['status']!=None):
                item.status= data['status']
             if (data['score']!=None):
                item.score= data['score']
             if (data['score_future']!=None):
                item.score_future= data['score_future']
             item.last_date = datetime.now(pytz.timezone('Europe/Amsterdam'))
             if (item.pub_date==None):
                 item.pub_date = datetime.now(pytz.timezone('Europe/Amsterdam'))
             try:
                item.save_to_db()
                return {
                'message': 'survey company {} was updated'.format( str(id))
                }
             except Exception as e:
                 print(e)
                 return {'message': 'Something went wrong '+str(e)}, 500 
    @jwt_required
    def delete(self,id):
        user= UserModel.find_by_username(email=get_jwt_identity())
        item=SurveyCompanyModel.find_by_id(id=id)
        
        if (item==None):
            return {'message':'the survey was not found'},500
        if (item.status=='submitted'):
            return {'message':'the survey has been already submitted,can not be deleted'},500
        if (item==None):
            return {'message':'the survey was not found'},500
        try:
            
            answers= [int(s) for s in item.answers.split(',')]
            answers_id=[]
            for answer in answers:
                found=AnswerModel.find_by_id(id=answer)
                #import ipdb;ipdb.set_trace()
                db.session.delete(found)
                db.session.commit()
            db.session.delete(item)
            db.session.commit()
            return {'message':'company_survey deleted'}
        except Exception as e:
                 print(e)
                 return {'message': 'Something went wrong '+str(e)}, 500 


