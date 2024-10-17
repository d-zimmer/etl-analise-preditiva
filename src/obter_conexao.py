import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def obter_conexao():
    engine = create_engine(os.getenv("DB_STRING"))

    return engine