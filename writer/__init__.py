import pandas as pd
import json

def write_data_into_xlsx_file(data, columns, index, filename='output.xlsx'):
    pd.DataFrame(data, index=index, columns=columns).to_excel(filename)
    return

def write_data_into_json_file(data, filename='experiments.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    return