from resifi.server import db


class InventoryItem(db.Model):
    id = db.Column(db.String, primary_key=True)
    dist_saved = db.Column(db.Float)
    count_saved = db.Column(db.Integer)
    money_saved = db.Column(db.Float)
    business_id = db.Column(db.String, db.ForeignKey("business.id"))
    item_id = db.Column(db.String, db.ForeignKey("item.id"))
    item = db.relationship("Item", backref="inventory_item")

    def to_dict(self):
        return {
            "id": self.id,
            "dist_saved": self.dist_saved,
            "count_saved": self.count_saved,
            "money_saved": self.money_saved,
            "business_id": self.business_id,
            "item_id": self.item_id,
            "item": self.item.to_dict(),
        }
