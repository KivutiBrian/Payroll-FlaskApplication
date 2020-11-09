from flask import render_template, redirect, url_for, flash, request,session
from models.department_model import DepartmentModel

class Department:

    @staticmethod
    def create_department():
        """"create"""
        if session:

            username = session['username']

            if request.method == 'POST':
                department_name = request.form['department_name']
                description = request.form['description']

                record = DepartmentModel(title=department_name, description=description)
                record.create()
                flash('new department successfully created', 'success')
                return redirect(url_for('add_department'))

            return render_template('add-department.html')
        else:
            return redirect(url_for('login'))

    @staticmethod
    def view_departments():
        if session:
            username = session['username']
            departments = DepartmentModel.fetch_all()
            return render_template('view-departments.html', departments=departments, username=username)
        else:
            return redirect(url_for('login'))


    @staticmethod
    def update_department(did:int):
        if request.method == 'POST':
            department_name = request.form['department_name_edit']
            description = request.form['description_edit']

            if DepartmentModel.update(id=did, title=department_name,desc=description):
                flash('record successfully updated', 'success')
                return redirect(url_for('view_departments'))
            else:
                flash('unable to update record', 'danger')
                return redirect(url_for('view_departments'))
                

    @staticmethod
    def delete_department(did:int):
        if session:
            if request.method == 'POST':
                dept = DepartmentModel.query.filter_by(id=did).first()

                if len(dept.employees) > 0 :
                    flash('This departments has employees! You cannot delete it', 'danger')
                    return redirect(url_for('view_departments'))
                else:

                    if DepartmentModel.delete(id=did):
                        flash('Departments has successfully been delete', 'success')
                        return redirect(url_for('view_departments'))
                    else:
                        flash('Error', 'danger')
                        return redirect(url_for('view_departments'))
        return redirect(url_for('login'))

    @staticmethod
    def get_department_employees(id:int):
        if session:

            username = session['username']

            dept = DepartmentModel.query.filter_by(id=id).first()

            return render_template('view-department-empl.html', department=dept, employees=dept.employees)
        else:
            return redirect(url_for('login'))

