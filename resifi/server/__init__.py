from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection
from resifi.server.config import apply_config

app = Flask(__name__)

with app.app_context():
    apply_config()

CORS(app)

db = SQLAlchemy(app)

# https://stackoverflow.com/questions/57726047/
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

from resifi.server.test.views import test_blueprint
app.register_blueprint(test_blueprint)