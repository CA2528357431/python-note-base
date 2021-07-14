#for 升级

a=[1,2,3,4,5,6]
for x in a:
    print(x)
    if x>3:
        break
else:
    print("finish")


for x in a:
    print(x)
else:
    print("finish")

##只有完整执行全部内容，无break，才执行else
