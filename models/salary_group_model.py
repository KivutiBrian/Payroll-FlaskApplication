from main import db

class SalaryGroupModel(db.Model):
    __tablename__ = 'salary_groups'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    basic_salary = db.Column(db.String(), nullable=False)
    house_rent_allowance = db.Column(db.String(), nullable=False)
    medical_allowance = db.Column(db.String(), nullable=False)
    employees = db.relationship('EmployeeModel', backref='salarygroup')

    # create
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    # read all
    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    # update
    @classmethod
    def edit_record(cls, record_id,title, bs,hra,ma):
        record = cls.query.filter_by(id=record_id).first()
        if record:
            record.title = title
            record.basic_salary = bs
            record.house_rent_allowance = hra
            record.medical_allowance = ma
            db.session.commit()
            return True
        else:
            return False

    # delete
    @classmethod
    def delete_record(cls, id):
        record = cls.query.filter_by(id=id)
        if record.first():
            record.delete()
            db.session.commit()
            return True
        else:
            return False

            