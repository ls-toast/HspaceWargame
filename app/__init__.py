from flask import Flask

app = Flask(__name__)

from app.web.index import main as main
from app.web.register import register as register
from app.web.login import login as login

app.register_blueprint(main)
app.register_blueprint(register)
app.register_blueprint(login)
