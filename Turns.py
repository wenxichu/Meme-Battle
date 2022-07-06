from Profiles import Stats, Fighter, Enemy
from Moves import CharStats, OppStats
from Actions import Action, EnemyAction
import time


class HealthLimit:

    @staticmethod
    def check_health():
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
        self.run_game()
        print(f"\nThis battle lasted a total of {self.num_turns} rounds.")
        self.trophies()
        # Reset Values
        CharStats.char_hp, CharStats.char_cg = (25, 0)
        OppStats.opp_hp, OppStats.opp_cg = (25, 0)

    def __le__(self):
        return OppStats.opp_hp <= 0

    def run_game(self):
        fighter = Fighter()
        enemy = Enemy()
        # Get Fighter
        fighter.set_fighter()
        enemy.enemy_profile()
        # Get Stats
        print(Stats().check_stats())
        print(f"Health: 25/25    Charge: 0/4    Special: {fighter.special}")
        # Turn Order
        while CharStats.char_hp > 0 and OppStats.opp_hp > 0:
            HealthLimit().check_health()
            Action()
            if self.__le__():
                break
            EnemyAction()
            if self.num_turns == 10:
                print("\nThe competition is starting to heat up. You hear cheering in the distance.")
            self.num_turns += 1
        time.sleep(1.0)
        print("\nThe game has finally ended. Time to tally up the results!")
        # Win
        if self.__le__():
            print(f"\nWell done, {Fighter.char_stats['Profile']} has won the match! The crowd goes absolutely wild.")
            print("The judges will now decide on your performance.")
        # Lose
        elif CharStats.char_hp <= 0:
            print(f"\n{Enemy.opponent_stats['Profile']} has won the match! Better luck next time. "
                  f"Remember...eye on the prize.")

    def trophies(self):
        time.sleep(1.2)
        # Bronze
        if self.__le__() and self.num_turns >= 30:
            print(f"\nBogdanoff awards {Fighter.char_stats['Profile']} with BRONZE medal #69. "
                  f"You receive 69 Magic: The Gathering trading cards.")
        # Silver
        elif self.__le__() and self.num_turns in range(20, 30):
            print(f"\nBogdanoff awards {Fighter.char_stats['Profile']} with SILVER medal #420. "
                  f"You receive a year\'s supply of home-grown weed.")
        # Gold
        elif self.__le__() and self.num_turns <= 19:
            print(f"\nBogdanoff awards {Fighter.char_stats['Profile']} with GOLD medal #51. "
                  f"You drive off to raid Area 51 on a new lambo.")
        # Defeat
        else:
            print(f"\nDespite the crushing defeat, {Fighter.char_stats['Profile']} still makes it to the "
                  f"Honorable Mentions list.")
