n = [10, 501, 22, 37, 100, 999, 87, 351]
hpy = []
for x in n:
    i = x
    while i >= 10:
        sum = 0
        while i > 0:
            r = i % 10
            sum = sum + (r**2)
            i = i//10
        print("sum:", sum)
        i = sum
    if i == 1:
        print(x, "is a happy number")
        hpy.append(x)
    else:
        print(x, "is not a happy number")
print("happy numbers list is:", hpy)
