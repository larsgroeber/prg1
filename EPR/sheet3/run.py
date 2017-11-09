import random as r
from sixteen_is_dead import sixteen_is_dead


def roll_dice(number=1, faces=6, seed=None):
    if not 1 <= number <= 10:
        raise ValueError(
            "The number of dice has to be in the interval [1,10]!")
    if not 2 <= faces <= 100:
        raise ValueError(
            "The number of faces has to be in the interval [2,100]!")

    r.seed(seed)
    return ','.join([str(r.randint(1, faces)) for i in range(number)])


def roll_cheating_dice():
    return [1, 2, 3, 3, 4, 5, 6][r.randint(0, 6)]


def get_players():
    players = input("Please enter the number of players: ")
    if not players.isdigit() or not 2 <= int(players):
        print("Please try again.")
        return get_players()
    return int(players)


print("//////")
print("//////")
print("////// Welcome to sixteen is dead!")
print("//////")
print("//////")
print()

sixteen_is_dead(get_players())
