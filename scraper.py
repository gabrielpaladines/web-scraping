# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
import json
import csv
from product import Product


class FoodScraper():

    def __init__(self, _url):
        self.url = _url
        self.data = []
        # Se permite limitar la búsqueda para acotar el tiempo dedicado.
        self.max_pages = 150


    def __download_html(self, url):
        html = None
        page = requests.get(url, verify=True)

        if page.status_code == 200:
            html = page.content

        return html


    def buildProduct(self, food_item):
        food_dict = json.loads(food_item)
        product = Product(food_dict)
        return product


    def scrape(self):
        page_counter = 2
        print("Iniciando la busqueda de productos en oferta\n")

        # timer
        start_time = time.time()
        # Download HTML
        html = self.__download_html(self.url)

        while html:
            soup = BeautifulSoup(html, 'html.parser')
            items = soup.findAll("div", class_ = "grid-item")
            print("Items encontrados: " + str(len(items)))

            for item in items:
                food_data = item['data-json'] if 'data-json' in item.attrs else "no content"
                product = self.buildProduct(food_data)
                # Agregamos la descripcion del descuento
                description = item.findAll("div", class_="offer-description")
                if description:
                    product.set_description(description[0].text)
                # Almacenamos el producto
                self.data.append(product)

            if page_counter > self.max_pages:
                break

            # Download HTML
            time.sleep(30)
            html = self.__download_html(self.url + str(page_counter))
            print(self.url + str(page_counter))
            page_counter += 1

        # Show elapsed time
        end_time = time.time()
        print("elapsed time: " + str(round(((end_time - start_time) / 60), 2)) + " minutes")


    def data2csv(self, file_name):
        # from another class
        with open(file_name, 'w') as csv_file:
            wr = csv.writer(csv_file, delimiter=',')
            wr.writerow(["Nombre", "Marca", "Categorias", "Precio Original",
                         "Precio Final", "Moneda", "Estado","Descripcion", "Fecha de captura"])
            for product in self.data:
                wr.writerow(list(product))

