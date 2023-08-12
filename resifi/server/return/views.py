from  flask import BluePrint, jsonify
from flask.views import MethodView

return_blueprint = Blueprint("return_blueprint", __name__)

class ReturnAPI(MethodView):
    pass

return_blueprint.add_url_rule(
    "/return",
    view_func=ReturnAPI.as_view("return_api"),
    methods=[],
)
