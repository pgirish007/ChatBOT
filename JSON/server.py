from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Function to load JSON data from file
def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)

# Function to save JSON data to file
def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Initial JSON data
json_data = load_data()

# Route to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Route to serve initial JSON data
@app.route('/get_user')
def get_user():
    return jsonify(json_data)

# Route to update JSON data
@app.route('/update_user', methods=['POST'])
def update_user():
    data = request.json
    for key in data:
        if key in json_data:
            json_data[key] = data[key]
    save_data(json_data)
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
