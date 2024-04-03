import pandas as pd

def generate_skill_matrix(employee_name, rating, data):
    try:
        # Sample dataset (replace with your actual dataset)
        df = pd.DataFrame(data)

        # Filter data for the specified employee
        employee_data = df[df['Name'] == employee_name]

        # Check if the employee exists
        if len(employee_data) == 0:
            return "Employee not found!"

        # Extract skills known by the employee
        employee_skills = ', '.join(employee_data['Skills']).split(', ')

        # Create a dictionary to store skill weights and associated learning resources for each role
        role_skill_info = {
            'Data Scientist': {
                'Python': {'weight': 3, 'learning': 'Complete Python Crash Course on Coursera'},
                'SQL': {'weight': 2, 'learning': 'Master SQL: A Beginner to Expert Course on Udemy'},
                'Machine Learning': {'weight': 4, 'learning': 'Machine Learning A-Z™: Hands-On Python & R In Data Science on Udemy'},
                'Data Analysis': {'weight': 3, 'learning': 'Data Analysis and Visualization with Python on Coursera'},
        	'Architecture': {'weight': 5, 'learning': 'Data Analysis and Visualization and architecture principle from the Princeton'}    
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
        employee_role = employee_data['Job Role'].iloc[0]

        # Get skill information for the employee's role
        role_skills_info = role_skill_info[employee_role]

        # Populate known skills and missing skills based on rating
        for skill, info in role_skills_info.items():
            if skill in employee_skills:
                known_skills[skill] = info
            elif info['weight'] > rating:
                missing_skills[skill] = info

        return {'Known Skills': known_skills, 'Missing Skills': missing_skills}

    except ValueError as ve:
        return "ValueError occurred:", ve
    except Exception as e:
        return "An error occurred:", e

# Sample dataset (replace with your actual dataset)
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Skills': ['Python, SQL, Machine Learning', 'Java, HTML, CSS', 'Python, Data Analysis'],
    'Proficiency': ['Intermediate, Intermediate, Advanced', 'Intermediate, Beginner, Beginner', 'Advanced, Intermediate'],
    'Job Role': ['Data Scientist', 'Software Engineer', 'Data Analyst'],
    'Industry': ['IT', 'IT', 'Finance']
}

employee_name = input("Enter employee name: ")
rating = int(input("Enter the rating: "))
skill_matrix = generate_skill_matrix(employee_name, rating, data)
print("Known and missing skills for\n '", employee_name, "'\n higher than rating '", rating, "' :", skill_matrix)

