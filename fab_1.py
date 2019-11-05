#斐波那契数列递归和迭代两种算法比较

def fab_1(n):
    if n<1:
        print('error')
        return -1
    elif n==1 or n==2:
        return 1
    else:
        return fab_1(n-1)+fab_1(n-2)

def fab_2(n):
    nf=1
    ns=1
    nt=0
    if n<1:
       print('error')
       return -1
    if n==1 or n==2:
       return 1
    while n>=3:
        nt=ns+nf
        nf=ns
        ns=nt
        n -= 1
    return nt
                    
n=int(input('please input one int number:'))
result_1 = fab_1(n)
result_2 = fab_2(n)
if result_1 != -1 and result_2 != -1:
    print('fab_1:%d,fab_2:%d' % (result_1,result_2))


    
