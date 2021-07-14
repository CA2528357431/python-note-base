#石头剪刀布

print("1=shitou 2=jiandao 3=bu")
x=int(input("x="))
y=int(input("y="))

if y-x==1 or y-x==-2:
    print("x win")
elif x==y:
    print("no")
else:
    print("y win")

# 注意计算结果之规律，而非无脑分类讨论