def FX1():
    print("xxx")
def FX2():
    print("yyy")
    FX1()
    print("zzz")
FX2()


#执行路径   FX2.1 < FX2.2/FX1 < FX3 