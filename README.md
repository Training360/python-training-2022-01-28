# Employees Python webapp

## Kiinduló projekt

```
pyproject.toml
setup.cfg
src/employees/__init__.py
src/employees/controllers.py
```

Függőség: `flask`
Blueprint

```shell
python -m venv venv
python -m pip install --upgrade pip
pip install -e .

set FLASK_APP=employees
set FLASK_ENV=development
flask run
```

Error: While importing 'employees', an ImportError was raised.
No traceback
https://github.com/pallets/flask/issues/4307


## Kódolási konvenciók

### Pylint

Pylint error
https://github.com/anybox/pylint_flask_sqlalchemy/issues/3

### flake8

`setup.cfg`

```shell
pip install -e .[test]
```

Code: F1 / Python: Select Linter

## Adatbázis

```shell
docker run -d -e POSTGRES_DB=employees -e POSTGRES_USER=employees -e POSTGRES_PASSWORD=employees -p 5432:5432  --name  employees-postgres postgres
```

`setup.cfg`

```
flask_sqlalchemy
psycopg2
```

```
database.py
__init__.py
models.py
```

`SQLALCHEMY_ECHO`

```sql
CREATE TABLE employee (id SERIAL NOT NULL, name VARCHAR(100),PRIMARY KEY (id))
```

`tests/employees.http`

## Repo

`@classmethod` in `class Employee`

## Controller

`201`, `204`
`errorhandler`

## DTO

`flask-marshmallow`, `marshmallow-sqlalchemy`, `marshmallow`

`EmployeeSchema`

## Logger

```python
current_app.logger.info(f"Employee: {employee}")
```

## Debug

## Migration

`__init__.py`

```python
migrate = Migrate(app, db)
```

`Flask-Migrate`

```shell
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## Integrációs tesztek

`pytest`, `test_employees.py`

## Mockolás

`pytest-mock`, `test_employees_mock.py`

## Docker előkészítés db hozzáférés

`os.environ.get`

## Docker

`Dockerfile`, `entrypoint.sh`, Docker Compose, `gunicorn`, `gevent`

## Server side

Blueprint

```
webcontrollers.py
templates
```

## Flash

`SECRET_KEY`

## Form validation

`Flask-WTF`

```
_formhelpers.html
```