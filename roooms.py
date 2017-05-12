from sys import exit

def restart():
    print "Would you like to play again? Y/N"
    play_again = raw_input()

    if play_again == "N" or play_again == "n" or play_again == "No" or play_again == "no":
        exit(0)
    if play_again == "Yes" or play_again == "yes" or play_again == "Y" or play_again == "y":
        start()

def start():
    print "Choose room 1, 2, 3"
    input = int(raw_input())

    if input == 1:
        room_of_death() # code to go into room of death
    elif input == 2:
        room_of_happiness()
    elif input == 3:
        fight_room()
    else:
        instant_death("You'll never be happy")

def fight_room():
    bear_life = 100
    my_life = 100
    print "Bear swings at you. What do you do? Duck, block, or poke"

    input = raw_input()
    if input == "duck":
        fight_room()
    if input == "block":
        my_life = my_life - 50  # aka my_life -= 50
        if my_life <= 0:
            instant_death("Don't try to fight a bear!")
        fight_room()
    if input == "poke":
        bear_life = bear_life - 100
        if bear_life <= 0:
            room_of_happiness()

def instant_death(reason):
    print reason + " You lose."
    restart()

def room_of_death():
    print "You are in the room of death."
    print "Choose 1 or 2"

    input = int(raw_input())

    if input == 1:
        bear_room()
    elif input == 2:
        instant_death("You made the wrong choice!!")

def room_of_happiness():
    print "You are in the room of happiness."
    print "You Won"
    restart()

def bear_room():
    print "There is a bear here. The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How will you move the bear?"
    bear_moved = False

    input = raw_input()

    if input == "take honey":
        instant_death("Never take honey from a bear. Bear slaps you.")
    elif input == "distract bear":
        bear_moved = True
        print "The bear has moved but you still need to scare the bear. Would you like to scare the bear? Y/N"
        inp = raw_input()
        if inp == "Yes" or inp == "yes" or inp == "Y" or inp == "y":
            room_of_happiness()
        else:
            bear_room()
    elif input == "scare bear" and bear_moved: # can get in door if you distract then scare
        room_of_happiness()
    elif input == "scare bear" and bear_moved is False:
        print "You need to distract the bear before you scare the bear"
        bear_room()
    else:
        print "You only have 4 choices: take honey, distract bear, or scare bear"
        bear_room()

start()
