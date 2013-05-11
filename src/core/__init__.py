# Flask imports
from flask import Flask
from flask.ext.assets import Environment, Bundle
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from settings import BASEDIR

# Python imports
import os

# Configuring Flask Application
app = Flask(__name__)
app.config.from_object("core.settings")

# Web Assets Configuration
webAssets = Environment(app)
webAssets.register("js_lib", Bundle("js/underscore.js",
                        "js/jquery.js", "js/backbone.js",
                        filters="jsmin",
                        output="assets/min.libs.js"))
webAssets.register("js_main", Bundle("js/main.js", filters="jsmin",
                        output="assets/min.main.js"))

# Configuring database
db = SQLAlchemy(app)

# Configuring Flask login
lm = LoginManager()
lm.setup_app(app)

# Configuring OpenID
oid = OpenID(app, os.path.join(BASEDIR, 'tmp'))

__import__("core.models")
__import__("core.views")

