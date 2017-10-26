input_string = input()
inputs = input_string.split(" ")

first_mark = float(inputs[0])
sex = inputs[1]
body_size = int(inputs[2])

mark = first_mark

# is 0.0 allowed?
if not (100 <= body_size <= 300) or not (0.0 <= first_mark <= 5.0):
    print("ERROR")
    exit(-1)

if sex == "w":
    mark -= 0.4
if body_size > 180:
    mark += (body_size - 180) * 0.05

mark = max(0.0, min(mark, 5.0))

print("{:0.1f}".format(mark))
