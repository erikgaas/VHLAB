
import pandas as pd
from bs4 import BeautifulSoup as bs

data = pd.read_csv('heart_results.csv')
data['Heart Number'] = data['Heart Number'].apply(lambda x: '{0:0>4}'.format(x))

result = data.to_html(na_rep='', index=False)

soup = bs(result)

table = soup.find('table')
table['border'] = '1'
table['cellpadding'] = '5'
table['cellspacing'] = '0'
table['bgcolor'] = '#FFFFFF'

header = soup.find('thead')
header.find('tr')['valign'] = 'top'
header.find('tr')['style'] = ''

for th in header.find_all('th'):
	th['style'] = 'text-align: center;'
	temp_text = th.string
	th.string = ''
	th.append(bs('<strong>' + temp_text + '</strong>').find('strong'))


for td in soup.find_all('td'):
	td['align'] = 'center'
	if td.getText() == "Yes":
		td['bgcolor'] = '#00FF00'
	


with open('heart_results.html', 'w') as f:
	f.write(str(soup))