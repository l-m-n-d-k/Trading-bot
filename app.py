from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)


def generate_text(prompt):
    try:
        client = OpenAI(api_key='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')
        response = client.chat.completions.create(
timeout=60,
model="ft:gpt-3.5-turbo-1106:t1::8mJFSyqI",
messages=[
                {"role": "system", "content": "This chatbot helps people understand if they are at risk of developing lung cancer and provides screening recommendations. The user enters symptoms in a yes/no format, and you answer whether they should get screened and start worrying about it."},
                {"role": "user", "content": prompt}
            ],
)
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_input = data['text']
    model_response = generate_text(user_input)
    response = {
        "prediction": model_response
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)