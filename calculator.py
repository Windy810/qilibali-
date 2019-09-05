import math

str = input("输入数据，并以空格分隔:")
#derta=input("输入仪器精确度:")
derta=0.004
num=[]
num1=str.split(" ")
i=0
while i <=len(num1)+4:
	num.append(float(num1.pop()))
	i+=1

def average(list):
	sum=0
	for i in list:
		sum+=i
	pjz=("%.20f"%(sum/float(len(list))))
	return float(pjz)

def adu(list):
	sum=0
	for i in list:
		sum+=math.pow(i-average(list),2)
	k=len(list)
	k=k*(k-1)
	da=math.sqrt(sum/k)
	return da

def bdu(list,y):
	db=float(y)/math.sqrt(3)
	return db

def zdu(a,b):
	d=math.hypot(a,b)
	return d

def s(list,a):
	sx=math.sqrt(len(list))*a
	return sx


print("平均值为：%.20f"%average(num),end='\n')
print("标准差为：%.8f"%s(num,adu(num)),end='\n')
print("A类不确定度为：%.8f"%adu(num),end='\n')
print("B类不确定度为：%.8f"%bdu(num,derta),end='\n')
print("总不确定度为：%.8f"%zdu(adu(num),bdu(num,derta)),end='\n')



#平方和开方：math.hypot(a,b)
