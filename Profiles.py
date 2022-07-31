from random import choice
import math
from time import sleep


# Meme Stats
class Stats:
    FULL_HEALTH, FULL_CHARGE = (25, 4)

    def __init__(self, health=25, charge=0):
        self.health = health
        self.charge = charge
        self.health_bar = "==|" * math.floor(self.health)
        self.charge_bar = "==|" * self.charge

        difference = Stats.FULL_HEALTH - self.health
        lose_health = "  |" * math.ceil(difference)
        lose_charge = "  |" * (Stats.FULL_CHARGE - self.charge)

        self.show_health = f"Health |{self.health_bar}{lose_health}"
        self.show_charge = f"Charge |{self.charge_bar}{lose_charge}"

    def check_stats(self):
        print(self.show_health)
        print(self.show_charge)
        return " "


# Choose a Fighter
class Fighter(Stats):
    all_fighters = ('Wojak', 'Doomer', 'Zoomer', 'Chad', 'Pepe')
    char_stats = {}
    char_copy = {}

    def __init__(self):
        Stats.__init__(self, 25, 0)
        self._attack = 0
        self._defense = 0
        self._special = None

    @property
    def attack(self):
        return int(self._attack)

    @property
    def defense(self):
        return int(self._defense)

    @property
    def special(self):
        return str(self._special)

    # Select Fighter
    def set_fighter(self):
        meme_fighter = input("Choose your fighter (Wojak, Doomer, Zoomer, Chad, Pepe): ").title()
        while meme_fighter not in Fighter.all_fighters:
            print("\nFighter not found. Try again!")
            meme_fighter = input("\nChoose your fighter (Wojak, Doomer, Zoomer, Chad, Pepe): ").title()
        print("\n" + '\033[1m' + meme_fighter + '\033[0m')

        # Wojak
        if meme_fighter == "Wojak":
            self._attack = 3
            self._defense = 3
            self._special = "Buy Crypto"

        # Doomer
        if meme_fighter == "Doomer":
            self._attack = 2
            self._defense = 4
            self._special = "Crippling Depression"

        # Zoomer
        if meme_fighter == "Zoomer":
            self._attack = 3
            self._defense = 3
            self._special = "Work at McWagies"

        # Chad
        if meme_fighter == "Chad":
            self._attack = 4
            self._defense = 3
            self._special = "OUCH!"

        # Pepe
        if meme_fighter == "Pepe":
            self._attack = 4
            self._defense = 2
            self._special = "Feels Bad Man"

        attack = int(self._attack)
        defense = int(self._defense)
        special = str(self._special)

        Fighter.char_stats.update({"Profile": meme_fighter, "Attack": attack, "Defense": defense, "Special": special})
        print(f"Attack: {attack}\nDefense: {defense}\nSpecial: {special}\n")
        Fighter.char_copy = dict(Fighter.char_stats)


# Meet The Normies
class Enemy(Stats):
    all_enemies = ('NPC', 'Meme Man', 'Boomer', 'Soyjak', 'Neckbeard')
    opponent_stats = {}
    opp_copy = {}
    countdown = 1.5

    def __init__(self):
        Stats.__init__(self, 25, 0)
        self._attack = 0
        self._defense = 0
        self._special = None
        self.opponent = choice(Enemy.all_enemies)

    @property
    def attack(self):
        return self._attack

    @property
    def defense(self):
        return self._defense

    @property
    def special(self):
        return self._special

    # Select Enemy
    def enemy_profile(self):
        # An NPC
        if self.opponent == "NPC":
            self._attack = 3
            self._defense = 3
            self._special = "Get Triggered"

        # Meme Man
        if self.opponent == "Meme Man":
            self._attack = 3
            self._defense = 3
            self._special = "ANGERY"

        # Boomer
        if self.opponent == "Boomer":
            self._attack = 3
            self._defense = 4
            self._special = "Wear Bootstraps"

        # Soyjak
        if self.opponent == "Soyjak":
            self._attack = 2
            self._defense = 4
            self._special = "Drink Soy Latte"

        # Neckbeard
        if self.opponent == "Neckbeard":
            self._attack = 4
            self._defense = 2
            self._special = "Tips Fedora"

        enemy_attack = int(self._attack)
        enemy_defense = int(self._defense)
        enemy_special = str(self._special)

        Enemy.opponent_stats.update({"Profile": self.opponent, "Attack": enemy_attack, "Defense": enemy_defense,
                                    "Special": enemy_special})
        Enemy.opp_copy = dict(Enemy.opponent_stats)
        sleep(Enemy.countdown)

        print("Your opponent is \033[1m{}\033[0m.\n".format(self.opponent))
        print(f"Attack: {enemy_attack}\nDefense: {enemy_defense}\nSpecial: {enemy_special}")
        print("\nPreparing for battle...\n")
