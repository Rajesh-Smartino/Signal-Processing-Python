import pandas as pd

with open('/Users/rajeshr/Desktop/result.txt') as file:
    data = file.read()

input_list = [int(i) for i in data.split('\n') if i.isnumeric()]

dictionary = {}
for i in input_list:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
        
for key in dictionary.keys():
    dictionary[key] = dictionary[key] * key
    
outfile = pd.DataFrame.from_dict(dictionary, orient='index')
outfile.columns = ['count sum']

outfile.to_csv('outfile.csv')