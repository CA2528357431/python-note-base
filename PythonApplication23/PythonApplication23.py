#循环循环

x=1
y=1
while x<10:
    while y<=x:
        print("%d * %d = %d "%(x,y,x*y),end="")#防止换行
        y=y+1
    x=x+1
    y=1
    print("\n")


#    \后加标点可输入特殊符号，如"
#    \t 对齐   \n 换行  约等于   \r回车
#    print 自带一个换行

