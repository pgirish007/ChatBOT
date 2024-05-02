from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initial JSON data
json_data = {
    "id": "",
    "name": "",
    "age": "",
    "Kisko": ""
}

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
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
