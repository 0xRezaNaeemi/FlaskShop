from flask import Flask
from blueprints.general import app as general
from blueprints.user import app as user
from blueprints.admin import app as admin
import config
import extentions

# create the app
app = Flask(__name__)

app.config["SECRET_KEY"] = config.SECRET_KEY

# register blueprints
app.register_blueprint(general)
app.register_blueprint(user)
app.register_blueprint(admin)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
# initialize the app with the extension
extentions.db.init_app(app)

# create database
with app.app_context():
    extentions.db.create_all()

# runserver
if __name__ == '__main__':
    app.run(debug=True)
