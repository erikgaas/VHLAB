

#TODO FUNCTIONS

#get_hearts: Retrieve all of the heart objects
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
#get_main_links



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


	def is_fuctional(self, page):
		if self.functional:
			return
		else:
			return
	def is_perfusion_fixed(self, page):
		if self.perfusion:
			return
		else:
			return
	def is_anatomical_plates(self, page):
		if self.anatomical_plate:
			return
		else:
			return
	def is_prefixed(self, page):
		if self.prefixed:
			return
		else:
			return
	def is_comp_imaging(self, page):
		if self.comp_imaging:
			return
		else:
			return
	def is_cardiac_mri(self, page):
		if self.cardiac_mri:
			return
		else:
			return
	def is_cor_venous(self, page):
		if self.cor_venous:
			return
		else:
			return
	def is_cor_arterial(self, page):
		if self.cor_arterial:
			return
		else:
			return
	def is_cor_both(self, page):
		if self.cor_both:
			return
		else:
			return
	def is_blood_vol(self, page):
		if self.blood_vol:
			return
		else:
			return




hearts = get_hearts() #List of hearts (Pass in the webpage?)

info_pages = get_all_pages() #BeautifulSoup objects?

for page in info_pages:
	for heart in hearts:







def get_hearts():
	URL = "http://www.vhlab.umn.edu/atlas/histories/database.shtml"
	#Urllib -> Beautiful Soup to get names and junk.

def get_all_pages():
	ROOT_URL = "http://www.vhlab.umn.edu/atlas/index.shtml"
	main_links = get_main_links(ROOT_URL)
	for main_link in main_links:
		


def get_main_links(url):
	#use BS to retieve the links of interest

