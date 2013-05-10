from flask.ext.wtf import Form, TextField
from flask.ext.wtf import Required

class LoginForm(Form):
    openid = TextField('OpenID: ', validators = [Required()])
    passwd = TextField('Password: ', validators = [Required()])
