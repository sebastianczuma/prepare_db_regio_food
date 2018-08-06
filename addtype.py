#coding: utf-8

import json
from pprint import pprint

with open('all.json') as data_file:
	data_item = json.load(data_file)

province_list = ['dolnoslaskie','kujawsko-pomorskie','lodzkie','lubelskie','lubuskie','malopolskie','mazowieckie','opolskie','podkarpackie','podlaskie','pomorskie','slaskie','swietokrzyskie','warminsko-mazurskie','wielkopolskie','zachodniopomorskie']

food_list = ['produkty_mleczne','produkty_miesne', 'produkty_rybolowstwa', 'warzywa_i_owoce', 'wyroby_piekarnicze_i_cukiernicze', 'oleje_i_tluszcze', 'miody', 'gotowe_dania_i_potrawy', 'napoje', 'inne_produkty']

THESIZE = len(food_list)

province_size = len(province_list)

print('{"' + 'wojewodztwa' + '": {\n"' + province_list[0] + '": {\n')

for k in range(province_size):
	if(k>0):	
		print('"'+province_list[k] + '": {\n')
	for j in range(THESIZE):
		size = len(data_item['wojewodztwa'][province_list[k]][food_list[j]])

		if(j>0):
			print(',"' + food_list[j] + '": [\n')
		else:
			print('"' + food_list[j] + '": [\n')

		for i in range(size):

			if(i>0):
				print(',')
			print('{')

			print('\"url\":')
			print('\"' + data_item['wojewodztwa'][province_list[k]][food_list[j]][i]['url'] + '\",')

			print('\"name\":')
			print('\"' + data_item['wojewodztwa'][province_list[k]][food_list[j]][i]['name'] + '\",')

			print('\"category\":')
			print('\"' + food_list[j] + '\",')

			
			print('}')
		print(']')
	print('},')




