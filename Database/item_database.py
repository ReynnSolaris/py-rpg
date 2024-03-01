from Classes.Items.armor import Armor
from Classes.Items.item import Item
from Classes.Items.potion import HealthPotion
from Classes.Items.weapon import Weapon

class ItemDatabase:
    def __init__(self) -> None:
        self.items = {}
        self.current_item_id = 1

        # Create instances of weapons and add them to the items dictionary
        self.add_weapon("Fists", "Default Weapon ||Cannot Be Dropped / Discarded / Sold||", 0, {"min": 1, "max": 2}, "blunt")
        self.add_weapon("Iron Sword", "", 10, {"min": 3, "max": 5}, "sharp")
        self.add_weapon("Short Bow", "", 10, {"min": 3, "max": 5}, "ranged")
        self.add_weapon("Iron Spear", "", 10, {"min": 3, "max": 5}, "sharp")

        self.add_weapon("Developer Golden Longsword", "", 1e9, {"min": 30, "max": 54}, "sharp", "legendary")

        self.add_potion("Health Potion", "Restores health when consumed.", 5, 10, "common")

        self.add_armor("Leather Armor", "Basic leather protection.", 8, "common")

    def add_item(self, name, description, value, item_type, rarity="common"):
        item_id = self.current_item_id
        self.items[item_id] = Item(name=name, description=description, value=value, item_type=item_type, rarity=rarity, id=item_id)
        self.current_item_id += 1

    def add_weapon(self, name, description, value, damage, weapon_type, rarity="common"):
        item_id = self.current_item_id
        self.items[item_id] = Weapon(name=name, description=description, value=value, weapon_type=weapon_type, damage=damage,
                                     rarity=rarity, id=item_id)
        self.current_item_id += 1

    def add_potion(self, name, description, value, healing_amount, rarity="common"):
        item_id = self.current_item_id
        self.items[item_id] = HealthPotion(name=name, description=description, value=value, healing_amount=healing_amount, rarity=rarity, id=item_id)
        self.current_item_id += 1

    def add_armor(self, name, description, value, armor_class, rarity="common"):
        item_id = self.current_item_id
        self.items[item_id] = Armor(name=name, description=description, value=value, armor_class=armor_class, rarity=rarity, id=item_id)
        self.current_item_id += 1

    def get_item_by_id(self, item_id):
        return self.items.get(item_id)

    def get_item_by_name(self, name):
        for item_id, item in self.items.items():
            if item.name == name:
                return item
        return None


ItemDB = ItemDatabase()