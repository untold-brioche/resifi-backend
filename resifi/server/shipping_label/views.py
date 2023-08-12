from flask import Blueprint, jsonify
from flask.views import MethodView
import random
import os
import base64

shipping_label_blueprint = Blueprint("shipping_label_blueprint", __name__)


# NOTE you can't just send images in response body, so it's base64 encoded


class ShippingLabelAPI(MethodView):
    def get(self, id):
        num_shipping_labels = 2
        random_num = random.randint(1, num_shipping_labels)
        shipping_label_path = os.path.join(
            os.path.dirname(__file__), f"shipping-label-{random_num}.png"
        )
        with open(shipping_label_path, "rb") as image_file:
            image_data = image_file.read()
        image_data_base64 = base64.b64encode(image_data).decode("utf-8")
        return jsonify({"shipping_label": image_data_base64})


shipping_label_blueprint.add_url_rule(
    "/shipping-label/<id>",
    view_func=ShippingLabelAPI.as_view("shipping_label_api"),
    methods=["GET"],
)
