import pandas as pd

def write_data_into_xlsx_file(data, columns, index, filename = 'output.xlsx'):
    pd.DataFrame(data, index=index, columns=columns).to_excel(filename)
    return