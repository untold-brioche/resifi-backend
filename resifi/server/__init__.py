from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection
from resifi.server.config import apply_config
from flask_httpauth import HTTPTokenAuth
from flask import jsonify
from geopy.geocoders import Nominatim

auth = HTTPTokenAuth(scheme="Bearer")

app = Flask(__name__)

with app.app_context():
    apply_config()

CORS(app)

db = SQLAlchemy(app)

geo = Nominatim(user_agent="resifi-server")


# https://stackoverflow.com/questions/57726047/
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


@auth.verify_token
def verify_token(token):
    if token == "basic-auth-token":
        return True
    return False


@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorized access"}), 401


from .business import business_blueprint

app.register_blueprint(business_blueprint)

from .charity import charity_blueprint

app.register_blueprint(charity_blueprint)

from .inventory import inventory_blueprint

app.register_blueprint(inventory_blueprint)

from .item import item_blueprint

app.register_blueprint(item_blueprint)

from resifi.server.returns.views import return_blueprint

app.register_blueprint(return_blueprint)

from resifi.server.savings.views import savings_blueprint

app.register_blueprint(savings_blueprint)

from .shipping_label import shipping_label_blueprint

app.register_blueprint(shipping_label_blueprint)

from .pdfservice import pdf_blueprint

app.register_blueprint(pdf_blueprint)

from .seed import seed_blueprint

app.register_blueprint(seed_blueprint)
