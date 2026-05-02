from flask import Flask, request, render_template
from groq import Groq
from config import GROQ_API_KEY
import os
# from rag import rag  # Lazy import
# from pdf_utils import extract_text  # Lazy import

app = Flask(
    __name__,
    template_folder=os.path.dirname(os.path.abspath(__file__))
)

# Initialize Groq client
try:
    client = Groq(api_key=GROQ_API_KEY)
    print(f"Groq client initialized successfully")
except Exception as e:
    print(f"Failed to initialize Groq client: {e}")
    client = None

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    error = None

    if request.method == 'POST':
        try:
            question = request.form.get('question', '').strip()
            print(f"Question received: '{question}'")
            
            if not question:
                error = "Please enter a question"
            elif not client:
                error = "Groq client not initialized"
            else:
                print(f"Processing question: {question}")
                
                # Retrieve relevant context using RAG
                from rag import rag
                retrieved_chunks = rag.search(question)
                context = "\n".join(retrieved_chunks) if retrieved_chunks else ""
                
                # Build prompt
                if context:
                    prompt = (
                        f"Context: {context}\n\n"
                        f"Question: {question}\n\n"
                        "Answer as a helpful AI student assistant. "
                        "Provide a clear, well-structured response with headings, short paragraphs, and bullet points where appropriate."
                    )
                else:
                    prompt = (
                        f"Answer as a helpful AI student assistant: {question}\n\n"
                        "Provide a clear, well-structured response with headings, short paragraphs, and bullet points where appropriate."
                    )
                
                # Use Groq API to generate answer
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model="llama-3.1-8b-instant",
                    max_tokens=1000,
                )
                answer = chat_completion.choices[0].message.content
                print(f"Answer generated successfully")
                
        except Exception as exc:
            error = f"Error: {str(exc)}"
            print(f"Exception occurred: {error}")

    return render_template('index.html', answer=answer, error=error)

@app.route('/upload', methods=['POST'])
def upload():
    from rag import rag
    from pdf_utils import extract_text
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and file.filename.lower().endswith('.pdf'):
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
            file.save(tmp.name)
            text = extract_text(tmp.name)
            os.unlink(tmp.name)
        rag.add_documents(text)
        return "PDF uploaded and processed successfully", 200
    return "Invalid file type. Please upload a PDF.", 400

if __name__ == "__main__":
    print("Starting AI Student Assistant...")
    app.run(debug=True)
