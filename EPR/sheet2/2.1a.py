input_string: str = input("Please enter a sentence: ")

for char in map(chr, [a for a in range(97, 97 + 24)]):
    if char not in input_string.lower():
        print("'{}' is not a pangram.".format(input_string))
        exit()

print("'{}' is a pangram.".format(input_string))
