import pandas as pd
import json
import os

def excel_to_json(excel_file):
    # Read Excel file into pandas ExcelFile object
    xls = pd.ExcelFile(excel_file)
    
    # Iterate over each sheet
    for sheet_name in xls.sheet_names:
        # Read the sheet into pandas DataFrame
        df = pd.read_excel(xls, sheet_name)
        
        # Convert each row to JSON and store in a list
        json_list = []
        for index, row in df.iterrows():
            json_data = row.to_json()
            json_obj = json.loads(json_data)
            json_list.append(json_obj)
        
        # Write the list of JSON objects to a separate JSON file for each sheet
        output_file = f"{os.path.splitext(excel_file)[0]}_{sheet_name}.json"
        with open(output_file, 'w') as f:
            json.dump(json_list, f, indent=4)

# Example usage:
excel_file = 'input.xlsx'  # Replace 'input.xlsx' with the path to your Excel file

excel_to_json(excel_file)
