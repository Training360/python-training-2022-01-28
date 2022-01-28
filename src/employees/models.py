from .database import db, ma


class Employee(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    @classmethod
    def create(cls, **kw):
        employee = cls(**kw)
        db.session.add(employee)
        db.session.commit()
        return employee

    @classmethod
    def find_by_id(cls, employee_id):
        return Employee.query.filter(Employee.id == employee_id).one()


class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        load_instance = True


def find_all():
    schema = EmployeeSchema(many=True)
    return schema.dump(Employee.query.order_by(Employee.name).all())


def find_by_id(employee_id):
    employee = Employee.find_by_id(employee_id)
    schema = EmployeeSchema()
    return schema.dump(employee)


def save(data):
    employee = Employee.create(name=data["name"])
    schema = EmployeeSchema()
    return schema.dump(employee)


def update(employee_id, data):
    employee = Employee.find_by_id(employee_id)
    employee.name = data['name']
    db.session.commit()
    schema = EmployeeSchema()
    return schema.dump(employee)


def delete(employee_id):
    employee = Employee.find_by_id(employee_id)
    db.session.delete(employee)
    db.session.commit()
