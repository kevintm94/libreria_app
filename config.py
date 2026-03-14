import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    SECRET_KEY = 'clave_secreta_123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/db_libreria'
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
    GROQ_MODEL = os.environ.get('GROQ_MODEL', 'llama-3.1-8b-instant')
    CHATBOT_TEMPERATURE = float(os.environ.get('CHATBOT_TEMPERATURE', 0.7))
    CHATBOT_SQL_TEMPERATURE = float(os.environ.get('CHATBOT_SQL_TEMPERATURE', 0.1))
    CHATBOT_MAX_TOKENS = int(os.environ.get('CHATBOT_MAX_TOKENS', 1024))