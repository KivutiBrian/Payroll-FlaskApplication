from flask import render_template, redirect, url_for, flash,request,session
from models.department_model import DepartmentModel
from models.salary_group_model import SalaryGroupModel
from models.employee_model import EmployeeModel
from models.salary_model import SalaryModel

from utils.payroll2 import TaxCalculator

class Employee:

    @staticmethod
    def create_employee():
        if session:

            username = session['username']

            departments = DepartmentModel.fetch_all()
            salary_groups = SalaryGroupModel.fetch_all()

            if request.method == 'POST':
                surname = request.form['surname']
                fname = request.form['fname']
                lname = request.form['lname']
                email = request.form['email']
                phone_number = request.form['phone_number']
                salary_group_id = request.form['salary_group']
                department_id = request.form['department']

                if EmployeeModel.check_employee_exists(email=email):
                    flash('Email already in use', 'danger')
                    return redirect(url_for('add_employee'))

                record = EmployeeModel(surname=surname, first_name=fname, last_name=lname, email=email,
                                            phone_number=phone_number,sgid=salary_group_id,did=department_id)
                
                record.create()
                flash('New employee record successfully created', 'success')
                return redirect(url_for('add_employee'))

            return render_template('add-employee.html', departments=departments, sgroups=salary_groups,username=username)
        else:
            return redirect(url_for('login'))


    @staticmethod
    def view_employees():
        if session:
            username = session['username']
            employees = EmployeeModel.fetch_all()
            return render_template('view-employees.html', employees=employees, username=username)
        else:
            return redirect(url_for('login'))

    @staticmethod
    def edit_employee(id:int):
        if session:
            if request.method == 'POST':
                surname = request.form['surname']
                fname = request.form['fname']
                lname = request.form['lname']
                email = request.form['email']
                phone_number = request.form['phone_number']
                salary_group_id = request.form['salary_group']
                department_id = request.form['department']

                if EmployeeModel.update(id=id, surname=surname,fname=fname,lname=lname,email=email,pno=phone_number,sgid=salary_group_id,did=department_id ):
                    flash('record successfully updated', 'success')
                    return redirect(url_for('view_employees'))
                else:
                    flash('unable to delete record', 'danger')
                    return redirect(url_for('view_employees'))
        return redirect(url_for('login'))
    
    @staticmethod
    def delete_record(id:int):
        if session:

            if request.method == 'POST':
                if EmployeeModel.delete(id=id):
                    flash('record successfully deleted', 'success')
                    return redirect(url_for('view_employees'))
        else:
            return redirect(url_for('login'))

    @staticmethod
    def employee_payroll(id:int):
        if session:

            username = session['username']
            employee = EmployeeModel.query.filter_by(id=id).first()

            if request.method == 'POST':
                bs = float(request.form['bs'])
                hra = float(request.form['hra'])
                ma = float(request.form['ma'])
                period = request.form['period']

                benefits = hra+ma
                calc = TaxCalculator(basic_salary=bs, benefits=benefits)
                
                record = SalaryModel(period=period, basic_salary=bs, benefits=benefits,nssf=calc.nssfContribution, nhif=calc.nhifContribution,
                                        taxable_income=calc.taxableIncome,payee=calc.payee,personal_relief=calc.personal_relief,
                                        tax_payable=calc.total_tax_payable,net_salary=calc.netSalary, employee_id=id)
                record.create()
                flash(f'Salary for period {period} has successfully been generated', 'success')
                return redirect(url_for('generate_employee_payroll', id=id))

            return render_template('view-employee-payroll.html', employee=employee,username=username)

        else:
            return redirect(url_for('login'))


# 192.168.10.2