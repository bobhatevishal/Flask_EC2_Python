from flask import Flask, jsonify
import os
import random
app = Flask(__name__)

quotes = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "In a world full of trends, I want to remain a classic.",
    "Talk is cheap. Show me the code.",
    "First, solve the problem. Then, write the code.",
    "Python is where the magic happens."
]

@app.route('/')
def home():
    return '''
    <h1 style="color: teal; text-align: center;">🚀 Welcome to My Flask Server 🚀</h1>
    <p style="text-align: center;">You’ve reached the root. Try <code>/quote</code>, <code>/call</code>, or <code>/json</code></p>
    '''

@app.route('/quote')
def quote():
    return f"<h2 style='color: purple; text-align: center;'>💡 {random.choice(quotes)}</h2>"

@app.route('/json')
def json_data():
    return jsonify({
        "status": "success",
        "language": "Python",
        "framework": "Flask",
        "message": "You're running a cool API 😎"
    })

@app.route('/call')
def ascii_art():
    art = r"""
     ______     ______     __   __     ______    
    /\  == \   /\  __ \   /\ "-.\ \   /\  ___\   
    \ \  __<   \ \ \/\ \  \ \ \-.  \  \ \___  \  
     \ \_____\  \ \_____\  \ \_\\"\_\  \/\_____\ 
      \/_____/   \/_____/   \/_/ \/_/   \/_____/ 
    """
    return f"<pre>{art}</pre>"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
