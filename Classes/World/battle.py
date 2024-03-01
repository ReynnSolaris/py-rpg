import os


class Battle:
    CurrentlyBattling = True

    def __init__(self, entity, entity_two) -> None:
        print(f"Battle initiated with {entity.name} and {entity_two.name}")
        while (entity.health > 0 and entity_two.health > 0) and self.CurrentlyBattling:
            os.system("cls")

            entity.health_bar.draw()
            entity_two.health_bar.draw()

            current_turn = True

            while current_turn:
                var = input()
                if var == "attack" or var == "a":
                    current_turn = False
                    entity.attack(target=entity_two)
                elif var == "defense" or var == "d":
                    current_turn = False
                    pass
                elif var == "spell" or var == "s":
                    current_turn = False
                    pass
                elif var == "heal" or var == "h":
                    current_turn = False
                    pass
                elif var == "run" or var == "r":
                    self.CurrentlyBattling = False
                    current_turn = False
                    print(f"You have successfully ran away from {entity_two.name}!")
                    pass
                else:
                    print(
                        f"Invalid Input, please type one of the following into the console.\n ['a', 'attack', 'd', 'defense', 'h', 'heal', 's', 'spell', 'r', 'run']")
                    pass
            if self.CurrentlyBattling:
                entity_two.attack(target=entity)
