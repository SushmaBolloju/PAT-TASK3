s = [10, 501, 22, 37, 100, 999, 87, 351]
s2 = []
s3 = []
for i in s:
    if i % 2 == 0:
        s2.append(i)
    else:
        s3.append(i)
print("even numbers list s2 is:", s2)
print("odd numbers list s3 is:", s3)
