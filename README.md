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

## Prompt Design

The prompt for generating technical questions is carefully crafted to:
- Understand the candidate's tech stack.
- Generate beginner-friendly and relevant questions.
- Provide concise hints and feedback on incorrect answers.

The evaluation prompt instructs the model to assess the response, detect incorrect or incomplete answers, and offer suggestions for improvement.

## Challenges & Solutions

1. **Input Validation:**
   - Implemented regex patterns and logical checks for proper validation of user inputs.

2. **Handling Incorrect Responses:**
   - Introduced a retry mechanism with hints for improvement after the first incorrect attempt.
   - Automatic progression to the next question after two incorrect attempts.

3. **Maintaining Conversation State:**
   - Utilized Streamlit's session state to store conversation history and user progress.

4. **API Error Handling:**
   - Handled exceptions to ensure smooth interaction even in case of API failures.

## Future Scope

- Integrate database support for storing candidate responses.
- Expand to advanced technical rounds and coding challenges.
- Implement a scoring system to evaluate candidate performance.

### Contact

For any queries or collaboration opportunities, reach out to [Vishakha Agrawal](https://github.com/vishakha1411).

