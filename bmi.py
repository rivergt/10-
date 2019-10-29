#计算BMI公式
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
height = float(input('请输入您的身高，单位为米，例如1.75，按Enter确认:'))
weight = float(input('请输入您的体重，单位为千克，例如70,按Enter确认:'))
if height>0 and weight>0:
    bmi = weight/(math.pow(height,2))
    if 0<=bmi<18.5:
         print ('您的身高是%.2f米，体重是%.2f千克，BMI指数为%.2f,过轻' % (height,weight,bmi))
    elif 18.5<=bmi<25:
         print ('您的身高是%.2f米，体重是%.2f千克，BMI指数为%.2f,正常' % (height,weight,bmi))
    elif 25<=bmi<28:
         print ('您的身高是%.2f米，体重是%.2f千克，BMI指数为%.2f,过重' % (height,weight,bmi))
    elif 28<=bmi<32:
         print ('您的身高是%.2f米，体重是%.2f千克，BMI指数为%.2f,肥胖' % (height,weight,bmi))
    else:
         print ('您的身高是%.2f米，体重是%.2f千克，BMI指数为%.2f,严重肥胖' % (height,weight,bmi))
else:
    print('输入错误，欢迎下次测试！')
