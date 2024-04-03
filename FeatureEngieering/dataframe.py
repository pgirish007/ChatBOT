import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

def generate_skill_matrix(employee_name, data):
    try:
        # Sample dataset (replace with your actual dataset)
        df = pd.DataFrame(data)

        # Filter data for the specified employee
        employee_data = df[df['Name'] == employee_name]

        # Check if the employee exists
        if len(employee_data) == 0:
            return "Employee not found!"

        # Feature Engineering
        # ColumnTransformer for encoding job roles and industries
        column_transformer = ColumnTransformer(
            transformers=[
                ('job_role', OneHotEncoder(), ['Job Role']),
                ('industry', OneHotEncoder(), ['Industry']),
                ('pass_through', 'passthrough', ['Skills'])  # Pass through the 'Skills' column
            ]
        )

        encoded_data = column_transformer.fit_transform(employee_data)

        # Get feature names after encoding
        feature_names = column_transformer.get_feature_names_out()

        # Create DataFrame for encoded features
        features_df = pd.DataFrame(encoded_data, columns=feature_names)

        return features_df

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
skill_matrix = generate_skill_matrix(employee_name, data)
print(skill_matrix)

