#!/usr/bin/python3
# 循环语句
from random import randrange

print("Hello, World!")
a, b = 0, 1
while b < 10:
    print(b)
    '''先计算右边的表达式，然后同时赋值给左边'''
    a, b = b, a + b
print("------------------")
myList = ["C++", "Java", "Python", "PHP", "Golang"]
for item in myList:
    if item == "PHP":
        print(item + "世界上最好的语言")
    elif item == "C++":
        print(item + "入门级语言")
    else:
        print(item)
print("---------------------")
myArray = [8, 1, 2, 3, 4, 5, 6, 7]
for item in myArray:
    print(item, end="\t")
print("\n")
print("--------try to write a bubble sort-------------")
print("---------begin------------")
array1 = [1, 5, 2, 7, 3, 0, 4, 9]
n = len(array1)
for i in range(n):
    flag = 1
    for j in range(0, n - i - 1):
        if array1[j] > array1[j + 1]:
            array1[j], array1[j + 1] = array1[j + 1], array1[j]
            flag = 0
    if flag == 1:
        break
for i in array1:
    print(i, end="\t")
print("\n")
print("---------end--------------")
a = 1
while a < 10:
    if a % 2 == 0:
        print(a, "is even")
        print
    else:
        print(a, "is odd")
    a += 1
#
age = 1
# int(input("please input your dog age"))
if age <= 0:
    print("no probable")
elif age == 1:
    print("this is a small dog")
elif age == 2:
    print("this is a big dog")
else:
    print("????????")
'''
real_answer = randrange(1, 10, 1)
player_answer = -1
while real_answer != player_answer:
    player_answer = int(input("please input you choice"))
    if player_answer == real_answer:
        print("Congregations!")
    elif player_answer > real_answer:
        print("The real answer is less than your input")
    else:
        print("The real answer is more than your input")

print("The final rea answer is ", real_answer)
'''
for letter in "Python":
    print('current letter:', letter)
fruits = ['apple', 'banana', 'orange', 'watermelon','pear']
# two print methods
for i in range(len(fruits)):
    print(fruits[i], end="\t")
print("")
for fruit in fruits:
    print(fruit, end="\t")


'''
str='helloworld'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print((str+'\n') * 20)             # 输出字符串两次
print(str + '你好')        # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
'''
