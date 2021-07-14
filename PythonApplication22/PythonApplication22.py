#continue

#x之下计算3倍数

z=0
y=1
x=int(input("x="))
while y<x:
    
    y=y+1
    if y%3!=0:
        continue
    z=z+1

print(z)