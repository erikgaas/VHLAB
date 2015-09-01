

#TODO FUNCTIONS

#get_hearts: Retrieve all of the heart objects WORKS
#is_functional
#is_perfusion_fixed
#is_anatomical_plates
#is_prefixed
#is_comp_imaging
#is_cardiac_mri
#is_cor_venous
#is_cor_arterial
#is_cor_both
#is_blood_vol
#get_all_pages
#get_main_links WORKS

import urllib.request as urlr
from bs4 import BeautifulSoup as bs



class Heart():
	def __init__(self, name):
		self.name = name
		self.functional = False
		self.perfusion = False
		self.anatomical_plate = False
		self.prefixed = False
		self.comp_imaging = False
		self.cardiac_mri = False
		self.cor_venous = False
		self.cor_arterial = False
		self.cor_both = False
		self.blood_vol = False


	def is_fuctional(self, data): #If title is Visible Heart (functional)
		if self.functional:
			return
		else:
			for row in data:
				for field in row:
					if "Visible Heart (functional)" in field and is_heart_in_list(self.name, row[field]):
						return True
			
	def is_perfusion_fixed(self, data): #If title is Perfusion Fixed (endoscope)
		if self.perfusion:
			return
		else:
			for row in data:
				for field in row:
					if "Perfusion Fixed (endoscope)" in field and is_heart_in_list(self.name, row[field]):
						return True
	def is_anatomical_plates(self, data): #If title is Anatomical Plates
		if self.anatomical_plate:
			return
		else:
			for row in data:
				for field in row:
					if "Anatomical Plates" in field and is_heart_in_list(self.name, row[field]):
						return True
	def is_prefixed(self, data): #If title is Pre-fixed Anatomical Plates
		if self.prefixed:
			return
		else:
			for row in data:
				for field in row:
					if "Perfusion Fixed (endoscope)" in field and is_heart_in_list(self.name, row[field]):
						return True
	def is_comp_imaging(self, data): #If title is Comparative Imaging
		if self.comp_imaging:
			return
		else:
			for row in data:
				for field in row:
					if "Comparative Imaging" in field and is_heart_in_list(self.name, row[field]):
						return True
	def is_cardiac_mri(self, data): #Dang last guy doesnt work
		if self.cardiac_mri:
			return
		else:
			for row in data:
				for field in row:
					if "Cardiac MRI" in field and is_heart_in_list(self.name, row[field]):
						return True
	def is_cor_venous(self, data): #If title is Venous
		if self.cor_venous:
			return
		else:
			for row in data:
				for field in row:
					if "Venous" in field and is_heart_in_list(self.name, row[field]):
						return True
	def is_cor_arterial(self, data): #If title is Arterial
		if self.cor_arterial:
			return
		else:
			for row in data:
				for field in row:
					if "Arterial" in field and is_heart_in_list(self.name, row[field]):
						return True
	def is_cor_both(self, data): #If title is combined
		if self.cor_both:
			return
		else:
			for row in data:
				for field in row:
					if "combined" in field and is_heart_in_list(self.name, row[field]):
						return True
	def is_blood_vol(self, data): #If title is Hypertrophic, Dilated Cardiomyopathy, Normal, or Pediatric
		if self.blood_vol:
			return
		else:
			for row in data:
				for field in row:
					if ("Hypertrophic" in field or "Dilated Cardiomyopathy" in field or "Normal" in field or "Pediatric" in field) and is_heart_in_list(self.name, row[field]):
						return True




# hearts = get_hearts() #List of hearts (Pass in the webpage?)

# info_pages = get_all_pages() #BeautifulSoup objects?

# for page in info_pages:
# 	for heart in hearts:





def get_hearts():
	URL = "http://www.vhlab.umn.edu/atlas/histories/database.shtml"
	#Urllib -> Beautiful Soup to get names and junk.
	data_page = urlr.urlopen(URL)
	soup = bs(data_page)
	#Get third table
	third_table = soup.find_all('table')[2]
	#Get third td from that
	third_td = third_table.find_all('td')[2]
	#Second table from that
	second_table = third_td.find_all('table')[1]
	#Get second table?
	second_table2 = second_table.find_all('table')[1]
	#Get all of the trs
	all_trs = second_table2.find_all('tr')[1:]
	#Filter out the number
	return [Heart("Heart" + tr.find('td').getText()) for tr in all_trs]


def get_all_pages():
	ROOT_URL = "http://www.vhlab.umn.edu/atlas/index.shtml"
	main_links = get_main_links(ROOT_URL)
	sub_pages = []
	for main_link in main_links:
		sub_pages = sub_pages + get_sub_pages(main_link)
	return sub_pages
		

def get_sub_pages(url):
	BASE_URL = "http://www.vhlab.umn.edu"
	page = urlr.urlopen(url)
	soup = bs(page)	
	third_td = soup.find('td', attrs={'class':'headbkgimage'})
	first_table = third_td.find('table')
	temp_trs = first_table.find_all('tr')
	if len(temp_trs) == 1:
		#Comp imaging
		return [url]
	else:
		#not comp imaging
		second_tr = temp_trs[1]
		all_tds = second_tr.find_all('td')[:-1]
		return [BASE_URL + td.find('a')['href'] for td in all_tds]



def get_main_links(url):
	BASE_URL = "http://www.vhlab.umn.edu"
	page = urlr.urlopen(url)
	#use BS to retieve the links of interest
	soup = bs(page)
	#Find third table
	third_table = soup.find_all('table')[2]
	#Get first td
	first_td = third_table.find_all('td')[0]
	#Get fourth through fifteenth a tags from there
	a_tags = first_td.find_all('a')[3:15]
	#Process them to extract the links
	return [BASE_URL + tag['href'] for tag in a_tags]

def get_sub_page_info(url):
	extra = ""
	if "cardiac-mri" in url:
		extra = "Cardiac MRI"
	elif "comparative-imaging" in url:
		extra = "Comparative Imaging"


	page = urlr.urlopen(url)
	soup = bs(page)
	#Get form info
	forms = soup.find_all('form')
	sub_dict = {}
	for form in forms[1:]:
		par_prev_sibling = form.parent.parent.previous_sibling.previous_sibling
		maybe_img = par_prev_sibling.find('img')
		if maybe_img != None:
			title = maybe_img['alt']
		else:
			title = par_prev_sibling.find('td').getText()
		sub_dict[title] = [extra + option.getText() for option in form.find_all('option')[1:]]
	return sub_dict

def is_heart_in_list(name, ls):
	for item in ls:
		if name in item:
			return True
	return False



hearts = get_hearts()
data = []

info_pages = get_all_pages()
for link in info_pages:
	data.append(get_sub_page_info(link))

for heart in hearts:
	heart.is_fuctional(data)
	heart.is_perfusion_fixed(data)
	heart.is_anatomical_plates(data)
	heart.is_prefixed(data)
	heart.is_comp_imaging(data)
	heart.is_cardiac_mri(data)
	heart.is_cor_venous(data)
	heart.is_cor_arterial(data)
	heart.is_cor_both(data)
	heart.is_blood_vol(data)

for heart in hearts:
	print(heart.is_prefixed)