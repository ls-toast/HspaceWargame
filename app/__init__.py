from flask import Flask

app = Flask(__name__)

from app.web.index import main as main

app.register_blueprint(main)
