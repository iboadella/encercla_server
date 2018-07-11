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
