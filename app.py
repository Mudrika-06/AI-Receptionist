```python
import streamlit as st

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
# PAGE HEADER
# --------------------------------------------------

st.title("🤖 AI Virtual Receptionist")

st.write(
    "Your intelligent virtual front-desk assistant"
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "greeted" not in st.session_state:
    st.session_state.greeted = False


# --------------------------------------------------
# INITIAL GREETING
# --------------------------------------------------

if not st.session_state.greeted:

    greeting = (
        "👋 **Hello! Welcome to our organization!**\n\n"
        "I'm your **AI Virtual Receptionist**. "
        "I can help you with office information, "
        "departments, appointments, timings, and contact details.\n\n"
        "**How may I assist you today?**"
    )

    st.session_state.messages.append({
        "role": "assistant",
        "content": greeting
    })

    st.session_state.greeted = True


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
            "👋 Hello! Welcome! How may I assist you today?",

        "timings":
            "🕘 **Office Timings**\n\n"
            "Monday to Friday: **9:00 AM – 5:00 PM**\n\n"
            "Saturday: **9:00 AM – 1:00 PM**\n\n"
            "Sunday: **Closed**.",

        "location":
            "📍 The reception desk is located at the "
            "**main entrance on the ground floor**.",

        "hr":
            "👥 The **HR Department** is located on the "
            "**first floor**.",

        "appointment":
            "📅 **Sure! I can help you book an appointment.**\n\n"
            "Please provide:\n"
            "1. Your name\n"
            "2. Person you want to meet\n"
            "3. Preferred date\n"
            "4. Preferred time",

        "contact":
            "📞 **Contact Information**\n\n"
            "Phone: **+91-9876543210**\n\n"
            "Email: **reception@example.com**",

        "thanks":
            "You're very welcome! 😊\n\n"
            "Is there anything else I can help you with?",

        "goodbye":
            "Goodbye! 👋\n\n"
            "Thank you for visiting. Have a wonderful day!"
    }

    return responses.get(
        intent,
        "I'm sorry, I couldn't understand your request. "
        "Could you please rephrase your question?"
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
# DETERMINE SELECTED OPTION
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
# PROCESS QUICK OPTION
# --------------------------------------------------

if selected_question:

    # Add selected option to chat
    st.session_state.messages.append({
        "role": "user",
        "content": selected_question
    })

    # NLP processing
    intent, confidence = predict_intent(
        selected_question
    )

    entities = extract_entities(
        selected_question
    )

    # Generate response
    response = generate_response(intent)

    # Save response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # Refresh page to display new messages
    st.rerun()


# --------------------------------------------------
# CUSTOM CHAT INPUT
# --------------------------------------------------

user_input = st.chat_input(
    "💬 Or type your question here..."
)


if user_input:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # NLP processing
    intent, confidence = predict_intent(
        user_input
    )

    entities = extract_entities(
        user_input
    )

    # Generate response
    response = generate_response(intent)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # Refresh page
    st.rerun()
