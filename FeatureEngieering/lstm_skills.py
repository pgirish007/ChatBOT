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

def generate_skill_matrix(employee_name, rating, data):
    try:
        # Check if the employee exists
        if employee_name not in data:
            return {"error": "Employee not found!"}, 404
        
        employee_data = data[employee_name]
        skill_sequences = employee_data['SkillSequences']
        
        # Preprocess skill sequences
        processed_sequences = preprocess_skill_sequences(skill_sequences)
        
        # Load cached role_skill_info
        load_role_skill_info()
        
        # Create output dictionary to store predicted sequences, associated learning messages, and missing skills
        output = {'predicted_sequences': [], 'missing_skills': []}
        
        # Iterate over each skill sequence
        for sequence in processed_sequences:
            # Placeholder for predicted sequence (using same sequence as input for illustration)
            predicted_sequence = sequence.tolist()
            predicted_skills = []
            missing_skills = []
            
            # Retrieve associated learning messages and check for missing skills
            for skill_index, skill_value in enumerate(sequence):
                skill_name = list(cached_role_skill_info.keys())[skill_index]
                learning_message = cached_role_skill_info[skill_name].get('learning_message', '')
                
                if skill_value < rating:
                    missing_skills.append({
                        'skill_name': skill_name,
                        'required_rating': rating,
                        'predicted_proficiency': skill_value,
                        'learning_message': learning_message
                    })
                
                predicted_skills.append({
                    'skill_name': skill_name,
                    'predicted_proficiency': skill_value,
                    'learning_message': learning_message
                })
            
            output['predicted_sequences'].append(predicted_skills)
            output['missing_skills'].append(missing_skills)
        
        return output, 200

    except Exception as e:
        return {"error": "An error occurred: {}".format(e)}, 500

@app.route('/generate_skill_matrix', methods=['GET'])
def generate_skill_matrix_api():
    employee_name = request.args.get('employee_name')
    rating = int(request.args.get('rating'))
    
    # Sample dataset (replace with your actual dataset)
    data = {
        'John': {
            'SkillSequences': [
                [0.8, 0.7, 0.9],  # Skill vector at time step 1
                [0.85, 0.75, 0.92],  # Skill vector at time step 2
                [0.9, 0.8, 0.95]  # Skill vector at time step 3
            ]
        },
        'Alice': {
            'SkillSequences': [
                [0.6, 0.5, 0.4],  # Skill vector at time step 1
                [0.65, 0.55, 0.45],  # Skill vector at time step 2
                [0.7, 0.6, 0.5]  # Skill vector at time step 3
            ]
        },
        'Bob': {
            'SkillSequences': [
                [0.75, 0.65, 0.55],  # Skill vector at time step 1
                [0.8, 0.7, 0.6],  # Skill vector at time step 2
                [0.85, 0.75, 0.65]  # Skill vector at time step 3
            ]
        }
    }
    
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

