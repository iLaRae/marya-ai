from flask import Flask, jsonify, request
import openai
from flask_cors import CORS
import os

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# app instance
app = Flask(__name__)
CORS(app)

#------------------------QUESTION---------------

@app.route('/question', methods=['POST'])
def question():
    data = request.json
    question = data.get('question')
    
    if question:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user", 
                    "content": question
                }
            ]
        )

        answer = completion.choices[0].message['content']
        return jsonify({"answer": answer})

    return jsonify({"error": "No question provided"})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
