from flask_restful import Resource, reqparse
from flask_jwt_extended import (JWTManager, create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models import UserModel,QuestionModel,SurveyModel,CompanyModel,SurveyCompanyModel,QuestionModelES,AnswerModel
from run import db,app
from flask import Flask, jsonify, request

jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'admin': user.type_user}


# Create a function that will be called whenever create_access_token
# is used. It will take whatever object is passed into the
# create_access_token method, and lets us define what the identity
# of the access token should be.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.email


class UserRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help = 'This field cannot be blank', required = True)
        parser.add_argument('password', help = 'This field cannot be blank', required = True)
        parser.add_argument('admin', help = 'This field cannot be blank', required = False)
        data = parser.parse_args()
        if UserModel.find_by_username(data['username']):
                  return {'message': 'Usuari ja existeix'}
        new_user = UserModel(
            email = data['username'],
            password = UserModel.generate_hash(data['password']),
            type_user=0 #0=normal_user
        )
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = new_user)
            refresh_token = create_refresh_token(identity = new_user)
            return {
                'message': 'User {} was created'.format( data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token,
                'admin': new_user.type_user
            }
        except:
           return {'message': 'Something went wrong'}, 500

class AdminRegistration(Resource):
    @jwt_required
    def post(self):
        

        user=UserModel.find_by_username(email=get_jwt_identity())
        
        if (user.type_user!=1):
           return {'message': 'not authorized'}, 500
        parser = reqparse.RequestParser()
        parser.add_argument('username', help = 'This field cannot be blank', required = True)
        parser.add_argument('password', help = 'This field cannot be blank', required = True)
        parser.add_argument('admin', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()
        type=0
        if (data['admin']):
            type=1

        
        if UserModel.find_by_username(data['username']):
                  return {'message': 'Usuari ja existeix'}
        new_user = UserModel(
            email = data['username'],
            password = UserModel.generate_hash(data['password']),
            type_user=type #0=normal_user
        )
        try:
            new_user.save_to_db()
            return {
                'message': 'User {} was created'.format( data['username']),
                'user_id': new_user.id
            }
        except:
           return {'message': 'Something went wrong'}, 500



class CompanyUpdate(Resource):
    @jwt_required
    def put(self,id):
        user_id=request.args.get('user_id')
        company=CompanyModel.find_by_id(id=id)
        user= UserModel.find_by_username(email=get_jwt_identity())

        if (user.id_company!=company.id and user.type_user!=1):
           return {'message': 'not authorized'}, 500
        if (user_id!=None and user.type_user!=1):
           return {'message': 'not authorized'}, 500
        else:
            user=UserModel.find_by_id(id=user_id)
        

        user=UserModel.find_by_username(email=get_jwt_identity())
        

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
        duplication=True

        if (data['duplication_survey']=='True'):
            duplication=True
        else:
            duplicaiton=False        
        company.sector = data['sector']
        company.subsector = data['subsector']
        company.commercial_name = data['commercial_name']
        company.fiscal_name = data['fiscal_name']
        company.nif = data['nif']
        company.name_surname = data['name_surname']
        company.telephone_number = data['telephone_number']
        company.description = data['description']
        company.comarca = data['comarca']
        company.territori_leader = data['territori_leader']
        company.number_workers = data['number_workers']
        company.duplication_survey=duplication
        
        try:

            company.save_to_db()
            return {
                'message': 'Company {} was update'.format( data['commercial_name'])
            }
        except Exception as e:
           print(e)
           return {'message': 'Something went wrong '+str(e)}, 500


class CompanyRegistration(Resource):
    @jwt_required
    def post(self):
        
        user_id=request.args.get('user_id')
        user=UserModel.find_by_username(email=get_jwt_identity())
        if (user_id!=None and user.type_user!=1):
           return {'message': 'not authorized'}, 500
        if (user_id!=None):
            user=UserModel.find_by_id(id=user_id)
        

        if (user==None):
           return {'message': 'User not found'}, 500
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
            duplication_survey = True,
            name_surname = data['name_surname'],
            telephone_number = data['telephone_number'],
            description = data['description'],
            comarca = data['comarca'],
            territori_leader = data['territori_leader'],
            number_workers = data['number_workers']
        )
        try:
            new_company.save_to_db()
            user.id_company= new_company.id
            user.save_to_db()
            return {
                'message': 'Company {} was created'.format( data['commercial_name'])
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
             access_token = create_access_token(identity = current_user)
             refresh_token = create_refresh_token(identity = current_user)
             return {'message': 'Logged in as {}'.format(current_user.email),
                'access_token': access_token,
                'refresh_token': refresh_token,
                'admin': current_user.type_user
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
    @jwt_required
    def get(self):
        user=UserModel.find_by_username(email=get_jwt_identity())
        
        if (user.type_user!=1):
           return {'message': 'not authorized'}, 500
        users= UserModel.find_all()
        results=[]
        if (len(users)==0):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             for item in users:
                 if (item.id_company!=None):
                    company=CompanyModel.find_by_id(id=item.id)
                    results.append({"id":item.id, "email":item.email,"type": item.type_user, "company" :company.commercial_name
                    ,"company_id" :user.id_company, "comarca": company.comarca, "leader": company.territori_leader})
                 else:
                    results.append({"id":item.id, "email":item.email,"type": item.type_user})



             
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
            questionsES= QuestionModelES.find_all()
        else:

            questions=QuestionModel.find_by_array(array=ids)
            questionsES=QuestionModelES.find_by_array(array=ids)

        if (len(questions)==0):
            return {'data':[]}
        else:
             #return jsonify(json_list = questions)
             for item in questions:
                 results.append({"cat":{
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
        "proposta_millora":item.proposta_millora}})

             for index,item in  enumerate(questionsES):
                
                results[index]['es']={
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
        "proposta_millora":item.proposta_millora}

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
        id_company=request.args.get('id')
        if (id_company!=None and user.type_user!=1):
            return {'message':'Not authorized'},500
        
        company=CompanyModel.find_by_id(id=user.id_company)
        if (id_company!=None):
            company=CompanyModel.find_by_id(id=id_company)
        if (company==None):
            return {"message":"company not found"},500
        results=[]
        #look for surveymodel by id_company_field otherwise by sector/subsector
        survey= SurveyModel.find_by_id_company(id_company=company.id)
        if (survey==None):
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
     @jwt_required
     def put(self):
        user=UserModel.find_by_username(email=get_jwt_identity())
        
        if (user.type_user!=1):
            return {'message':'Not authorized'},500        
        parser = reqparse.RequestParser()
        parser.add_argument('questions', help = 'This field cannot be blank', required = True)
        parser.add_argument('id_company', help = 'This field cannot be blank', required = True)
        data = parser.parse_args()
        
        survey=SurveyModel.find_by_id_company(id_company=data['id_company'])
        
        if (survey!=None):
            survey.questions=data['questions']
        else:
          survey = SurveyModel(
             sector = 'company',
             id_company = data['id_company'],
             questions = data['questions']
          )
        try:
            survey.save_to_db()
            surveys=SurveyCompanyModel.find_by_company_id_and_status(survey.id_company,"created")
            new_questions=survey.questions.split(",")
            news=[]
            
            for i in surveys:
                old_answers=i.answers.split(",")
                for value in old_answers:
                    if(str(AnswerModel.find_by_id(id=value).id_question) in new_questions):
                        news.append(value)
                i.answers=','.join(news)
                i.save_to_db()



            return {
                'message': 'Survery {} was created'.format( data['id_company'])
            }              
        except Exception as e:
           print(e)
           return {'message': 'Something went wrong '+str(e)}, 500
import csv
class loadDataQuestion(Resource):

    def get(self):
        #tsvin1 = open('/home/ericanoanira/projects/encercla_server/data_questions.csv', 'rt')
        tsvin1 = open('/home/ericanoanira/projects/encercla_server/questionsES.txt', 'rt')
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

class loadDataQuestionES(Resource):

    def get(self):
        #tsvin1 = open('/home/ericanoanira/projects/encercla_server/data_questions.csv', 'rt')
        

        tsvin1 = open('questionsES_new.csv', 'rt')
        tsvin2 = csv.reader(tsvin1, delimiter='\t')
        
        for row in tsvin2:
            new_question = QuestionModelES(
                statement=row[0],
                strategy=row[1],
                ld_option_1=row[2],
                ld_option_2=row[3],
                ld_option_3=row[4],
                ld_option_4=row[5],
                futurible=row[6],
                more_information=row[7],
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
         
class User(Resource):
    @jwt_required
    def get(self,id):
        user=UserModel.find_by_username(email=get_jwt_identity())
        admin=False
        if (user.type_user==1):
            admin=True

        if (user.type_user!=1 and id!=user.id):
           return {'message': 'not authorized'}, 500
        user=UserModel.find_by_id(id=id)
        if (user==None):
            return {'message':'user not found'}
        else:
            if admin:
            
                    return {"id":user.id, "email":user.email,"type_user": user.type_user}
            else:
                    return {"id":user.id, "email":user.email}

    @jwt_required
    def delete(self,id):
        item=UserModel.find_by_username(email=get_jwt_identity())
        if (item.type_user!=1):
            return {'message':'Not authorized'},500
        else:
            item=UserModel.find_by_id(id=id)

        if (item==None):
            return {'message':'the user was not found'},500
        try:
            
            if (item.id_company!=None):
                company=CompanyModel.find_by_id(id=item.id_company)
                db.session.delete(company)
                db.session.commit()
            db.session.delete(item)
            db.session.commit()
            return {'message':'user deleted'}
        except Exception as e:
                 print(e)
                 return {'message': 'Something went wrong '+str(e)}, 500    

    @jwt_required             
    def put(self,id):

        user=UserModel.find_by_username(email=get_jwt_identity())
        if (user.type_user!=1):
            return {'message':'Not authorized'},500
        else:
            user=UserModel.find_by_id(id=id)

        if (user==None):
            return {'message':'the user was not found'},500
        
        
        parser = reqparse.RequestParser()
        parser.add_argument('username', help = 'This field cannot be blank', required = True)
        parser.add_argument('password', help = 'This field cannot be blank', required = False)
        parser.add_argument('admin', help = 'This field cannot be blank', required = False)
        data = parser.parse_args()
        
        if (data['username']!=''):
              user.email=data['username']
        if (data['password']!=''):
              user.password=data['password']  
        
        if (data['admin'])=='True':
            user.type_user=1
        else:
            user.type_user=0         
        try:
               user.save_to_db()
               return {
                'message': 'User {} was update'.format( user.email),
                }
        except:
                return {'message': 'Something went wrong'}, 500

class UserAlone(Resource):
    @jwt_required
    def get(self):
        user=UserModel.find_by_username(email=get_jwt_identity())

        
        if (user==None):
            return {'message':'user not found'}
        else:
            if (user.type_user==1):
                return  {"id":user.id, "email":user.email}

            

    @jwt_required
    def delete(self):
        item=UserModel.find_by_username(email=get_jwt_identity())
   
        if (item==None):
            return {'message':'the user was not found'},500
        try:
            
            if (item.id_company!=None):
                company=CompanyModel.find_by_id(id=item.id_company)
                db.session.delete(company)
                db.session.commit()
            db.session.delete(item)
            db.session.commit()
            return {'message':'user deleted'}
        except Exception as e:
                 print(e)
                 return {'message': 'Something went wrong '+str(e)}, 500    
    @jwt_required             
    def put(self):
        user=UserModel.find_by_username(email=get_jwt_identity())
        parser = reqparse.RequestParser()
        parser.add_argument('username', help = 'This field cannot be blank', required = True)
        parser.add_argument('password', help = 'This field cannot be blank', required = False)
        parser.add_argument('admin', help = 'This field cannot be blank', required = False)
        data = parser.parse_args()

        if (data['username']!=''):
            user.email=data['username']
        if (data['password']!=''):
            user.password=data['password']
        if (user.type_user==1):
            if (data['admin'])=='true':
               user.admin=1
            else:
               user.admin=0        
        try:
            user.save_to_db()
            return {
                'message': 'User {} was update'.format( user.email),
            }
        except:
           return {'message': 'Something went wrong'}, 500    
