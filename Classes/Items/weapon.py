from Classes.Items.item import Item

class Weapon(Item):
    def __init__(self, name, description, value, weapon_type, damage, id, rarity="common") -> None:
        super().__init__(name, description, value, "weapon", rarity)
        self.id = id
        self.weapon_type = weapon_type
        self.damage = damage
