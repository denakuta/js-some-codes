# nums = [1,3,5,6]
# target = 7
#
# for num in nums:
#     if num >= target:
#         print(nums.index(num))
#         break
# print(nums.index(nums[-1]) + 1)

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    if x == 0:
        return 0
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

print(sqrt(10))