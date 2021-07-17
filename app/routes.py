from flask_graphql import GraphQLView
from app.schema import schema


def add_app_rule(app, uri, view, name, **view_params):
    app.add_url_rule(
        uri,
        view_func=view(
            name,
            **view_params
        )
    )


def graphql_url(app):
    add_app_rule(
        app,
        "/graphql",
        GraphQLView.as_view,
        "graphql",
        schema=schema,
        graphql=True
    )
