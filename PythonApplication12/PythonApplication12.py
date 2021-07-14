#逻辑运算

x=int(input())
y=int(input())

if x>0 and y>0:
    print("good")


if not x>0:
    print("rrr")

if x>0 or y>0:
    print("go")




z=int (input())
if z%400==0 or z%100!=0 and z%4==0:
    print("good")
