import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample dataset (replace with your actual dataset)
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Skills': ['Python, SQL, Machine Learning', 'Java, HTML, CSS', 'Python, Data Analysis'],
    'Proficiency': ['Intermediate, Intermediate, Advanced', 'Intermediate, Beginner, Beginner', 'Advanced, Intermediate'],
    'Job Role': ['Data Scientist', 'Software Engineer', 'Data Analyst'],
    'Industry': ['IT', 'IT', 'Finance']
}

df = pd.DataFrame(data)

# Feature Engineering
# One-hot encoding for job roles and industries
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
job_role_encoded = encoder.fit_transform(df[['Job Role']])
industry_encoded = encoder.fit_transform(df[['Industry']])

# TF-IDF Vectorization for skill descriptions
tfidf_vectorizer = TfidfVectorizer()
skills_tfidf = tfidf_vectorizer.fit_transform(df['Skills'])

# Create DataFrame for one-hot encoded features
job_role_df = pd.DataFrame(job_role_encoded, columns=encoder.categories_[0])
industry_df = pd.DataFrame(industry_encoded, columns=encoder.categories_[0])

# Combine all features into a single DataFrame
features_df = pd.concat([job_role_df, industry_df], axis=1)
features_df = pd.concat([features_df, pd.DataFrame(skills_tfidf.toarray(), columns=tfidf_vectorizer.get_feature_names_out())], axis=1)

print("Feature Engineered DataFrame:")
print(features_df)

