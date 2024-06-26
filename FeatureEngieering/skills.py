import pandas as pd

def generate_skill_matrix(employee_name, data):
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
                'Data Analysis': 3
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

        # Initialize dictionaries to store categorized skills for the employee's role
        high_weight_skills = {}
        medium_weight_skills = {}
        low_weight_skills = {}
        missing_skills = {}

        # Get the employee's role
        employee_role = employee_data['Job Role'].iloc[0]

        # Categorize skills based on weight for the employee's role
        for skill, weight in role_skill_weights[employee_role].items():
            if skill in employee_skills:
                if weight >= 3:
                    high_weight_skills[skill] = weight
                elif weight == 2:
                    medium_weight_skills[skill] = weight
                else:
                    low_weight_skills[skill] = weight
            else:
                missing_skills[skill] = weight

        # Sort skills within each category based on weight
        high_weight_skills = dict(sorted(high_weight_skills.items(), key=lambda x: x[1], reverse=True))
        medium_weight_skills = dict(sorted(medium_weight_skills.items(), key=lambda x: x[1], reverse=True))
        low_weight_skills = dict(sorted(low_weight_skills.items(), key=lambda x: x[1], reverse=True))
        missing_skills = dict(sorted(missing_skills.items(), key=lambda x: x[1], reverse=True))

        return high_weight_skills, medium_weight_skills, low_weight_skills, missing_skills

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
high_weight_skills, medium_weight_skills, low_weight_skills, missing_skills = generate_skill_matrix(employee_name, data)
print("High Weight Skills known by", employee_name, "for the role:", high_weight_skills)
print("Medium Weight Skills known by", employee_name, "for the role:", medium_weight_skills)
print("Low Weight Skills known by", employee_name, "for the role:", low_weight_skills)
print("Missing skills for", employee_name, "for the role:", missing_skills)

