from resifi.server import db
from datetime import datetime


class InventoryItem(db.Model):
    id = db.Column(db.String, primary_key=True)
    dist_saved = db.Column(db.Float)
    count_saved = db.Column(db.Integer)
    money_saved = db.Column(db.Float)
    business_id = db.Column(db.String, db.ForeignKey("business.id"))
    charity_id = db.Column(db.String, db.ForeignKey("charity.id"))
    item_id = db.Column(db.String, db.ForeignKey("item.id"))
    item = db.relationship("Item", backref="inventory_item")
    create_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_date = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "dist_saved": self.dist_saved,
            "count_saved": self.count_saved,
            "money_saved": self.money_saved,
            "business_id": self.business_id,
            "charity_id": self.charity_id,
            "item_id": self.item_id,
            "create_date": datetime.timestamp(self.create_date.now()),
            "item": self.item.to_dict(),
        }
