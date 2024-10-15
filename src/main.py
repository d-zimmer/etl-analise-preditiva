from gerador_dados import gerar_dados_csv, gerar_dados_json, gerar_dados_txt
import ler_dados
import load_sql
import obter_conexao
import gravar_dados
from datetime import time, timedelta

while True:
    print("Iniciando processo ETL...")

    arquivo_json = 'dados.json'
    arquivo_csv = 'dados.csv'
    arquivo_txt = 'dados.txt'

    gerar_dados_json(100, arquivo_json)
    gerar_dados_csv(100, arquivo_csv)
    gerar_dados_txt(100, arquivo_txt)

    dados_consolidados = ler_dados(arquivo_json, arquivo_csv, arquivo_txt)

    gravar_dados(dados_consolidados, 'mongodb://localhost:27017/', 'meu_banco', 'minha_colecao')

    print("Processo ETL finalizado. Aguardando 1 minuto...")
    time.sleep(60)
