class Item:
    def __init__(self, name: str, description: str, value: int, item_type: str = "basic", rarity: str = "common") -> None:
        self.name = name
        self.description = description
        self.value = value
        self.rarity = rarity
        self.item_type = item_type