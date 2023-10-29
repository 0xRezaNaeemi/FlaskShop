from flask import Blueprint
from models import user

app = Blueprint('user', __name__)


@app.route('/user')
def user():
    return 'This is user page!'

