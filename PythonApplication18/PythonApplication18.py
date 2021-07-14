#人机石头剪刀布

import random
#引入随机工具包



print("1=shitou 2=jiandao 3=bu")
x=int(input("x="))
y=random.randint(1,3) # 随机
print(x,y)
if y-x==1 or y-x==-2:
    print("x win")
elif x==y:
    print("no")
else:
    print("y win")

