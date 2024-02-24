n = 567
last_digit = n % 10
first_digit = n
while int(first_digit/10) > 0:
    first_digit = int(first_digit/10)
print("sum=", first_digit+last_digit)


