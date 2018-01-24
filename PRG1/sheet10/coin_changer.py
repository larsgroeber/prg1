"""
Exercise 10.3.
"""

import math

class CoinChanger:
    """
    Implements a CoinChanger with Backtracking,
    following: https://en.wikipedia.org/wiki/Backtracking
    """

    def __init__(self, coins: [int]):
        self.available_coins = coins
        self.solution = None
        self.goal = None

    def input(self):
        """Gets user input."""
        goal = input(
            "Please enter the amount (integer, Cent) to calculate change for.\n>>> ")
        try:
            return float(goal)
        except ValueError:
            print("Please enter a float!")
            return self.input()

    def __reject(self, coins: []):
        """Returns True if current solution is not viable."""
        min_coins = len(self.solution) if self.solution else math.inf
        return len(coins) >= min_coins or CoinChanger.sum_coins(coins) > self.goal

    def __accept(self, coins: []):
        """Returns True if current coins is a solution."""
        return CoinChanger.sum_coins(coins) == self.goal

    def __first(self, coins: []):
        """Returns the first extension to coins."""
        return coins + [self.available_coins[0]]

    def __next(self, coins: []):
        """Returns the next sibling to coins."""
        if not coins:
            return None
        next_sibling_coins = CoinChanger.get_next_bigger_coin(self.available_coins, coins[-1])
        if next_sibling_coins is None:
            return None
        return coins[:-1] + [next_sibling_coins]

    def __output(self, coins: []):
        """Saves the current coins as a solution."""
        self.solution = coins

    def change(self, goal):
        """
        Calculates the change for a given goal.
        """
        self.goal = goal
        self.solution = []
        self.__change()
        return sorted(self.solution)

    def __change(self, current_coins = []):
        """Starts the backtracking algorithm."""
        if self.__reject(current_coins):
            return
        if self.__accept(current_coins):
            self.__output(current_coins)
        sibling = self.__first(current_coins)
        while sibling is not None:
            self.__change(sibling)
            sibling = self.__next(sibling)

    @staticmethod
    def sum_coins(coins):
        """Sums all coins."""
        return sum(coins)

    @staticmethod
    def get_next_bigger_coin(coins, coin):
        """Returns the next bigger coin to coin in coins."""
        index = coins.index(coin) + 1
        if index == len(coins):
            return None
        return coins[index]

if __name__ == "__main__":
    c = CoinChanger([11, 5, 1])
    change = c.change(c.input())
    print(f"The change for your amount is {change}.")
