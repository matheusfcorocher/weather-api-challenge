from flasgger import Swagger
from config import config

flasgger_template = {
  "info": {
    "title": config["swagger"]["title"],
    "description": config["swagger"]["description"],
    "version": config["swagger"]["version"],
  },
  "basePath": config["swagger"]["basePath"],
}

flasgger_swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": config["swagger"]["docsPath"]
}

def create_swagger_docs(app):
    Swagger(app, template=flasgger_template, config=flasgger_swagger_config)