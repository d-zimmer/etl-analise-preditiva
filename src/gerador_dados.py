import json
import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta

fake = Faker()

# Função para gerar dados de Promoções
def gerar_dados_promocao(num_registros, arquivo_json):
    promocoes = []
    for _ in range(num_registros):
        id_promocao = fake.uuid4()
        de_promocao = fake.catch_phrase()
        dt_inicio_promocao = fake.date_between(start_date='-1y', end_date='today')
        dt_fim_promocao = dt_inicio_promocao + timedelta(days=random.randint(1, 60))
        qt_desconto_promocao = random.randint(5, 50)
        id_regiao_promocao = random.choice(['Norte', 'Nordeste', 'Centro-Oeste', 'Sul', 'Sudeste'])

        promocoes.append({
            'id_promocao': id_promocao,
            'de_promocao': de_promocao,
            'dt_inicio_promocao': dt_inicio_promocao,
            'dt_fim_promocao': dt_fim_promocao,
            'qt_desconto_promocao': qt_desconto_promocao,
            'id_regiao_promocao': id_regiao_promocao
        })

    df = pd.DataFrame(promocoes)
    df.to_json(arquivo_json, orient='records', lines=True)
    print(f"Arquivo JSON '{arquivo_json}' gerado com sucesso.")

# Função para gerar dados de Vendas
def gerar_dados_vendas(num_registros, arquivo_csv):
    vendas = []
    for _ in range(num_registros):
        cd_venda = fake.uuid4()
        cd_cliente = fake.uuid4()
        cd_filial = fake.uuid4()
        cd_produto = fake.uuid4()
        dt_movimento = fake.date_this_year()
        id_promocao = fake.uuid4() if random.choice([True, False]) else None
        vl_total = round(random.uniform(20, 500), 2)

        vendas.append({
            'cd_venda': cd_venda,
            'cd_cliente': cd_cliente,
            'cd_filial': cd_filial,
            'cd_produto': cd_produto,
            'dt_movimento': dt_movimento,
            'id_promocao': id_promocao,
            'vl_total': vl_total
        })

    df = pd.DataFrame(vendas)
    df.to_csv(arquivo_csv, index=False)
    print(f"Arquivo CSV '{arquivo_csv}' gerado com sucesso.")

# Função para gerar dados de Clientes
def gerar_dados_clientes(num_registros, arquivo_txt):
    clientes = []
    for _ in range(num_registros):
        cd_cliente = fake.uuid4()
        nm_cliente = fake.name()
        nr_idade = random.randint(18, 80)

        clientes.append({
            'cd_cliente': cd_cliente,
            'nm_cliente': nm_cliente,
            'nr_idade': nr_idade
        })

    df = pd.DataFrame(clientes)
    df.to_csv(arquivo_txt, index=False, sep=';')
    print(f"Arquivo TXT '{arquivo_txt}' gerado com sucesso.")

# Função para gerar dados de Filiais
def gerar_dados_filial(num_registros, arquivo_csv):
    filiais = []
    for _ in range(num_registros):
        cd_filial = fake.uuid4()
        de_filial = fake.company()
        de_endereco = fake.address()
        id_regiao = random.choice(['Norte', 'Nordeste', 'Centro-Oeste', 'Sul', 'Sudeste'])

        filiais.append({
            'cd_filial': cd_filial,
            'de_filial': de_filial,
            'de_endereco': de_endereco,
            'id_regiao': id_regiao
        })

    df = pd.DataFrame(filiais)
    df.to_csv(arquivo_csv, index=False)
    print(f"Arquivo CSV '{arquivo_csv}' gerado com sucesso.")

# Função para gerar dados de Produtos
def gerar_dados_produto(num_registros, arquivo_json):
    produtos = []
    for _ in range(num_registros):
        cd_produto = fake.uuid4()
        de_produto = fake.word().capitalize()
        vl_preco = round(random.uniform(10, 1000), 2)

        produtos.append({
            'cd_produto': cd_produto,
            'de_produto': de_produto,
            'vl_preco': vl_preco
        })

    df = pd.DataFrame(produtos)
    df.to_json(arquivo_json, orient='records', lines=True)
    print(f"Arquivo JSON '{arquivo_json}' gerado com sucesso.")
