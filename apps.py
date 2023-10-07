from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load and preprocess the model and vectorizer
df = pd.read_csv('questions.csv')
df['text'] = df['question'] + ' ' + df['choice_A'] + ' ' + df['choice_B'] + ' ' + df['choice_C'] + ' ' + df['choice_D']
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(df['text'])
model = LogisticRegression(max_iter=1000)
model.fit(X_train, df['difficulty_level'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_text = request.form['input_text']
        # Vectorize the input text
        input_vectorized = vectorizer.transform([input_text])
        # Make a prediction
        predicted_difficulty = model.predict(input_vectorized)[0]

        # Get a recommended next question (you might need to customize this part)
        recommended_question = df[df['difficulty_level'] == predicted_difficulty].sample(1)['question'].values[0]

        return render_template('index.html', input_text=input_text, predicted_difficulty=predicted_difficulty, recommended_question=recommended_question)

if __name__ == '__main__':
    app.run(debug=True)
