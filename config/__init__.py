import json
from os import path
from itertools import product

class Config:
    def __init__(self):
        prefix = path.dirname(path.realpath(__file__))
        full_path = path.join(prefix, 'config.json')

        with open(full_path) as file:
            self.config = json.load(file)

    def get_product(self):
        return list(product(*self.config.values()))