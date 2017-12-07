"""A program, that visualises the dice-game '16 is dead'.

At the beginning of the program you have to choose a number of players, dices and a number of faces
for the dices. The game can be reseted at any point or even being interrupted. The possible options
are told at each point of the program.
"""

import random
import time


def user_interface(player):
    """This function is the user_interface: It gives the user the ability to interact with the pro-
    gram."""
    
    while True:
        print ("Spieler",player,"ist am Zug:")
        print ("Drücke 'ENTER' zum Würfeln, tippe 'n', um deinen Zug zu beenden, tippe 'q', um das\
 Spiel zu beenden oder tippe 'r', um das Spiel neu zu starten")
        user_input = str(input("Erwarte Eingabe: "))
        if user_input == "":
            break
        elif user_input == "n":
            break
        elif user_input == "q":
            quit()
        elif user_input == "r":
            print()
            print()
            print("SPIEL-WURDE-NEUGESTARTET------------------------------------------------------")
            print()
            sixteen_is_dead(set_players())
        else:
            print()
            print("ERROR: Falsche Eingabe - bitte versuchen Sie es erneut!")
            print()
    return user_input

def user_interface_2():
    """This is the second user_interface: The user can select the dice he wants to use here."""
    
    while True:
        print("Drücken Sie erneut 'ENTER' um den normalen Würfel zu benutzen oder tippen S\
ie 'c', um den 'Cheating Dice' zu benutzen")
        user_input_2 = str(input("Erwarte Eingabe: "))
        if user_input_2 == "" or user_input_2 == "c":
            break
        else:
            print("ERROR: Falsche Eingabe - bitte versuchen Sie es erneut!")
    return user_input_2
    
def roll_dice(number,faces):
    """This function generates a random number for every dice roll."""
    
    dice_number = 0
    for i in range(number):
        dice_number += random.randint(1, faces)
    return dice_number

def roll_cheating_dice(number,faces):
    """In contrast to the roll_dice function this function selects a random number out of a list,
    which has the length of the size of the dice, including an extra 3 to make its appearance like-
    lier."""
    
    dice_number = 0
    cheating_list = list(range(1,faces+1))
    cheating_list.append(3)
    for i in range(number):
        dice_number += random.choice(cheating_list)
    return dice_number

def sixteen_is_dead(players):
    """This is the main function. The whole game runs here."""
    
    number = setup_number_of_dices()
    faces = setup_number_of_faces()
    result_list = []
    for player in range(1, players+1):
        total_points = 0
        while total_points < 16:
            user_input = user_interface(player)
            if user_input == "":
                while True:
                    user_input_2 = user_interface_2()
                    if user_input_2 == "":
                        dice_number = roll_dice(number,faces)
                        total_points += dice_number
                        print()
                        print ("Deine aktuelle Punktzahl beträgt:",total_points)
                        print()
                        if total_points == 10:
                            time.sleep(3)
                            continue
                        else:
                            break
                    else:
                        dice_number = roll_cheating_dice(number,faces)
                        total_points += dice_number
                        print()
                        print ("Deine aktuelle Punktzahl beträgt:",total_points)
                        print()
                        if total_points == 10:
                            time.sleep(3)
                            continue
                        else:
                            break
            if (total_points >= 16) or (total_points == 9) or (user_input == "n"):
                print()
                break
        if total_points < 16:
             result_list.append(total_points)
        else:
            print()
            break
    if total_points >= 16:
        print("Spieler",player,"hat das Spiel verloren!")
        print()
        restart()
    else:
        player = 1
        for i in result_list:
            if i == min(result_list):
                print("Spieler",player,"hat das Spiel mit",i,"Punkten verloren!")
            player += 1
        print()
        restart()
    
def set_players():
    """The user can set the number of players here. This function is always called at first, when a
    new game starts."""
    
    while True:
        players = eval(input("Geben Sie die Anzahl Spieler an oder tippe '0' zum Abbruch: "))
        if int(players) > 0:
            break
        elif int(players) == 0:
            quit()
        else:
            print("ERROR: Du musst eine positive Ganzzahl eingeben!")
        print()
    print()
    return players

def setup_number_of_dices():
    """The user can set the number of dices he wants to use in the game here."""
    
    while True:
        number = int(input("Geben Sie die Anzahl Würfel an (1 - 10) oder tippe '0' zum Abbruch: "))
        if 1 <= number <= 10:
            break
        elif number == 0:
            quit()
        else:
            print("ERROR: Du musst eine Zahl zwischen 1 und 10 eingeben!")
        print()
    print()
    return number

def setup_number_of_faces():
    """The user can set the number of faces of the dices here."""
    
    while True:
        faces = int(input("Geben Sie die Seitenanzahl der Würfel an (2 - 100) oder tippe '0' zum A\
bbruch: "))
        if 2 <= faces <= 100:
            break
        elif faces == 0:
            quit()
        else:
            print("ERROR: Du musst eine Zahl zwischen 2 und 100 eingeben!")
        print()
    print()
    return faces

def restart():
    """This function is called, when the user wants to start a new game."""
    
    while True:
        print("Spiel wurde beendet: Tippe 'r' zum Neustart oder 'q' zum Beenden")
        user_input_3 = str(input("Erwarte Eingabe: "))
        if user_input_3 == "q":
            quit()
        elif user_input_3 == "r":
            print()
            print()
            print("SPIEL-WURDE-NEUGESTARTET------------------------------------------------------")
            print()
            sixteen_is_dead(set_players())
        else:
            print()
            print("ERROR: Falsche Eingabe - bitte versuchen Sie es erneut!")
            print()


sixteen_is_dead(set_players())
