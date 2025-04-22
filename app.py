from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get("question")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant specialized in Al Madinah Al Munawwarah in Saudi Arabia. You can answer questions related to its history, landmarks, events, religious and cultural aspects. You are also able to help tourists by providing suggested itineraries, travel tips, and organizing visit plans around Madinah. Always keep your answers related to Madinah and try to be as helpful and creative as possible. Respond in the same language the user is using.",
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        answer = response.choices[0].message['content'].strip()
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)