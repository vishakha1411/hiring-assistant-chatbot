import streamlit as st
import google.generativeai as genai
import re  # For email validation

# Configure Gemini API
genai.configure(api_key="AIzaSyATKzzncrUDZl2oF7-IAs65o2km1yvRxaU")

# Function to get Gemini API response
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Input validation functions
def validate_name(name):
    return len(name.strip()) >= 2

def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email)

def validate_phone(phone):
    return phone.strip().isdigit() and len(phone.strip()) >= 10

def validate_experience(experience):
    return experience.strip().isdigit() and 0 <= int(experience) <= 50

def validate_position(position):
    return len(position.strip()) >= 2

def validate_location(location):
    return len(location.strip()) >= 2

def validate_tech_stack(tech_stack):
    return len(tech_stack.strip()) >= 2

# Initialize Streamlit session state
if "conversation" not in st.session_state:
    st.session_state.conversation = [
        {"role": "Bot", "text": "Hello! I'm your AI interviewer. Let's start with your basic details."}
    ]
    st.session_state.user_details = {}
    st.session_state.tech_stack_collected = False
    st.session_state.technical_questions = []
    st.session_state.current_question = 0
    st.session_state.attempts = 0  # Track attempts for each question
    st.session_state.conversation_ended = False
    st.session_state.input_key = 0  # Dynamic key for input field

# Streamlit UI
st.title("💼 AI Interview Chatbot 🤖")

# Display conversation history
for message in st.session_state.conversation:
    role = "🤖" if message["role"] == "Bot" else "👤"
    st.markdown(f"{role}: {message['text']}")

# Exit if conversation ended
if st.session_state.conversation_ended:
    st.success("Thank you for your time! We'll be in touch soon. 🚀")
    st.stop()

# Step 1: Collect Candidate Details
if not st.session_state.user_details:
    with st.form(key="user_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.text_input("Years of Experience")
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (e.g., Python, React, MySQL)")

        submit_button = st.form_submit_button("Submit Details")

    if submit_button:
        # Validate user input
        if not validate_name(full_name):
            st.error("Please enter a valid Full Name.")
        elif not validate_email(email):
            st.error("Please enter a valid Email Address.")
        elif not validate_phone(phone):
            st.error("Please enter a valid Phone Number.")
        elif not validate_experience(experience):
            st.error("Please enter a valid experience (0-50 years).")
        elif not validate_position(position):
            st.error("Please enter a valid Position.")
        elif not validate_location(location):
            st.error("Please enter a valid Location.")
        elif not validate_tech_stack(tech_stack):
            st.error("Please list at least one tech skill.")
        else:
            # Store user details in session state
            st.session_state.user_details = {
                "Full Name": full_name,
                "Email": email,
                "Phone": phone,
                "Experience": experience,
                "Position": position,
                "Location": location,
                "Tech Stack": [t.strip() for t in tech_stack.split(",") if t.strip()]
            }

            # Add user details to the conversation
            st.session_state.conversation.append({"role": "User", "text": f"My tech stack is: {tech_stack}"})

            # Generate technical questions
            prompt = f"""Generate 5 short one line or word answer technical interview questions about the following technologies: {tech_stack}. 
Tailor the difficulty of the questions to a candidate with {experience} years of experience with 0 being very easy , 1-2 being easy-medium and 3+ being good level.
Ensure the questions are clear, concise, and relevant to their skill level. Return only the questions, numbered sequentially."""
            generated_questions = get_gemini_response(prompt)

            if "Error:" not in generated_questions:
                st.session_state.technical_questions = [q for q in generated_questions.split("\n") if q.strip()]
                st.session_state.current_question = 0
                st.session_state.conversation.append({"role": "Bot", "text": "Great! Let's begin the technical round."})
                st.session_state.conversation.append({"role": "Bot", "text": st.session_state.technical_questions[0]})
            else:
                st.session_state.conversation.append({"role": "Bot", "text": "I'm facing an issue generating questions. Try again later."})

            st.rerun()

# Step 2: Handle User's Answers
if st.session_state.user_details and not st.session_state.conversation_ended:
    # Use a dynamic key for the input field
    user_input = st.text_input("Your Answer:", key=f"input_{st.session_state.input_key}")

    if user_input:
        # Store user response
        st.session_state.conversation.append({"role": "User", "text": user_input})
        st.session_state.input_key += 1  # Increment key to clear input field

        # Exit condition
        exit_keywords = ["exit", "quit", "end", "stop", "bye"]
        if any(word in user_input.lower() for word in exit_keywords):
            st.session_state.conversation.append({"role": "Bot", "text": "Thank you for the interview! We'll get back to you soon. 👋"})
            st.session_state.conversation_ended = True
            st.rerun()

        # Handle "I don't know" scenarios
        if "i don't know" in user_input.lower() or "skip" in user_input.lower():
            st.session_state.conversation.append({"role": "Bot", "text": "No worries! Moving to the next question."})
            st.session_state.current_question += 1
            st.session_state.attempts = 0  # Reset attempts
        else:
            # Evaluate User's Answer
            evaluation_prompt = f"""You are an expert technical interviewer. Evaluate the candidate's answer: '{user_input}' 
for the technical interview question: '{st.session_state.technical_questions[st.session_state.current_question]}'. 
If the answer is incorrect, provide a hint. if incomplete, provide improvement. 
Keep the response brief."""

            evaluation_response = get_gemini_response(evaluation_prompt)

            st.session_state.conversation.append({"role": "Bot", "text": evaluation_response})

            # Check if answer is satisfactory
            satisfactory_keywords = ["incorrect", "wrong", "inaccurate", "inappropriate", "irrelevant"]
            if any(word in evaluation_response.lower() for word in satisfactory_keywords):
                st.session_state.attempts += 1

                if st.session_state.attempts == 1:
                    st.session_state.conversation.append({"role": "Bot", "text": "Hmm... Try again!"})
                elif st.session_state.attempts >= 2:
                    st.session_state.conversation.append({"role": "Bot", "text": "Let's move to the next question."})
                    st.session_state.current_question += 1
                    st.session_state.attempts = 0  # Reset attempts
            else:
                st.session_state.current_question += 1
                st.session_state.attempts = 0  # Reset attempts

        # Move to next question or end interview
        if st.session_state.current_question < len(st.session_state.technical_questions):
            next_question = st.session_state.technical_questions[st.session_state.current_question]
            st.session_state.conversation.append({"role": "Bot", "text": next_question})
        else:
            st.session_state.conversation.append({"role": "Bot", "text": "That's the end of the technical round. Thank you for your responses!"})
            st.session_state.conversation_ended = True

        st.rerun()