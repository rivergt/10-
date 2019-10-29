#连续20道10以内加减法
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

def add():
    counter = 0
    right = 0
    wrong = 0
    print('现在开始练习10以内加法，一共20道')
    while counter<20:
        counter +=1
        x = random.randint(0,6)
        y = random.randint(0,6)
        print('第%d题，请问%d + %d等于多少？'% (counter,x,y))
        answer = int(input('请输入你的答案，按Enter确认：'),base=10)
        if answer == x+y:
            right +=1
            print('恭喜你,答对了，你已经答对%d道题了！'% (right))
        else:
            wrong +=1
            print('不好意思，答错了，你已经答错%d道题了！' % (wrong))
    rate = right/counter*100
    print('练习结束，此次练习共答对%d道题，正确率是%.1f%%。' % (right,rate))

def subtract():
    counter = 0
    right = 0
    wrong = 0
    print('现在开始练习10以内减法，一共20道')
    while counter<20:
        counter +=1
        x = random.randint(0,10)
        y = random.randint(0,x)
        print('第%d题，请问%d - %d等于多少？'% (counter,x,y))
        answer = int(input('请输入你的答案，按Enter确认：'),base=10)
        if answer == x-y:
           right +=1
           print('恭喜你,答对了，你已经答对%d道题了！'% (right))
        else:
           wrong +=1
           print('不好意思，答错了，你已经答错%d道题了！' % (wrong))
    rate = right/counter*100
    print('练习结束，此次练习共答对%d道题，正确率是%.1f%%。' % (right,rate))

select=int(input('现在开始练习10以内加减法，加法请输入1，减法请输入2，按Enter确认：'))
if select == 1:
    add()
elif select == 2:
    subtract()
else:
    print('输入错误，再见')
