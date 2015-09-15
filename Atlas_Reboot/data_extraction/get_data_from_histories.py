import re


#Delete all "Non known" occurances. Also "-"
#Delete "History of" in all forms" on second thought dont.
#Deal with all of the initialisms


#Split based off of commas.
#Replace all lone initialisms with proper name.
#trim off all spaces, commas, or whatever.
#For each element look for the term fllowed by a number + or range of numbers followed by years or yrs.
import pandas as pd

data = pd.read_csv('original_hist.csv')

cardiac_diseases = data['Cardiac Medical History'].tolist()
systemic_diseases = data['Systemic Medical History'].tolist()

def convert_element(element):
	split_element = [i.strip(' .').lower() for i in element.split(',') if i != '-' and i.strip(' .').lower() != 'none known']
	return split_element


cardiac_result = sorted(set(sum([convert_element(disease) for disease in cardiac_diseases], [])))
systemic_result = sorted(set(sum([convert_element(disease) for disease in systemic_diseases], [])))

with open('results.txt', 'w') as results_file:
	results_file.write('CARDIAC RESULTS\n')
	for element in cardiac_result:
		results_file.write(element + '\n')
	results_file.write('\n\nSYSTEMIC RESULTS\n')
	for element in systemic_result:
		results_file.write(element + '\n')

		
#need regular expression to deal with severity and years

