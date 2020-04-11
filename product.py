# -*- coding: utf-8 -*-
from datetime import date

class Product():

    def __init__(self, iterable=(), **kwargs):
        # Inicializamos el producto con el dictionario de datos
        self.__dict__.update(iterable, **kwargs)
        # Inicializamos la descripcion del producto
        self.descripcion = ''
        # Colocamos la fecha de creacion
        self.created_at = date.today()
        # Convertimos las categorias del producto a texto
        self.categories = ','.join([str(elem) for elem in self.category])
        # Inicializamos los precios relacionados al productos
        # el producto puede tener dos precios el original y el final
        # estos dos difieren si existe un descuento a nivel de precios
        _price = self.price
        self.price_final = _price['final']
        self.price_original = _price['original'] if 'original' in _price \
            else _price['final']

    def __iter__(self):
        return iter([self.name, self.brand, self.categories,
                     self.price_original, self.price_final,
                     self.currency, self.status,self.descripcion, self.created_at])

    def set_description(self, description):
        self.descripcion = description