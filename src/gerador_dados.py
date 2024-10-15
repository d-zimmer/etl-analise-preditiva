from faker import Faker
import json
import random

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
            'salario': random.choice([None, fake.random_number(digits=5, fix_len=True)]),  # Salário com valores ausentes
        }
        dados.append(pessoa)

    with open(arquivo_json, 'w') as f:
        json.dump(dados, f, indent=4)

def gerar_dados_csv(num_registros, arquivo_csv):
    fake = Faker()
    with open(arquivo_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        # Escreve o cabeçalho
        writer.writerow(['nome', 'endereco', 'idade'])

        for _ in range(num_registros):
            writer.writerow([fake.name(), fake.address(), random.randint(18, 80)])

def gerar_dados_txt(num_registros, arquivo_txt):
    fake = Faker()
    with open(arquivo_txt, 'w') as f:
        for _ in range(num_registros):
            f.write(f"{fake.name()};{fake.company()};{random.choice(['M', 'F'])}\n")