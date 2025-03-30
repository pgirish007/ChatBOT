from flask import Flask, request, jsonify
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download("punkt")
nltk.download("stopwords")

# Initialize Flask app
app = Flask(__name__)

# Initialize stop words and stemmer
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

# Define keyword-action mapping
keyword_map = {
    "build": "Starting build process...",
    "linux": "Setting up Linux environment...",
    "server": "Configuring server settings...",
    "deploy": "Deploying the application...",
    "database": "Setting up the database...",
    "network": "Configuring network settings..."
}

def extract_keywords(text):
    """Extracts key terms from user input."""
    tokens = word_tokenize(text.lower())  # Tokenize input
    keywords = [stemmer.stem(word) for word in tokens if word not in stop_words and word not in string.punctuation]
    return keywords

def process_input(user_input):
    """Processes user input and maps to actions."""
    keywords = extract_keywords(user_input)
    actions = [keyword_map[word] for word in keywords if word in keyword_map]
    
    return {
        "keywords": keywords,
        "actions": actions if actions else ["No matching actions found"]
    }

@app.route('/chatbot', methods=['POST'])
def chatbot_api():
    """REST API endpoint to process text input."""
    data = request.json  # Get JSON data from request
    user_input = data.get("text", "")

    if not user_input:
        return jsonify({"error": "No input text provided"}), 400

    response = process_input(user_input)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

