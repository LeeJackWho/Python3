#函数的定义与调用
# def add2num(a,b):
#     c=a+b
#     return c
# d=add2num(11,22)
# print(d)

#txt文件的读写 文件所在位置：E:\Python\C1
# f=open('itheima.txt','w')
# f.write('hello itheima,i am here!\n')
# f.write('who are you')
# f.close()

# #使用read读取文件
# f=open('itheima.txt','r')
# content=f.read(12)
# print(content)
# print("-"*30)
# content=f.read()
# print(content)
# f.close()

# #使用readlines读取文件
# f=open('itheima.txt','r')
# content=f.readlines()
# i=1
# for temp in content:
#     print("%d:%s"%(i,temp))
#     i+=1
# f.close()

#使用readline方法一行一行读
f=open('itheima.txt','r')
content=f.readline()
print("1:%s"%content)
content=f.readline()
print("2:%s"%content)
f.close()