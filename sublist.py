def sublist(l):
    prefix_sums = set() #initialising a set to store prefix sums
    current_sum = 0
    for num in l:
        current_sum = current_sum+num
        if current_sum == 0 or current_sum in prefix_sums:
            return True
        prefix_sums.add(current_sum)
    return False


given_list = [4, 2, -3, 1, 6]
result = sublist(given_list)
print("is there a sublist with sum zero :", result)
