"""A program, that visualises the dice-game 'Studenten-Pasch'.

At the beginning of the program you have to choose a number of players, dices and a number of faces
for the dices. The game can be reseted at any point or even being interrupted. The possible options
are told at each point of the program.
"""


import random


def user_interface(player, throw):
    """This function is the user_interface: It gives the user the ability to interact with the pro-
    gram."""
    
    while True:
        print ("Spieler",player,"ist am Zug:")
        print ("Es ist dein",str(throw + 1) + ". Wurf.")
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
            student_pasch(set_players())
        else:
            print()
            print("ERROR: Falsche Eingabe - bitte versuchen Sie es erneut!")
            print()
    return user_input


def user_interface_2():
    """
    This is the second user_interface: The user can select the dice he wants to use here.
    Returns a list of dice indexes of the dice which should not be thrown again.
    """
    
    while True:
        print("Drücken Sie erneut 'ENTER' um mit allen Würfeln (erneut) zu werfen oder schreiben"
              " Sie die Indizes der Würfel (Leerzeichen separiert), die liegen bleiben sollen"
              " (z.B. '0 2').")
        user_input_2 = input("Erwarte Eingabe: ")
        if user_input_2 == "":
            break
        numbers = user_input_2.split(' ')
        if all(n.isdigit() and 0 <= int(n) <= 2 for n in numbers) and len(numbers) <= 2:
            return list(map(int, numbers))
        else:
            print("ERROR: Falsche Eingabe - bitte versuchen Sie es erneut!")
    return user_input_2


def roll_dice(number,faces):
    """This function generates a random number for every dice roll and returns them in a list."""
    
    rolled_faces = []
    for i in range(number):
        rolled_faces.append(random.randint(1, faces))
    return rolled_faces


def get_points_from_dice(dice_numbers):
    """Returns the points a given dice throw yields."""
    result = 0
    for dice in dice_numbers:
        if dice == 1:
            result += 100
        elif dice == 6:
            result += 60
        else:
            result += dice
    return result


def student_pasch(players):
    """This is the main function. The whole game runs here."""
    
    number = 3
    faces = 6
    result_list = []
    for player in range(1, players+1):
        total_points = 0
        dice_numbers = []
        # player can throw 3 times
        for throw in range(3):
            user_input = user_interface(player, throw)
            if user_input == "":
                user_input_2 = ""
                # at the beginning, throw immediately
                if len(dice_numbers) > 0:
                    user_input_2 = user_interface_2()
                # throw all dice again
                if user_input_2 == "":
                    dice_numbers = roll_dice(number,faces)
                else:
                    for index, dice in enumerate(dice_numbers):
                        if index not in user_input_2:
                            dice_numbers[index] = roll_dice(1,faces)[0]
                total_points = get_points_from_dice(dice_numbers)
                print()
                print("Deine aktuellen Würfel sind:", ', '.join(map(str,dice_numbers)))
                print("Deine aktuelle Punktzahl beträgt:", total_points)
                print()

            # 300 is the maximum points
            if total_points == 300 or user_input == "n":
                print()
                print("Dein Zug ist beendet.")
                print()
                break
        result_list.append(total_points)
    # end of game, show scores
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
        if int(players) > 1:
            break
        elif int(players) < 0:
            quit()
        else:
            print("ERROR: Du musst eine positive Ganzzahl eingeben, die größer oder gleich 2 ist!")
        print()
    print()
    return players


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
            student_pasch(set_players())
        else:
            print()
            print("ERROR: Falsche Eingabe - bitte versuchen Sie es erneut!")
            print()


def main():
    student_pasch(set_players())


if __name__ == '__main__':
    main()