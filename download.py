#coding: utf-8
import urllib.request
from bs4 import BeautifulSoup
import re

import json
from pprint import pprint


urlBase = 'https://www.gov.pl/rolnictwo/'

with open('dane.json') as data_file:
	data_item = json.load(data_file)

with open('wojewodztwa.json') as data_file2:
	data_item2 = json.load(data_file2)

province_list = ['dolnoslaskie','kujawsko-pomorskie','lodzkie','lubelskie','lubuskie','malopolskie','mazowieckie','opolskie','podkarpackie','podlaskie','pomorskie','slaskie','swietokrzyskie','warminsko-mazurskie','wielkopolskie','zachodniopomorskie']

food_list = ['produkty_mleczne','produkty_miesne', 'produkty_rybolostwa', 'warzywa_i_owoce', 'wyroby_piekarnicze_i_cukiernicze', 'oleje_i_tluszcze', 'miody', 'gotowe_dania_i_potrawy', 'napoje', 'inne_produkty']

THESIZE = len(food_list)

province = province_list[15]

print('{"' + 'wojewodztwa' + '": {\n"' + province + '": {\n')

for j in range(THESIZE):
	size = len(data_item['wojewodztwa'][province][food_list[j]])

	if(j>0):
		print(',"' + food_list[j] + '": [\n')
	else:
		print('"' + food_list[j] + '": [\n')

	for i in range(size):
		urlEnd = data_item['wojewodztwa'][province][food_list[j]][i]['name']
		urlEnd = urlEnd.replace(' ', '-')
		#print(urlEnd)

		finalUrl = urlBase + urlEnd
		page = urllib.request.urlopen(finalUrl)
		soup = BeautifulSoup(page, 'html.parser')

		divBox = soup.find('div', {'class': 'paragraph article_section_content'})

		headers = divBox.find_all('h4')

		info = divBox.find_all('p')

		tags = []
		text = []

		for one in headers:
			tags.append(one.text.strip())

		for one in info:
			text.append(one.text.strip())

		url = province + '/' + food_list[j] + '/' + urlEnd

		if(i>0):
			print(',')
		print('{')

		print('\"url\":')
		print('\"' + url + '\",')

		print('\"name\":')
		print('\"' + data_item2['wojewodztwa'][province][food_list[j]][i]['name'] + '\",')

		for z in range(len(tags)):
			print('\"' + tags[z] + '\":')
			print('\"' + text[z] + '\"')
			if (z < len(tags)-1):
				print(',')
		
		print('}')
	print(']')
print('},')






