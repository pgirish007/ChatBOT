import json
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import schedule
import time

app = Flask(__name__)
CORS(app)

# Global variable to store cached role_skill_info
cached_role_skill_info = None

def load_role_skill_info():
    global cached_role_skill_info
    with open('role_skills_info.json') as f:
        cached_role_skill_info = json.load(f)

@app.before_request
def load_cached_role_skill_info():
    load_role_skill_info()

def preprocess_skill_sequences(skill_sequences):
    # Convert skill sequences to numpy array
    sequences_array = np.array(skill_sequences)
    return sequences_array

def create_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, input_shape=input_shape, activation='relu', return_sequences=True))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

def train_lstm_model(skill_sequences):
    processed_sequences = preprocess_skill_sequences(skill_sequences)
    X, y = processed_sequences[:, :-1], processed_sequences[:, -1]
    X = X.reshape((X.shape[0], X.shape[1], 1))
    model = create_lstm_model((X.shape[1], 1))
    model.fit(X, y, epochs=100, verbose=0)
    return model

def generate_skill_matrix(employee_name, rating, data):
    try:
        # Find the employee by name
        employee = next((emp for emp in data['employees'] if emp['name'] == employee_name), None)
        
        # Check if the employee exists
        if not employee:
            return {"error": "Employee not found!"}, 404
        
        role = employee['role']
        skill_sequences = employee['SkillSequences']
        
        # Train LSTM model
        lstm_model = train_lstm_model(skill_sequences)
        
        # Load cached role_skill_info
        load_role_skill_info()
        
        # Create output dictionary to store predicted sequences and missing skills
        output = {'matching_skills': [], 'missing_skills': []}
        
        # Predict proficiency for each skill sequence
        for sequence in skill_sequences:
            X_test = np.array(sequence[:-1]).reshape((1, len(sequence)-1, 1))
            predicted_proficiency = lstm_model.predict(X_test)[0][0]
            skill_name = list(cached_role_skill_info.keys())[sequence.index(max(sequence))]
            learning_message = cached_role_skill_info[skill_name].get('learning_message', '')
            
            if predicted_proficiency >= rating:
                output['matching_skills'].append({
                    'skill_name': skill_name,
                    'predicted_proficiency': predicted_proficiency,
                    'learning_message': learning_message
                })
            else:
                output['missing_skills'].append({
                    'skill_name': skill_name,
                    'required_rating': rating,
                    'predicted_proficiency': predicted_proficiency,
                    'learning_message': learning_message
                })
        
        # Convert numpy arrays to lists
        for key, value in output.items():
            for item in value:
                for k, v in item.items():
                    if isinstance(v, np.ndarray):
                        item[k] = v.tolist()
        
        return output, 200

    except Exception as e:
        return {"error": "An error occurred: {}".format(e)}, 500

@app.route('/generate_skill_matrix', methods=['GET'])
def generate_skill_matrix_api():
    employee_name = request.args.get('employee_name')
    rating = int(request.args.get('rating'))
    
    # Load the input data from JSON file
    with open('input_employee_data.json') as f:
        data = json.load(f)
    
    result, status_code = generate_skill_matrix(employee_name, rating, data)
    return jsonify(result), status_code

def update_role_skill_info():
    load_role_skill_info()

# Schedule the task to update role_skill_info once a day at midnight
schedule.every().day.at("00:00").do(update_role_skill_info)

# Function to run the scheduled tasks
def run_scheduled_tasks():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    # Start a separate thread to run scheduled tasks
    import threading
    threading.Thread(target=run_scheduled_tasks).start()
    
    # Run the Flask app
    app.run(debug=True)
