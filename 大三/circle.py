# nameList = [['张三',175,75],['李四',180,50],['王五',165,100]]
# for name in nameList:
#     print(name)

# if __name__ == "__main__":
# 	a = eval(input())
# 	b = eval(input())
# 	print('%d + %d = %d'  %(a,b,a+b))
# 	print('%d - %d = %d'  %(a,b,a-b))
# 	print('%d * %d = %d'  %(a,b,a*b))
# 	print("%d / %d = %f"  %(a,b,a/b))

import string
import random
x=string.ascii_letters+string.digits+string.punctuation
y=[random.choice(x) for i in range(1000)]
z=''.join(y)
d=dict()
for ch in z:
    d[ch]=d.get(ch,0)+1
print("x:"+x)
print("y:%s" %y)
print("z:%s" %z)
print("d:%s" %d)
