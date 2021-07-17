# from app.models import Role, Department, Employee
from app import create_app
# from app.routes import graphql_url
import click


app = create_app()
app.app_context().push()


from app.routes import graphql_url
graphql_url(app)
# app.cli.run()  # https://flask.palletsprojects.com/en/2.0.x/cli/


@app.shell_context_processor
def make_shell_context():
    from app import db, Role, Department, Employee
    return {
        'app': app,
        'db': db,
        'Role': Role,
        'Department': Department,
        'Employee': Employee
    }
