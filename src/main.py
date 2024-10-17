import os
import random
from time import sleep
from gerador_dados import gerar_dados_csv, gerar_dados_json, gerar_dados_txt
from gravar_dados import gravar_dados  # Função consolidada que faz a inserção no banco

def main():
    # Diretório onde os arquivos serão salvos
    diretorio_dados = 'data'

    # Garante que a pasta de saída 'data' existe
    os.makedirs(diretorio_dados, exist_ok=True)

    while True:
        print("Iniciando processo ETL...")

        # Definir caminhos para os arquivos de dados
        arquivo_json = os.path.join(diretorio_dados, 'dados.json')
        arquivo_csv = os.path.join(diretorio_dados, 'dados_produtos.csv')
        arquivo_txt = os.path.join(diretorio_dados, 'dados_transacoes.txt')

        # Geração de dados
        gerar_dados_json(random.randrange(1,150), arquivo_json)
        gerar_dados_csv(random.randrange(1,150), arquivo_csv)
        gerar_dados_txt(random.randrange(1,150), arquivo_txt)

        # Inserção dos dados no banco
        gravar_dados(arquivo_json, 'json')
        gravar_dados(arquivo_csv, 'csv')
        gravar_dados(arquivo_txt, 'txt')

        print("Processo ETL finalizado. Aguardando 1 minuto...")
        sleep(60)

if __name__ == "__main__":
    main()
