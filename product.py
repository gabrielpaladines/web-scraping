import time

class Product():

    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)
        self.created_at = time.time()

    def __iter__(self):
        return iter([self.name, self.brand])