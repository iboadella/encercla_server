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
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

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
    def find_all(cls):
        return cls.query.all() 


