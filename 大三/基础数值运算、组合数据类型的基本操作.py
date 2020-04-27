#1.球体体积计算公式：V=4/3πr³;其中r为球的半径，V为球的体积；
#2.π取3.14159。
# r=eval(input())
# V=4/3*3.14159*r**3
# print(round(V,2))

# 1.用input()函数读取两个字符串strA和strB；
# 2.打印出strA的第一个字符；
# 3.对strA进行分片操作，打印出除最后2个字符以外的内容；
# 4.把strA和strB拼接在一起，用空格” “隔开，打印出来。
strA = input()
strB = input()
print(strA[0:1])
print(strA[:-2])
print(strA+' '+strB)
#实例输入
# apple
# python
#实例输出
# a
# app
# apple python