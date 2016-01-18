import pandas as pd
import numpy as np

heart_table = pd.read_html('hearttable.html')[0]
heart_table.columns = ['Heart Number', 'Sex', 'Age', 'BMI', 'Body Weight (kg)', 'Body Height (cm)', 'Cardiac Medical History', 'Systemic Medical History']
items = pd.read_csv('Item.csv')
tags = pd.read_csv('tag.csv')

table_hearts = heart_table['Heart Number']
item_hearts = items['item_name']
tag_hearts = tags['tag_text']

table_hearts = ['Heart' + "%04d" % i for i in list(table_hearts)]
all_things = set(table_hearts + list(item_hearts) + list(table_hearts))
all_things = [i for i in all_things if "Heart" in i]

completed_hearts = []
for heart in all_things:
	if 'Heart' in heart:
		completed_hearts.append(heart[0:9])

completed_hearts = sorted(set(completed_hearts))[1:]

not_in_table = [i for i in completed_hearts if i not in table_hearts]


#Go through populated hearts
#If there is a corresponding heart in 

insert_string = "INSERT INTO heart VALUES ('{}','{}',{},{},{},{},'{}','{}','{}')"

import sqlite3

conn = sqlite3.connect('vhlab.db')
c = conn.cursor()

heart_table['Comment'] = '-'
heart_table = heart_table.replace('-', np.nan)

heart_table['Heart Number'] = table_hearts

#heart_table[['BMI', 'Body Weight (kg)', 'Body Height (cm)']].astype(float)

db_hearts = [tuple(i[1]) for i in heart_table.iterrows()]
db_rest_hearts = [tuple([i] + 8*[np.nan]) for i in not_in_table]
db_all_hearts = db_hearts + db_rest_hearts

c.execute('DELETE FROM heart')
c.executemany('INSERT INTO heart VALUES (?,?,?,?,?,?,?,?,?)', db_all_hearts)
conn.commit()
c.close()