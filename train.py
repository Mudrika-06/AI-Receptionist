import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Training dataset
training_data = [
    ("hello", "greeting"),
    ("hi", "greeting"),
    ("what are your office timings?", "timings"),
    ("when do you open?", "timings"),
    ("where is the office located?", "location"),
    ("where is the reception?", "location"),
    ("where is the hr department?", "hr"),
    ("i want to book an appointment", "appointment"),
    ("what is your contact number?", "contact"),
    ("thank you", "thanks"),
    ("goodbye", "goodbye")
]

texts, labels = zip(*training_data)

# Create & train model pipeline
model_pipeline = make_pipeline(TfidfVectorizer(), MultinomialNB())
model_pipeline.fit(texts, labels)

# Save model.pkl
joblib.dump(model_pipeline, "model.pkl")
print("Saved model.pkl successfully!")
