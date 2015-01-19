from preprocessing import *
from git_tree import *

names=['Age', 'sex', 'chest_pain','blood_pressure','cholesteral','blood_sugar','ecg','heart_rate','eia','oldpeak','slope',
	  'num_color','thal','class']


data = get_input_data()
training = data[:240]
test = data[240:]
#vals = [record['class'] for record in data]
#print(vals)
final_tree = makeTree(training,names,'class',0)
print(final_tree)

