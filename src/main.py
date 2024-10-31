import os
import random
from time import sleep
from gerador_dados import gerar_dados_promocao, gerar_dados_vendas, gerar_dados_clientes, gerar_dados_filial, gerar_dados_produto
from gravar_dados import gravar_dados

def main():
    diretorio_dados = 'data'
    os.makedirs(diretorio_dados, exist_ok=True)

    while True:
        print("Iniciando processo ETL...")

        # Definir arquivos para cada tabela
        arquivo_json_promocao = os.path.join(diretorio_dados, 'promocoes.json')
        arquivo_csv_vendas = os.path.join(diretorio_dados, 'vendas.csv')
        arquivo_txt_clientes = os.path.join(diretorio_dados, 'clientes.txt')
        arquivo_csv_filial = os.path.join(diretorio_dados, 'filiais.csv')
        arquivo_json_produto = os.path.join(diretorio_dados, 'produtos.json')

        # Gerar dados para cada tabela
        gerar_dados_promocao(random.randint(1, 150), arquivo_json_promocao)
        gerar_dados_vendas(random.randint(1, 150), arquivo_csv_vendas)
        gerar_dados_clientes(random.randint(1, 150), arquivo_txt_clientes)
        gerar_dados_filial(random.randint(1, 50), arquivo_csv_filial)
        gerar_dados_produto(random.randint(1, 100), arquivo_json_produto)

        # Inserir dados no banco de dados
        gravar_dados(arquivo_json_promocao, 'json', 'tabela_promocao')
        gravar_dados(arquivo_csv_vendas, 'csv', 'tabela_vendas')
        gravar_dados(arquivo_txt_clientes, 'txt', 'tabela_clientes')
        gravar_dados(arquivo_csv_filial, 'csv', 'tabela_filial')
        gravar_dados(arquivo_json_produto, 'json', 'tabela_produto')

        print("Processo ETL finalizado. Aguardando 1 minuto...")
        sleep(60)

if __name__ == "__main__":
    main()
