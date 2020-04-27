# print('hello kitty')
# print('今天我们，''开始学习，''python编程，'"祝大家，"'''编程愉快''')
# print(100)
# print(1.2345)
# print(100+1.2345)

#输入输出 两个数的加减乘除
# if __name__ == "__main__":
#     a = eval(input())
#     b = eval(input())
#     print('%d + %d = %d'  %(a,b,a+b))
#     print('%d - %d = %d'  %(a,b,a-b))
#     print('%d * %d = %d'  %(a,b,a*b))
#     print("%d / %d = %f"  %(a,b,a/b))

# print("2017是我国GDP是",82.71,"万亿元")
# a=100
# b=234.567
# s="这是个字符串"
# print(a,b,s)

# print(123,"abc",45,"book","东软")
# print(123,"abc",45,"book","东软",sep="$")

# print('我是\n gg\n')

# a=input("输入一个整数")
# print(a)#输出a的值，可以看出输出的是一个字符串类型
# print(a+1)#输出a+1的值，会因为试图执行字符串和数字的加法而报错

# x=float(input("请输入第一个数："))
# y=float(input("请输入第二个数："))
# z=float(input("请输入第三个数："))
# sum=x+y+z
# ave=sum/3
# print("三个数的和是：%f"%sum)
# print("三个数的平均数是：%0.2f"%ave)

# 单行注释
'''
多行注释
'''

# 语句换行
# string = (
#     "wa ta xi\t"
#     "gg"
# )
# print(string)

# 学习通练习
# name = input("姓名是：")
# height = int(input("请输入身高（米）："))
# weight = int(input("请输入体重（千克）："))
# BMI = weight/(height*height)
# print("姓名是%s，身高是%s，体重是%s，BMI值是%s"%(name,height,weight,BMI))

# 学习通任务1输入和输出综合练习
# name = input("姓名是：")
# height = input("请输入身高（米）：%.2f")
# weight = input("请输入体重（千克）：%.1f")
# waistline = int(input("请输入腰围（厘米）："))
# print("{0} {1} {2} {3}".format(name,height,weight,waistline))

x = input() # 输入数据
y = [] # 列表
y = x.split(" ") # 把数据按空格切片放入y
print("姓名"+"    "+"身高"+"    "+"体重"+"     "+"腰围"+"  ")
for i in range(len(y)):
    print(y[i],end="    ")
    if (i+1)%4 == 0 :
        print("\n")
# 张三 1.85 1.5.5 108 李四 1.62 62.5 70 王五 1.73 76.3 74

#模块导入与使用
#import math
#只想用sin函数
#print(math.sin(0.5))#求0.5的正弦
# from math import sin as f#别名
# print(f(30))
# import random
# x=random.random()#获得[0,1]内随机小数
# y=random.random()
# n=random.randint(1,100)#获得[1,100]的随机整数
# print(x,y,n)