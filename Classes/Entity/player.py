import random

from Classes.Entity.creature import Creature
from Database.item_database import ItemDB
from Classes.UserInterface.health_bar import HealthBar

death_messages = [
    "Alas, your journey has come to an end. May your legacy live on in the tales of adventurers yet to come.",
    "In the realm of shadows, your story concludes. Fear not, for new heroes will rise to face the challenges you could not.",
    "The echoes of your footsteps fade as you succumb to the perils of this world. Your name will be whispered in regret and remembered in legend.",
    "A cold wind blows through the land, carrying news of your demise. Your valiant efforts shall not be forgotten, but your time in this realm has expired.",
    "The fates have woven a dark tapestry, and your thread has reached its end. May your spirit find peace in the afterlife.",
    "As the last breath leaves your body, a solemn silence falls over the land. Your saga ends here, but the world will continue its eternal dance.",
    "The hands of fate have closed around you, and the curtain falls on your journey. Take solace in knowing that your existence has left an indelible mark on the tapestry of time.",
    "The stars above bear witness to the end of your quest. May your soul find tranquility in the great beyond.",
    "In the face of insurmountable odds, you have met your match. Your story concludes with a solemn note, and the world mourns the passing of a brave adventurer.",
    "The darkness claims you, and the world mourns the loss of a champion. Your deeds will be remembered, even as your body returns to the earth."
]

class Player(Creature):
    def __init__(self, name, health, stats):
        super().__init__(name, health)
        self.stats = stats
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color="green")

    def damage(self, damage):
        super().damage(damage)
        if self.health <= 0:
            print(
                f"\t#######################\n\t"
                f"#    YOU HAVE DIED    #\n\t"
                f"#######################\n"
                f"{random.choice(death_messages)}"
            )
            quit()

    def equip(self, item):
        if item:
            self.weapon = item
        else:
            self.weapon = self.default_weapon
        print(f'{self.name} has equipped a(n) {self.weapon.name}')

    def drop(self):
        print(f'{self.name} dropped {self.weapon.name}')
        self.weapon = self.default_weapon