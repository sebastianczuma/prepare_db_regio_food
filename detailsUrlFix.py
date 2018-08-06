#coding: utf-8

import json
from pprint import pprint

with open('details.json') as data_file:
	data_item = json.load(data_file)

province_list = ['dolnoslaskie','kujawsko-pomorskie','lodzkie','lubelskie','lubuskie','malopolskie','mazowieckie','opolskie','podkarpackie','podlaskie','pomorskie','slaskie','swietokrzyskie','warminsko-mazurskie','wielkopolskie','zachodniopomorskie']

food_list = ['produkty_mleczne','produkty_miesne', 'produkty_rybolowstwa', 'warzywa_i_owoce', 'wyroby_piekarnicze_i_cukiernicze', 'oleje_i_tluszcze', 'miody', 'gotowe_dania_i_potrawy', 'napoje', 'inne_produkty']

THESIZE = len(food_list)

province_size = len(province_list)

print('{"'  + '": {\n"' + province_list[0] + '": {\n')

for k in range(province_size):
	if(k>0):	
		print('"'+province_list[k] + '": {\n')
	for j in range(THESIZE):
		size = len(data_item[province_list[k]][food_list[j]])

		if(j>0):
			print(',"' + food_list[j] + '": \n')
		else:
			print('"' + food_list[j] + '":\n')

		if(size==0):
			print('{')

		for i in range(size):

			if(i>0):
				print(',\"' + data_item[province_list[k]][food_list[j]][i]['url'] + '\":{')
			else:
				print('{\"'+data_item[province_list[k]][food_list[j]][i]['url']+'\":{')

			print('\"url\":')
			print('\"' + data_item[province_list[k]][food_list[j]][i]['url'] + '\",')

			print('\"name\":')
			print('\"' + data_item[province_list[k]][food_list[j]][i]['name'] + '\",')

			if('look' in data_item[province_list[k]][food_list[j]][i]):
				print('\"look\":')
				print('\"' + data_item[province_list[k]][food_list[j]][i]['look'] + '\",')

			if('shape' in data_item[province_list[k]][food_list[j]][i]):
				print('\"shape\":')
				print('\"' + data_item[province_list[k]][food_list[j]][i]['shape'] + '\",')
			
			if('size' in data_item[province_list[k]][food_list[j]][i]):		
				print('\"size\":')
				print('\"' + data_item[province_list[k]][food_list[j]][i]['size'] + '\",')

			if('color' in data_item[province_list[k]][food_list[j]][i]):
				print('\"color\":')
				print('\"' + data_item[province_list[k]][food_list[j]][i]['color'] + '\",')

			if('consistency' in data_item[province_list[k]][food_list[j]][i]):
				print('\"consistency\":')
				print('\"' + data_item[province_list[k]][food_list[j]][i]['consistency'] + '\",')

			if('taste' in data_item[province_list[k]][food_list[j]][i]):
				print('\"taste\":')
				print('\"' + data_item[province_list[k]][food_list[j]][i]['taste'] + '\",')

			if('other' in data_item[province_list[k]][food_list[j]][i]):
				print('\"other\":')
				print('\"' + data_item[province_list[k]][food_list[j]][i]['other'] + '\",')

			if('tradition' in data_item[province_list[k]][food_list[j]][i]):
				print('\"tradition\":')
				print('\"' + data_item[province_list[k]][food_list[j]][i]['tradition'] + '\",')

			print('\"category\":')
			print('\"' + food_list[j] + '\"')

			
			print('}')
		print('}')
	print('},')




