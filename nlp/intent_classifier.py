from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# 1. Dataset for intent classification
TRAINING_DATA = [
    # Greeting
    ("hello", "greeting"),
    ("hi", "greeting"),
    ("hey", "greeting"),
    ("good morning", "greeting"),
    
    # Timings
    ("what are your office timings?", "timings"),
    ("when do you open?", "timings"),
    ("what time do you close?", "timings"),
    ("working hours", "timings"),
    
    # Location
    ("where is the office located?", "location"),
    ("where is the reception?", "location"),
    ("how can I reach the building?", "location"),
    
    # HR
    ("where is the hr department?", "hr"),
    ("how to contact human resources?", "hr"),
    ("hr team location", "hr"),
    
    # Appointment
    ("i want to book an appointment", "appointment"),
    ("schedule a meeting", "appointment"),
    ("can i fix a time to visit?", "appointment"),
    
    # Contact
    ("what is your contact number?", "contact"),
    ("give me your phone number and email", "contact"),
    ("how can i call reception?", "contact"),
    
    # Thanks & Goodbye
    ("thank you very much", "thanks"),
    ("thanks for the help", "thanks"),
    ("goodbye", "goodbye"),
    ("bye see you", "goodbye")
]

# 2. Extract texts and labels
texts, labels = zip(*TRAINING_DATA)

# 3. Create and train the model in memory on startup
model_pipeline = make_pipeline(TfidfVectorizer(), MultinomialNB())
model_pipeline.fit(texts, labels)


def predict_intent(user_text):
    if not user_text:
        return "unknown", 0.0
        
    intent = model_pipeline.predict([user_text])[0]
    
    probabilities = model_pipeline.predict_proba([user_text])[0]
    confidence = float(max(probabilities))
    
    return intent, confidence
