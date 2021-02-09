import time

import random


def random_villain():
    villain = ["a vampire", "a demon", "a witch"]
    bad_guy = random.choice(villain)
    print_pause(bad_guy)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in "
                "a rather large graveyard and "
                "it appears to be night.")
    print_pause("There is a rumor going around "
                "that something has been killing "
                "unlucky nightime grievers.")
    print_pause("In the distance you can see "
                "a young woman fighting something "
                "strange, all on her own.")


def make_approach(items):
    print_pause("You walk over to the woman.")
    if "Sword" in items:
        print_pause("As soon as you approach her "
                    "she mimes out a stabbing motion "
                    "and distracts the big bad. ")
        print_pause("Taking your opportunity, you "
                    "swing your sword and chop "
                    "off the head of what appears "
                    "to be...")
        random_villain()
        print_pause("Caught by surprise, the head "
                    "rolls away and the body hits "
                    "the ground.")
        print_pause("Congratulations! You have "
                    "saved the day!")
        play_again()
    else:
        print_pause("She looks over to you and "
                    "says 'I lost my weapon!'")
        print_pause("Maybe if you take a look "
                    "around, you can help her "
                    "find it!")
        hero_choice(items)


def look_around(items):
    print_pause("You take a few breaths and see "
                "if there is anything nearby "
                "to help you.")
    if "Sword" in items:
        print_pause("It looks like the sword was "
                    "the only weapon lying around.")
        print_pause("You look back towards the woman.")
        hero_choice(items)
    else:
        print_pause("You notice something shiny a few "
                    "feet away.")
        print_pause("When you get a little closer, you "
                    "realize it's a beautiful but bloodied "
                    "sword.")
        print_pause("It's kind of gross but you pick it "
                    "up anyway.")
        items.append("Sword")
        hero_choice(items)


def run_away():
    print_pause("You turn on your feet and run away.")
    print_pause("Before you realize what is happening, "
                "you are confronted with...")
    random_villain()
    print_pause("You feel yourself falling backwards "
                "and sure enough, you're murdered.")
    print_pause("Your last thought is how weird "
                "things always seem to happen in "
                "your strange little town.")
    print_pause("GAME OVER")
    play_again()


def play_again():
    print_pause("Would you like to play again?\n")
    response = input("Press Y for Yes\n"
                     "Press N for No\n").lower()
    if response == 'y':
        play_game()
    elif response == 'n':
        print_pause("OK, Goodbye!")
    else:
        print_pause("Sorry, I don't understand")
        play_again()


def hero_choice(items):
    print_pause("Would you like to approach her, "
                "run away, or look around?\n")
    response = input("Press 1 to approach her.\n"
                     "Press 2 to run away\n"
                     "Press 3 to look around\n")
    if response == '1':
        make_approach(items)
    elif response == '2':
        run_away()
    elif response == '3':
        look_around(items)
    else:
        print_pause("Sorry, I don't understand")
        hero_choice(items)


def play_game():
    items = []
    intro()
    hero_choice(items)


play_game()
