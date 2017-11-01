i_values = [1,5,9,12,16]
for i in i_values:
    a = i
    b = 1
    while (a - b) > 0.001:
        a = (a + b) / 2
        b = i / a
    print((a + b) / 2)