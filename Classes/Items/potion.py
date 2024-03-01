from Classes.Items.item import Item

class HealthPotion(Item):
    def __init__(self, name, description, value, healing_amount, id, rarity="common") -> None:
        super().__init__(name, description, value, "potion", rarity)
        self.healing_amount = healing_amount
        self.id = id
