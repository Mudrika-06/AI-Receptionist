from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def predict_intent(text):
    text_vector = vectorizer.transform([text])

    intent = classifier.predict(text_vector)[0]

    confidence = max(
        classifier.predict_proba(text_vector)[0]
    )

    return intent, confidence
