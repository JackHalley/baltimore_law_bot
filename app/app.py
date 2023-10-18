from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return open('index.html').read()


@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    user_query = request.json['query']
    # For now, we'll just echo back the query.
    # In a real-world scenario, you'd pass this to your NLP model or logic for processing.
    return jsonify({"response": f"You said: {user_query}"})


if __name__ == '__main__':
    app.run(debug=True)
