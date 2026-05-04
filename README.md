# AI_student_Assistant

🤖 AI Student Assistant
An intelligent AI-powered student assistant built using Flask, LLMs, and optional RAG (Retrieval-Augmented Generation). This assistant can answer questions, assist with studies, and provide helpful explanations in a clean web interface.

📌 Features:
💬 Ask any question and get AI-generated answers
📚 Supports study-related queries (programming, theory, etc.)
🔎 Optional RAG support for document-based answers
🎨 Clean and simple UI (customizable templates)
🔊 Text-to-speech (optional feature)
⚡ Fast response using modern LLM APIs

🛠️ Technologies Used:
Python
Flask
HTML, CSS, JavaScript
LLM APIs (Groq )
RAG (optional with embeddings)


⚙️ Installation:
Clone the repository
git clone https://github.com/zoneragoraya/AI_Student_Assistant.gitcd AI_Student_Assistant
Create virtual environment
python -m venv venvvenv\Scripts\activate   # Windows
Install dependencies
pip install -r requirements.txt
Add API Key
Create a .env file and add:
API_KEY=your_api_key_here

▶️ Run the Project:
python app.py
Open browser:
http://127.0.0.1:5000

💡 How It Works:
User enters a question
Flask backend receives request
Query is processed using:
LLM API (for general answers)
RAG (if enabled, for document-based answers)
Response is sent back and displayed on UI

🎨 Customization:
Modify UI in templates/index.html
Add styles in static/style.css
Update AI logic in utils.py


🚀 Future Improvements:
User authentication
Chat history saving
Voice input support
Multi-language support

👩‍💻 Author:
Your Name: Zonera Maqbool
Roll No: 2k24/AI/107
AI Student Assistant Project




