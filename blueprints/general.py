from flask import Blueprint, render_template

from models.product import Product

app = Blueprint('general', __name__)


@app.route('/')
def home():
    products = Product.query.all()
    return render_template("home.html", products=products)


@app.route('/contact/')
def contact():
    return render_template("contact.html")


@app.route('/about/')
def about():
    return render_template("about.html")
