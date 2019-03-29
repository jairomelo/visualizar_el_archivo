#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##### Urllib

##import urllib.request
##
##url = "http://pares.mcu.es/ParesBusquedas20/catalogo/contiene/65591"
##ur = urllib.request.urlopen(url).read()
##print(ur)

##### Requests

##import requests
##
##url = "http://pares.mcu.es/ParesBusquedas20/catalogo/contiene/65591"
##r = requests.get(url)
##print(r.text)

####### URL
######
# http://pares.mcu.es/ParesBusquedas20/catalogo/contiene/1930216
######

##import requests
##
##ident = input('Ingresar el número de la unidad de descripción: ')
##
##host = "http://pares.mcu.es"
##ruta_entrada = "/ParesBusquedas20/catalogo/contiene/{}".format(ident)
##url = "{}{}".format(host, ruta_entrada)
##
##r = requests.get(url)
##print(r.text)

####### URL Omeka

##import requests
##
##url_base = "http://localhost/fichero/items/browse?search=&advanced%5B0%5D%5Bjoiner%5D=and&advanced%5B0%5D%5Belement_id%5D=1&advanced%5B0%5D%5Btype%5D=contains&advanced%5B0%5D%5Bterms%5D="
##busqueda = "indulto"
##url_coda = "&range=&collection=&type=&tags=&featured=&exhibit=&geolocation-address=&geolocation-latitude=&geolocation-longitude=&geolocation-radius=10&submit_search=Buscar+por+items"
##
##url = "{}{}{}".format(url_base, busqueda, url_coda)
##
##r = requests.get(url)
##print(r.text)

###### Beautiful Soup

##import urllib
##from bs4 import BeautifulSoup
##
##ident = input('Ingresar el número de la unidad de descripción: ')
##
##host = "http://pares.mcu.es"
##ruta_entrada = "/ParesBusquedas20/catalogo/contiene/{}".format(ident)
##url = "{}{}".format(host, ruta_entrada)
##
##salsa = urllib.request.urlopen(url).read()
##sopa = BeautifulSoup(salsa, 'html.parser')
##
##print(sopa)

#### Beautiful Soup 2

##import urllib
##from bs4 import BeautifulSoup
##
##ident = input('Ingresar el número de la unidad de descripción: ')
##
##host = "http://pares.mcu.es"
##ruta_entrada = "/ParesBusquedas20/catalogo/contiene/{}".format(ident)
##url = "{}{}".format(host, ruta_entrada)
##
##salsa = urllib.request.urlopen(url).read()
##sopa = BeautifulSoup(salsa, 'html.parser')
##
##for links in sopa.find_all('a'):
##	print(links.prettify())


###### Beautiful Soup 3

##import urllib
##from bs4 import BeautifulSoup
##
##ident = input('Ingresar el número de la unidad de descripción: ')
##
##host = "http://pares.mcu.es"
##ruta_entrada = "/ParesBusquedas20/catalogo/contiene/{}".format(ident)
##url = "{}{}".format(host, ruta_entrada)
##
##salsa = urllib.request.urlopen(url).read()
##sopa = BeautifulSoup(salsa, 'html.parser')
##
##for links in sopa.find_all('a'):
##	print(links.text)

##### Selenium

##from bs4 import BeautifulSoup
##from selenium import webdriver
##
##ident = input('Ingresar el número de la unidad de descripción: ')
##
##host = "http://pares.mcu.es"
##ruta_entrada = "/ParesBusquedas20/catalogo/contiene/{}".format(ident)
##url = "{}{}".format(host, ruta_entrada)
##
##browser = webdriver.Chrome(executable_path=r'bin/chromedriver.exe')
##browser.get(url)
##
##input('Presione ENTER para salir del navegador de pruebas')
##browser.quit()

###### Selenium 2

##import time
##from bs4 import BeautifulSoup
##from selenium import webdriver
##from selenium.webdriver.common.keys import Keys
##
##ident = input('Ingresar el número de la unidad de descripción: ')
##
##host = "http://pares.mcu.es"
##ruta_entrada = "/ParesBusquedas20/catalogo/contiene/{}".format(ident)
##url = "{}{}".format(host, ruta_entrada)
##
##browser = webdriver.Chrome(executable_path=r'bin/chromedriver.exe')
##browser.get(url)
##
##time.sleep(1)
##ruti = browser.find_element_by_xpath('//*[@id="resultados"]/div[2]/a[5]')
##ruti.click()
##time.sleep(3)
##
##input('Presione ENTER para salir del navegador de pruebas')
##browser.quit()

###### Selenium 3

##import time
##from bs4 import BeautifulSoup
##from selenium import webdriver
##from selenium.webdriver.common.keys import Keys
##
##ident = input('Ingresar el número de la unidad de descripción: ')
##
##host = "http://pares.mcu.es"
##ruta_entrada = "/ParesBusquedas20/catalogo/contiene/{}".format(ident)
##url = "{}{}".format(host, ruta_entrada)
##
##browser = webdriver.Chrome(executable_path=r'bin/chromedriver.exe')
##browser.get(url)
##
##listado = []
##
##soup = BeautifulSoup(browser.page_source, 'html.parser')
##for em in soup("em"):
##	soup.em.decompose()
##caja = soup.select('table.displayTable tbody')
##for box in caja:
##	total = box.select('p.fecha')
##	for columns in total:
##		fecha = columns.get_text()
##		listado.append(fecha)
##time.sleep(1)
##ruti = browser.find_element_by_xpath('//*[@id="resultados"]/div[2]/a[5]')
##ruti.click()
##time.sleep(3)
##soup = BeautifulSoup(browser.page_source, 'html.parser')
##for em in soup("em"):
##	soup.em.decompose()
##caja = soup.select('table.displayTable tbody')
##for box in caja:
##	total = box.select('p.fecha')
##	for columns in total:
##		fecha = columns.get_text()
##		listado.append(fecha)
##
##browser.quit()
##
##print(listado)
##
##input('Presione ENTER para salir del programa')
