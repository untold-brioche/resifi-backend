from flask import Blueprint, jsonify
from flask.views import MethodView
from resifi.server.item.models import Item
from flask import request
from resifi.server.utils import generate_id
from resifi.server import auth
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

pdf_blueprint = Blueprint("pdf_blueprint", __name__)


class PDFServiceAPI(MethodView):
    @auth.login_required
    def post(self):
        data = request.json
        required_fields = [
            "name",
            "address",
            "item",
        ]

        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return (
                jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}),
                400,
            )

        pdf = generate_pdf(data["name"], data["address"], data["item"])

        return (
            jsonify(
                {
                    "message": "PDF Created",
                    "pdf": pdf,
                }
            ),
            201,
        )


def generate_pdf(name, address, item):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = "output.pdf"
    filepath = os.path.join(script_dir, filename)
    c = canvas.Canvas(filepath, pagesize=letter)
    width, height = letter
    c.drawString(100, height - 100, f"Name: {name}")
    c.drawString(100, height - 130, f"Address: {address}")
    c.drawString(100, height - 160, f"Item: {item}")
    c.save()
    return filepath


view_func = PDFServiceAPI.as_view("pdf_api")
pdf_blueprint.add_url_rule(
    "/pdf",
    view_func=view_func,
    methods=["POST"],
)
