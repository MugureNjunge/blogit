from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
# from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] ='d78e69eb079c01200c9732204cb2aa12'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///codeblog.db'


# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'blogit'
app.config['MAIL_PASSWORD'] = '42625435'
mail = Mail(app)

from app import views