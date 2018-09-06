from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models import UserModel,QuestionModel,SurveyModel,CompanyModel,SurveyCompanyModel,AnswerModel,QuestionModelES

from flask import Flask, jsonify, request, send_file
from datetime import datetime
from run import app
import os
import zipfile
import json



class AnswerAll(Resource):
    @jwt_required
    def get(self):
        results=[]
        ids=request.args.get('ids')
        if (ids==None):
            answers= AnswerModel.find_all()
        else:
            answers=AnswerModel.find_by_array(array=ids)
        if (len(answers)==0):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             for item in answers:
                 results.append({
           "id":item.id,
           "id_question":item.id_question ,
           "id_option":item.id_option,
           "score":item.score,
            "score_future":item.score_future,
           "future":item.future,
           "future_justification_text":item.future_justification_text,
           "justification_text":item.justification_text,
           "justification_file":item.justification_file })
             
             return {'data':results}
class Answer(Resource):
    @jwt_required
    def get(self,id):

        results=[]
        ids=request.args.get('ids')

        item=AnswerModel.find_by_id(id=id)
        if (item==None):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
            return {
           "id":item.id,
           "id_question":item.id_question ,
           "id_option":item.id_option,
           "score":item.score,
           "future_justification_text":item.future_justification_text,
           "score_future":ite.score_future,
           "future":item.future,
           "justification_text":item.justification_text,
           "justification_file":item.justification_file }
    @jwt_required
    def put(self,id):
        item=AnswerModel.find_by_id(id=id)
        if (item==None):
            return {'data':[]}
        else:
             data= request.json['answer']
             if (data['id_option']!=None):
                item.id_option= data['id_option']
             if (data['justification_text']!=None):
                item.justification_text= data['justification_text']
             if (data['justification_file']!=None):
                item.justification_file= data['justification_file']
             if (data['score']!=None):
                item.score= data['score']
             if (data['future']!=None):
                item.future= data['future']
             if (data['future_justification_text']!=None):
                item.future_justification_text= data['future_justification_text']
             if (data['score_future']!=None):
                item.score_future= data['score_future']
             try:
                item.save_to_db()
                return {
                'message': 'answer {} was updated'.format( str(id))
                }
             except Exception as e:
                 print(e)
                 return {'message': 'Something went wrong '+str(e)}, 500                     
          


from werkzeug.utils import secure_filename 
import os
import errno
class UploadFile(Resource):
    @jwt_required
    def post(self):
        
        answer_id = request.args.get('answer')
        surveycompany_id = request.args.get('surveycompany_id')
        if (answer_id == None and surveycompany_id ==None):
            return ({'message': 'you need to specifiy answer id or dari id'}, 500)

        # check if the post request has the file part

        if 'file' not in request.files:

            return {'message': 'no file part'}
        file = request.files['file']

        # if user does not select file, browser also
        # submit a empty part without filename

        if file.filename == '':

            return {'message': 'no selected file'}
        if file:
            if (answer_id!=None):
                filename = app.config['UPLOAD_FOLDER'] + '/answers/' \
                + answer_id +'/'+ secure_filename(file.filename)
            else :
                filename = app.config['UPLOAD_FOLDER'] + '/surveycompany/' \
                + surveycompany_id +'/'+ secure_filename(file.filename)                
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc:

                                     # Guard against race condition

                    if exc.errno != errno.EEXIST:
                        return ({'message': 'error saving file'}, 500)

            try:
                print(filename)
                file.save(filename)
                return {'message': 'uploaded'}
            except Exception as e:
                 print(e)
                 return {'message': 'Something went wrong '+str(e)}, 500  
            

    @jwt_required
    def delete(self):
        
        
        answer_id = request.args.get('answer')
        surveycompany_id = request.args.get('surveycompany_id')
        if (answer_id == None and surveycompany_id ==None):
            return ({'message': 'you need to specifiy answer id or dari id'}, 500)
        if (answer_id!=None):
                answer=AnswerModel.find_by_id(id=answer_id)
                filename = app.config['UPLOAD_FOLDER'] + '/answers/' \
                + answer_id +'/'+ answer.justification_file
                try:
                    os.remove(filename)
                except Exception as e:
            
                     return ({'message': 'Something went wrong ' + str(e)}, 500)       
                return {'message': 'uploaded'}


