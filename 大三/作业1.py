'''
要求：首先输入学生人数
并根据输入的人数输入姓名（n个）
身高（0.5<height<2.5）
体重（20<weight<300）
腰围（50<waistline<200）
要求在一行输入一个人的所有数据
通过字符串分割得到数据内容
输入值如果不在合理范围要输出提醒信息并要求重新输入
如果输入类型错误，会正确设置异常处理使得程序继续运行
计算每位同学的BMI指数并按照BMI指数排序（可以使用列表的sort函数完成）
判断出每个同学属于偏瘦（<18.5）、正常（>=18.5 and <24）、偏胖（>24 and <28）、肥胖（>28）
排序后的数据排版输出到文件中，关闭文件，手工打开文件验证正确性
能够读出预定文件的内容并把其中的所有数据保存在预设的变量中，在屏幕中输出所有变量内容
'''
n=int(input("一共有多少位学生："))
i=0
result=0
student=[]
list_a=[]
while i < n:
    try:
        name,height,weight,waistline = input().split(" ")
        height = float(height )
        weight = float(weight)
        waistline = int(waistline)
        if 0.5 < height  < 2.5 and 20 < weight < 300 and 50 < waistline < 200:
            i += 1
            BMI = round(weight / (height ** 2), 1)
            if BMI > 28:
                result = '肥胖'
            elif BMI > 24 and BMI < 28:
                result = '偏胖'
            elif BMI >= 18.5 and BMI < 24:
                result = '正常'
            elif BMI < 18.5:
                result = '偏瘦'
            student = [name, height, weight, waistline, BMI, result]
            list_a.append(student)
            list_a.sort(key=lambda x: x[4], reverse=True)
        else:
            print("输入数据不符合实际")
    except:
        print("输入内容类型出错")
    else:
        pass
f=open('BMI.txt','w')
f.write('姓名    身高     体重      腰围     BMI指数   分析结果')
for i in range(n):
    print(file=f)
    for j in range(6):
        print(list_a[i][j], end='      ',file=f)
f.close()
'''输入内容
张三 1.85 105.5 108
王五 1.73 76.3 74
李四 1.62 62.5 70
'''
'''BMI.txt文件显示
姓名    身高     体重      腰围     BMI指数   分析结果
张三      1.85      105.5      108      30.8      肥胖      
王五      1.73      76.3      74      25.5      偏胖      
李四      1.62      62.5      70      23.8      正常 
'''
