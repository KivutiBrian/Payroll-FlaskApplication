from flask import render_template, redirect, url_for, flash, request,session
from models.salary_group_model import SalaryGroupModel

class SalaryGroups:

    @staticmethod
    def create_salary_group():
        """create a new salary group"""
        if session:

            username = session['username']

            if request.method == 'POST':
                title = request.form['title']
                basic_salary = request.form['basic_salary']
                house_rent_allowance = request.form['hra']
                medical_allowance = request.form['ma']

                record = SalaryGroupModel(title=title,basic_salary=basic_salary,house_rent_allowance=house_rent_allowance,
                                        medical_allowance=medical_allowance)
                record.create()
                
                flash('Salary group successfully added', 'success')
                return redirect(url_for('add_salary_groups'))

            return render_template('add-salary-group.html', username=username)
        else:
            return redirect(url_for('login'))


    @staticmethod
    def view_salary_groups():
        """fetch all salary groups"""
        if session:

            username = session['username']

            salary_groups = SalaryGroupModel.fetch_all()
            return render_template('view-salary-groups.html', groups=salary_groups,username=username)
        else:
            return redirect(url_for('login'))

    @staticmethod
    def edit_salary_group(sgid:int):
        """ëdit salary group"""
        if session:

            if request.method == 'POST':
                title = request.form['title_edit']
                basic_salary = request.form['basic_salary_edit']
                house_rent_allowance = request.form['hra_edit']
                medical_allowance = request.form['ma_edit']

                if SalaryGroupModel.edit_record(record_id=sgid,title=title,bs=basic_salary,hra=house_rent_allowance,ma=medical_allowance):
                    flash('record updated sucessfully', 'success')
                    return redirect(url_for('view_salary_groups'))
                else:
                    flash('Error while updating record')
                    return redirect(url_for('view_salary_groups'))
        else:
            return redirect(url_for('login'))

    @staticmethod
    def delete_salary_group(sgid:int):
        """delete salary group"""
        if session:

            if request.method == 'POST':

                salary_group =  SalaryGroupModel.query.filter_by(id=sgid).first()

                if len(salary_group.employees ) > 0:
                    flash('Cannot delete salary group that contains employees', 'danger')
                    return redirect(url_for('view_salary_groups'))


                if SalaryGroupModel.delete_record(id=sgid):
                    flash('record successfully deleted', 'success')
                    return redirect(url_for('view_salary_groups'))
                else:
                    flash('Could not delete record', 'danger')
                    return redirect(url_for('view_salary_groups'))
        else:
            return redirect(url_for('login'))

    @staticmethod
    def get_salary_group_employees(sgid:int):
        if session:
            username = session['username']
        
            salary_group =  SalaryGroupModel.query.filter_by(id=sgid).first()
            return render_template('view-salary-groups-empl.html',salarygroup=salary_group, employees=salary_group.employees)
        else:
            return redirect(url_for('login'))




        


    
