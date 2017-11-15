"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

__author__ = "123456: John Cleese, 654321: Terry Gilliam"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "your email address"


# a)
def ackermann_recursive(n, m):
    """Recursive implementation of the given ackermann function"""
    if n == 0:
        return m + 1
    if m == 0:
        return ackermann_recursive(n - 1, 1)
    return ackermann_recursive(n - 1, ackermann_recursive(n, m - 1))


# b)
def recursive_implementation(n):
    """Recursive implementation for exercise b) (for testing purpose)"""
    if n <= 1:
        return n
    return recursive_implementation(n - 1) + recursive_implementation(n - 2)


def iterativ_implementation(n):
    """Iterative implementation for exercise b)"""
    stack = []
    stack.append(n)
    result = 0
    while len(stack) != 0:
        value = stack.pop()
        if value <= 1:
            result += value
            continue
        stack.append(value - 1)
        stack.append(value - 2)
    return result


# c)
def words_to_digits_converter():
    """Converts an input string to a decimal number.
       Does not convert (for some reason) more than 4 numbers."""
    user_input = input("Please enter your numbers as words: ")
    digit_words = user_input.split(",")
    DIGITS = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"]
    result = ""
    # I assume "maximal 4 Dezimalstellen" means, only show the last 4
    for word in digit_words[-4:]:
        result += str(DIGITS.index(word))
    print(result)


# d)
def words_to_digits_converter_while():
    print("I have no idea what you want from me...")


def main():
    print("Ackermann function for n = 2, m = 3:")
    print(ackermann_recursive(2, 3))  # 9
    print()
    test = 6
    print("Test if the iterative implementation equals the recursive one:")
    print(recursive_implementation(test) == iterativ_implementation(test))  # true

    print()
    words_to_digits_converter()


if __name__ == '__main__':
    main()
