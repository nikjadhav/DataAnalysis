'''finding running median'''
import math
def run_med(list_):
	#print (list_)
	if(len(list_)==1):
		return (list_[0])
	elif(len(list_)%2==0):
		m=int(math.ceil(float((len(list_)))/float(2)))
		#print(m)
	        res=(float(list_[m])+float(list_[m-1]))/float(2)	
		return(res)
	else:
		m=int(math.floor(float((len(list_)))/float(2)))
		return list_[m]
n=int(input())
arr=[]
for i in range(0,n):
	n=int(input())
	arr.append(n)
	arr.sort()
	res=run_med(arr)
	print(res)
	
