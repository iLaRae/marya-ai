from flask import Flask, jsonify, request
from flask import Flask 
from openai import OpenAI
from flask_cors import CORS



# app instance
app = Flask(__name__)
CORS(app)
client = OpenAI()


#------------------------QUESTION---------------

@app.route('/question', methods=['POST'])
def question():
    data = request.json
    question = data['question']
    
    if question:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[

                {
                    "role": "user", 
                    "content": question
                }

            ]
        )

        answer = completion.choices[0].message.content
        return jsonify({"answer": answer})

    return jsonify({"error": "No question provided"})




if __name__ == "__main__":
    app.run(debug=True, port=8080)


