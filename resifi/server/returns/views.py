from random import random, shuffle
from flask import Blueprint, jsonify, request
from flask.views import MethodView
from resifi.server.business.models import Business
from resifi.server.charity.models import Charity
from resifi.server.inventory.models import InventoryItem
from resifi.server.item.models import Item
from resifi.server.utils import generate_id
from resifi.server import db

return_blueprint = Blueprint("return_blueprint", __name__)

class ReturnAPI(MethodView):
    def post(self):
        data = request.get_json()
        required_fields = [
            "item_id",
            "business_id",
        ]

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return (
                jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}),
                400,
            )

        item_id = data.get("item_id")
        business_id = data.get("business_id")

        business = Business.query.filter_by(id=business_id).first()
        return_item = Item.query.filter_by(id=item_id).first()

        if business == None:
            return (
                jsonify({"error": f"No such business: ID {business}"}),
                400,
            )
        if return_item == None:
            return (
                jsonify({"error": f"No such business: ID {business}"}),
                400,
            )

        charities = Charity.query.all()
        if charities is None or len(charities) == 0:
            return jsonify({"error": "No charities have been configured."}), 500

        shuffle(charities)

        charity_sent = charities[0]

        new_item = InventoryItem(
            id=generate_id(),
            dist_saved=random() * 48 + 2,
            count_saved=1,
            money_saved=return_item.price,
            business_id=business_id,
            charity_id=charity_sent.id,
            item_id=item_id
        )
        db.session.add(new_item)
        db.session.commit()

        return (
            jsonify(
                {
                    "message": "Return successfully performed",
                    "inventory_item": new_item.to_dict(),
                }
            ),
            201,
        )


return_blueprint.add_url_rule(
    "/return",
    view_func=ReturnAPI.as_view("return_api"),
    methods=["POST"],
)
