#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####
# Con este código vamos a descargar "unidades de descripción" completas 
####

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests, time, os, urllib, codecs, csv, sys
import reconex
import itertools

#########################################################################
#Ingresar la búsqueda

url = input('Pega la cadena de búsqueda: ')
ident = input('Ingresa el nombre del archivo csv: ')
num_pags = int(input('Cantidad de páginas a consultar: '))
rango = int(num_pags)-2
pag_rest = int(num_pags)+2

browser = webdriver.Chrome(executable_path=r'bin/chromedriver.exe')
browser.get(url)

#########################################################################
## Estos loops hay que convertirlos en una función... pero con un poco más de tiempo :D
## Listados que serán columnas en el csv

listado = []
tipolist = []
signalist = []
titulist = []

## Loops para recuperar los elementos

if num_pags == 1:
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	for em in soup("em"):
		soup.em.decompose()
	caja = soup.select('table.displayTable tbody')
	for box in caja:
		total = box.select('p.fecha')
		for columns in total:
			fecha = columns.get_text()
			listado.append(fecha)
		archi = box.select('p.tipo_archivo')
		for columns in archi:
			tip = columns.get_text()
			tipolist.append(tip)
		signa = box.select('p.signatura')
		for columns in signa:
			signat = columns.get_text()
			signalist.append(signat)
		titul = box.select('p.titulo a')
		for columns in titul:
			titu = columns.get_text()
			titulist.append(titu)
	
###si el número de págs está entre 2 y 5

elif num_pags in range(1,5):
# page 1
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	for em in soup("em"):
		soup.em.decompose()
	caja = soup.select('table.displayTable tbody')
	for box in caja:
		total = box.select('p.fecha')
		for columns in total:
			fecha = columns.get_text()
			listado.append(fecha)
		archi = box.select('p.tipo_archivo')
		for columns in archi:
			tip = columns.get_text()
			tipolist.append(tip)
		signa = box.select('p.signatura')
		for columns in signa:
			signat = columns.get_text()
			signalist.append(signat)
		titul = box.select('p.titulo a')
		for columns in titul:
			titu = columns.get_text()
			titulist.append(titu)
	#page 2
	ruti = browser.find_element_by_xpath('//*[@id="resultados"]/div[2]/a[{}]'.format(num_pags))
	ruti.click()
	time.sleep(1)
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	for em in soup("em"):
		soup.em.decompose()
	caja = soup.select('table.displayTable tbody')
	for box in caja:
		total = box.select('p.fecha')
		for columns in total:
			fecha = columns.get_text()
			listado.append(fecha)
		archi = box.select('p.tipo_archivo')
		for columns in archi:
			tip = columns.get_text()
			tipolist.append(tip)
		signa = box.select('p.signatura')
		for columns in signa:
			signat = columns.get_text()
			signalist.append(signat)
		titul = box.select('p.titulo a')
		for columns in titul:
			titu = columns.get_text()
			titulist.append(titu)

### si el número de págs es mayor a 5

elif num_pags > 5:
	# page 1
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	for em in soup("em"):
		soup.em.decompose()
	caja = soup.select('table.displayTable tbody')
	for box in caja:
		total = box.select('p.fecha')
		for columns in total:
			fecha = columns.get_text()
			listado.append(fecha)
		archi = box.select('p.tipo_archivo')
		for columns in archi:
			tip = columns.get_text()
			tipolist.append(tip)
		signa = box.select('p.signatura')
		for columns in signa:
			signat = columns.get_text()
			signalist.append(signat)
		titul = box.select('p.titulo a')
		for columns in titul:
			titu = columns.get_text()
			titulist.append(titu)
	# page 2
	time.sleep(1)
	ruti = browser.find_element_by_xpath('//*[@id="resultados"]/div[2]/a[5]')
	ruti.click()
	time.sleep(3)
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	for em in soup("em"):
		soup.em.decompose()
	caja = soup.select('table.displayTable tbody')
	for box in caja:
		total = box.select('p.fecha')
		for columns in total:
			fecha = columns.get_text()
			listado.append(fecha)
		archi = box.select('p.tipo_archivo')
		for columns in archi:
			tip = columns.get_text()
			tipolist.append(tip)
		signa = box.select('p.signatura')
		for columns in signa:
			signat = columns.get_text()
			signalist.append(signat)
		titul = box.select('p.titulo a')
		for columns in titul:
			titu = columns.get_text()
			titulist.append(titu)
	# resto de págs
	for i in range(rango):
		i = browser.find_element_by_xpath('//*[@id="resultados"]/div[2]/a[7]')
		i.click()
		time.sleep(5)
		soup = BeautifulSoup(browser.page_source, 'html.parser')
		for em in soup("em"):
			soup.em.decompose()
		caja = soup.select('table.displayTable tbody')
		for box in caja:
			total = box.select('p.fecha')
			for columns in total:
				fecha = columns.get_text()
				listado.append(fecha)
			archi = box.select('p.tipo_archivo')
			for columns in archi:
				tip = columns.get_text()
				tipolist.append(tip)
			signa = box.select('p.signatura')
			for columns in signa:
				signat = columns.get_text()
				signalist.append(signat)
			titul = box.select('p.titulo a')
			for columns in titul:
				titu = columns.get_text()
				titulist.append(titu)
else:
	print("ERROR")
	time.sleep(3)

# Finalizar el navegador
browser.quit()

###########################################################################
## Crea el directorio

if not os.path.exists('metadata_d/{}'.format(ident)):
	os.makedirs('metadata_d/{}'.format(ident))

#########################################################################
## Convertir el resultado en *.csv

with open('metadata_d/{}/{}.csv'.format(ident, ident), "w", newline="") as csv_file:
	fieldnames = ['Título','Fecha','Signatura','Archivo']
	writer_h = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer_h.writeheader()
	writer = csv.writer(csv_file)
	writer.writerows(zip(titulist,listado,signalist,tipolist))

##########################################################################

time.sleep(3)
sys.exit(0)