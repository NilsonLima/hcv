import pandas as pd
from os import path
from functools import reduce
from pprint import pprint

class Dataset:
    def __init__(self):
        prefix = path.dirname(path.realpath(__file__))
        full_path = path.join(prefix, 'hcv.xlsx')

        self.df = pd.read_excel(full_path, "Recorte - Planilha (10SNP's)")
        self.target = 'fibrose'
        self.features = ['ptx3_0', 'ptx3_1', 'mbl', 'il_0', 'il_1', 'il_2', 'tnf', 'sod', 'mpo', 'il_3']

    def filter_df_by_targets(self, targets):
        filter_condition = self.df[self.target] == targets[0]
        for t in targets[1:]:
            filter_condition |= self.df[self.target] == t

        return self.df[filter_condition]

    def get_X(self):
        return self.df[self.features]
    
    def get_y(self):
        return self.df[self.target]

    def extract_X(self, df, features = None):
        return df[features or self.features]
    
    def extract_y(self, df, target = None):
        return df[target or self.target]