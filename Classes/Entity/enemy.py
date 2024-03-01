from Classes.Entity.creature import Creature
from Classes.UserInterface.health_bar import HealthBar
from Database.item_database import ItemDatabase


class Enemy(Creature):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color="red")