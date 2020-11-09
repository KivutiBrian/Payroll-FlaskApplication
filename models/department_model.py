from main import db
from sqlalchemy import func

class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.String(),default=func.now(), nullable=False)
    employees = db.relationship('EmployeeModel', backref='department')

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
    def update(cls, id, title, desc):
        record = cls.query.filter_by(id=id).first()
        if record:
            record.title = title
            record.description = desc
            db.session.commit()
            return True
        else:
            return False

    # delete
    @classmethod
    def delete(cls, id):
        record = cls.query.filter_by(id=id)
        if record.first():
            record.delete()
            db.session.commit()
            return True
        else:
            return False