from flask import render_template, flash, url_for, request, redirect, url_for, session
from werkzeug.security import generate_password_hash
from models.employee_model import EmployeeModel
from models.department_model import DepartmentModel
from models.salary_group_model import SalaryGroupModel
from models.users import User

class Dashboard:

    @staticmethod
    def dashboard():
        if session:

            username = session['username']
            user_role = session['role']

            # stats
            all_employees = EmployeeModel.fetch_all()
            all_departments = DepartmentModel.fetch_all()
            all_salary_groups = SalaryGroupModel.fetch_all()
            all_users = User.fetch_all()

            if request.method == 'POST':
                fname = request.form['fname']
                lname = request.form['lname']
                email = request.form['email']
                password = request.form['password']
                role = request.form['role']

                username = fname[0].upper() + lname.title()

                email.lower()

                record = User(username=username,first_name=fname.title(), last_name=lname.title(), email=email, password=generate_password_hash(password), role=role)
                record.create()
                flash('user successfully created', 'success')
                return redirect(url_for('dashboard'))

            return render_template('dashboard.html', emps=len(all_employees),depts=len(all_departments),sgs=len(all_salary_groups), 
                                    users=len(all_users), allusers=all_users, username=username, role=user_role)
        else:
            flash("Unauthorized!", "danger")
            return redirect(url_for('login'))