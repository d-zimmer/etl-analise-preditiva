import json
import pandas as pd
from obter_conexao import obter_conexao
from tratamento_dados import tratar_dados_json, tratar_dados_csv, tratar_dados_txt

def gravar_dados(arquivo, tipo, tabela_destino):
    try:
        # Conectar ao banco de dados
        engine = obter_conexao()

        if tipo == 'json':
            # Ler dados do JSON
            df = pd.read_json(arquivo, lines=True)
            df = tratar_dados_json(df)
            df.to_sql(tabela_destino, engine, if_exists='append', index=False)
            print(f"Dados JSON inseridos na tabela {tabela_destino} com sucesso.")

        elif tipo == 'csv':
            df = pd.read_csv(arquivo)
            df = tratar_dados_csv(df)
            df.to_sql(tabela_destino, engine, if_exists='append', index=False)
            print(f"Dados CSV inseridos na tabela {tabela_destino} com sucesso.")

        elif tipo == 'txt':
            df = pd.read_csv(arquivo, sep=';')
            df = tratar_dados_txt(df)
            df.to_sql(tabela_destino, engine, if_exists='append', index=False)
            print(f"Dados TXT inseridos na tabela {tabela_destino} com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro ao gravar os dados na tabela {tabela_destino}: {e}")
