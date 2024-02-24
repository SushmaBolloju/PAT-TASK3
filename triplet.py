list1 = [10, 20, 30, 9]
n = len(list1)
list_triplets = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if list1[i]+list1[j]+list1[k] == 59:
                list_triplets.append(list1[i])
                list_triplets.append(list1[j])
                list_triplets.append(list1[k])
print("sum of triplets equal to 59:", list_triplets)
