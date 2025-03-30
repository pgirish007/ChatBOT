import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download("punkt")
nltk.download("stopwords")

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
    
    if actions:
        return " -> ".join(actions)
    else:
        return "I don't understand. Can you rephrase?"

def ai_chatbot():
    """Runs the chatbot in a loop."""
    print("AI Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit"]:
            print("AI Chatbot: Goodbye!")
            break
        response = process_input(user_input)
        print(f"AI Chatbot: {response}")

if __name__ == "__main__":
    ai_chatbot()

