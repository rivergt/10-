# Tower of Hanoi
def hanoi(n,x,y,z):
    if n == 1:
        print(x,'->',z)
    else:
        #将前n-1个盘子从X移动到y上
        hanoi(n-1,x,z,y)
        print(x,'->',z)
        #将y上的n-1个盘子移动到z上
        hanoi(n-1,y,x,z)

n = int(input('please input hanoi level:'))
hanoi(n,'X','Y','Z')
