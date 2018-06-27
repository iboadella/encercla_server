from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models import UserModel,QuestionModel,SurveyModel

from flask import Flask, jsonify, request
class UserRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help = 'This field cannot be blank', required = True)
        parser.add_argument('password', help = 'This field cannot be blank', required = True)

        data = parser.parse_args()
        if UserModel.find_by_username(data['username']):
                  return {'message': 'User {} already exists'. format(data['username'])}
        new_user = UserModel(
            username = data['username'],
            password = UserModel.generate_hash(data['password'])
        )
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'User {} was created'.format( data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except:
           return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help = 'This field cannot be blank', required = True)
        parser.add_argument('password', help = 'This field cannot be blank', required = True)

        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        
        if UserModel.verify_hash(data['password'], current_user.password):
             access_token = create_access_token(identity = data['username'])
             refresh_token = create_refresh_token(identity = data['username'])
             return {'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
             }
        else:
             return {'message': 'Wrong credentials'}
      
      
class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}
      
      
class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}
      
      
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}
      
      
class AllUsers(Resource):
    def get(self):
        return {'message': 'List of users'}

    def delete(self):
        return {'message': 'Delete all users'}
      
      
class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }
class Questions(Resource):
    def get(self):
        results=[]
        questions= QuestionModel.find_all()
        if (len(questions)==0):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             for item in questions:
                 results.append({"id":item.id,"q1":item.question1,"q2":item.question2,"q3":item.question3})
             
             return {'data':results}
    def post(self):
        
        parser = reqparse.RequestParser()
        json_data = request.get_json(force=True)
        
        data = parser.parse_args()
        return {json_data}
        
class Survey(Resource):
     def get(self,id):
        results=[]
        survey= SurveyModel.find_by_id(id)
        if (survey==None):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             return {"id":survery.id,"sector":survey.sector,"subsector":survey.subsector,"questions":survey.questions}
     def post(self):
        
        data = request.get_json(force=True)
        
        import pdb
        pdb.set_trace()
        new_survey = SurveyModel(
            name = data['name'],
            sector = data['sector'],
            subsector = data['subsector'],
            questions = data['questions']
        )
        try:
            new_survey.save_to_db()          
            return {
                'message': 'Survery {} was created'.format( data['name'])
            }              
        except:
           return {'message': 'Something went wrong'}, 500
