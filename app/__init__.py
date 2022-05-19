from flask import Flask

app = Flask(__name__)

from .views import index as main
app.register_blueprint(main.main)

from .views import register as register
app.register_blueprint(register.register)

from .views import login as login
app.register_blueprint(login.login)

from .views import ranking as rank
app.register_blueprint(rank.rank)