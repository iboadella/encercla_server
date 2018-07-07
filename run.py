from flask import Flask,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
#https://github.com/oleg-agapov/flask-jwt-auth

app = Flask(__name__,static_url_path='')
@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

api = Api(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

jwt = JWTManager(app)
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()
import views, models, resources, apis

api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.CompanyRegistration, '/registrationcompany')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')

api.add_resource(resources.Questions, '/questions')
api.add_resource(resources.loadDataQuestion, '/Loadquestions')
api.add_resource(resources.Survey,'/survey', '/survey/<id>')

api.add_resource(resources.specificsurvey, '/specificsurvey')
api.add_resource(apis.SectorList, '/sectors')
api.add_resource(apis.Company, '/company/<company_id>')
api.add_resource(apis.SurveyCompany, '/companysurvey')