class Download(Resource):
    @jwt_required
    def get(self,id):

        user= UserModel.find_by_username(email=get_jwt_identity())
        if (user.type_user!=1):
           return {'message': 'no autoritzat'}, 500
        survey=SurveyCompanyModel.find_by_id(id=id)
        if (survey==None):
            return {'message':'survey not found'},500

        folder=app.config['UPLOAD_FOLDER']+'/'+str(user.id)+'/survey/'
        filename=folder+str(survey.id)+'.zip'
        
        if not os.path.exists(os.path.dirname(folder)):
                try:
                    os.makedirs(os.path.dirname(folder))
                except OSError as exc:

                                     # Guard against race condition

                    if exc.errno != errno.EEXIST:
                        return ({'message': 'error saving file'}, 500)
        zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
        answers = survey.answers.split(",")
        if (survey.file_dari!=''):
            True
            #app.config['UPLOAD_FOLDER'] + '/surveycompany/' \
               # + surveycompany_id +'/'+ secure_filename(file.filename) 
            zipf.write(os.path.join(app.config['UPLOAD_FOLDER'] + '/surveycompany/'+str(survey.id), survey.file_dari.replace(" ","_")),arcname=survey.file_dari)
        for id_answer in answers:
            answer=AnswerModel.find_by_id(id=id_answer)
            if (answer.justification_file!=''):
                zipf.write(os.path.join(app.config['UPLOAD_FOLDER'] + '/answers/'+str(answer.id), answer.justification_file.replace(" ","_")),arcname=str(answer.id)+'/'+ answer.justification_file)
        zipf.close()
        try:
            return send_file(filename, as_attachment=True)
        except Exception as e:
                 print(e)
                 return {'message': 'Something went wrong '+str(e)}, 500          


class DownloadAll(Resource):

    @jwt_required
    def get(self):
        ids=request.args.get('ids')
        surveys_id= ids.split(",")
        user = UserModel.find_by_username(email=get_jwt_identity())
        if user.type_user != 1:
            return ({'message': 'no autoritzat'}, 500)
        

        # change status to submitted

        companies = CompanyModel.find_all()
        folder=app.config['UPLOAD_FOLDER']+'/'+str(user.id)+'/survey/'
        filename=folder+'all_surveys.zip'
        if not os.path.exists(os.path.dirname(folder)):
                try:
                    os.makedirs(os.path.dirname(folder))
                except OSError as exc:

                                     # Guard against race condition

                    if exc.errno != errno.EEXIST:
                        return ({'message': 'error saving file'}, 500)
        zipf = zipfile.ZipFile(filename, 'w',
                               zipfile.ZIP_DEFLATED)
     
        for company in companies:
            surveys = \
                SurveyCompanyModel.find_by_company_id_and_status(id_company=company.id,
                    status='submitted')
            
            for survey in surveys:
                if (not str(survey.id) in  surveys_id):
                    continue
                if (survey.file_dari!=''):
                    zipf.write(os.path.join(app.config['UPLOAD_FOLDER'] + '/surveycompany/'+str(survey.id), survey.file_dari.replace(" ","_")),arcname=company.commercial_name + '/' + survey.name_survey + '/' +survey.file_dari)

                answers = survey.answers.split(',')
                for id_answer in answers:
                    answer = AnswerModel.find_by_id(id=id_answer)
                    
                    if answer.justification_file != '':
                        zipf.write(os.path.join(app.config['UPLOAD_FOLDER'
                                   ] + '/answers/' + str(answer.id),
                                   answer.justification_file),
                                   arcname=company.commercial_name + '/'
                                   + survey.name_survey + '/'
                                   + str(answer.id_question) + '/' +  answer.justification_file.replace(" ","_"))

        zipf.close()
        try:
            return send_file(filename, as_attachment=True)
        except Exception as e:
            
            return ({'message': 'Something went wrong ' + str(e)}, 500)

class DownloadDataExcel(Resource):

    @jwt_required
    def get(self):
        user = UserModel.find_by_username(email=get_jwt_identity())

        ids=request.args.get('ids')
        surveys_id= ids.split(",")
        lang= request.args.get("lang")
        if user.type_user != 1:
            return ({'message': 'no autoritzat'}, 500)
        

        # change status to submitted

        companies = CompanyModel.find_all()
        zipf = zipfile.ZipFile('all_surveys.zip', 'w',
                               zipfile.ZIP_DEFLATED)
        data=[{"id":""}]
        word="Preguntes"
        questions= QuestionModel.find_all()
        if (lang=='es'):
            word='Preguntas'
            questions=QuestionModelES.find_all()
        for question in questions:
            #for company in companies:
            #    surveys = \
            #    SurveyCompanyModel.find_by_company_id_and_status(id_company=company.id,
             #       status='created')
             #   for survey in surveys:
              #       answers = survey.answers.split(',')
                     data.append({"id":question.id,word:question.statement})
        for company in companies:
            surveys=SurveyCompanyModel.find_by_company_id_and_status(id_company=company.id,status='submitted')
            for survey in surveys:
                   if (not str(survey.id) in  surveys_id):
                       continue
                   answers = survey.answers.split(',')


                   for id_answer in answers:
                       answer = AnswerModel.find_by_id(id=id_answer)
                       if (answer.id_question>23):
                          break
                       data[answer.id_question][survey.name_survey]=answer.score
                       data[answer.id_question][survey.name_survey+'_futurible']=answer.score_future
 
        try:
            
            return data
        except Exception as e:
            
            return ({'message': 'Something went wrong ' + str(e)}, 500)        




			
