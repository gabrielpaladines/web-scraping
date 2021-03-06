# -*- coding: utf-8 -*-
import builtwith
import whois
from scraper import FoodScraper



_url = 'https://www.elcorteingles.es/ofertas-supermercado/'
output_file = "dataset.csv"

# Conocer la tecnologia del Sitio
print(builtwith.builtwith(_url))

# Propietario
# En este caso no se va a mostrar porque toda la información que devuelve es "null"
# print(whois.whois(_url))

# Scraping
scraper = FoodScraper(_url)
scraper.scrape()
scraper.data2csv(output_file)
