from flask import Flask, render_template, request, session
import requests
from openaichat import *

app = Flask(__name__)
app.secret_key = 'e1b8fae957289d4a4a86d5d51c9f8329'

# Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    conversation = []
    if 'conversation' in session:
        conversation = session['conversation']
    if request.method == 'POST':
        message = request.form['message']
        conversation.append({'type': 'user', 'content': message})
        prompt = f"User: {message}\nAI:"
        response = make_api_call(prompt)
        conversation.append({'type': 'api', 'content': response})

    session['conversation'] = conversation
    return render_template('index.html', conversation=conversation)

# API call function
def make_api_call(message):
    response = generate_response(message)
    return response

if __name__ == '__main__':
    app.run(debug=True)