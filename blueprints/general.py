from flask import Blueprint

app = Blueprint('general', __name__)


@app.route('/')
def main():
    return 'This is main page!'


@app.route('/contact')
def contact():
    return 'This is contact page!'


@app.route('/about')
def about():
    return 'This is about page!'
