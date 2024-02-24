list1=[1,2,3,4,5,6]
list2=[3,4,5,6,7,8]
list3=[5,6,7,8,9,10]
unique_elements =[]
duplicates = set()
for number in list1:
    if number in unique_elements:
        duplicates.add(number)
    else:
        unique_elements.append(number)
for number in list2:
    if number in unique_elements:
        duplicates.add(number)
    else:
        unique_elements.append(number)
for number in list3:
    if number in unique_elements:
        duplicates.add(number)
    else:
        unique_elements.append(number)

print("duplicate elements are : ", duplicates)
