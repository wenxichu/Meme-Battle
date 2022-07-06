import random
from time import sleep
from Profiles import Stats, Fighter, Enemy
from Moves import CharStats, OppStats, CharSpecial, OppSpecial, Effects


class Action(Fighter, Enemy):
    defending, round = (False, 0)

    def __init__(self):
        super().__init__()
        sleep(Enemy.countdown)
        self.action = input(
            f'''\nIt is {self.char_stats["Profile"]}\'s turn. 

[ ATK ]
[ DEF ]
[ SPL ]

What will {self.char_stats["Profile"]} do? (Pick One) ''').upper()
        self.selection()

        if Action.round > 0:
            Action.round -= 1
        else:
            Action.defending = False

    def selection(self):
        is_valid = ["ATK", "DEF", "SPL"]

        while self.action not in is_valid:
            print("\nNot sure what that means. Try again!")
            self.action = input("\nWhat will {} do? ".format(self.char_stats["Profile"])).upper()
            continue

        if self.action == "ATK":
            self.attack()
            print(f"\033[1m{self.opponent_stats['Profile']}\033[0m")
            Stats(OppStats.opp_hp, OppStats.opp_cg).check_stats()
            print(f"Health: {OppStats.opp_hp}/25    Charge: {OppStats.opp_cg}/4")
        elif self.action == "DEF":
            self.defend()
            print(f"\033[1m{self.char_stats['Profile']}\033[0m")
            Stats(CharStats.char_hp, CharStats.char_cg).check_stats()
            print(f"Health: {CharStats.char_hp}/25    Charge: {CharStats.char_cg}/4")
        elif self.action == "SPL":
            print(f"\nSpecial: {self.char_stats['Special']}")
            self.special()
        return Action.char_power_up()

    @staticmethod
    def char_power_up():
        if CharStats.char_cg < Stats.FULL_CHARGE:
            CharStats.char_cg += 1
        if CharStats.active:
            Effects.char_wear_off()
        return CharStats.char_cg

    def attack(self):
        char_atk = self.char_stats["Attack"]
        enemy_def = self.opponent_stats["Defense"]
        damage = char_atk - enemy_def
        if EnemyAction.defending:
            if damage <= 0:
                print("\nOh no, {}'s attack missed!\n".format(self.char_stats["Profile"]))
                return None
            print(f"\n{self.char_stats['Profile']} deals only {damage} damage this turn!\n")
            OppStats.opp_hp -= damage
        else:
            print(f"\n{self.char_stats['Profile']} deals {char_atk} damage this turn!\n")
            OppStats.opp_hp -= char_atk

    @classmethod
    def defend(cls):
        if cls.defending:
            print(f"\n{cls.char_stats['Profile']} is already defending! You lose a turn.\n")
            if CharStats.char_cg < 4:
                CharStats.char_cg += 1
            return None
        cls.defending, cls.round = (True, 3)
        print("\n{} is now defending.\n".format(cls.char_stats["Profile"]))

    def special(self):
        power_up = Stats.FULL_CHARGE - CharStats.char_cg
        if CharStats.disabled:
            print(f"\nUh oh! {self.char_stats['Profile']}\'s special move is disabled.")
            return
        if CharStats.char_cg == 4:
            print(f"\n{self.char_stats['Profile']} unleashes his special move!\n")
            CharSpecial(self.char_stats["Special"])
            CharStats.char_cg, CharStats.active = (0, 1)
        elif CharStats.char_cg < 4:
            print(f"\nSpecial move not fully charged yet. Only {power_up} left to go!")


class EnemyAction(Enemy, Fighter):
    opp_actions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    defending, round = (False, 0)

    def __init__(self):
        super().__init__()
        sleep(Enemy.countdown)
        print(f"\nIt is {self.opponent_stats['Profile']}\'s turn.")
        enemy_act = EnemyAction.opp_actions
        self.opp_choice = random.choice(enemy_act)
        self.decision()

        if EnemyAction.round > 0:
            EnemyAction.round -= 1
        else:
            EnemyAction.defending = False

    def decision(self):
        if self.opp_choice in range(4):
            self.enemy_attack()
            print(f"\033[1m{self.char_stats['Profile']}\033[0m")
            Stats(CharStats.char_hp, CharStats.char_cg).check_stats()
            print(f"Health: {CharStats.char_hp}/25    Charge: {CharStats.char_cg}/4")
        elif self.opp_choice in range(4, 7):
            self.enemy_defend()
            print(f"\033[1m{self.opponent_stats['Profile']}\033[0m")
            Stats(OppStats.opp_hp, OppStats.opp_cg).check_stats()
            print(f"Health: {OppStats.opp_hp}/25    Charge: {OppStats.opp_cg}/4")
        elif self.opp_choice in range(7, 9):
            print(f"\nSpecial: {self.opponent_stats['Special']}")
            self.enemy_special()
        return EnemyAction.opp_power_up()

    @staticmethod
    def opp_power_up():
        if OppStats.opp_cg < Stats.FULL_CHARGE:
            OppStats.opp_cg += 1
        if OppStats.active:
            Effects.opp_wear_off()
        return OppStats.opp_cg

    def enemy_attack(self):
        enemy_atk = self.opponent_stats["Attack"]
        char_def = self.char_stats["Defense"]
        opp_damage = enemy_atk - char_def
        if Action.defending:
            if opp_damage <= 0:
                print(f"\nHaha, {self.opponent_stats['Profile']} missed their attack.\n")
                return None
            print(f"\n{self.opponent_stats['Profile']} deals only {opp_damage} damage this turn!\n")
            CharStats.char_hp -= opp_damage
        else:
            print(f"\n{self.opponent_stats['Profile']} deals {enemy_atk} damage this turn!\n")
            CharStats.char_hp -= enemy_atk

    @classmethod
    def enemy_defend(cls):
        if OppStats.opp_hp < Stats.FULL_HEALTH:
            OppStats.opp_hp += 1
        if cls.defending:
            print(f"\n{cls.opponent_stats['Profile']} has lost a turn from defending again.\n")
            return None
        cls.defending, cls.round = (True, 3)
        print(f"\n{cls.opponent_stats['Profile']} is now defending.\n")

    def enemy_special(self):
        if OppStats.disabled:
            print(f"\n{self.opponent_stats['Profile']} forgot their moves. Nothing of value was lost.")
            return
        if OppStats.opp_cg == 4:
            print(f"\n{self.opponent_stats['Profile']} unleashes his special move!")
            OppSpecial(self.opponent_stats["Special"])
            OppStats.opp_cg, OppStats.active = (0, 1)
        elif OppStats.opp_cg < 4:
            OppStats.opp_cg += 1
            print(f"\n{self.opponent_stats['Profile']} performs a special move! It has no effect...")
