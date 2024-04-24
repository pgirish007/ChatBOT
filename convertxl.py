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
        
        # Initialize dictionary to hold grouped data
        grouped_data = {}
        
        # Group rows based on values in column 2
        for index, row in df.iterrows():
            key = row.iloc[1]  # Assuming column 2 is index 1
            if key not in grouped_data:
                grouped_data[key] = []
            grouped_data[key].append(row.to_dict())
        
        # Write the grouped data to a separate JSON file for each sheet
        output_folder = f"{os.path.splitext(excel_file)[0]}_{sheet_name}_json"
        os.makedirs(output_folder, exist_ok=True)
        for key, value in grouped_data.items():
            output_file = os.path.join(output_folder, f"{key}.json")
            with open(output_file, 'w') as f:
                json.dump(value, f, indent=4)

# Example usage:
excel_file = 'input.xlsx'  # Replace 'input.xlsx' with the path to your Excel file

excel_to_json(excel_file)
