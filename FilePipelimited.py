import json

def convert_pipe_delimited_to_json(file_path, output_file):
    # Initialize an empty dictionary to store the JSON objects
    json_data = {}

    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by pipe delimiter
            fields = line.strip().split('|')

            # Extract the root key from the first field
            root_key = fields[0]

            # Create a dictionary to store the data excluding the root key
            data = {
                "field1": fields[1],
                "field2": fields[2],
                "field3": fields[3],
                # Add more fields as needed
            }

            # Check if the data is unique for the root key
            if root_key in json_data:
                unique_data = all(data != item for item in json_data[root_key])
            else:
                unique_data = True

            # If the data is unique, append it to the existing JSON object
            if unique_data:
                if root_key in json_data:
                    json_data[root_key].append(data)
                else:
                    json_data[root_key] = [data]

    # Write the JSON data to the output file
    with open(output_file, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)

    print(f"JSON data written to {output_file}")

# Example usage:
input_file_path = 'data.txt'  # Replace 'data.txt' with the path to your pipe-delimited data file
output_file_path = 'output.json'  # Replace 'output.json' with the desired output file path
convert_pipe_delimited_to_json(input_file_path, output_file_path)
