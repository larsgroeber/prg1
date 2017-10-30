input_string = input()
inputs = input_string.split(" ")

first_mark = float(inputs[0])
sex = inputs[1]
body_size = int(inputs[2])

mark = first_mark

if not (100 <= body_size <= 300) or not (1.0 <= first_mark <= 5.0):
    print("ERROR")
    exit(-1)

if sex == "w":
    mark -= 0.4
if body_size > 180:
    mark += (body_size - 180) * 0.05

# make sure the mark is allowed
allowed_marks = [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 5.0]
# returns the closest allowed mark
mark = allowed_marks[min(range(len(allowed_marks)), key=lambda index: abs(allowed_marks[index] - mark))]

print("{:0.1f}".format(mark))
