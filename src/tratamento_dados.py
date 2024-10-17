import pandas as pd
import re

def tratar_dados_json(df):
    # Exemplo: Converter salário para decimal
    df['salario'] = pd.to_numeric(df['salario'], errors='coerce').fillna(0).astype('float64')
    
    df['telefone'] = df['telefone'].apply(padronizar_telefone)
    return df

def tratar_dados_csv(df):
    # Exemplo: Converter preços para decimal e quantidade para inteiro
    df['preco'] = pd.to_numeric(df['preco'], errors='coerce').fillna(0).astype('float64')
    df['quantidade_em_estoque'] = pd.to_numeric(df['quantidade_em_estoque'], errors='coerce').fillna(0).astype('int')
    return df

def tratar_dados_txt(df):
    # Exemplo: Converter valores para decimal
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce').fillna(0).astype('float64')
    return df

def padronizar_telefone(numero):
    # Remove caracteres não numéricos
    numero = re.sub(r'\D', '', numero)
    
    # Verifica se o número tem o tamanho esperado
    if len(numero) == 11:  # Formato: DDD + Número
        return f"({numero[:2]}) {numero[2:7]}-{numero[7:]}"
    elif len(numero) == 10:  # Formato sem o 9 extra
        return f"({numero[:2]}) {numero[2:6]}-{numero[6:]}"
    else:
        return numero
