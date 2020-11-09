from flask import render_template,flash,redirect,url_for,request, session
from werkzeug.security import generate_password_hash
from models.users import User

class AuthController:

    @staticmethod
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            if User.check_email_exists(email=email):
                if User.validate_password(email=email, password=password):
                    user = User.get_user(email=email)
                    session['username'] = user.username
                    session['role'] = user.role
                    session['logged_in'] = True
                    return redirect(url_for('dashboard'))
                else:
                    flash('Invalid credentials', 'danger')
                    return redirect(url_for('login'))
            else:
                flash('Invalid credentials', 'danger')
                return redirect(url_for('login'))

        return render_template('login.html')

    @staticmethod
    def register():
        if request.method == 'POST':
            first_name: str = request.form['fname'] 
            last_name: str = request.form['lname']
            email: str = request.form['email'] 
            password = request.form['password'] 
            username = first_name[0].upper() + last_name.title()

            email.lower()

            if User.check_email_exists(email=email):
                flash("User already exists", "danger")
                return redirect(url_for('login'))
            else:
                record = User(username=username,first_name=first_name.title(), last_name=last_name.title(), email=email, password=generate_password_hash(password), role=0)
                record.create()
                flash("User has successfully been created!", 'success')
                return redirect(url_for('login'))
        return render_template('register.html')
                
            
