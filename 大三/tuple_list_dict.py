#list列表
#第一步 请在列表fruits中找出不属于水果一类元素，赋值给变量 a
# fruit = ["苹果","梨子","菠萝","黄瓜","香蕉"]
# a = fruit[3]
# print(a)
# #第二步 将变量 a 的值添加到列表vegetable 的末尾
# vegetable = ["土豆","萝卜","茄子","白菜"]
# vegetable.append(a)
# print(vegetable)
# #第三步 删去列表fruit中不属于水果的元素
# fruit.pop(3)
# print(fruit)
# #两个列表合在一个列表
# food = fruit+vegetable
# print(food)
# print(food)
# print(food[0])
# print(food[2])
# #第四步 将列表fruit和列表vegetable作为元素按顺序加入到列表food中
# food=[fruit,vegetable]
# #最后打印输出列表food，打印输出列表food中第1个元素的第3个元素
# print(food)
# print(food[0][2])

# #tuple元组
# #第一题  列表和元组相互转换，修改元组中的数据
# #第一步  将元组 fruit 转换为一个名为 fruit 的列表并打印输出
# fruit = ("苹果","梨子","菠萝","黄瓜","香蕉")
# fruit = list(fruit)
# print(fruit)
# #第二步  在上一步得到的列表 fruit 通过索引位置将"黄瓜"去掉并打印输出
# fruit.pop(3)
# print(fruit)
# #第三步  将上一步的到的列表 fruit 转换为元组并打印输出
# fruit = tuple(fruit)
# print(fruit)

# #第二题  通过元组的嵌套修改元组中的数据
# #第一步  创建元组 food 将列表 fruit 和 vegetable 放入其中并打印输出元组food
# fruit = ["苹果","梨子","菠萝","黄瓜","香蕉"]
# vegetable = ["土豆","萝卜","茄子","白菜"]
# food = [fruit,vegetable]
# food = tuple(food)
# print(food)
# #第二步  打印输出上一步得到的元组 food 的第一个元素（列表fruit）
# print(food[0])
# #第三步  通过索引位置去掉元组 food 的第一个元素（列表fruit）的"黄瓜"
# del(food[0][3])
# print(food[0])          #打印输出列表 food 的第一个元素
# #第四步  打印输出元组 food
# print(food)

#set集合
# # -*- coding: utf-8 -*-
# #********* Begin *********#
# #第一步 请将列表fruit转换为一个集合
# fruit = ["苹果","梨子","菠萝","黄瓜","香蕉"]
# fruit = set(fruit)
# #第二步 将集合fruit中的“黄瓜”去掉
# fruit.remove("黄瓜")
# #第三步 使用"in"判断"黄瓜"是否在fruit中，将判断结果打印输出
# print("黄瓜" in fruit)
# #第四步 创建空集合food，输出集合food的长度
# food=set()
# print(len(food))
# #第五步 将fruit和vegetable合并到food并输出此时food的长度
# vegetable = {"土豆","萝卜","茄子","白菜"}
# food = (fruit | vegetable)
# print(len(food))
# #********* End *********#

#dict(dictionary)字典
#第一步 创建一个空字典 menu
menu={}
#第二步 将列表fruit中水果与prices中的价格对应给menu赋值并输出
fruit = ["苹果","梨子","菠萝","黄瓜","香蕉"]
prices = [2,3,10,2,1]
menu = {"苹果":2,"梨子":3,"菠萝":10,"黄瓜":2,"香蕉":1}
print(menu)
#第三步 将20块钱的"哈密瓜"添加到字典menu中并输出
menu["哈密瓜"] = 20
print(menu)
#第四步 将"黄瓜"从menu中去掉并输出
del menu["黄瓜"]
print(menu)
#第五步 将菠萝的价格修改为9.9，打印输出menu
menu["菠萝"]=9.9
print(menu)