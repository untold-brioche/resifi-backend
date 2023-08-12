from flask import Blueprint, request, jsonify
from flask.views import MethodView

test_blueprint = Blueprint("test_blueprint", __name__)

class HelloWorldAPI(MethodView):
    def get(self):
        return jsonify(dict(
            hello="world"
        )), 200

test_blueprint.add_url_rule(
    "/test/helloworld", view_func=HelloWorldAPI.as_view("hello_world_api", methods=["GET"])
)
