from flask import Blueprint

app = Blueprint('admin', __name__)


@app.route('/admin')
def admin():
    return 'This is admin page!'
