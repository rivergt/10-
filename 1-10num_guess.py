#猜数字游戏2.0版本【20191018AM11:25】
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
answer = random.randint(1,10)
print("我爱猜数字游戏2.0版本")
guess = int(input("来猜猜我心里想的是哪个数字，1-10随便选一个吧："))
counter = 0
if (guess == answer) and (counter == 0) :
    print("恭喜你，第一次就答对了")
else:
    while (guess != answer) and (counter < 4) :
        counter += 1
        if guess > answer:  
            print("猜大了，您已经猜过",counter,"次了，最多5次哦")
            guess = int(input("再猜小一点试试吧："))
        else:
                print("猜小了，您已经猜过",counter,"次了，最多5次哦")
                guess = int(input("再猜大一点试试吧："))     
if counter == 0 :
    print("再见！")
else:
    if guess != answer:
        print("次数超过5次，您依然没有猜对，游戏结束。\n再见")
    else:
        print("恭喜你，答对了，游戏结束。\n再见！")


