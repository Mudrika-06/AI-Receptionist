# import streamlit as st
# import spacy
# import re
# from datetime import datetime
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression

# # nlp = spacy.load("en_core_web_sm")
# # import streamlit as st
# # import spacy

# nlp = spacy.load("en_core_web_sm")

# training_sentences = [
#     # Greeting
#     "hello",
#     "hi",
#     "hey",
#     "good morning",
#     "good afternoon",
#     "good evening",

#     # Office timings
#     "what are the office timings",
#     "when is the office open",
#     "what time does the office open",
#     "when does the office close",
#     "tell me the working hours",

#     # Location
#     "where is the office",
#     "where is the reception",
#     "where can I find the HR department",
#     "where is the meeting room",
#     "tell me the office location",

#     # HR
#     "I want to meet HR",
#     "where is the HR department",
#     "how can I contact HR",
#     "I need to speak with HR",
#     "who is the HR manager",

#     # Appointment
#     "I want to book an appointment",
#     "I need an appointment",
#     "schedule a meeting",
#     "can I meet the manager",
#     "I want to schedule a meeting",

#     # Contact
#     "what is the contact number",
#     "give me the phone number",
#     "how can I contact the office",
#     "what is the office number",
#     "give me contact details",

#     # Thanks
#     "thank you",
#     "thanks",
#     "thank you so much",
#     "thanks for your help",

#     # Goodbye
#     "bye",
#     "goodbye",
#     "see you",
#     "have a nice day"
# ]

# intent_labels = [
#     "greeting", "greeting", "greeting",
#     "greeting", "greeting", "greeting",

#     "timings", "timings", "timings",
#     "timings", "timings",

#     "location", "location", "location",
#     "location", "location",

#     "hr", "hr", "hr", "hr", "hr",

#     "appointment", "appointment", "appointment",
#     "appointment", "appointment",

#     "contact", "contact", "contact", "contact",
#     "contact",

#     "thanks", "thanks", "thanks", "thanks",

#     "goodbye", "goodbye", "goodbye", "goodbye"
# ]


# # --------------------------------------------------
# # TRAIN NLP CLASSIFIER
# # --------------------------------------------------

# vectorizer = TfidfVectorizer(
#     lowercase=True,
#     stop_words="english"
# )

# X = vectorizer.fit_transform(training_sentences)

# classifier = LogisticRegression()
# classifier.fit(X, intent_labels)


# # --------------------------------------------------
# # KNOWLEDGE BASE
# # --------------------------------------------------

# knowledge_base = {
#     "office_timings":
#         "Our office is open from 9:00 AM to 5:00 PM, Monday to Friday.",

#     "location":
#         "The reception desk is located at the main entrance on the ground floor.",

#     "hr":
#         "The HR department is located on the first floor. You can contact HR during office hours.",

#     "contact":
#         "You can contact the office at +91-9876543210 or email reception@example.com.",

#     "meeting_room":
#         "The main meeting room is located on the first floor near the HR department."
# }


# # --------------------------------------------------
# # EXTRACT ENTITIES USING SPACY
# # --------------------------------------------------

# def extract_entities(text):

#     doc = nlp(text)

#     entities = {}

#     for ent in doc.ents:
#         entities[ent.label_] = ent.text

#     return entities


# # --------------------------------------------------
# # EXTRACT PHONE NUMBER
# # --------------------------------------------------

# def extract_phone(text):

#     phone_pattern = r'\b(?:\+91[-\s]?)?[6-9]\d{9}\b'

#     match = re.search(phone_pattern, text)

#     if match:
#         return match.group()

#     return None


# # --------------------------------------------------
# # EXTRACT NAME
# # --------------------------------------------------

# def extract_name(text):

#     patterns = [
#         r"my name is ([A-Za-z ]+)",
#         r"i am ([A-Za-z ]+)",
#         r"this is ([A-Za-z ]+)"
#     ]

#     for pattern in patterns:

#         match = re.search(pattern, text, re.IGNORECASE)

#         if match:
#             return match.group(1).strip()

#     return None


# # --------------------------------------------------
# # RESPONSE GENERATOR
# # --------------------------------------------------

# def generate_response(user_input):

#     # Convert text into vector
#     user_vector = vectorizer.transform([user_input])

#     # Predict intent
#     intent = classifier.predict(user_vector)[0]

#     # Extract NLP entities
#     entities = extract_entities(user_input)

#     # Extract name
#     name = extract_name(user_input)

#     # Extract phone
#     phone = extract_phone(user_input)


#     # -----------------------------
#     # INTENT RESPONSES
#     # -----------------------------

#     if intent == "greeting":

