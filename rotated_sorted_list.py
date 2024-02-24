def min_element(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        middle = left + (right-left)//2
        if nums[middle] > nums[right]:
            left = middle+1
        else:
            right = middle
    return nums[left]


rotated_sorted_list = [5, 6, 7, 1, 2, 3, 4]
print("minimum element in the rotated and sorted list is:", min_element(rotated_sorted_list))