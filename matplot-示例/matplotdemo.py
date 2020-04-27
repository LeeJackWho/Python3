# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 11:35:49 2019

@author: Yu-weiz
"""
"""
matplot数据可视化-基本操作示例
"""
#1、 绘制人口数量折线图
import matplotlib.pyplot as plt
year = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
pop = [6.49, 6.558, 6.656, 6.725, 6.804, 6.884, 6.965, 7.043, 7.125, 7.207]
plt.figure() # 创建图表
plt.plot(year,pop) # 绘制图像
plt.show() # 显示图像

#自定义线的样式和颜色
plt.figure()
pop_cn = [1.30756, 1.31448, 1.32129, 1.32802, 1.33450, 1.34091, 1.34735, 1.35404, 1.36072, 1.36782]
plt.plot(year,pop,color = "g")
plt.plot(year,pop_cn,linestyle ="--", color = "r")
plt.show()

#3、添加图例
plt.figure()
plt.plot(year,pop,color = "g",label = "World population")
plt.plot(year,pop_cn,linestyle ="--", color = "r",label = "China population")
plt.legend()
plt.show()

# 4、添加标题和轴标签
plt.plot(year, pop)
plt.title("World Population Summary")
plt.xlabel("Year")
plt.ylabel("Polulation")
plt.show()

#5、设置刻度以及刻度标签
plt.figure()
plt.plot(year, pop)
plt.title("World Population Summary")
plt.xlabel("Year")
plt.ylabel("Polulation")
plt.yticks([6, 6.5, 7, 7.5], ['6B', '6.5B', '7B', '7.5B'])
plt.show()

#6、绘制散点图
plt.figure()
plt.scatter(year, pop)
plt.title("World Population Summary")
plt.xlabel("Year")
plt.ylabel("Polulation(Billion)")
plt.show()

#给图标添加注解
plt.figure()
plt.scatter(year, pop)
plt.title("World Population Summary")
plt.xlabel("Year")
plt.ylabel("Polulation(Billion)")
plt.text(2013,7.13,'2013')
plt.show()

#绘制共享x轴的两个子图
f, (ax1,ax2) = plt.subplots(2, sharex=True)
ax1.scatter(year, pop)
ax1.set_title('World Population Summary')
ax2.scatter(year, pop_cn)
ax2.set_title('China Population Summary')
plt.show()

#绘制双y轴的图表
fig = plt.figure()
ax3 = fig.add_subplot(111)
ax3.plot(year,pop,color = "g",label = "World population")
ax3.set_ylabel('World population')
ax3.set_title("Double Y axis")
ax4 = ax3.twinx()
ax4.plot(year,pop_cn,linestyle ="--", color = "r",label = "China population")
ax4.set_ylabel('China population')
ax4.set_xlabel('Year')
plt.show()

#5、将图片保存到文件
fig = plt.figure()
ax3 = fig.add_subplot(111)
ax3.plot(year,pop,color = "g",label = "World population")
ax3.set_ylabel('World population')
ax3.set_title("Double Y axis")
ax4 = ax3.twinx()
ax4.plot(year,pop_cn,linestyle ="--", color = "r",label = "China population")
ax4.set_ylabel('China population')
ax4.set_xlabel('Year')
plt.show()
plt.savefig('figure.svg', dpi=400, bbox_inches = 'tight')
#保存的结果可以在“C:\Users\Administrator\.spyder-py3”目录中看到。文件名为“figure.svg”

#6、绘制柱状图
fig = plt.figure()  
plt.bar(year,pop,0.4,color="blue")  
plt.xlabel("year")  
plt.ylabel("pop")  
plt.title("bar chart")
plt.show()
