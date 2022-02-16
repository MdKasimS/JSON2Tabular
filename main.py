import sys
import json

fp=open("sample.json")
rawData=fp.readlines()
fp.close()

#print(len(rawData))
data=[]

for i in rawData:
	if ":" in i:
		data.append(i)
				

jsonData=[]
fNameIndices=[]
fNames=[]


for i in range(0,len(data)):
	if ':' in data[i]:
		if ',' in data[i] and "[" not in data[i]:
			data[i]=data[i].strip()
			data[i]=data[i].replace(',','')
			data[i]="{"+data[i]+"}"
			#print('yes',data[i],end='\n',sep=' - ')	
			jsonData.append(json.loads(data[i]))
			#print(i,".",data[i])

		elif "[" in data[i] or  "{" in data[i]:
			data[i]=data[i].strip()
			data[i]=data[i].replace(',','')
			#print('no',data[i],end='\n',sep=' - ')
			fNameIndices.append(i)
			fNames.append(data[i])

		else:
			data[i]=data[i].strip()
			data[i]=data[i].replace(',','')
			data[i]="{"+data[i]+"}"
			#print("Special",data[i],end="\n",sep=" - ")
			jsonData.append(json.loads(data[i]))
			#print(i,".",data[i])


for i in range(0,len(data)):
	print(data[i])