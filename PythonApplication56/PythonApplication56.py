# 递归

def n(a):
    if a==1:
        re=1
    else:
        re=a*n(a-1)
    return re
h=n(4)
print(h)