from flask import Blueprint, jsonify
from flask.views import MethodView
from resifi.server.item.models import Item
from resifi.server import db
from flask import request
from resifi.server.utils import generate_id
from resifi.server import auth

item_blueprint = Blueprint("item_blueprint", __name__)


class ItemAPI(MethodView):
    def get(self, id=-1):
        if id == -1:
            items = Item.query.all()
            return jsonify(
                {"items": [item.to_dict() for item in items], "count": len(items)}
            )
        item = Item.query.get(id)
        if not item:
            return jsonify({"error": "Item not found"}), 404
        return jsonify(item.to_dict())

    @auth.login_required
    def post(self):
        data = request.json
        required_fields = [
            "name",
            "description",
            "price",
        ]

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return (
                jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}),
                400,
            )

        new_item = Item(
            id=generate_id(),
            name=data["name"],
            description=data["description"],
            price=data["price"],
        )

        db.session.add(new_item)
        db.session.commit()

        return (
            jsonify(
                {
                    "message": "Item successfully added",
                    "item": new_item.to_dict(),
                }
            ),
            201,
        )


view_func = ItemAPI.as_view("item_api")
item_blueprint.add_url_rule(
    "/item/<id>",
    view_func=view_func,
    methods=["GET"],
)

item_blueprint.add_url_rule(
    "/item",
    view_func=view_func,
    methods=["GET", "POST"],
)
