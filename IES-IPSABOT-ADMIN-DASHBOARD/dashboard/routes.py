import time

import requests
from flask import render_template, flash, redirect, url_for
from flask_login import login_required, logout_user, login_user

from dashboard import app, db
from dashboard.forms import LoginForm, RegisterForm, AlertForm
from dashboard.models import Login

# API BASE URL
API = "http://127.0.0.1:8000"
CHARTS_END_POINT = "/chart/all"
ALERTS_END_POINT = "/alert"
STUDENT_END_POINT = "/student"
USER_END_POINT = "/user"
CG_END_POINT = "/cg"
NOTE_END_POINT = "/note"


# ############## LOGIN/LOG-OUT/REGISTER ####################################

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = Login.query.filter_by(username=form.username.data).first()
        if not attempted_user:
            flash('Could not log-in. Invalid username or password.', category='danger')

        else:
            login_user(attempted_user, remember=form.remember_me.data)
            return redirect(url_for('home_page'))

    return render_template('login_page.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = Login(username=form.username.data, first_name=form.first_name.data,
                               last_name=form.last_name.data,
                               designation=form.designation.data,
                               password=form.password.data, image_url=form.image_url.data)

        db.session.add(user_to_create)
        db.session.commit()
        print(user_to_create)

        flash(f"User '{form.username.data}' Created Successfully!", category="success")

    if form.errors != {}:
        # if at least 1 error in form validators
        for error_msg in form.errors.values():
            flash(f"{error_msg[0]}", category='danger')

    return render_template('register_page.html', form=form)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('login'))


# ############## HOME PAGE ####################################

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@login_required
def home_page():
    # get the statistic data for dashboard from the api
    print("Requesting for data...")
    start = time.time()
    response = requests.get(API + CHARTS_END_POINT)
    print(f"Time Taken: {round(time.time() - start, 2)}s")

    if response.status_code == 200:
        response = response.json()
        users_data = response[0]
        students_data = response[1]
        faculty_data = response[2]
        notes_data = response[3]

        print(users_data)
        print(students_data)
        print(notes_data)
        print(faculty_data)
    else:
        users_data = []
        students_data = []
        notes_data = []
        faculty_data = []

    print("Now rendering the template..")
    return render_template('home_page.html', user_data=users_data, student_data=students_data, notes_data=notes_data,
                           faculty_data=faculty_data)


# ############## MENU ####################################

@app.route('/users', methods=['GET'])
@login_required
def users_page():
    response = requests.get(url=API + USER_END_POINT)

    if response.status_code == 200:
        response = response.json()
    else:
        flash(f"An error occurred! Alert Could not be load users data.", category="danger")

    return render_template('users_page.html', users=response)


@app.route('/students', methods=['GET'])
@login_required
def students_page():
    response = requests.get(url=API + STUDENT_END_POINT)

    if response.status_code == 200:
        response = response.json()
    else:
        flash(f"An error occurred! Alert Could not be load students.", category="danger")

    return render_template('students_page.html', students=response)


@app.route('/campus_guide', methods=['GET'])
@login_required
def campus_guide_page():
    response = requests.get(url=API + CG_END_POINT)

    if response.status_code == 200:
        response = response.json()
    else:
        flash(f"An error occurred! Alert Could not be load campus-guide data.", category="danger")

    return render_template('campus_guide_page.html', faculty=response)


@app.route('/trigger_scheduler', methods=['GET'])
@login_required
def trigger_schedulers_page():
    # todo: send a check request to api

    return render_template('schedulers.html')


@app.route('/notes', methods=['GET'])
@login_required
def notes_page():
    # todo: get notes data using api and render to template

    return render_template('notes_page.html')


@app.route('/alerts', methods=['GET'])
@login_required
def alerts_page():
    return render_template('alerts_page.html', form=AlertForm())


# ########### SEND ALERTS #####################3
@app.route('/alerts/send', methods=['GET', 'POST'])
def send_alerts():
    form = AlertForm()

    if form.validate_on_submit():
        send_alert_to = form.send_to.data
        alert_message = form.alert_message.data

        # message body as in api-documentation
        alert = {
            "alert_msg_sender": "ADMIN",
            "alert_msg_text": alert_message.strip(),
            "alert_msg_code": send_alert_to
        }

        response = requests.post(url=API + ALERTS_END_POINT, json=alert)

        if response.status_code == 200:
            flash(f"Alert Request Sent Successfully!", category="success")
        else:
            flash(f"An error occurred! Alert Could not be send", category="danger")

    if form.errors != {}:
        # if at least 1 error in form validators
        for error_msg in form.errors.values():
            flash(f"{error_msg[0]}", category='danger')

    return render_template('alerts_page.html', form=form)


# ############## ERROR PAGE ####################################
@app.errorhandler(500)
def internal_error(error):
    return render_template('error-500.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('error-404.html')

# ###############################################################
