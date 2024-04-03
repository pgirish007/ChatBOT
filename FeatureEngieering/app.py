from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample dataset (replace with your actual dataset)
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Skills': ['Python, SQL, Machine Learning', 'Java, HTML, CSS', 'Python, Data Analysis'],
    'Proficiency': ['Intermediate, Intermediate, Advanced', 'Intermediate, Beginner, Beginner', 'Advanced, Intermediate'],
    'Job Role': ['Data Scientist', 'Software Engineer', 'Data Analyst'],
    'Industry': ['IT', 'IT', 'Finance']
}

@app.route('/skill-matrix', methods=['POST'])
def generate_skill_matrix():
    try:
        req_data = request.get_json()

        # Extract inputs from request
        employee_name = req_data['employee_name']
        rating = req_data['rating']

        # Find employee data
        employee_index = data['Name'].index(employee_name)
        employee_data = {key: data[key][employee_index] for key in data}

        # Check if the employee exists
        if not employee_data:
            return jsonify({"error": "Employee not found!"}), 404

        # Extract skills known by the employee
        employee_skills = employee_data['Skills'].split(', ')

        # Create a dictionary to store skill weights and associated learning resources for each role
        role_skill_info = {
            'Data Scientist': {
                'Python': {'weight': 3, 'learning': 'Complete Python Crash Course on Coursera'},
                'SQL': {'weight': 2, 'learning': 'Master SQL: A Beginner to Expert Course on Udemy'},
                'Machine Learning': {'weight': 4, 'learning': 'Machine Learning A-Z™: Hands-On Python & R In Data Science on Udemy'},
                'Data Analysis': {'weight': 3, 'learning': 'Data Analysis and Visualization with Python on Coursera'}
            },
            'Software Engineer': {
                'Java': {'weight': 3, 'learning': 'Java Programming Masterclass for Software Developers on Udemy'},
                'HTML': {'weight': 2, 'learning': 'HTML, CSS, and Javascript for Web Developers on Coursera'},
                'CSS': {'weight': 2, 'learning': 'The Complete CSS Flexbox Guide With a Complete Project 2021 on Udemy'}
            },
            'Data Analyst': {
                'Python': {'weight': 3, 'learning': 'Python for Data Science and Machine Learning Bootcamp on Udemy'},
                'Data Analysis': {'weight': 3, 'learning': 'Data Analysis with Python: Zero to Pandas on Jovian.ml'}
            }
            # Add more roles and their respective skills, weights, and learning resources as needed
        }

        # Initialize dictionaries to store known and missing skills
        known_skills = {}
        missing_skills = {}

        # Get the employee's role
        employee_role = employee_data['Job Role']

        # Get skill information for the employee's role
        role_skills_info = role_skill_info[employee_role]

        # Populate known skills and missing skills based on rating
        for skill, info in role_skills_info.items():
            if skill in employee_skills:
                known_skills[skill] = info
            elif info['weight'] > rating:
                missing_skills[skill] = info

        response = {
            'employee_name': employee_name,
            'employee_role': employee_role,
            'known_skills': known_skills,
            'missing_skills': missing_skills
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

