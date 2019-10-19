import pandas as pd

class RecessiveEncoder:
    @staticmethod
    def get_alleles(col):
        alleles = set()
        for snp in col.unique():
            alleles.add(snp[0])
            alleles.add(snp[1])
        return list(alleles)

    @staticmethod
    def get_columns_map(col):
        dataset = {}
        alleles = RecessiveEncoder.get_alleles(col)
        for a in alleles:
            col_name = f'{col.name}_{a}'
            col_data = [int(a in c) for c in col.values]
            dataset[col_name] = col_data
        return dataset

    @staticmethod
    def encode(X):
        dataset = {}
        for col in X:
            dataset.update(RecessiveEncoder.get_columns_map(X[col]))
        return pd.DataFrame(dataset)
