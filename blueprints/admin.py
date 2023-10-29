from flask import Blueprint, render_template, request, redirect, session, abort
import config

app = Blueprint('admin', __name__)


@app.route('/admin/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD:
            session['admin_login'] = username
            return redirect("/admin/dashboard")
        else:
            return redirect("/admin/login")

    else:
        return render_template("admin/login.html")


@app.route("/admin/dashboard", methods=["GET"])
def dashboard():
    if session.get("admin_login", None) is None:
        abort(403)
    return render_template("admin/dashboard.html")


@app.route("/admin/dashboard/products", methods=["GET"])
def products():
    if session.get("admin_login", None) is None:
        abort(403)
    return render_template("admin/products.html")
