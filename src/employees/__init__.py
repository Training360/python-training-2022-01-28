from flask import Flask
from flask_migrate import Migrate

from .controllers import employees
from .webcontrollers import employeesweb
from .database import db, ma

import os

app = Flask(__name__)

DEFAULT_DATABASE_URI = 'postgresql://employees:employees@localhost/employees'
DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", DEFAULT_DATABASE_URI)
app.logger.info(f"Database URI: {DATABASE_URI}")

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "employees"

db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(employees)
app.register_blueprint(employeesweb)
