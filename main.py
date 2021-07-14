from app import create_app, db
import click


app = create_app()
# app.cli.run()  # https://flask.palletsprojects.com/en/2.0.x/cli/


@app.shell_context_processor
def make_shell_context():
    from app.models import Role, Department, Employee
    return {
        'app': app,
        'db': db,
        'Role': Role,
        'Department': Department,
        'Employee': Employee
    }
