from flask import Flask, render_template, session, flash,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from sqlalchemy.orm import Session

# database imports
from settings.db_config import Development

app = Flask(__name__)
app.config.from_object(Development)
db = SQLAlchemy(app)


#model
from models.department_model import DepartmentModel
from models.employee_model import EmployeeModel
from models.salary_group_model import SalaryGroupModel
from models.salary_model import SalaryModel
from models.users import User

# import controllers
from controllers import (auth,dashboard_controller, department, employee, salary_groups)


@app.before_first_request
def create_table():
    db.create_all()


# create a login required wrapper for user
def login_required(f): #define a function whose first parameter is f, which is convention for the fact that it wraps a function
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized! Please log in','danger')
            return redirect(url_for('login', next=request.url))
    return wrap

@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    flash('Successfully logged out!', 'success')
    return redirect(url_for('login'))


@app.route('/', methods=['GET','POST'])
def login():
    return auth.AuthController.login()


@app.route('/register', methods=['GET', 'POST'])
def register():
    return auth.AuthController.register()

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    return dashboard_controller.Dashboard.dashboard()
    

################################################################################################################################

@app.route('/add-salary-groups', methods=['GET', 'POST'])
@login_required
def add_salary_groups():
    return salary_groups.SalaryGroups.create_salary_group()


@app.route('/view-salary-groups', methods=['GET','POST'])
@login_required
def view_salary_groups():
    return salary_groups.SalaryGroups.view_salary_groups()


@app.route('/edit-salary-group/<int:id>', methods=['GET','POST'])
@login_required
def edit_salary_group(id):
    return salary_groups.SalaryGroups.edit_salary_group(sgid=id)

@app.route('/delete/<int:id>/salary-group', methods=['POST'])
@login_required
def delete_salary_group(id):
    return salary_groups.SalaryGroups.delete_salary_group(sgid=id)


@app.route('/salary-group/<int:id>/employees', methods=['GET','POST'])
@login_required
def salary_group_employees(id):
    return salary_groups.SalaryGroups.get_salary_group_employees(sgid=id)


###############################################################################################################################

@app.route('/add-department', methods=['GET','POST'])
@login_required
def add_department():
    return department.Department.create_department()


@app.route('/view-departments', methods=['GET', 'POST'])
@login_required
def view_departments():
    return department.Department.view_departments()


@app.route('/edit/<int:id>/departments', methods=['POST'])
@login_required
def edit_department(id):
    return department.Department.update_department(did=id)


@app.route('/delete/<int:id>/departments',methods=['POST'])
@login_required
def delete_department(id):
    return department.Department.delete_department(did=id)


@app.route('/department/<int:id>/employees', methods=['GET','POST'])
@login_required
def department_employees(id):
    return department.Department.get_department_employees(id=id)

##############################################################################################################################

@app.route('/add-employee', methods=['GET','POST'])
@login_required
def add_employee():
    return employee.Employee.create_employee()

@app.route('/view-employees', methods=['GET', 'POST'])
@login_required
def view_employees():
    return employee.Employee.view_employees()

@app.route('/edit/<int:id>/employees', methods=['POST'])
@login_required
def edit_employees(id):
    return employee.Employee.edit_employee(id=id)

@app.route('/delete/<int:id>/employees', methods=['POST'])
@login_required
def delete_employee(id):
    return employee.Employee.delete_record(id=id)

@app.route('/employee/<int:id>/generate-payroll', methods=['GET', 'POST'])
@login_required
def generate_employee_payroll(id):
    return employee.Employee.employee_payroll(id=id)

