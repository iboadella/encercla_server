from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models import UserModel,QuestionModel,SurveyModel,CompanyModel,SurveyCompanyModel,AnswerModel

from flask import Flask, jsonify, request
from datetime import datetime

class Company(Resource):
     @jwt_required
     def get(self):
        
        user= UserModel.find_by_username(email=get_jwt_identity())
        results=[]
        company= CompanyModel.find_by_id(id=user.id_company)
        if (company==None):
            return {'data':[]}
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
class SurveyCompanyAll(Resource):
    @jwt_required
    def get(self):
        user= UserModel.find_by_username(email=get_jwt_identity())
        results=[]
        company= CompanyModel.find_by_id(id=user.id_company)
        items=SurveyCompanyModel.find_by_company_id(id_company=user.id_company)
        if (len(items)==0):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             for item in items:
                 results.append({
"id":item.id,
"id_survey": item.id_survey ,
"name_survey":item.name_survey,
"id_company":item.id_company,
"status":item.status,
"last_modified":item.last_date.strftime('%m/%d/%Y'),
"version":item.version})
             return results
    
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_survey', help = 'This field cannot be blank', required = True)
        parser.add_argument('name_survey', help = 'This field cannot be blank', required = True)
        parser.add_argument('id_company', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()
        if SurveyCompanyModel.find_by_name_survey(data['name_survey']):
                  return {'message': 'Survey {} already exists'. format(data['name_survey'])},500
        items=SurveyCompanyModel.find_by_company_id(id_company=data['id_company'])
        
        version=len(items)+1
        new_surveycompany = SurveyCompanyModel(
            id_survey = data['id_survey'],
            name_survey = data['name_survey'],
            id_company = data['id_company'],
            version=version,
            status = 'created',
            start_date = datetime.utcnow(),
            last_date = datetime.utcnow(),
            score=0
        )
        try:
            survey = SurveyModel.find_by_id(id=data['id_survey'])
            questions= [int(s) for s in survey.questions.split(',')]
            answers_id=[]
            for question in questions:
                answer=AnswerModel(id_question=question,
                            score=-1,
                            future=False,
                            id_option=-1,
                            justification_text='',
                            justification_file='')
                answer.save_to_db()
                answers_id.append(answer.id)
            new_surveycompany.answers=','.join([str(i) for i in answers_id])
                     
            new_surveycompany.save_to_db()
            return {
                'message': 'Company {} was created'.format( data['name_survey'])
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
             return {
"id":item.id,
"id_survey": item.id_survey ,
"name_survey":item.name_survey,
"id_company":item.id_company,
"status":item.status,
"score":item.score,
 #"last_modified": item.last_date,
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
             last_date = datetime.utcnow(),
             pub_date = datetime.utcnow(),
             try:
                item.save_to_db()
                return {
                'message': 'survey company {} was updated'.format( str(id))
                }
             except Exception as e:
                 print(e)
                 return {'message': 'Something went wrong '+str(e)}, 500 
     
	
