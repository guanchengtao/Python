import random
from methods import GetSum, GetDev

print(max(1, 2))

num1 = random.choice(range(1, 10))
print(num1)

num2 = random.randrange(10)
print(num2)

num3 = random.random()
print(num3)
myarray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(myarray)
for i in myarray:
    print(i, end="\t")
var1 = 'Hello World!'

letter = "abcdefghijklmn"
print(letter.upper())
print(letter[2:6])  # cdef
print(letter[2:8])  # cdefgh
print(letter[1:5])  # bcde
# letter[m:n] 可以理解成从索引为m开始，往后取 n - m 个
print(letter[:5])  # 从开始取到5个
print(letter[3:])  # 从索引为3开始取到最后
print(letter[:1] + letter[-1:])  # -1是从倒数第二个开始
n = len(myarray)
for i in range(n):
    for j in range(n - i - 1):
        if myarray[j] > myarray[j + 1]:
            myarray[j], myarray[j + 1] = myarray[j + 1], myarray[j]
print("after sort")
for i in myarray:
    print(i, end="\t")
pass
list = []  ## 空列表
count = 0
while count < 10:
    list.append(random.random())
    count += 1
for i in list:
    print(i, end="\n")
print(max(list),min(list))
dic = {"name": "gct", "class": 1, "age": 21}
print(dic["name"])
dic["home"] = "QingDao"
del dic["name"]
keys = dic.keys()
for i in keys:
    print("key =", i, "value =", dic[i], end=",")
a = int(input("please input sum number..."))
b = int(input("please input added number"))
result = GetSum(a, b)
print('the sum is', result)

