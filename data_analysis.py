import random
import csv
from sys import argv
def marksgen():
	marks=[]
	marks=random.sample(range(35,100),5)
	return (marks)
def gendergen():
	n=random.randint(1,100)
	if(n%2==0):
		return 'M'
	else:
		return 'F'
def avg_cal(sub_marks):
	avg=float(sum(sub_marks))/float(len(sub_marks))
	return (avg)
def file_creator(stud_data,file1):
	csv=open(file1,"w")
	row="student_id"+","+"Gender"+","+"english"+","+"maths"+","+"science"+","+"history"+","+"Geography"+","+"average"+"\n"
	csv.write(row)
	for i in range(0,len(stud_data)):
		marks=""
		row=""
		marks=",".join(str(x) for x in stud_data[i][2])
		row=stud_data[i][0]+","+stud_data[i][1]+","+marks+","+str(stud_data[i][3])+"\n"
		#print(row)
		csv.write(row)
def overall_topper(stud_data):
	top=0
	res=[]
	maxx=stud_data[0][3]
	for i in range(1,len(stud_data)):
		if(stud_data[i][3]>maxx):
			top=i
			maxx=stud_data[i][3]
	for i in range(0,len(stud_data)):
		if(stud_data[i][3]==stud_data[top][3]):
			res.append(stud_data[i][0])
	return (res)		
def gender_topper(stud_data,ch):
	i=0
	res=[]
	while(stud_data[i][1]!=ch):
		i=i+1
	top=i
	maxx=stud_data[i][3]
	for i in range(i,len(stud_data)):
		if(stud_data[i][3]>maxx and stud_data[i][1]==ch):
			top=i
			maxx=stud_data[i][3]
	for i in range(0,len(stud_data)):
		if(stud_data[i][3]==stud_data[top][3] and stud_data[i][1]==ch):
			res.append(stud_data[i][0])
	return(res)
def sub_topper(stud_data,j):
        res=[]
        e=stud_data[0][2][j]
        for i in range(0,len(stud_data)):
                if(stud_data[i][2][j]>e):
                        e=stud_data[i][2][j]
        #print (e)
        for i in range(0,len(stud_data)):
                if(stud_data[i][2][j]==e):
                        res.append(stud_data[i][0])
        return res
def list_to_str(lst):
	s=",".join(str(x) for x in lst)
	return s
		
def main(n,file1,file2):
	subjects=["ENGLISH","MATHS","SCIENCE","HISTORY","GEOGRAPHY"]
	temp=[]
	stud_data=[]
	sub_marks=[]
	n=int(n)
	i=0
	for i in range(0,n):
		temp=[]
		temp.append("Stud"+str(i))
		g=gendergen()
		temp.append(g)
		sub_marks=marksgen()
		temp.append(sub_marks)
		avg=avg_cal(sub_marks)
		temp.append(avg)
		stud_data.append(temp)	
	file_creator(stud_data,file1)
	f=open(file2,"w+")
	temp=overall_topper(stud_data)
	s=",".join(str(x) for x in temp)
	f.write("overall topper id:"+s+"\n")
	temp=gender_topper(stud_data,'M')
	s=",".join(str(x) for x in temp)
	f.write("male topper id:"+s+"\n")
        temp=gender_topper(stud_data,'F')
	s=",".join(str(x) for x in temp)
	f.write("female topper id:"+s+"\n")
	for i in range(0,5):
		res=sub_topper(stud_data,i)
		s=list_to_str(res)
		f.write(subjects[i]+"topper id:"+" "+s+"\n")
script,n,file1,file2=argv
main(n,file1,file2)


	
	
