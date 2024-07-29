from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'sk-proj-L6HEQLIrzRhqyiQXhwyAT3BlbkFJ8xkTHcsIjLxGK5mVcpp6'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    content = request.form['content']
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize the following content: {content}"}
            ]
        )
        summary = response.choices[0].message['content'].strip()
        return jsonify({'summary': summary})
    except openai.error.OpenAIError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
