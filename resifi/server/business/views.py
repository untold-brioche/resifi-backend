from flask import Blueprint, jsonify
from resifi.server.business.models import Business
from flask.views import MethodView
from resifi.server import db
from flask import request
from resifi.server.utils import generate_id
from resifi.server import auth

business_blueprint = Blueprint("business_blueprint", __name__)


class BusinessAPI(MethodView):
    def get(self, id=-1):
        if id == -1:
            businesses = Business.query.all()
            return jsonify(
                {
                    "items": [business.as_dict() for business in businesses],
                    "count": len(businesses),
                }
            )
        business = Business.query.get(id)
        if not business:
            return jsonify({"error": "No business found with that id."}), 404
        return jsonify(business.as_dict())

    @auth.login_required
    def post(self):
        data = request.json
        name = data.get("name")
        address = data.get("address")

        if not name or not address:
            return (
                jsonify({"error": "Both 'name' and 'address' are required."}),
                400,
            )

        id = generate_id()
        new_business = Business(id=id, name=name, address=address)
        # Assuming you're using some kind of database session and committing changes
        db.session.add(new_business)
        db.session.commit()
        return (
            jsonify({"id": id, "name": name, "address": address}),
            201,
        )


business_view = BusinessAPI.as_view("business_api")
business_blueprint.add_url_rule(
    "/business/<id>", view_func=business_view, methods=["GET"]
)

business_blueprint.add_url_rule(
    "/business", view_func=business_view, methods=["GET", "POST"]
)
