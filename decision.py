import numpy as np

f = open("mod_cleve.txt","r")
l = f.readlines()
f.close()

'''
inp=[Age; sex; chest pain type (angina, abnang, notang, asympt)
  Trestbps (resting blood pres); cholesteral; fasting blood sugar < 120
  (true or false); resting ecg (norm, abn, hyper); max heart rate; 
  exercise induced angina (true or false); oldpeak; slope (up, flat, down)
  number of vessels colored (???); thal (norm, fixed, rever). Finally, the
  class is either healthy (buff) or with heart-disease (sick)]
'''
names=['Age', 'sex', 'chest_pain','blood_pressure','cholesteral','blood_sugar','ecg','heart_rate','eia','oldpeak','slope',
  'num_color','thal']
#print l
data=[]
#print l
for i in l:
	line=i[:-1].split()
	data.append(line)

data=data[:-1]
#print data

x=[]

'''Old peak-
		<1.5	 : low risk 	1
		1.5-2.55 : risk			2
		>2.5  	 : terrible		3 
	
	Max heart rate-
		<111 	 : low			1
		<111-152 : medium		2
		>152 	 :high			3

	Cholestrol-
		<187		:low		1
		188-250		:medium		2
		250-281		:high		3
		>281		:very high	4

	Age-
		<33			:young		1
		33-45		:middle age	2
		45-52		:old		3
		>52			:very old	4

	Blood pressure-
		<127		:low		1
		127-142		:medium		2
		142-154		:high		3
		>154		:very high	4
'''


for line in data:
		temp=line[:]
		#print line
		#print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#age
		if float(line[0])<33:
			temp[0]=1
		elif float(line[0])<45 and float(line[0])>33:
			temp[0]=2
		elif float(line[0])<52 and float(line[0])>45:
			temp[0]=3
		else:
			temp[0]=4


		#blood pressure
		if float(line[3])<127:
			temp[3]=1
		elif float(line[3])<142 and float(line[3])>127:
			temp[3]=2
		elif float(line[3])<154 and float(line[3])>142:
			temp[3]=3
		else:
			temp[3]=4

		#cholestrol
		if float(line[4])<187:
			temp[4]=1
		elif float(line[4])<250 and float(line[4])>187:
			temp[4]=2
		elif float(line[4])<281 and float(line[4])>250:
			temp[4]=3
		else:
			temp[4]=4

		#heart rate
		if float(line[7])<111:
			temp[7]=1
		elif float(line[7])<152 and float(line[7])>111:
			temp[7]=2
		else:
			temp[7]=3

		#old peak
		if float(line[9])<1.5:
			temp[9]=1
		elif float(line[9])<2.55 and float(line[9])>1.5:
			temp[9]=2
		else:
			temp[9]=3	

		x.append(temp)	 

y=[k[-1] for k in x]
x=[k[:-1] for k in x]
#print x

x_vals=[]
for arr in x:
	data={}
	for i in range(len(names)):
		data[names[i]]=arr[i]
	x_vals.append(data)

print x_vals

	
