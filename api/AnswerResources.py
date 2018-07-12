from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models import UserModel,QuestionModel,SurveyModel,CompanyModel,SurveyCompanyModel,AnswerModel

from flask import Flask, jsonify, request
from datetime import datetime
from run import app
class AnswerAll(Resource):

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
           "future":item.future,
           "justification_text":item.justification_text,
           "justification_file":item.justification_file })
             
             return {'data':results}
class Answer(Resource):

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
           "future":item.future,
           "justification_text":item.justification_text,
           "justification_file":item.justification_file }
    def put(self,id):
        item=AnswerModel.find_by_id(id=id)
        if (item==None):
            return {'data':[]}
        else:
             data= request.json['answer']
             if (data['id_option']!=None):
                item.id_option= data['id_option']
             if (data['id_option']!=None):
                item.justification_text= data['justification_text']
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
class UploadFile(Resource):
     def post(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            
            return {'message':'no file part'}
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            
            return {'message':'no selected file'}
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return {'message':'uploaded'}
