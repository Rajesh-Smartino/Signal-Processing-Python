file_path = "/Users/rajeshr/Desktop/data_records.txt"

with open(file_path) as file:
    content = file.read()
def split_records(string):
    l = string.split('\t')
    l = l[-1].split()
    return l
   
x = [split_records(c) for c in content.split('\n')]
x = [i for i in x if i]

locations = [i[3] for i in x]

unique_locations = set(locations)
location_counts = [locations.count(l) for l in unique_locations]

#print(unique_locations)
location_counts

departments = [i[-1] for i in x]

unique_departments = set(departments)
departments_counts = [departments.count(l) for l in unique_departments]

#												 	#
#	TOTAL NUMBER OF EMPLOYEES IN EACH DEPARTMENT 	#
#												 	#
print('\n 1) TOTAL NUMBER OF EMPLOYEES IN EACH DEPARTMENT\n')
print(unique_departments)
print(departments_counts)
print('\n')

departments = [i[-1] for i in x]
places = [i[3] for i in x]

merged = ["{}_{}".format(departments[i], places[i]) for i in range(len(x))]

unique_merged = list(set(merged))
merged_counts = [merged.count(l) for l in unique_merged]

#												 				#
#	TOTAL NUMBER OF EMPLOYEES IN DEPARTMENT WISE IN EACH CITY	#
#												 				#
print('\n 2) TOTAL NUMBER OF EMPLOYEES IN DEPARTMENT WISE IN EACH CITY\n')
print(unique_merged)
print(merged_counts)
print('\n')


#												 				#
#			EMPLOYEES NAME AND LOCATION IN CSV FILE				#
#												 				#
import pandas as pd #Using for making csv

df = pd.DataFrame(x, columns=['FirstName', 'LastName', 'Date', 'Place', 'Department'])
df[['FirstName', 'LastName', 'Place']].to_csv('/Users/rajeshr/Desktop/output.csv')

print('CSV file created')