#         return (
#             "Hello! 👋 Welcome to our virtual reception desk. "
#             "How may I help you today?"
#         )


#     elif intent == "timings":

#         return knowledge_base["office_timings"]


#     elif intent == "location":

#         return knowledge_base["location"]


#     elif intent == "hr":

#         return knowledge_base["hr"]


#     elif intent == "contact":

#         return knowledge_base["contact"]


#     elif intent == "appointment":

#         st.session_state.appointment_mode = True

#         return (
#             "Sure! I can help you schedule an appointment. "
#             "Please provide your name, the person you want to meet, "
#             "and your preferred date and time."
#         )


#     elif intent == "thanks":

#         return "You're very welcome! 😊 Is there anything else I can help you with?"


#     elif intent == "goodbye":

#         return "Goodbye! 👋 Have a wonderful day."


#     else:

#         return (
#             "I'm sorry, I couldn't understand your request. "
#             "Could you please rephrase it?"
#         )


# # --------------------------------------------------
# # STREAMLIT USER INTERFACE
# # --------------------------------------------------

# st.set_page_config(
#     page_title="AI Receptionist",
#     page_icon="🤖",
#     layout="centered"
# )


# # --------------------------------------------------
# # HEADER
# # --------------------------------------------------

# st.title("🤖 AI Virtual Receptionist")

# st.write(
#     "An NLP-powered virtual receptionist that can understand "
#     "user queries and provide information."
# )


# # --------------------------------------------------
# # SESSION STATE
# # --------------------------------------------------

# if "messages" not in st.session_state:

#     st.session_state.messages = []


# # --------------------------------------------------
# # DISPLAY PREVIOUS CHAT
# # --------------------------------------------------

# for message in st.session_state.messages:

#     with st.chat_message(message["role"]):

#         st.write(message["content"])


# # --------------------------------------------------
# # USER INPUT
# # --------------------------------------------------

# user_input = st.chat_input(
#     "Type your message here..."
# )


# if user_input:

#     # Add user message
#     st.session_state.messages.append({
#         "role": "user",
#         "content": user_input
#     })

#     with st.chat_message("user"):

#         st.write(user_input)


#     # Generate response
#     response = generate_response(user_input)


#     # Add assistant response
#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": response
#     })


#     with st.chat_message("assistant"):

#         st.write(response)


# # --------------------------------------------------
# # SIDEBAR
# # --------------------------------------------------

# with st.sidebar:

#     st.header("📌 NLP Features")

#     st.write("✓ Intent Recognition")
#     st.write("✓ TF-IDF Vectorization")
#     st.write("✓ Text Classification")
#     st.write("✓ Named Entity Recognition")
#     st.write("✓ Entity Extraction")
#     st.write("✓ Context-based Responses")

#     st.divider()

#     st.subheader("Try asking:")

#     st.write("• What are the office timings?")
#     st.write("• Where is the HR department?")
#     st.write("• I want to book an appointment")
#     st.write("• What is the contact number?")
#     st.write("• Where is the reception?")


