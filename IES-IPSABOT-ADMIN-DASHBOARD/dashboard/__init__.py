from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL

# from dashboard.services.data_for_chart import get_student_count_by_branch, get_student_count_by_year
# from dashboard.services.data_for_chart import get_student_data, get_faculty_data, get_notes_data
# from dashboard.services.data_for_chart import get_users_count, get_unsubscribed_user_count
# from dashboard.services.student_service import get_all_students
# from dashboard.services.user_service import get_all_users
from database.local_settings import postgresql as db_cred
from database.local_settings import SECRET_KEY, alert_code

# ####################### CREATE APP ###############################

app = Flask(__name__)

# ################# SETTING FUNCTIONS IN JINJA'S GLOBAL SCOPE #########
#
# app.jinja_env.globals.update(get_all_users=get_all_users)
# app.jinja_env.globals.update(get_user_count=get_users_count)
# app.jinja_env.globals.update(get_all_students=get_all_students)
# app.jinja_env.globals.update(get_student_data=get_student_data)
# app.jinja_env.globals.update(get_faculty_data=get_faculty_data)
# app.jinja_env.globals.update(get_notes_data=get_notes_data)
# app.jinja_env.globals.update(get_student_count_by_year=get_student_count_by_year)
# app.jinja_env.globals.update(get_student_count_by_branch=get_student_count_by_branch)

# ################## CONFIG WITH SQLALCHEMY ##############

url = URL.create(drivername=db_cred['drivername'],
                 username=db_cred['pguser'],
                 password=db_cred['pgpasswd'],
                 host=db_cred['pghost'],
                 database=db_cred['pgdb'],
                 port=db_cred['pgport'])

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # to suppress FSADeprecationWarning

db = SQLAlchemy(app)

# ###########################################################

app.config['SECRET_KEY'] = SECRET_KEY  # secret key in order to use session

login_manager = LoginManager(app)  # will manage log-in log-out
login_manager.login_view = 'login'  # The name of the view to redirect to when the user needs to log in.
login_manager.login_message = 'You must be logged-in to see this page!!'
login_manager.login_message_category = "info"

from dashboard import routes
