import math
import random
from Profiles import Fighter, Enemy


class CharStats:
    char_hp = Fighter().health
    char_cg = Fighter().charge
    active = 0
    disabled = False


class OppStats:
    opp_hp = Enemy().health
    opp_cg = Enemy().charge
    active = 0
    disabled = False


class CharSpecial(Fighter, Enemy):

    def __init__(self, special_move):
        super().__init__()
        self.special_move = special_move
        move = str(self.special_move)

        if move == "Buy Crypto":
            self.wojak()
        elif move == "Crippling Depression":
            self.doomer()
        elif move == "Work at McWagies":
            self.zoomer()
        elif move == "OUCH!":
            self.chad()
        elif move == "Feels Bad Man":
            self.pepe()
        elif move == "Avoid Eye Contact":
            self.virgin()

    def wojak(self):
        amount = int(input("How much charge to spend? (1-3) "))
        self.char_stats["Attack"] = 4
        if isinstance(amount, int) and amount <= 3:
            CharStats.char_hp += amount
            CharStats.char_cg -= amount
            print("\nHealth restored by {}.".format(amount))
        else:
            print("\nIt has to be an integer less than 4.")
            return None

    def doomer(self):
        CharStats.char_hp += 2
        self.char_stats["Attack"] += 1
        OppStats.opp_cg = 0
        print(f"Doomer\'s attack is increased. {self.opp_stats['Profile']} loses the will to fight.")

    def zoomer(self):
        CharStats.char_hp += 1
        self.char_stats["Defense"] = 4
        self.opp_stats["Attack"] -= 1
        print(f"Zoomer\'s defense is increased. {self.opp_stats['Profile']}\'s attacks are now weaker!")

    def chad(self):
        roll = [1, 2, 3, 4]
        if random.choice(roll) == 3:
            OppStats.opp_hp = 0
            print("\nIncredible! You knocked out your opponent.")
            return None
        else:
            OppStats.disabled = True
            print(f"Your knockout punch failed...{self.opp_stats['Profile']} is crippled this turn.")

    def pepe(self):
        self.char_stats["Defense"] = 3
        self.opp_stats["Attack"] -= 1
        self.opp_stats["Defense"] -= 1
        print("{} attack and defense lowered. REEEEE!".format(self.opp_stats['Profile']))

    def virgin(self):
        self.char_stats["Attack"] = 3
        for count in range(2):
            hp_decay = 0.1 * OppStats.opp_hp
            OppStats.opp_hp -= math.ceil(hp_decay)
        print("You ignore the incel hoping he would go away. The music in your ears blocks out everything else.")


class OppSpecial(Fighter, Enemy):

    def __init__(self, special_move):
        super().__init__()
        self.special_move = special_move
        move = str(self.special_move)

        if move == "Get Triggered":
            self.mindless_npc()
        elif move == "ANGERY":
            self.meme_man()
        elif move == "Wear Bootstraps":
            self.boomer()
        elif move == "Drink Soy Latte":
            self.soyjak()
        elif move == "Tips Fedora":
            self.neckbeard()
        elif move == "Rant About Society":
            self.incel()

    def mindless_npc(self):
        self.char_stats["Attack"] = 1
        OppStats.opp_cg += 2
        print(f"\nOh no, {self.char_stats['Profile']} can't fight back! He has been canceled for 3 turns.")

    def meme_man(self):
        self.char_stats["Defense"] -= 2
        self.opp_stats["Attack"] += 1
        print(f"\nUh oh, {self.char_stats['Profile']}\'s defense is weakened from the impending explosion!")

    def boomer(self):
        CharStats.char_cg = 0
        self.opp_stats["Defense"] -= 1
        self.opp_stats["Attack"] += 1
        print(f"\n{self.char_stats['Profile']} is lectured by the boomer. Charge depleted to 0!")

    def soyjak(self):
        self.opp_stats["Attack"] += 2
        self.char_stats["Attack"] -= 1
        print("\nSoyjak boosts his attack! {}\'s attack is lower.".format(self.char_stats['Profile']))

    def neckbeard(self):
        self.opp_stats["Defense"] += 1
        CharStats.disabled = True
        print(f"\nWhat an awkward greeting...{self.char_stats['Profile']} special attack disabled!")

    def incel(self):
        coin_flip = ["Heads", "Tails"]
        if random.choice(coin_flip) == "Heads":
            self.opp_stats["Attack"] = 6
        elif coin_flip == "Tails":
            self.opp_stats["Defense"] = 6
        print("The incel goes on to blame women for his problems. You give up trying to reason with him.")


class Effects:
    char_duration, opp_duration = (3, 3)

    @staticmethod
    def reset_stats():
        char_copy = Fighter.char_copy
        opp_copy = Enemy.opp_copy
        Fighter.char_stats.update(char_copy)
        Enemy.opp_stats.update(opp_copy)
        CharStats.active, OppStats.active = (0, 0)

    @classmethod
    def char_wear_off(cls):
        if cls.char_duration > 0:
            cls.char_duration -= 1
        elif cls.char_duration <= 0:
            OppStats.disabled = False
            Effects.reset_stats()
            cls.char_duration = 3

    @classmethod
    def opp_wear_off(cls):
        if cls.opp_duration > 0:
            cls.opp_duration -= 1
        elif cls.opp_duration <= 0:
            CharStats.disabled = False
            Effects.reset_stats()
            cls.opp_duration = 3

