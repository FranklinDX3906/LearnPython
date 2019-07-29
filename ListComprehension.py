#coding:UTF-8
#列表生成式

l = [x**2 for x in range(1,10,2)]#隔两个生成x的平方
print(l)

L = ['HeLlO']
print([s.lower() for s in L])#变成小写输出