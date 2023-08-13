from resifi.server import db
from resifi.server.item.models import Item
from resifi.server.business.models import Business
from resifi.server.inventory.models import InventoryItem
from resifi.server.charity.models import Charity

items = [
    {
        "id": 1,
        "name": "Bottle",
        "description": "A bottle",
        "price": 10.0,
    },
    {
        "id": 2,
        "name": "Cup",
        "description": "A cup",
        "price": 5.0,
    },
    {
        "id": 3,
        "name": "Plate",
        "description": "A plate",
        "price": 15.0,
    },
    {
        "id": 4,
        "name": "Fork",
        "description": "A fork",
        "price": 2.0,
    },
    {
        "id": 5,
        "name": "Spoon",
        "description": "A spoon",
        "price": 2.0,
    },
    {
        "id": 6,
        "name": "Knife",
        "description": "A knife",
        "price": 2.0,
    },
    {
        "id": 7,
        "name": "Bowl",
        "description": "A bowl",
        "price": 10.0,
    },
    {
        "id": 8,
        "name": "Mug",
        "description": "A mug",
        "price": 5.0,
    },
    {
        "id": 9,
        "name": "Saucer",
        "description": "A saucer",
        "price": 5.0,
    },
    {
        "id": 10,
        "name": "Glass",
        "description": "A glass",
        "price": 5.0,
    },
]


def seed_items():
    for item in items:
        new_item = Item(
            id=item["id"],
            name=item["name"],
            description=item["description"],
            price=item["price"],
        )
        db.session.add(new_item)
        db.session.commit()
        print("Added item")
    print(f"Seeded ({len(items)}) items")


# https://www.feedingamerica.org/find-your-local-foodbank
charities = [
    {
        "id": 2,
        "name": "Food Bank of the Rockies",
        "address": "10700 E. 45th Ave, Denver, CO 80239",
    },
    {
        "id": 4,
        "name": "City Harvest Food Bank",
        "address": "150 52nd Street, Brooklyn, NY 11232",
    },
]


def seed_charities():
    for charity in charities:
        new_charity = Charity(
            id=charity["id"],
            name=charity["name"],
            address=charity["address"],
        )
        db.session.add(new_charity)
        db.session.commit()
        print("Added charity")
    print(f"Seeded ({len(charities)}) charities")


businesses = [
    {
        "id": 1,
        "name": "Resifi",
        "address": "123 Main St, San Francisco, CA 94122",
    },
    {
        "id": 2,
        "name": "Resifi",
        "address": "123 Main St, San Francisco, CA 94122",
    },
    {
        "id": 3,
        "name": "Resifi",
        "address": "123 Main St, San Francisco, CA 94122",
    },
    {
        "id": 4,
        "name": "Resifi",
        "address": "123 Main St, San Francisco, CA 94122",
    },
    {
        "id": 5,
        "name": "Resifi",
        "address": "123 Main St, San Francisco, CA 94122",
    },
]


def seed_businesses():
    for business in businesses:
        new_business = Business(
            id=business["id"],
            name=business["name"],
            address=business["address"],
        )
        db.session.add(new_business)
        db.session.commit()
        print("Added business")
    print(f"Seeded ({len(businesses)}) businesses")


inventory_items = [
    {
        "id": 1,
        "business_id": 1,
        "item_id": 1,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 2,
        "business_id": 1,
        "item_id": 2,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 3,
        "business_id": 1,
        "item_id": 3,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 4,
        "business_id": 1,
        "item_id": 4,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 5,
        "business_id": 1,
        "item_id": 5,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 6,
        "business_id": 1,
        "item_id": 6,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 7,
        "business_id": 1,
        "item_id": 7,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 8,
        "business_id": 1,
        "item_id": 8,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 9,
        "business_id": 1,
        "item_id": 9,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 10,
        "business_id": 1,
        "item_id": 10,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 11,
        "business_id": 2,
        "item_id": 1,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 12,
        "business_id": 2,
        "item_id": 2,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 13,
        "business_id": 2,
        "item_id": 3,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 14,
        "business_id": 3,
        "item_id": 4,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 15,
        "business_id": 4,
        "item_id": 5,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 16,
        "business_id": 2,
        "item_id": 6,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 17,
        "business_id": 2,
        "item_id": 7,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 18,
        "business_id": 2,
        "item_id": 8,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 19,
        "business_id": 2,
        "item_id": 9,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
    {
        "id": 20,
        "business_id": 3,
        "item_id": 10,
        "dist_saved": 100,
        "count_saved": 10,
        "money_saved": 1000,
    },
]


def seed_inventory_items():
    for inventory_item in inventory_items:
        new_inventory_item = InventoryItem(
            id=inventory_item["id"],
            business_id=inventory_item["business_id"],
            item_id=inventory_item["item_id"],
            dist_saved=inventory_item["dist_saved"],
            count_saved=inventory_item["count_saved"],
            money_saved=inventory_item["money_saved"],
        )
        db.session.add(new_inventory_item)
        db.session.commit()
        print("Added inventory item")
    print(f"Seeded ({len(inventory_items)}) inventory items")


def seed_all():
    seed_items()
    seed_charities()
    seed_businesses()
    # this happens during execution
    #seed_inventory_items()
    print("Seeded all")
