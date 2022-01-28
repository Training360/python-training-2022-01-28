from flask import Blueprint, current_app, jsonify, make_response, request
from sqlalchemy.orm.exc import NoResultFound
from . import models

employees = Blueprint('employees', __name__, template_folder='templates')


@employees.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@employees.route("/info")
def info():
    return '{"status" = "on"}'


@employees.route("/api/employees", methods=['GET'])
def find_all():
    # jsonify nélkül nem megy
    return jsonify(models.find_all())


@employees.route("/api/employees/<employee_id>", methods=['GET'])
def find_by_id(employee_id):
    employee = models.find_by_id(employee_id)
    current_app.logger.info(f"Employee: {employee}")
    return employee


@employees.route('/api/employees', methods=['POST'])
def save():
    return models.save(request.json), 201


@employees.route('/api/employees/<employee_id>', methods=['PUT'])
def update(employee_id):
    return models.update(employee_id, request.json), 200


@employees.route("/api/employees/<employee_id>", methods=['DELETE'])
def delete(employee_id):
    models.delete(employee_id)
    return "", 204


@employees.errorhandler(NoResultFound)
def handle_no_result_found(e):
    response = make_response(
        jsonify({"type": "not-found", "title": "Not found", "status": 404}),
        404)
    response.headers.set("Content-Type", "application/problem+json")
    return response
