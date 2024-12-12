Talk AI - A Chatbot Application
Overview
Talk AI is a simple chatbot application built using Streamlit. It provides a real-time chat interface that interacts with OpenAI's API to generate conversational responses. This project demonstrates how to integrate OpenAI's language model into a Streamlit app to create an interactive user experience.
Features
•	Chat Interface: Engage in conversations with the AI assistant.
•	Real-time Updates: Messages from the user and AI are displayed in a conversational format.
•	Session Management: Maintains chat history during a single session.
Prerequisites
To run this application, ensure you have the following installed:
•	Python 3.8 or later
•	Streamlit
•	OpenAI Python SDK
Installation
1.	Clone the repository or download the app.py file.
2.	Install the required Python packages:
pip install streamlit openai
Usage
1.	Run the application using Streamlit:
streamlit run app.py
2.	Open the local URL displayed in your terminal (e.g., http://localhost:8501) in a web browser.
3.	Start interacting with the chatbot by typing in the input box.
Configuration
The chatbot uses OpenAI's API for generating responses. Update the following variables in app.py to configure your API settings:
•	base_url: The base URL of your OpenAI API endpoint.
•	api_key: Replace "random-text" with your actual OpenAI API key.
Dependencies
The application uses the following dependencies:
•	Streamlit: For creating the interactive web application.
•	OpenAI Python SDK: For integrating OpenAI's API.
Limitations
•	The application relies on the OpenAI model specified (llama3 in the code). Ensure the model is available on your API server.
•	The code uses a local API endpoint (http://localhost:11434/v1). Ensure the server is running and accessible.
