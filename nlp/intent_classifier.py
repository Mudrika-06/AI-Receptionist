import os
import joblib

# Locate model.pkl dynamically in the root folder (one level above nlp/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model.pkl")

# Load trained pipeline
model_pipeline = joblib.load(MODEL_PATH)

def predict_intent(user_text):
    if not user_text:
        return "unknown", 0.0
        
    intent = model_pipeline.predict([user_text])[0]
    
    probabilities = model_pipeline.predict_proba([user_text])[0]
    confidence = float(max(probabilities))
    
    return intent, confidence
