from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models import UserModel,QuestionModel,SurveyModel,CompanyModel

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
            email = data['username'],
            password = UserModel.generate_hash(data['password']),
            type_user=0 #0=normal_user
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

class CompanyRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sector', help = 'This field cannot be blank', required = True)
        parser.add_argument('subsector', help = 'This field cannot be blank', required = True)
        parser.add_argument('commercial_name', help = 'This field cannot be blank', required = True)
        parser.add_argument('fiscal_name', help = 'This field cannot be blank', required = True)
        parser.add_argument('nif', help = 'This field cannot be blank', required = True)
        parser.add_argument('duplication_survey', help = 'This field cannot be blank', required = True)
        parser.add_argument('name_surname', help = 'This field cannot be blank', required = True)
        parser.add_argument('telephone_number', help = 'This field cannot be blank', required = True)
        parser.add_argument('description', help = 'This field cannot be blank', required = True)
        parser.add_argument('comarca', help = 'This field cannot be blank', required = True)
        parser.add_argument('territori_leader', help = 'This field cannot be blank', required = True)
        parser.add_argument('number_workers', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()
        if CompanyModel.find_by_nif(data['nif']):
                  return {'message': 'Company {} already exists'. format(data['nif'])}
        new_company = CompanyModel(
            sector = data['sector'],
            subsector = data['subsector'],
            commercial_name = data['commercial_name'],
            fiscal_name = data['fiscal_name'],
            nif = data['nif'],
            number_survey = 0,
            duplication_survey = False,
            name_surname = data['name_surname'],
            telephone_number = data['telephone_number'],
            description = data['description'],
            comarca = data['comarca'],
            territori_leader = data['territori_leader'],
            number_workers = data['number_workers']
        )
        try:
            new_company.save_to_db()
            return {
                'message': 'Company {} was created'.format( data['username'])
            }
        except Exception as e:
           print(e)
           return {'message': 'Something went wrong '+str(e)}, 500
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
             return {'message': 'Logged in as {}'.format(current_user.email),
                'access_token': access_token,
                'refresh_token': refresh_token
             }
        else:
             return {'message': 'Wrong credentials'}
      
      
class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}
      
    
class LoggedIn(Resource):
     @jwt_required
     def post(self):
         return {'message':'you are logged in'}
         
class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}
      
      
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}
      
class Allcompanies(Resource):
    def get(self):
        users= CompanyModel.find_all()
        results=[]
        if (len(users)==0):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             for item in users:
                 results.append({"email":item.email,"type": item.type_user, "company" :item.id_company})
             
             return {'data':results}
    
class AllUsers(Resource):
    def get(self):
        users= UserModel.find_all()
        results=[]
        if (len(users)==0):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             for item in users:
                 results.append({"email":item.email,"type": item.type_user, "company" :item.id_company})
             
             return {'data':results}

    def delete(self):
        return {'message': 'Delete all users'}
      
      
class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }
class Questions(Resource):
    def get(self,id):
        results=[]
        question= QuestionModel.find_by_id(id=id)
        if (questions==None):
            return {'data':[]}
        else:
 
                 return {
"id":question.id,
"statement": question.statement ,
"q1":question.ld_option_1,
"q2":question.ld_option_2,
"q3":question.ld_option_3,
"q4":question.ld_option_4,
"futurible":question.futurible,
"statement":question.statement,
"strategy":question.strategy}

    #@jwt_required
    def get(self):
        results=[]
        ids=request.args.get('ids')
        print(ids)
        if (ids==None):
            questions= QuestionModel.find_all()
        else:
            questions=QuestionModel.find_by_array(array=ids)
        if (len(questions)==0):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             for item in questions:
                 results.append({
	"id":item.id,
	"statement": item.statement ,
	"q1":item.ld_option_1,
	"q2":item.ld_option_2,
	"q3":item.ld_option_3,
	"q4":item.ld_option_4,
	"futurible":item.futurible,
	"statement":item.statement,
	"strategy":item.strategy,
        "more_information":item.more_information,
        "proposta_millora":item.proposta_millora})
             
             return {'data':results}
    def post(self):
        
        parser = reqparse.RequestParser()
        json_data = request.get_json(force=True)
        
        data = parser.parse_args()
        return {json_data}
        
class Survey(Resource):
     @jwt_required
     def get(self,id):
        results=[]
        survey= SurveyModel.find_by_id(id)
        if (survey==None):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             return {"id":survery.id,"sector":survey.sector,"subsector":survey.subsector,"questions":survey.questions}
     @jwt_required
     def get(self):
        user=UserModel.find_by_username(email=get_jwt_identity())
        company=CompanyModel.find_by_id(id=user.id_company)
        
        results=[]
        survey= SurveyModel.find_by_sector(company.sector,company.subsector)
        if (survey==None):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             return {"id":survey.id,"sector":survey.sector,"subsector":survey.subsector,"questions":survey.questions}
     def post(self):
        
        data = request.get_json(force=True)
        

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
import csv
class loadDataQuestion(Resource):

    def get(self):
        tsvin1 = open('/home/ericanoanira/projects/encercla_server/data_questions.csv', 'rt')
        tsvin2 = csv.reader(tsvin1, delimiter='\t')
        for row in tsvin2:
            new_question = QuestionModel(
                statement=row[1],
                strategy=row[0],
                ld_option_1=row[2],
                ld_option_2=row[3],
                ld_option_3=row[4],
                ld_option_4=row[5],
                futurible=row[7],
                more_information=row[6],
                advise=row[8],
                proposta_millora=row[9]
                )
            new_question.save_to_db()

class specificsurvey(Resource):

    def get(self):
        tsvin1 = open('/home/ericanoanira/projects/encercla_server/resumquestionarisespecifics.csv', 'rt')
        tsvin2 = csv.reader(tsvin1, delimiter='\t')
        for row in tsvin2:
            new_question = SurveyModel(
                sector=row[0],
                subsector=row[1],
                questions=row[2]               
                )
            new_question.save_to_db()

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}
         
          
