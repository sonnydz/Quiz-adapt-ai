import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load and preprocess the dataset
dataset_path = 'questions.csv'
df = pd.read_csv(dataset_path)

# Combine question and choices into a single text column
df['text'] = df['question'] + ' ' + df['choice_A'] + ' ' + df['choice_B'] + ' ' + df['choice_C'] + ' ' + df['choice_D']

# Split the dataset into training and testing sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Vectorize the text using CountVectorizer
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train_df['text'])
X_test = vectorizer.transform(test_df['text'])

# Train a logistic regression model for difficulty prediction
y_train = train_df['difficulty_level']
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(test_df['difficulty_level'], predictions)
print(f"Accuracy on the test set: {accuracy}")

# Example of making a prediction
input_text = "What is the sum of 3 + 3?"
input_vectorized = vectorizer.transform([input_text])
predicted_difficulty = model.predict(input_vectorized)[0]
print(f"Predicted difficulty for '{input_text}': {predicted_difficulty}")
