match=["Jrip","Jrip:","Ridor","J48","SC","NB","IBK","SimpleCart(SC)"]
classifier=["Jrip","Ridor","J48","SC","NB","IBK"]
attribute=["TP Rate","FP Rate","Precision","Recall","F-Measure","ROC Area", "Class"]
vars=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
import os
files = os.listdir('data')
for file in files:
	try:
		print("using file:",file)
		fo=open("data/"+file,"r")
		fw=open("results/"+file+".csv","w")
		fw.write('"","","","","",'+file+'\n\n\n\n')
		import re
		data={}
		current=''
		for i in fo:
			j=i.split("\n")[0]
			if j in match:
				current=j
				data[j]=''
			else:
				if(current!=""):
					data[current]+=i
		for key in data:
			fw.write('"","","","","",'+key+'\n')
			dt=data[key]
			a=dt.split(" <-- classified as\n")[1]
			a=a.split("\n")
			data0=[]
			for ai in a:
				if(ai !=""):
					data0.append(re.split("\s*",ai.split(" |")[0]))
			data1=[]
			b=dt.split("ROC Area  Class\n")[1].split("Weighted Avg")[0]
			b=b.split("\n")
			for ai in b:
				if(ai !=""):
					data1.append(re.split("\s*",ai))
			fw.write(",".join(vars[0:len(data0)]+attribute)+"\n")
			for i in range(len(data0)):
				temp=data0[i][1:]+data1[i][1:]
				fw.write(",".join(temp)+"\n")
			fw.write("\n\n\n")
		fw.close()
		print(file," done")
	except:
		print(file," faild to parse may be contain some errors in structure ")
	print("---------------------------------------------")	