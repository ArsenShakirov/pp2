def spy_game(nums):
    sequence = [0, 0, 7]
    idx = 0
    for num in nums:
        if num == sequence[idx]:
            idx += 1
        if idx == len(sequence):
            return True
    return False

n = int(input())
nums = [int(input()) for i in range(n)]
print(spy_game(nums))
