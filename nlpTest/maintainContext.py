from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

app = Flask(__name__)
# COMMAND: curl -X POST http://127.0.0.1:5000/chatbot -H "Content-Type: application/json" -d '{"user_id": "123", "message": "I want to build"}'

# Store user conversation state
user_states = {}

# Multi-level conversation flow
conversation_flow = {
    "build": {
        "question": "What kind of build do you need? (e.g., software, infrastructure, CI/CD)",
        "next_steps": {
            "software": {
                "question": "Do you need a frontend or backend build?",
                "next_steps": {
                    "frontend": {
                        "question": "Which frontend framework do you prefer? (e.g., React, Angular, Vue)?",
                        "next_steps": {
                            "react": {"response": "Great choice! Do you need SSR or CSR?"},
                            "angular": {"response": "Angular is solid! Are you using Angular CLI?"}
                        }
                    },
                    "backend": {
                        "question": "Which backend framework do you prefer? (e.g., Spring Boot, Django, Node.js)?",
                        "next_steps": {
                            "spring boot": {"response": "Spring Boot is powerful! Are you using REST or GraphQL?"},
                            "django": {"response": "Django is great! Do you need ORM support?"}
                        }
                    }
                }
            },
            "infrastructure": {
                "question": "Are you building on-premise or cloud?",
                "next_steps": {
                    "on-premise": {"question": "What server OS will you use? (e.g., Linux, Windows Server)"},
                    "cloud": {
                        "question": "Which cloud provider are you using? (AWS, Azure, GCP)?",
                        "next_steps": {
                            "aws": {"question": "Do you need EC2, Lambda, or Kubernetes setup?"},
                            "azure": {"response": "Azure is solid! Are you using Azure DevOps?"}
                        }
                    }
                }
            },
            "CI/CD": {
                "question": "Which CI/CD tool do you prefer? (e.g., Jenkins, GitHub Actions, GitLab CI)?",
                "next_steps": {
                    "jenkins": {"response": "Jenkins is powerful! Do you need a pipeline for Docker or Kubernetes?"},
                    "github actions": {"response": "GitHub Actions is great! Are you using self-hosted runners?"}
                }
            }
        }
    },
    "linux": {
        "question": "Are you looking to install Linux or troubleshoot an issue?",
        "next_steps": {
            "install": {
                "question": "Which Linux distribution do you want to install? (e.g., Ubuntu, CentOS, Debian)?",
                "next_steps": {
                    "ubuntu": {"response": "Ubuntu is popular! Do you need LTS or latest release?"},
                    "centos": {"response": "CentOS is stable. Are you setting up a web server?"}
                }
            },
            "troubleshoot": {
                "question": "What issue are you facing? (e.g., boot failure, network issue, package installation)?",
                "next_steps": {
                    "boot failure": {"response": "Check GRUB settings. Do you need recovery mode help?"},
                    "network issue": {"response": "Are you troubleshooting WiFi or Ethernet?"}
                }
            }
        }
    }
}

@app.route("/chatbot", methods=["POST"])
def chatbot():
    global user_states
    data = request.get_json()
    user_id = data.get("user_id", "default_user")  # Track user state
    user_message = data.get("message", "").lower()

    # Tokenize user input
    tokens = word_tokenize(user_message)

    # Check if user is in a follow-up state
    if user_id in user_states and user_states[user_id]["pending"]:
        pending_state = user_states[user_id]["pending"]
        possible_answers = pending_state["next_steps"]

        for token in tokens:
            if token in possible_answers:
                next_step = possible_answers[token]
                
                if "question" in next_step:  # If another level exists
                    user_states[user_id] = {"pending": next_step}
                    return jsonify({"response": next_step["question"]})
                
                elif "response" in next_step:  # If it's a final response
                    user_states[user_id] = {"pending": None}
                    return jsonify({"response": next_step["response"]})

        return jsonify({"response": f"Please specify: {', '.join(possible_answers.keys())}"})

    # Identify keywords in user input
    for keyword, flow in conversation_flow.items():
        if keyword in tokens:
            user_states[user_id] = {"pending": flow}
            return jsonify({"response": flow["question"]})

    return jsonify({"response": "I'm not sure what you're asking. Could you provide more details?"})


if __name__ == "__main__":
    app.run(debug=True)

