##1
# num = input('трехзначное число: ')
# print(int(num[0]) - int(num[2]))

##2
# num = int(input('число: '))
# numx = num % 9
# if numx == 0:
#     print('делится')
# else:
#     print('не делится')

##3
num = input('двухзначное число: ')



##12
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

##13
a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
     if i % 2 == 0:
          count += 1
print('колво четных: ', count)

