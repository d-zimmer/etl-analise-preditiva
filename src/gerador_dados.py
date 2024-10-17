import json
import random
from faker import Faker
import csv

def gerar_dados_json(num_registros, arquivo_json):
    fake = Faker()
    dados = []

    for _ in range(num_registros):
        pessoa = {
            'nome': fake.name(),
            'endereco': fake.address(),
            'email': fake.email(),
            'telefone': fake.phone_number(),
            'data_nascimento': fake.date_of_birth().isoformat(),
            'salario': random.choice([None, fake.random_number(digits=5, fix_len=True)])  # Salário com valores ausentes
        }
        dados.append(pessoa)

    # Abre e grava os dados no arquivo JSON
    with open(arquivo_json, 'w') as f:
        json.dump(dados, f, indent=4)

def gerar_dados_csv(num_registros, arquivo_csv):
    fake = Faker()

    with open(arquivo_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        # Escreve o cabeçalho
        writer.writerow(['produto', 'categoria', 'preco', 'quantidade_em_estoque'])

        for _ in range(num_registros):
            writer.writerow([
                fake.word(),  # Nome do produto
                random.choice(['Eletrônicos', 'Roupas', 'Alimentos', 'Livros', 'Móveis']),
                round(random.uniform(10, 1000), 2),  # Preço
                random.randint(1, 100)  # Quantidade em estoque
            ])

def gerar_dados_txt(num_registros, arquivo_txt):
    fake = Faker()

    with open(arquivo_txt, 'w') as f:
        for _ in range(num_registros):
            f.write(f"{fake.uuid4()};{fake.date_time_this_year()};{random.choice(['compra', 'venda', 'transferencia'])};"
                    f"{round(random.uniform(10, 5000), 2)};{random.choice(['concluido', 'pendente', 'falhado'])}\n")
