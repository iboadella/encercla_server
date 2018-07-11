from run import db
from passlib.hash import pbkdf2_sha256 as sha256

class UserModel(db.Model):
    __tablename__ = 'users'

    #class type_users(enum.Enum):
	#administration=1
	#company=2

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    type_user = db.Column (db.Integer,nullable = False)
    id_company= db.Column(db.Integer,nullable= True)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_username(cls, email):
        return cls.query.filter_by(email = email).first()
    @classmethod
    def find_all(cls):
        return cls.query.all() 

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

class CompanyModel(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key = True)
    sector = db.Column(db.String(50), nullable = False)
    subsector = db.Column(db.String(50), nullable = False)
    commercial_name = db.Column(db.String(120), nullable = False)
    fiscal_name = db.Column(db.String(120), nullable = False)
    nif = db.Column(db.String(50), nullable = False)
    number_survey = db.Column (db.Integer,nullable = False)
    duplication_survey = db.Column(db.Boolean, nullable = False)
    name_surname = db.Column(db.String(50), nullable = False)
    telephone_number = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(500), nullable = False)
    comarca = db.Column(db.String(50), nullable = False)
    territori_leader = db.Column(db.String(50), nullable = False)
    number_workers = db.Column (db.Integer,nullable = False)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()
    @classmethod
    def find_by_nif(cls, nif):
        return cls.query.filter_by(nif = nif).first()


class QuestionModel(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key = True)
    statement =db.Column(db.String(200), nullable = False)
    strategy=db.Column(db.String(200), nullable = False)
    ld_option_1 = db.Column(db.String(220), nullable = False)
    ld_option_2 = db.Column(db.String(220), nullable = False)
    ld_option_3 = db.Column(db.String(220), nullable = False)
    ld_option_4 = db.Column(db.String(220), nullable = False)
    futurible = db.Column(db.Boolean, nullable = False)
    more_information= db.Column(db.String(500), nullable = False)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()
    @classmethod
    def find_by_array(cls, array):

        ids=[int(s) for s in array.split(',')]

        return cls.query.filter(QuestionModel.id.in_(ids)).all()   
    @classmethod
    def find_all(cls):
        return cls.query.all() 
class SurveyModel(db.Model):
    __tablename__ = 'survey'
    
    id = db.Column(db.Integer, primary_key = True)     
    sector = db.Column(db.String(50),nullable=False)
    subsector= db.Column(db.String(50), nullable=True)
    questions= db.Column(db.String(100),nullable=True)
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()  
    @classmethod
    def find_by_sector(cls, sector,subsector):
        return cls.query.filter_by(sector = sector).filter_by(subsector = subsector).first()  
    @classmethod
    def find_all(cls):
        return cls.query.all() 

class SurveyCompanyModel(db.Model):
    __tablename__ = 'surveycompany'
    
    id = db.Column(db.Integer, primary_key = True)     
    id_survey = db.Column(db.Integer, nullable = False)
    name_survey= db.Column(db.String(50), nullable=True)
    id_company = db.Column(db.Integer, nullable = False)
    version =  db.Column(db.Integer, nullable = False)
    status = db.Column(db.String(50), nullable = False)
    start_date = db.Column(db.DateTime)
    pub_date = db.Column(db.DateTime)
    last_date = db.Column(db.DateTime)
    answers=db.Column(db.String(100),nullable=True)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_name_survey(cls, name_survey):
        return cls.query.filter_by(name_survey = name_survey).first()
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first() 
    @classmethod
    def find_by_company_id(cls, id_company):
        return cls.query.filter_by(id_company = id_company).all()
   
    @classmethod
    def find_all(cls):
        return cls.query.all() 


class AnswerModel(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key = True)
    id_question =db.Column(db.Integer, nullable = False)
    id_option=db.Column(db.Integer, nullable = True)
    score = db.Column(db.Integer, nullable = True)
    future = db.Column(db.Boolean, nullable = True)
    justification_text = db.Column(db.String(1000), nullable = True)
    justification_file = db.Column(db.String(220), nullable = True)

    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()
    @classmethod
    def find_all(cls):
        return cls.query.all() 
    @classmethod
    def find_by_array(cls, array):

        ids=[int(s) for s in array.split(',')]

        return cls.query.filter(AnswerModel.id.in_(ids)).all()  
