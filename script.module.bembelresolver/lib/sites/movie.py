import re

import help_fns

class Movie:
	
	def __init__(self, row):
		columns = help_fns.extractText(row, '<td', '</td>')
		
		self.fillPictureIDByRow(row)
		self.fillURLAndNameByColumn(columns[0])
		self.fillYearByColumn(columns[2])
		self.fillPointsByColumn(columns[4])
		self.fillLanguageByColumn(columns[5])
		
	def fillPictureIDByRow(self, row):
		match = re.compile('<tr id="(coverPreview\d{0,7})">').findall(row)
		self.pictureID = match[0]
	
	def fillURLAndNameByColumn(self, column):
		match = re.compile('<a href="(.*)">(.*)<\/a>').findall(column)
		self.url = match[0][0]
		self.name = match[0][1].strip().replace("\t", "")
		
	def fillYearByColumn(self, column):
		match = re.compile('(\d{4})<\/div>').findall(column)
		if match:
			self.year = match[0]
		else:
			self.year = ""
		
	def fillPointsByColumn(self, column):
		match = re.compile('<strong>(.*)<\/strong>').findall(column)
		self.points = match[0][0]
		
	def fillLanguageByColumn(self, column):
		match = re.compile('src="http:\/\/img\.movie2k\.to\/img\/(.*)"').findall(column)
		
		self.language = ""
		if match:
			if match[0] == "us_ger_small.png":
				self.language = "de"
			if match[0] == "us_flag_small.png":
				self.language = "en"
	
	def display(self):
		res = ""
		if self.year:
			res = self.year
		if self.language:
			if res:
				res = res + " "
			res = res + self.language
		res = self.name + " (" + res + ")"
		return res