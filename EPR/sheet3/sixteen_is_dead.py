import random as r
from time import sleep


def roll_dice_sensible(num_dice=1, faces=6):
    return [r.randint(1, faces) for i in range(num_dice)]


def get_num_dice():
    num_dice = input("Please enter the number of dice (default is 1): ")
    if num_dice == '':
        return 1
    elif num_dice.isdigit() and 1 <= int(num_dice) <= 10:
        return int(num_dice)
    print("Please try again.")
    return get_num_dice()


def get_faces():
    faces = input("Please enter the number of faces (default is 6): ")
    if faces == '':
        return 6
    elif faces.isdigit() and 2 <= int(faces) <= 100:
        return int(faces)
    print("Please try again.")
    return get_faces()


def show_scoreboard(player_scores):
    print("\nScoreboard:")
    for index, score in enumerate(player_scores):
        print("Player {} got {} points".format(index, score))
    print()


def ask_throw_again(player_scores):
    player_input = input(
        "Do you want to continue? (Press RETURN to continue or <n> "
        "for next player or <s> for the scoreboard)")
    if player_input == '':
        return True
    elif player_input == 'n':
        return False
    elif player_input == 's':
        show_scoreboard(player_scores)
        return ask_throw_again(player_scores)
    print("Please try again")
    return ask_throw_again(player_scores)


def sixteen_is_dead(players):
    if players < 1:
        raise ValueError("The number of player cannot be smaller than 0!")

    num_dice = get_num_dice()
    faces = get_faces()

    player_score = [0 for i in range(players)]
    active_player = -1

    game_running = True

    print()
    print("Game ist starting with {} dice which have {} faces each.".format(
        num_dice, faces))
    print()
    while game_running and active_player < players - 1:
        active_player += 1
        print("It is your turn player {}".format(active_player))
        while True:
            print("You're throwing the dice...")
            sleep(1)
            rolled = roll_dice_sensible(num_dice, faces)
            print("You got: {}".format(", ".join([str(r) for r in rolled])))
            throw_sum = sum(rolled)
            player_score[active_player] += throw_sum
            print("That sets your total score to {}".format(
                player_score[active_player]))

            if player_score[active_player] >= 16:
                print("You lost")
                game_running = False
                break
            print()

            if player_score[active_player] == 9:
                print(
                    "You have reached a score of 9 and are not allowed "
                    "to throw again.")
                break

            if player_score[active_player] == 10:
                print(
                    "You have reached a score of 10 and have to throw again.")
                sleep(3)
                continue

            if ask_throw_again(player_score):
                continue
            break
        print()

    print()
    print("Game Over!")
    show_scoreboard(player_score)

    player_lost = active_player

    if max(player_score) < 16:
        min_score = min(player_score)
        num_lost_players = player_score.count(min_score)
        if num_lost_players != 1:
            player_lost = [str(i) for i, s in enumerate(player_score) if
                           s == min_score]
            print("Player {} lost.".format(" and player ".join(player_lost)))
        else:
            player_lost = player_score.index(min(player_score))
            print("Player {} lost.".format(player_lost))
    else:
        print("Player {} lost.".format(player_lost))
