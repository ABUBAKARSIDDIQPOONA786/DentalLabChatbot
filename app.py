from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Predefined responses
predefined_responses = {
    'greet': 'Hello! Welcome to MyDental Labs. How can I assist you today?',
    'goodbye': 'Goodbye! Have a great day!',
    'about_lab': 'We are MyDental Labs, providing top-notch dental lab services.',
    'services': 'We offer services including Crown and Bridge, Implants, Orthodontics, and Dentures.',
    'contact': 'You can contact us at info@mydentallabs.in or call us at +123-456-7890.',
    'services1' : 'Crown and bridge are common dental procedures used to restore and replace damaged or missing teeth.',
    'services2' : 'Dental implants are a permanent solution for missing teeth.',
    'services3' : 'Orthodontics is a dental specialty that focuses on diagnosing, preventing, and correcting issues with teeth and jaws, as well as bite patterns.',
    'services4' : 'Dentures are removable replacements for missing teeth and surrounding tissues.'
}

def get_predefined_response(user_input):
    user_input = user_input.lower()
    if 'hello' in user_input or 'hi' in user_input or 'hey' in user_input:
        return predefined_responses['greet']
    elif 'bye' in user_input or 'goodbye' in user_input:
        return predefined_responses['goodbye']
    elif 'about' in user_input and 'lab' in user_input:
        return predefined_responses['about_lab']
    elif 'services' in user_input:
        return predefined_responses['services']
    elif 'contact' in user_input:
        return predefined_responses['contact']
    elif 'crown' in user_input or 'bridge' in user_input:
        return predefined_responses['services1']
    elif 'implants' in user_input:
        return predefined_responses['services2']
    elif 'orthodontics' in user_input:
        return predefined_responses['services3']
    elif 'dentures' in user_input:
        return predefined_responses['services4']
    else:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'response': 'No message received'})
    
    predefined_response = get_predefined_response(user_input)
    if predefined_response:
        response = predefined_response
    else:
        response = "Sorry I can't assist you here."
    
    return jsonify({'response': response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port)
