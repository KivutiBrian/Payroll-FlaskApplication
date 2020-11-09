from main import db
from sqlalchemy import func

class SalaryModel(db.Model):
    __tablename__ = 'salaries'
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.String, nullable=False)
    basic_salary = db.Column(db.Float, nullable=False)
    benefits = db.Column(db.Float, nullable=False)
    nssf = db.Column(db.Float, nullable=False)
    nhif = db.Column(db.Float, nullable=False)
    taxable_income = db.Column(db.Float, nullable=False)
    payee = db.Column(db.Float, nullable=False)
    personal_relief = db.Column(db.Float, nullable=False)
    tax_payable = db.Column(db.Float, nullable=False)
    net_salary = db.Column(db.Float, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    # create
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    # read all
    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    