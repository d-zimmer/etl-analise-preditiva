import pandas as pd
import re

# Tratar dados de JSON (ex. Promoções e Produtos)
def tratar_dados_json(df):
    if 'salario' in df.columns:
        df['salario'] = pd.to_numeric(df['salario'], errors='coerce').fillna(0).astype('float64')
    if 'telefone' in df.columns:
        df['telefone'] = df['telefone'].apply(padronizar_telefone)
    if 'qt_desconto_promocao' in df.columns:
        df['qt_desconto_promocao'] = pd.to_numeric(df['qt_desconto_promocao'], errors='coerce')
    if 'vl_preco' in df.columns:
        df['vl_preco'] = pd.to_numeric(df['vl_preco'], errors='coerce').fillna(0).astype('float64')
    return df

# Tratar dados de CSV (ex. Vendas e Filiais)
def tratar_dados_csv(df):
    if 'preco' in df.columns:
        df['preco'] = pd.to_numeric(df['preco'], errors='coerce').fillna(0).astype('float64')
    if 'quantidade_em_estoque' in df.columns:
        df['quantidade_em_estoque'] = pd.to_numeric(df['quantidade_em_estoque'], errors='coerce').fillna(0).astype('int')
    if 'vl_total' in df.columns:
        df['vl_total'] = pd.to_numeric(df['vl_total'], errors='coerce').fillna(0).astype('float64')
    return df

# Tratar dados de TXT (ex. Clientes)
def tratar_dados_txt(df):
    if 'valor' in df.columns:
        df['valor'] = pd.to_numeric(df['valor'], errors='coerce').fillna(0).astype('float64')
    if 'nr_idade' in df.columns:
        df['nr_idade'] = pd.to_numeric(df['nr_idade'], errors='coerce').fillna(0).astype('int')
    return df

# Padronizar o número de telefone
def padronizar_telefone(numero):
    numero = re.sub(r'\D', '', numero)
    if len(numero) == 11:
        return f"({numero[:2]}) {numero[2:7]}-{numero[7:]}"
    elif len(numero) == 10:
        return f"({numero[:2]}) {numero[2:6]}-{numero[6:]}"
    return numero
