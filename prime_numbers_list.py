a = [10, 501, 22, 37, 100, 999, 87, 351]
prime = []
for i in a:
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count = count+1
    if count == 0:
        prime.append(i)
print("prime numbers list is:", prime)