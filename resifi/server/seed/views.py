from flask import Blueprint
from flask.views import MethodView
from .seed import seed_all
from resifi.server import db

seed_blueprint = Blueprint("seed_blueprint", __name__)


class SeedingAPI(MethodView):
    def get(self):
        db.drop_all()
        db.create_all()
        seed_all()
        return {"message": "Seeded database"}


seed_blueprint.add_url_rule(
    "/seed",
    view_func=SeedingAPI.as_view("seed_api"),
    methods=["GET"],
)
