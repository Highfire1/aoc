x = [['79', -1, '70', -1, -1], [-1, '8', -1, '23', -1], ['40', '67', '66', '55', -1], [-1, '61', -1, -1, -1], [-1, -1, '24', -1, -1]]
x = sum(x, [])


print(x)

value = 0

for num in x:
    if num != -1:
        value += int(num)

finalnum = 91
print(value * finalnum)

# 44863 too high