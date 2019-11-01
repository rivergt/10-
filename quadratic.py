#一元二次方程求解程序
#!/usr/bin/python
# -*- coding: UTF-8 -*-

##### 导入数学模块
import math
##### 定义求解公式
def quadratic(a,b,c):
    delta =  b*b-4*a*c
    if delta < 0:
        print('判别式<0，无实根')
        return()
    elif delta == 0:
        x1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
        print('判别式=0，有两个相同实根，分别是',x1,x1)
        return(x1,x1)
    else:
        x1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
        print('判别式>0，有两个不同实根，分别是',x1,x2)
        return (x1,x2)
##### 廖老师的测试程序，删除了print字段:
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
##### 输入三个系数，求解
a = int(input('请输入一元二次方程的二次项系数：'))
b = int(input('请输入一元二次方程的一次项系数：'))
c = int(input('请输入一元二次方程的常数项系数：'))
print(quadratic(a,b,c))


    
