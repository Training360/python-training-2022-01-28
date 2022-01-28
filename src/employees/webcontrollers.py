from flask import Blueprint, current_app, flash, jsonify, make_response, redirect, render_template, request, url_for
from sqlalchemy.orm.exc import NoResultFound
from wtforms import Form, StringField, validators
from . import models

employeesweb = Blueprint('employeesweb', __name__, template_folder='templates')


class EmployeeForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])


@employeesweb.route("/employees", methods=["GET"])
def list_employees():
    return render_template("employees.html", employees=models.find_all(), form=EmployeeForm())


@employeesweb.route("/employees", methods=["POST"])
def save_employee():
    form = EmployeeForm(request.form)
    # models.save({"name": request.form.get("name")})
    if form.validate():
        flash("Created")
        models.save({"name": form.name.data})
        return redirect(url_for("employeesweb.list_employees"))
    current_app.logger.info(f"Errors: {form._fields.get('name').errors}")
    
    return render_template("employees.html", employees=models.find_all(), form=form)
