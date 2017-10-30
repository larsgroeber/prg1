input_string = input("Please enter a number between 0 and 99: ")

# we only accept integers
input_number = int(input_string)

if not 0 <= input_number <= 99:
    print("ERROR")
    exit(-1)

output = ""

if input_number % 3 == 0 or "3" in input_string:
    output += "fizz"

if input_number % 7 == 0 or "7" in input_string:
    output += "buzz"

# print output only if it is not an empty string
print(input_string if output == "" else output)
