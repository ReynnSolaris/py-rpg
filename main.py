import os

from Classes.Entity.player import Player
from Classes.Entity.enemy import Enemy
from Database.item_database import ItemDB

from Classes.World.battle import Battle

MainPlayer = Player("Adventurer", 100, {})
MainPlayer.equip(ItemDB.get_item_by_id(item_id=5))

EnemyTest = Enemy("Enemy 1", 100, ItemDB.get_item_by_name("Short Bow"))

#newBattle = Battle(MainPlayer, EnemyTest)

while True:
    os.system("cls")


    var = input()
    if var.lower() == "q":
        break
    elif var.lower() == "itemlist":
        for itemId, item in ItemDB.items.items():
            print(f"[{item.id}] - {item.name}\n\tDescription: {item.description}\n\tType: {item.item_type.upper()}\n\tRarity: {item.rarity.upper()}")