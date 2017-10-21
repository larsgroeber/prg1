input_string = input("Please enter 4 comma separated numbers: ")

input_array = input_string.split(",")

if len(input_array) != 4:
    raise ValueError("Input string does not contain 4 elements!")

input_sum = sum([float(e) for e in input_array])

print("Sum: {}".format(input_sum))
