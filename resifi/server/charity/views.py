from flask import Blueprint, jsonify
from resifi.server.charity.models import Charity
from flask.views import MethodView
from resifi.server import db
from flask import request
import random
from resifi.server.utils import generate_id

charity_blueprint = Blueprint("charity_blueprint", __name__)


class CharityAPI(MethodView):
    def get(self, id=-1):
        if id == -1:
            charityes = Charity.query.all()
            return jsonify(
                {
                    "items": [charity.as_dict() for charity in charityes],
                    "count": len(charityes),
                }
            )
        charity = Charity.query.get(id)
        if not charity:
            return jsonify({"error": "No charity found with that id."}), 404
        return jsonify(charity.as_dict())

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
        new_charity = Charity(id=id, name=name, address=address)
        # Assuming you're using some kind of database session and committing changes
        db.session.add(new_charity)
        db.session.commit()
        return (
            jsonify({"id": id, "name": name, "address": address}),
            201,
        )


charity_view = CharityAPI.as_view("charity_api")
charity_blueprint.add_url_rule("/charity/<id>", view_func=charity_view, methods=["GET"])

charity_blueprint.add_url_rule(
    "/charity", view_func=charity_view, methods=["GET", "POST"]
)
