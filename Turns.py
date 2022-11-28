from Profiles import Stats, Fighter, Enemy
from Moves import CharStats, OppStats
from Actions import Action, EnemyAction
import time

games_played = 0


def prep_match():
    fighter = Fighter()
    enemy = Enemy()
    # Get Fighter
    if games_played == 0:
        fighter.set_fighter()
        enemy.enemy_profile()
    else:
        bonus_fighter()
        bonus_enemy()
    # Get Stats
    print(Stats().check_stats())


def bonus_fighter():
    Fighter()._attack = 2
    Fighter()._defense = 3
    Fighter()._special = "Avoid Eye Contact"

    Fighter.char_stats.update({"Profile": "Virgin", "Attack": 2, "Defense": 3, "Special": "Avoid Eye Contact"})
    print("\n" + '\033[1mVirgin\033[0m')
    print(f"Attack: {2}\nDefense: {3}\nSpecial: Avoid Eye Contact\n")
    Fighter.char_copy = dict(Fighter.char_stats)


def bonus_enemy():
    Enemy()._attack = 3
    Enemy()._defense = 2
    Enemy()._special = "Rant About Society"

    Enemy.opp_stats.update({"Profile": "Incel", "Attack": 3, "Defense": 2, "Special": "Rant About Society"})
    Enemy.opp_copy = dict(Enemy.opp_stats)
    time.sleep(Enemy.countdown)

    print("Your opponent is the\033[1m Incel\033[0m.\n")
    print(f"Attack: {3}\nDefense: {2}\nSpecial: Rant About Society\n")
    print("Preparing for battle...\n")


class Health:

    @staticmethod
    def check_limit():
        if CharStats.char_hp > Stats.FULL_HEALTH:
            CharStats.char_hp = 25

        if OppStats.opp_hp > Stats.FULL_HEALTH:
            OppStats.opp_hp = 25

        if CharStats.char_hp <= 0:
            CharStats.char_hp = 0

        if OppStats.opp_hp <= 0:
            OppStats.opp_hp = 0


class Round(CharStats, OppStats):

    def __init__(self):
        super().__init__()
        self.num_turns = 0
        prep_match()
        print(f"Health: 25/25    Charge: 0/4    Special: {Fighter.char_stats['Special']}")
        self.run_game()
        print(f"\nThis battle lasted a total of {self.num_turns} rounds.")
        self.trophies()
        global games_played
        games_played = 1
        # Reset Values
        CharStats.char_hp, CharStats.char_cg = (25, 0)
        OppStats.opp_hp, OppStats.opp_cg = (25, 0)

    def __le__(self, hit_points):
        return hit_points <= 0

    def run_game(self):
        # Turn Order
        while CharStats.char_hp > 0 and OppStats.opp_hp > 0:
            Health().check_limit()
            Action()
            if OppStats.opp_hp <= 0:
                break
            EnemyAction()
            if self.num_turns == 10:
                print("\nThe competition is starting to heat up. You hear cheering in the distance.")
            self.num_turns += 1
        time.sleep(1.0)
        print("\nThe game has finally ended. Time to tally up the results!")
        # Win
        if self.__le__(OppStats.opp_hp):
            print(f"\nWell done, {Fighter.char_stats['Profile']} has won the match! The crowd goes absolutely wild.")
            print("The judges will now decide on your performance.")
        # Lose
        elif self.__le__(CharStats.char_hp):
            print(f"\n{Enemy.opp_stats['Profile']} has won the match! Better luck next time. "
                  f"Remember...eye on the prize.")

    def trophies(self):
        time.sleep(1.2)
        # Bronze
        if self.__le__(OppStats.opp_hp) and self.num_turns >= 30:
            print(f"\nBogdanoff awards {Fighter.char_stats['Profile']} with BRONZE medal #69. "
                  f"You receive 69 Magic: The Gathering trading cards.")
        # Silver
        elif self.__le__(OppStats.opp_hp) and self.num_turns in range(20, 30):
            print(f"\nBogdanoff awards {Fighter.char_stats['Profile']} with SILVER medal #420. "
                  f"You receive a year\'s supply of home-grown weed.")
        # Gold
        elif self.__le__(OppStats.opp_hp) and self.num_turns <= 19:
            print(f"\nBogdanoff awards {Fighter.char_stats['Profile']} with GOLD medal #51. "
                  f"You drive off to raid Area 51 on a new lambo.")
        # Defeat
        else:
            print(f"\nDespite the crushing defeat, {Fighter.char_stats['Profile']} still makes it to the "
                  f"Honorable Mentions list.")

