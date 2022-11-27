from Turns import Round
from Moves import Effects, CharStats, OppStats
from Actions import Action, EnemyAction
import time


class Game:

    @classmethod
    def start_game(cls):
        time.sleep(0.8)
        print(Game())
        options = {"Yes", "No"}
        player = input("Do you want to start the game? (Type Yes/No) ").title()
        while player not in options:
            print("\nThe game did not recognize that. Please try again.")
            player = input("\nStart the game? (Yes/No) ").title()
        if player == "Yes":
            print(Game.tutorial())
            Round()
            cls.play_again()
        elif player == "No":
            print("\nOh well, see you later then!")
            print("\nYou exit the ring and forfeit the bonus match.")
            print("\n ============>> [Exit] ")
            exit()

    def __str__(self):
        game_intro = ("Welcome to Meme Battle. May the dankest of memes win! You enter the ring as everyone gambles",
                      "their wagie paychecks on your (almost guaranteed) success.",
                      "\nWill you take home the grand prize and etch your name into meme history? Or will you leave ",
                      "the dock of shame on national TV?",
                      "\nStep right up fearless underdogs and introduce yourselves to the crowd! \x1B[3mLooks like "
                      "your", "training is about to pay off.\x1B[0m")

        for line in game_intro:
            print(line)
            time.sleep(0.5)

        return " "

    @staticmethod
    def tutorial():
        instructions = ("\nMeme Battle is a turn-based RPG where you type in commands and the game responds to your "
                        "actions. It is ", "entirely text-based, so you must use the exact letters or else the game "
                                           "will not recognize your input.\n",

                        "1. Choose Your Favorite Meme Fighter",
                        "2. Select an Action on Your Turn",
                        "3. GOAL: Try Not to Get Knocked Out",
                        "4. HINT: The Best Offense is a Good Defense",
                        "5. Have Fun Playing or Add Your Own Mods\n",

                        "Disclaimer: The developer was too lazy to add any images showing said memes. Use your "
                        "imagination to see what went down.")

        for line in instructions:
            print(line)
            time.sleep(0.5)
        return " "

    @classmethod
    def play_again(cls):
        print("\n")
        new_round = input("Do you want to play the bonus match? (Yes/No) ").title()
        Effects.reset_stats()
        CharStats.disabled, OppStats.disabled = (False, False)
        Action.defending, EnemyAction.defending = (False, False)

        if new_round == "Yes":
            print("\nWelcome back seasoned fighters. We hoped you enjoyed the commercial break.")
            print("\nHere are the next two contestants. Step up to the ring and introduce yourselves!")
            time.sleep(1.5)
            Round()
        elif new_round == "No":
            print("\nYou take your winnings and leave. Had enough excitement for one day.")
            print("\n ============>> [Exit] ")
            exit()
        else:
            print("\nOops, the game has crashed! Relaunching the program...")
            print("\n ============== \n")
            meme_battle.start_game()


meme_battle = Game()
meme_battle.start_game()

