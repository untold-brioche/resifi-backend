from flask import Blueprint, jsonify
from flask.views import MethodView
from resifi.server.inventory.models import InventoryItem

savings_blueprint = Blueprint("savings_blueprint", __name__)


class SavingsAPI(MethodView):
    def get(self, id):
        items = InventoryItem.query.filter_by(business_id=id).all()
        total_distance = sum([item.dist_saved for item in items])
        total_count = sum([item.count_saved for item in items])
        total_money = sum([item.money_saved for item in items])
        res = {
            "distance_saved": total_distance,
            "count_saved": total_count,
            "money_saved": total_money,
        }
        return jsonify(res)


savings_blueprint.add_url_rule(
    "/business/<id>/savings",
    view_func=SavingsAPI.as_view("savings_api"),
    methods=["GET"],
)
