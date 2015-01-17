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
x = []
y = []
for line in l:
	k = line[:-1].split()
	y_inp = k[-2]
	for i in len(y_inp):
		if(y_inp[i] == 'buff'):
			y[i] = -1
		else:
			y[i] = 1
	x[i] = k[:-2]


