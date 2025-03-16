# Hiring Assistant Chatbot

## Overview

The Hiring Assistant Chatbot is an AI-driven web application built using Streamlit and Google Gemini API. It aims to streamline the technical interview process by collecting candidate details, generating personalized technical questions, and evaluating responses. The chatbot leverages advanced NLP models to provide hints and feedback, ensuring a smooth and engaging interview experience.

## Features

- **Candidate Information Collection**: Collects essential details such as name, email, phone number, experience, desired position, location, and technical skills.
- **Dynamic Technical Question Generation**: Uses the Gemini API to generate tailored interview questions based on the candidate's tech stack.
- **Real-time Answer Evaluation**: Analyzes responses and provides immediate feedback, hints, or improvements.
- **Incorrect Response Handling**: Allows candidates to attempt again, receive hints, or move to the next question after repeated incorrect attempts.
- **Exit Mechanism**: Candidates can exit the interview anytime using predefined keywords.
- **Streamlit UI**: User-friendly interface for seamless interaction.

## Installation Instructions

1. Clone the repository:
```bash
$ git clone https://github.com/vishakha1411/hiring-assistant-chatbot.git
```

2. Navigate to the project directory:
```bash
$ cd hiring-assistant-chatbot
```

3. Install the required dependencies:
```bash
$ pip install -r requirements.txt
```

4. Run the Streamlit application:
```bash
$ streamlit run app1.py
```

## Usage Guide

1. Launch the chatbot and enter your basic details (Name, Email, Phone, Experience, Position, Location, and Tech Stack).
2. The chatbot will generate technical questions based on your information entered.
3. Respond to each question. If your answer is incorrect, the chatbot will provide hints or allow you to skip to the next question.
4. You can type 'exit' or 'stop' to end the interview.

## Technical Details

- **Frontend:** Streamlit
- **Backend API:** Google Gemini API (gemini-2.0-flash model)
- **Programming Language:** Python 3.12
- **Libraries Used:**
  - Streamlit
  - google-generativeai
  - Regex for input validation

### Prompt Design

The prompt design plays a crucial role in ensuring the effectiveness of the Hiring Assistant Chatbot. The prompts were meticulously crafted to gather accurate candidate details and assess their technical expertise.

1. **Information Gathering Prompt:**
   - A structured prompt was designed to collect essential candidate details such as name, email, experience, tech stack, and desired position. The chatbot uses input validation functions to ensure data accuracy and completeness.

2. **Technical Question Generation Prompt:**
   - The following prompt was used to dynamically generate technical questions:
   ```
   Generate 5 short one-line or word-answer technical interview questions about the following technologies: {tech_stack}.
   Tailor the difficulty of the questions to a candidate with {experience} years of experience with 0 being very easy, 1-2 being easy-medium, and 3+ being good level.
   Ensure the questions are clear, concise, and relevant to their skill level. Return only the questions, numbered sequentially.
   ```
   This prompt enables the chatbot to adapt the complexity of questions based on the candidate's experience level.

3. **Answer Evaluation Prompt:**
   ```
   You are an expert technical interviewer. Evaluate the candidate's answer: '{user_input}'
   for the technical interview question: '{current_question}'.
   If the answer is incorrect, provide a hint. If incomplete, suggest improvements.
   Keep the response brief.
   ```
   This allows the chatbot to assess the candidate's response and offer constructive feedback.


### Challenges & Solutions

1. **Accurate Candidate Data Collection:**
   - **Challenge:** Handling invalid inputs like incorrect email format or incomplete tech stack.
   - **Solution:** Implemented regex-based validation functions for email, phone number, and experience to ensure accurate data collection.

2. **Generating Relevant Technical Questions:**
   - **Challenge:** Generating questions tailored to the candidate's tech stack and experience level.
   - **Solution:** Utilized the Gemini API to dynamically generate relevant and concise questions based on the provided tech stack and experience.

3. **Handling Incorrect or Incomplete Responses:**
   - **Challenge:** Providing feedback when a candidate's answer is incorrect or incomplete.
   - **Solution:** Integrated an evaluation prompt to analyze the user's response and provide hints or improvements for better learning.

### Future Scope

1. **Enhanced User Experience:**
   - Integrate natural language understanding (NLU) models to improve the chatbot's conversational flow and adaptability.

2. **Advanced Question Difficulty Tuning:**
   - Introduce a feature to allow interviewers to manually adjust the difficulty of questions or select specific domains for deeper evaluation.

3. **Real-time Performance Analysis:**
   - Implement a scoring system to evaluate candidate performance and generate detailed analytics for hiring managers.

4. **Multi-Language Support:**
   - Expand the chatbot's capability to handle interviews in multiple languages for global hiring.

5. **Integration with ATS (Applicant Tracking Systems):**
   - Seamlessly integrate the chatbot with popular ATS platforms like Greenhouse or Lever to streamline candidate evaluation and tracking.

6. **Voice-Based Interaction:**
   - Introduce voice-based interviews for a more interactive and engaging experience.


### Contact

For any queries or collaboration opportunities, reach out to [Vishakha Agrawal](https://github.com/vishakha1411).

