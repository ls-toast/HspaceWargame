from flask import Flask

app = Flask(__name__)

from .views import index as main
from .views import register as register
from .views import login as login

app.register_blueprint(main.main)
app.register_blueprint(register.register)
app.register_blueprint(login.login)
