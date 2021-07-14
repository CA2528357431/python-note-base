# eval函数


#计算
x="13//6+17%5-3*3"
print(eval(x))

#字符串重复/加
x="'a'*10+'@'*5"
print(eval(x))

#字符串转化为list/dict/tuple
x="[1,0.5,'a']"
print(type(eval(x)))
x="(1,0.5,'a')"
print(type(eval(x)))
x="{'name':'ca','iq':15}"
print(type(eval(x)))
