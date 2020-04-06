# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
import json
import csv
from product import Product
from pprint import pprint


class FoodScraper():

    def __init__(self, _url):
        self.url = _url
        self.data = []

    def __download_html(self, url):
        page = requests.get(url)
        html = page.content
        return html


    def buildProduct(self, food_item):
        food_dict = json.loads(food_item)
        product = Product(food_dict)
        # pprint(vars(product))
        return product


    def scrape(self):
        print("Iniciando la busqueda de productos en oferta\n")

        # timer
        start_time = time.time()

        # Download HTML
        html = self.__download_html(self.url)
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup.prettify())

        items = soup.findAll("div", class_ = "grid-item")
        print("Items encontrados: " + str(len(items)))

        for item in items:
            food_data = item['data-json'] if 'data-json' in item.attrs else "no content"
            product = self.buildProduct(food_data)
            # Store the data
            self.data.append(product)

        # Show elapsed time
        end_time = time.time()
        print("elapsed time: " + str(round(((end_time - start_time) / 60), 2)) + " minutes")


    def data2csv(self, file_name):
        # from another class
        with open(file_name, 'w') as csv_file:
            wr = csv.writer(csv_file, delimiter=',')
            wr.writerow(["Nombre", "Marca", "Categorias", "Precio Original",
                         "Precio Final", "Moneda", "Fecha de captura"])
            for product in self.data:
                wr.writerow(list(product))

