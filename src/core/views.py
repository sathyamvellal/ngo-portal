# Local project imports
from core import app, lm
from core.models import User
from core.forms import LoginForm
import helpers as util

# Standard python imports
import json

# Third party imports
from flask import render_template, jsonify, request, g
from flask.ext.login import login_required, login_user, logout_user, current_user

# Application homepage
@app.route('/index')
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated():
		pass 
	return render_template('/login.html', form = LoginForm())

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    elif request.method == 'POST':
        return render_template("register.html")

@app.route('/copyright')
def copyright():
    return "Copyright Message Here"

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/partners")
def partners():
    return render_template("partners.html")

@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Other necessary functions
@lm.user_loader
def user_loader(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user;

# Application error handlers
@app.errorhandler(400)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
def not_found(error=None):
    message = {
            'code': error.code,
            'status': 'failure',
            'url': request.url,  # set the requested url
            'reason': error.name
    }
    resp = jsonify(message)  # generate a response object
    resp.status_code = error.code  # set the error status code
    return resp
