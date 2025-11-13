import json
import nltk
import string
from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

app = Flask(__name__)

# Load FAQs
with open("faqs.json", "r") as f:
    faqs = json.load(f)

questions = [faq["question"] for faq in faqs]
answers = [faq["answer"] for faq in faqs]

# Text cleaning function
def preprocess(text):
    text = text.lower()
    text = "".join([c for c in text if c not in string.punctuation])
    return text

cleaned_questions = [preprocess(q) for q in questions]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(cleaned_questions)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["message"]
    cleaned_input = preprocess(user_input)

    user_vector = vectorizer.transform([cleaned_input])
    similarity_scores = cosine_similarity(user_vector, faq_vectors)
    best_match_idx = similarity_scores.argmax()

    response = answers[best_match_idx]
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
