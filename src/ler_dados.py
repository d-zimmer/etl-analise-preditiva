import json
import csv
import pandas as pd

def ler_e_consolidar_dados(arquivo_json, arquivo_csv, arquivo_txt):
    dados_consolidados = []

    # Ler dados do JSON
    with open(arquivo_json, 'r') as f:
        dados_json = json.load(f)
        for registro in dados_json:
            dados_consolidados.append({
                'nome': registro['nome'],
                'email': registro.get('email', None),
                'telefone': registro.get('telefone', None),
                'salario': registro.get('salario', None),
                'endereco': None,
                'idade': None,
                'genero': None,
                'empresa': None
            })

    # Ler dados do CSV
    with open(arquivo_csv, 'r') as f:
        reader = csv.DictReader(f)
        for registro in reader:
            dados_consolidados.append({
                'nome': registro['nome'],
                'email': None,
                'telefone': None,
                'salario': None,
                'endereco': registro.get('endereco', None),
                'idade': registro.get('idade', None),
                'genero': None,
                'empresa': None
            })

    # Ler dados do TXT
    with open(arquivo_txt, 'r') as f:
        for linha in f:
            nome, empresa, genero = linha.strip().split(';')
            dados_consolidados.append({
                'nome': nome,
                'email': None,
                'telefone': None,
                'salario': None,
                'endereco': None,
                'idade': None,
                'genero': genero,
                'empresa': empresa
            })

    return dados_consolidados