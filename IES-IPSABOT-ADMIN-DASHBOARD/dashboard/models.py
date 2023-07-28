from flask_login import UserMixin

from dashboard import db
from dashboard import login_manager


@login_manager.user_loader
def load_user(user_id):
    return Login.query.get(int(user_id))


class Login(db.Model, UserMixin):
    __table_args__ = {"schema": "dashboard_sch"}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), unique=True)
    password = db.Column(db.String(length=50))
    first_name = db.Column(db.String(length=30))
    last_name = db.Column(db.String(length=30))
    designation = db.Column(db.String(length=30))
    image_url = db.Column(db.String())

    def __init__(self, username, password, first_name, last_name, designation, image_url):
        # self.id = id
        self.username = username
        self.password = password
        self.designation = designation
        self.first_name = first_name
        self.last_name = last_name
        self.image_url = image_url
        
    def __repr__(self):
        return f"<Login User {self.username}>"