```python
import streamlit as st
import spacy

from nlp.intent_classifier import predict_intent
from nlp.entity_extractor import extract_entities


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Virtual Receptionist",
    page_icon="🤖",
    layout="centered"
)


# --------------------------------------------------
# LOAD NLP MODEL
# --------------------------------------------------

nlp = spacy.load("en_core_web_sm")


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("🤖 AI Virtual Receptionist")

st.write(
    "Your intelligent virtual front-desk assistant"
)


# --------------------------------------------------
# INITIALIZE CHAT
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# INITIAL GREETING
# --------------------------------------------------

if "greeted" not in st.session_state:

    st.session_state.greeted = True

    greeting = (
        "👋 Hello! Welcome to our organization.\n\n"
        "I'm your **AI Virtual Receptionist**. "
        "I can help you with office information, "
        "departments, appointments, and contact details.\n\n"
        "**How may I assist you today?**"
    )

    st.session_state.messages.append({
        "role": "assistant",
        "content": greeting
    })


# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# RESPONSE FUNCTION
# --------------------------------------------------

def generate_response(intent):

    responses = {

        "greeting":
            "Hello! 👋 Welcome! How may I assist you today?",

        "timings":
            "🕘 Our office is open from **9:00 AM to 5:00 PM, Monday to Friday**.\n\n"
            "Saturday: **9:00 AM to 1:00 PM**\n\n"
            "Sunday: **Closed**.",

        "location":
            "📍 The reception desk is located at the **main entrance on the ground floor**.",

        "hr":
            "👥 The HR department is located on the **first floor**.",

        "appointment":
            "📅 Sure! I can help you book an appointment.\n\n"
            "Please provide:\n"
            "1. Your name\n"
            "2. Person you want to meet\n"
            "3. Preferred date\n"
            "4. Preferred time",

        "contact":
            "📞 You can contact our office at **+91-9876543210**.\n\n"
            "📧 Email: reception@example.com",

        "thanks":
            "You're very welcome! 😊 Is there anything else I can help you with?",

        "goodbye":
            "Goodbye! 👋 Thank you for visiting. Have a wonderful day!"
    }

    return responses.get(
        intent,
        "I'm sorry, I couldn't understand that. Could you please rephrase your question?"
    )


# --------------------------------------------------
# QUICK OPTIONS
# --------------------------------------------------

st.markdown("### 💡 How can I help you?")


col1, col2 = st.columns(2)

with col1:

    office_button = st.button(
        "🏢 Office Information",
        use_container_width=True
    )

    department_button = st.button(
        "👥 Departments",
        use_container_width=True
    )

    appointment_button = st.button(
        "📅 Book Appointment",
        use_container_width=True
    )


with col2:

    timings_button = st.button(
        "🕘 Office Timings",
        use_container_width=True
    )

    contact_button = st.button(
        "📞 Contact Us",
        use_container_width=True
    )

    location_button = st.button(
        "📍 Location",
        use_container_width=True
    )


# --------------------------------------------------
# BUTTON RESPONSES
# --------------------------------------------------

selected_question = None


if office_button:

    selected_question = "Where is the office?"


elif department_button:

    selected_question = "Where is the HR department?"


elif appointment_button:

    selected_question = "I want to book an appointment"


elif timings_button:

    selected_question = "What are the office timings?"


elif contact_button:

    selected_question = "What is the contact number?"


elif location_button:

    selected_question = "Where is the reception?"


# --------------------------------------------------
# PROCESS BUTTON INPUT
# --------------------------------------------------

if selected_question:

    # Display user's selected option
    st.session_state.messages.append({
        "role": "user",
        "content": selected_question
    })

    with st.chat_message("user"):

        st.write(selected_question)


    # NLP processing
    intent, confidence = predict_intent(
        selected_question
    )

    entities = extract_entities(
        selected_question
    )


    # Generate response
    response = generate_response(intent)


    # Store response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


    with st.chat_message("assistant"):

        st.markdown(response)

        # Show NLP information
        with st.expander("🔍 NLP Analysis"):

            st.write(
                f"**Detected Intent:** {intent}"
            )

            st.write(
                f"**Confidence:** {confidence:.2f}"
            )

            if entities:

                st.write("**Detected Entities:**")

                for entity in entities:

                    st.write(
                        f"• {entity['text']} → {entity['label']}"
                    )


# --------------------------------------------------
# CUSTOM CHAT INPUT
# --------------------------------------------------

user_input = st.chat_input(
    "💬 Or type your question here..."
)


if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })


    with st.chat_message("user"):

        st.write(user_input)


    # NLP processing
    intent, confidence = predict_intent(
        user_input
    )

    entities = extract_entities(
        user_input
    )


    # Generate response
    response = generate_response(intent)


    # Store response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


    with st.chat_message("assistant"):

        st.markdown(response)

        with st.expander("🔍 NLP Analysis"):

            st.write(
                f"**Detected Intent:** {intent}"
            )

            st.write(
                f"**Confidence:** {confidence:.2f}"
            )

            if entities:

                st.write("**Detected Entities:**")

                for entity in entities:

                    st.write(
                        f"• {entity['text']} → {entity['label']}"
                    )
```

This version gives you the interaction you described:

```text
          🤖 AI RECEPTIONIST

              👋
     Hello! Welcome to our
          organization.

    How may I assist you today?

 ┌─────────────────────────────┐
 │ 🏢 Office Information       │
 │ 👥 Departments              │
 │ 📅 Book Appointment         │
 │ 🕘 Office Timings           │
 │ 📞 Contact Us               │
 │ 📍 Location                 │
 └─────────────────────────────┘

       💬 Type your question...
```

### One improvement I'd make next

For a **real receptionist**, we can make the buttons hierarchical.

For example, if the user clicks **🏢 Office Information**:

```text
🏢 Office Information

What would you like to know?

📍 Location
🕘 Office Timings
🏢 Facilities
📞 Contact Information
```

And if they click **📅 Book Appointment**:

```text
📅 Book Appointment

Who would you like to meet?

👨‍💼 HR
👩‍💼 Manager
👨‍💻 Technical Team
🔙 Back
```

That will make it feel much more like an **actual interactive AI receptionist** rather than a normal chatbot, while the NLP component continues working behind the scenes.
