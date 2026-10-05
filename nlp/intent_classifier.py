import joblib  # or pickle / spacy depending on your implementation

# Load your pre-trained model/vectorizer at the top of the file
# Make sure these files exist in your project repository!
model = joblib.load("model.pkl") 
vectorizer = joblib.load("vectorizer.pkl")

def predict_intent(text):
    text_vectorized = vectorizer.transform([text])
    intent = model.predict(text_vectorized)[0]
    
    # Get prediction confidence if supported
    confidence = 0.95
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(text_vectorized)
        confidence = max(probs[0])
        
    return intent, confidence
