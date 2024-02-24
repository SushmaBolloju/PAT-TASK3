list = [1,7, 2, 3, 2, 1, 4, 5, 4, 6, 3, 6, 5]
frequency = {}
for i in list:
    if i in frequency:
        frequency[i] = frequency[i]+1
    else:
        frequency[i] = 1
l = len(list)
for r in range(0, l):
    if frequency[list[r]] == 1:
        print("first non repeating element is:", list[r])
        break
    elif r == l-1:
        print("no non repeating element found")
