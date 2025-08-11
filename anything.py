##НЕПРАВИЛЬНО
# from testing_import import my_list
from calendar import month
from operator import length_hint


# n = int(input())
# hours = n // 60
# if hours < 24:
#     hours = n
# else:
#     hours = 0
# print(hours)
# print(n % 60)

##ПРАВИЛЬНО
# n = int(input())
# hours = n // 60
# while hours >= 24:
#     if hours < 24:
#         pass
#     else:
#         hours = hours - 24
# print(hours)
# print(n % 60)



# name = input()
# print(f'Hello, {name}!')

# a = float(input())
# n = int(input())
# def power(a, n):
#     return a ** n
# print(power(a, n))

# word = 'книга'
# print(ord(word[0]))
# print(chr(1082).upper())
# print(word[0].upper() + word[])


# x = 0
# while x == 0:
#     try:
#         a = int(input())
#         b = int(input())
#         print(a / b)
#         x = 1
#     except ZeroDivisionError:
#         print('Деление на ноль!')

# s = 'плохо хуево не круто не хорошо плохо'
# # print(s.replace('плохо', 'хорошо'))
# a = s.replace('плохо', 'хорошо').casefold().split()
# print(a)



# months = {
#     "01": "января",
#     "02": "февраля",
#     "03": "марта",
#     "04": "апреля",
#     "05": "мая",
#     "06": "июня",
#     "07": "июля",
#     "08": "августа",
#     "09": "сентября",
#     "10": "октября",
#     "11": "ноября",
#     "12": "декабря"
# }
#
# dates = ['2025-08-10', '2024-12-31', '2023-03-01']
# for date in dates:
#     parts = date.split('-')
#     print(f'{int(parts[2])} {months[parts[1]]} {parts[0]}')


# greet = 'Пользователь {name}, зашел в {hour} часов'
# print(greet.format(name='Иван', hour=12))

# text = 'qweQWES&? cjsd выфафы'
# print(text.casefold().upper().strip().split())

# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         return len(s.split()[-1])

# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         nums = ''.join(str(d) for d in digits)
#         int_num = int(nums)
#         int_num += 1
#         str_num = [int(d) for d in str(int_num)]
#         return str_num