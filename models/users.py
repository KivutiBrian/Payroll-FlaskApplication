from main import db
from sqlalchemy import func
from werkzeug.security import check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True) 
    password = db.Column(db.String, nullable=True)
    role = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

        # create
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    # read all
    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    @classmethod
    def check_email_exists(cls, email):
        record = cls.query.filter_by(email=email).first()
        if record:
            return True
        else:
            return False

    @classmethod
    def validate_password(cls, email, password):
        record = cls.query.filter_by(email=email).first()
        if record and check_password_hash(record.password, password):
            return True
        else:
            False

    @classmethod
    def get_user(cls, email):
        return cls.query.filter_by(email=email).first()
        


    
