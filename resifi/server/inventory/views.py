from flask import Blueprint, jsonify
from flask.views import MethodView
from resifi.server.charity.models import Charity
from resifi.server.inventory.models import InventoryItem
from resifi.server import db
from flask import request
from resifi.server.utils import generate_id
from resifi.server import auth

inventory_blueprint = Blueprint("inventory_blueprint", __name__)


class InventoryAPI(MethodView):
    def get(self, id):
        items = InventoryItem.query.filter_by(business_id=id).all()
        return jsonify(
            {"items": [item.to_dict() for item in items], "count": len(items)}
        )

    @auth.login_required
    def post(self, id):
        data = request.json
        required_fields = [
            "dist_saved",
            "count_saved",
            "money_saved",
            "charity_id",
        ]

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return (
                jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}),
                400,
            )

        sent_charity = Charity.query(charity_id=data["charity_id"]).first()
        if sent_charity is None:
            return (
                jsonify({"error": f"No such charity: ID {data['charity_id']}"}),
                400,
            )

        new_item = InventoryItem(
            id=generate_id(),
            dist_saved=data["dist_saved"],
            count_saved=data["count_saved"],
            money_saved=data["money_saved"],
            business_id=id,
            charity_id=id,
        )

        db.session.add(new_item)
        db.session.commit()

        return (
            jsonify(
                {
                    "message": "Inventory item successfully added",
                    "inventory_item": new_item.to_dict(),
                }
            ),
            201,
        )


inventory_blueprint.add_url_rule(
    "/business/<id>/inventory",
    view_func=InventoryAPI.as_view("inventory_api"),
    methods=["GET", "POST"],
)
