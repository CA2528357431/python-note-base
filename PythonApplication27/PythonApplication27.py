#return

def fx1(x,y,z):
  
   r=x**6+y+z**3
   s=100*x
#把结果导出
   return r,s
#return会终结函数


fx1(3,2,4)
result=fx1(2,3,4)  # 接受fx1结果
print(result[1])
print(result[1])
# 若接受多个结果则变为数组