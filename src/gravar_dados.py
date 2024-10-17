import json
import pandas as pd
from obter_conexao import obter_conexao
from tratamento_dados import tratar_dados_json, tratar_dados_csv, tratar_dados_txt

def gravar_dados(arquivo, tipo):
    try:
        # Conectar ao banco de dados
        engine = obter_conexao()

        if tipo == 'json':
            # Ler dados do JSON
            with open(arquivo, 'r') as f:
                dados_json = json.load(f)
            
            # Converte para DataFrame do Pandas
            df = pd.DataFrame(dados_json)
            
            # Tratar dados antes de inserir
            df = tratar_dados_json(df)
            
            # Insere os dados no banco de dados
            df.to_sql('tabela_json', engine, if_exists='append', index=False)
            print("Dados JSON inseridos com sucesso!")

        elif tipo == 'csv':
            # Ler dados do CSV
            try:
                df = pd.read_csv(arquivo, encoding='utf-8')
            except UnicodeDecodeError:
                df = pd.read_csv(arquivo, encoding='ISO-8859-1')

            # Tratar dados antes de inserir
            df = tratar_dados_csv(df)
            
            # Insere os dados no banco de dados
            df.to_sql('tabela_csv', engine, if_exists='append', index=False)
            print("Dados CSV inseridos com sucesso!")

        elif tipo == 'txt':
            # Ler dados do TXT e transformar em DataFrame
            dados = []
            with open(arquivo, 'r') as f:
                for linha in f:
                    try:
                        id_transacao, data, tipo_transacao, valor, status = linha.strip().split(';')
                        dados.append({
                            'id_transacao': id_transacao,
                            'data': data,
                            'tipo': tipo_transacao,
                            'valor': float(valor),
                            'status': status
                        })
                    except ValueError:
                        print(f"Erro ao processar a linha: {linha}")
            
            # Converte para DataFrame do Pandas
            df = pd.DataFrame(dados)
            
            # Tratar dados antes de inserir
            df = tratar_dados_txt(df)
            
            # Insere os dados no banco de dados
            df.to_sql('tabela_txt', engine, if_exists='append', index=False)
            print("Dados TXT inseridos com sucesso!")

        else:
            print("Tipo de arquivo não suportado!")

    except Exception as e:
        print(f"Ocorreu um erro ao gravar os dados: {e}")

    finally:
        # Fechar a conexão com o banco de dados, se existir
        if 'engine' in locals():
            engine.dispose()
