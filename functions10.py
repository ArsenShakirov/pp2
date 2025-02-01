def unique_elements(nums):
    unique_list = []
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

nums = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(nums))


