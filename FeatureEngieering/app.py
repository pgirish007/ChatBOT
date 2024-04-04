import json
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
import schedule
import time

app = Flask(__name__)
CORS(app)

# Global variable to store cached role_skill_info
cached_role_skill_info = None

def load_role_skill_info():
    global cached_role_skill_info
    with open('role_skill_info.json') as f:
        cached_role_skill_info = json.load(f)

@app.before_request
def load_cached_role_skill_info():
    load_role_skill_info()

def generate_skill_matrix(employee_name, rating, data):
    try:
        # Check if the employee exists
        if employee_name not in data:
            return {"error": "Employee not found!"}, 404
        
        employee_data = data[employee_name]
        
        # Extract skills known by the employee
        employee_skills = set(employee_data['Skills'].split(', '))
        
        # Initialize dictionaries to store known and missing skills
        known_skills = {}
        missing_skills = {}

        # Get the employee's role
        employee_role = employee_data['Job Role']
        
        # Get skill information for the employee's role
        role_skills_info = cached_role_skill_info.get(employee_role, {})
        
        # Populate known skills and missing skills based on rating
        for skill, info in role_skills_info.items():
            if skill in employee_skills:
                known_skills[skill] = info
            elif info['weight'] > rating:
                missing_skills[skill] = info
        
        # Assign learning paths for missing skills
        for skill, info in missing_skills.items():
            missing_skills[skill]['learning_path'] = f"Learn {skill}: {info['learning']}"
        
        return {'Known Skills': known_skills, 'Missing Skills': missing_skills}, 200

    except Exception as e:
        return {"error": "An error occurred: {}".format(e)}, 500

@app.route('/generate_skill_matrix', methods=['GET'])
def generate_skill_matrix_api():
    employee_name = request.args.get('employee_name')
    rating = int(request.args.get('rating'))
    
    # Sample data (replace with your actual data)
    data = {
        'John': {
            'Skills': 'Python, SQL, Machine Learning',
            'Proficiency': 'Intermediate, Intermediate, Advanced',
            'Job Role': 'Data Scientist',
            'Industry': 'IT'
        },
        'Alice': {
            'Skills': 'Java, HTML, CSS',
            'Proficiency': 'Intermediate, Beginner, Beginner',
            'Job Role': 'Software Engineer',
            'Industry': 'IT'
        },
        'Bob': {
            'Skills': 'Python, Data Analysis',
            'Proficiency': 'Advanced, Intermediate',
            'Job Role': 'Data Analyst',
            'Industry': 'Finance'
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
