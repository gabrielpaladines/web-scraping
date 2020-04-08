# -*- coding: utf-8 -*-
from datetime import date

class Product():

    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)
        self.created_at = date.today()
        self.categories = ','.join([str(elem) for elem in self.category])
        _price = self.price
        self.price_final = _price['final']
        self.price_original = _price['original'] if 'original' in _price \
            else _price['final']

    def __iter__(self):
        return iter([self.name, self.brand, self.categories,
                     self.price_original, self.price_final,
                     self.currency, self.status, self.created_at])
