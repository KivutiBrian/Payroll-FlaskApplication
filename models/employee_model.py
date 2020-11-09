from main import db
from sqlalchemy import func

class EmployeeModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    phone_number = db.Column(db.String(), nullable=False)
    sgid = db.Column(db.Integer, db.ForeignKey('salary_groups.id'), nullable=False)
    did = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    salaries = db.relationship('SalaryModel', backref='employee')

    
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
    def update(cls, id, surname,fname,lname,email,pno,sgid,did):
        record = cls.query.filter_by(id=id).first()
        if record:
            record.surname = surname
            record.first_name = fname
            record.last_name = lname
            record.email = email
            record.phone_number = pno
            record.sgid = sgid
            record.did = did
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def delete(cls, id):
        record = cls.query.filter_by(id=id)
        if record.first():
            record.delete()
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def check_employee_exists(cls, email):
        record = cls.query.filter_by(email=email).first()
        if record:
            return True
        else:
            return False