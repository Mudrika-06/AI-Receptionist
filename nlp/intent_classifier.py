from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# --------------------------------------------------
# TRAINING DATA
# --------------------------------------------------

training_sentences = [
    # Greetings
    "hello",
    "hi",
    "hey",
    "good morning",
    "good afternoon",
    "good evening",

    # Office Timings
    "what are the office timings",
    "when is the office open",
    "when does the office close",
    "what are the working hours",
    "tell me office hours",

    # Location
    "where is the office",
    "where is the reception",
    "where is the meeting room",
    "where is the office located",

    # HR
    "I want to meet HR",
    "I need to speak with HR",
    "who is the HR manager",
    "how can I contact HR",

    # Appointment
    "I want to book an appointment",
    "I need an appointment",
    "schedule a meeting",
    "I want to meet the manager",

    # Contact
    "what is the contact number",
    "give me the phone number",
    "how can I contact the office",
    "give me contact details",

    # Thanks
    "thank you",
    "thanks",
    "thank you so much",

    # Goodbye
    "bye",
    "goodbye",
    "see you later"
]


# --------------------------------------------------
# INTENT LABELS
# --------------------------------------------------

intent_labels = [
    # Greetings
    "greeting",
    "greeting",
    "greeting",
    "greeting",
    "greeting",
    "greeting",

    # Timings
    "timings",
    "timings",
    "timings",
    "timings",
    "timings",

    # Location
    "location",
    "location",
    "location",
    "location",

    # HR
    "hr",
    "hr",
    "hr",
    "hr",

    # Appointment
    "appointment",
    "appointment",
    "appointment",
    "appointment",

    # Contact
    "contact",
    "contact",
    "contact",
    "contact",

    # Thanks
    "thanks",
    "thanks",
    "thanks",

    # Goodbye
    "goodbye",
    "goodbye",
    "goodbye"
]


# --------------------------------------------------
# TF-IDF VECTORIZER
# --------------------------------------------------

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)


# Convert training sentences into numerical vectors
X = vectorizer.fit_transform(training_sentences)


# --------------------------------------------------
# MACHINE LEARNING CLASSIFIER
# --------------------------------------------------

classifier = LogisticRegression()

classifier.fit(
    X,
    intent_labels
)


# --------------------------------------------------
# INTENT PREDICTION FUNCTION
# --------------------------------------------------

def predict_intent(text):

    # Convert user's question into TF-IDF vector
    text_vector = vectorizer.transform([text])

    # Predict the intent
    intent = classifier.predict(
        text_vector
    )[0]

    # Calculate confidence
    confidence = max(
        classifier.predict_proba(
            text_vector
        )[0]
    )

    return intent, confidence
