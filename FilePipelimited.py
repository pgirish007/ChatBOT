import json

def convert_pipe_delimited_to_json(file_path):
    # Initialize an empty list to store the JSON objects
    json_data = []

    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by pipe delimiter
            fields = line.strip().split('|')

            # Create a dictionary to store the data
            data = {
                "field1": fields[0],
                "field2": fields[1],
                "field3": fields[2],
                # Add more fields as needed
            }

            # Append the dictionary to the list
            json_data.append(data)

    # Convert the list of dictionaries to JSON
    json_output = json.dumps(json_data, indent=4)

    return json_output

# Example usage:
file_path = 'data.txt'  # Replace 'data.txt' with the path to your pipe-delimited data file
json_output = convert_pipe_delimited_to_json(file_path)
print(json_output)
