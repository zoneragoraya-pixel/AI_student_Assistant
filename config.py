import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path(__file__).with_name('.env')
load_dotenv(dotenv_path)

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
