# import random as r
#
# print(r.randint(1, 10))
#
# print(r.random())
#
# print(r.randrange(0, 30, 5))
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r.shuffle(nums)
# print(nums)
#
# print(r.choice(nums))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)

another_new_list = list(map(lambda x: (x % 2 ==0), my_list))

print(another_new_list)