from resifi.server import db


class Charity(db.Model):
    # id should auto increment
    id = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    def as_dict(self):
        return {"id": self.id, "name": self.name, "address": self.address}
