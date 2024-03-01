from Classes.Items.item import Item

class Armor(Item):
    def __init__(self, name, description, value, armor_class, id, rarity="common") -> None:
        super().__init__(name, description, value, "armor", rarity)
        self.armor_class = armor_class
        self.id = id
