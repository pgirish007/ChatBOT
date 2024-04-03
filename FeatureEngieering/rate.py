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

        # Create a dictionary to store skill weights for each role
        role_skill_weights = {
            'Data Scientist': {
                'Python': 3,
                'SQL': 2,
                'Machine Learning': 4,
                'Data Analysis': 3,'Architecutre':5
            },
            'Software Engineer': {
                'Java': 3,
                'HTML': 2,
                'CSS': 2
            },
            'Data Analyst': {
                'Python': 3,
                'Data Analysis': 3
            }
            # Add more roles and their respective skills and weights as needed
        }

        # Initialize dictionaries to store known and missing skills
        known_skills = {}
        missing_skills = {}

        # Get the employee's role
        employee_role = employee_data['Job Role'].iloc[0]

        # Get skill weights for the employee's role
        skill_weights = role_skill_weights[employee_role]

        # Populate known skills and missing skills based on rating
        for skill, weight in skill_weights.items():
            if skill in employee_skills:
                known_skills[skill] = weight
            elif weight > rating:
                missing_skills[skill] = weight

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
print("Known and missing skills for", employee_name, "higher than rating", rating, ":", skill_matrix)

