from Database.item_database import ItemDB
import random
class Creature:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = ItemDB.get_item_by_id(item_id=1)

    def damage(self, damage):
        self.health -= damage
        self.health = max(self.health, 0)

    def attack(self, target):
        dmg = random.randint(self.weapon.damage["min"], self.weapon.damage["max"])
        print(f'{self.name} has dealt {dmg} Damage to {target.name} with {self.weapon.name}!')
        target.damage(dmg)
        target.health_bar.update()