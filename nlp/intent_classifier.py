import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# 1. Define sample training data for intents
training_data = [
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

# Separate texts and target intent labels
texts, labels = zip(*training_data)

# 2. Build a Text Classification Pipeline
# Combine TF-IDF Vectorization and Naive Bayes Classifier
model_pipeline = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

# 3. Train the model
model_pipeline.fit(texts, labels)

# 4. Save the trained pipeline as model.pkl in the root directory
output_path = os.path.join(os.path.dirname(__file__), "model.pkl")
joblib.dump(model_pipeline, output_path)

print(f"Model successfully saved to: {output_path}")
