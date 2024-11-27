import pandas as pd
from obter_conexao import obter_conexao

def carregar_dados(tabela):
    engine = obter_conexao()
    query = f"SELECT * FROM {tabela}"
    return pd.read_sql(query, con=engine)
