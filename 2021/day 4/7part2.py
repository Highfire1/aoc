x = [['24', '9', '94', '69', -1], ['97', -1, '85', '53', -1], ['92', '11', '61', -1, '8'], [-1, -1, -1, -1, -1], [-1, '68', '55', '52', '93']]
x = sum(x, [])


print(x)

value = 0

for num in x:
    if num != -1:
        value += int(num)

finalnum = 75
print(value * finalnum)
