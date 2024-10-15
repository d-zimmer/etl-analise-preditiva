from pymongo import MongoClient

def carregar_no_mongodb(dados, uri, db_name, collection_name):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(dados)
    print(f"{len(dados)} registros inseridos no MongoDB.")