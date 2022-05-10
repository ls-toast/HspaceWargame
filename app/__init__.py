from flask import Flask

app = Flask(__name__)

from app.web.index import main as main
from app.web.register import register as register

app.register_blueprint(main)
app.register_blueprint(register)
