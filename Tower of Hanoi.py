# Tower of Hanoi
#定义汉诺塔移动核心函数，输出移动步骤
def hanoi(n,x,y,z):
    if n == 1:
        print(x,'->',z)
    else:
        #将前n-1个盘子从X移动到y上
        hanoi(n-1,x,z,y)
        print(x,'->',z)
        #将y上的n-1个盘子移动到z上
        hanoi(n-1,y,x,z)

#定义汉诺塔移动步数函数
def count(n):
    if n == 1:
        return 1
    else:
        return 2*count(n-1)+1
   

#汉诺塔程序
n = int(input('please input hanoi level:'))
if n < 1:
    pirnt('error')
else:
    counter = count(n)
    print('%d级三柱汉诺塔需要%d步' % (n,counter))
    hanoi(n,'X','Y','Z')
