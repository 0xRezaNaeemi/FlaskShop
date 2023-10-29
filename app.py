from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blueprints.general import app as general
from blueprints.user import app as user
from blueprints.admin import app as admin

# create sqlalchemy object as db
db = SQLAlchemy()

# create the app
app = Flask(__name__)

# register blueprints
app.register_blueprint(general)
app.register_blueprint(user)
app.register_blueprint(admin)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# initialize the app with the extension
db.init_app(app)

# create database
with app.app_context():
    db.create_all()

# runserver
if __name__ == '__main__':
    app.run()
