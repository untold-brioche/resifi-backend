from flask import Blueprint, jsonify
from flask.views import MethodView

business_blueprint = Blueprint("business_blueprint", __name__)

#class HelloWorldAPI(MethodView):
#    def get(self):
#        return jsonify({"hello": "world"})

#business_blueprint.add_url_rule(
#    "/test/helloworld", view_func=HelloWorldAPI.as_view("hello_world_api"), methods=["GET"]
#)

# once the above is implemented, uncomment the lines to register this in /resifi/server/__init__.py
