import random
import uuid
import os
from datetime import datetime, timedelta

# Gerar dados para Paises (expandido)
paises = [
    ("Brasil", "BR"),
    ("Estados Unidos", "US"),
    ("França", "FR"),
    ("Japão", "JP"),
    ("Canadá", "CA"),
    ("Alemanha", "DE"),
    ("Argentina", "AR"),
    ("Austrália", "AU"),
    ("Índia", "IN"),
    ("Reino Unido", "UK")
]

# Gerar dados para Estados (expandido)
estados = {
    "BR": [("São Paulo", "SP"), ("Rio de Janeiro", "RJ"), ("Bahia", "BA"), ("Minas Gerais", "MG"), ("Paraná", "PR")],
    "US": [("California", "CA"), ("Texas", "TX"), ("Florida", "FL"), ("New York", "NY"), ("Illinois", "IL")],
    "FR": [("Île-de-France", "IDF"), ("Provence", "PACA"), ("Normandie", "NOR"), ("Bretagne", "BRE"), ("Aquitaine", "AQU")],
    "JP": [("Tóquio", "TK"), ("Osaka", "OS"), ("Hokkaido", "HK"), ("Fukuoka", "FK"), ("Kyoto", "KYO")],
    "CA": [("Ontário", "ON"), ("Quebec", "QC"), ("Colúmbia Britânica", "BC"), ("Alberta", "AB"), ("Manitoba", "MB")],
    "DE": [("Baviera", "BY"), ("Berlim", "BE"), ("Hamburgo", "HH"), ("Saxônia", "SN"), ("Hesse", "HE")],
    "AR": [("Buenos Aires", "BA"), ("Córdoba", "CB"), ("Santa Fe", "SF"), ("Mendoza", "MZ"), ("Salta", "SA")],
    "AU": [("Nova Gales do Sul", "NSW"), ("Victoria", "VIC"), ("Queensland", "QLD"), ("Austrália Ocidental", "WA"), ("Tasmânia", "TAS")],
    "IN": [("Maharashtra", "MH"), ("Tamil Nadu", "TN"), ("Karnataka", "KA"), ("Gujarat", "GJ"), ("Punjab", "PB")],
    "UK": [("Inglaterra", "ENG"), ("Escócia", "SCO"), ("País de Gales", "WLS"), ("Irlanda do Norte", "NIR"), ("Londres", "LDN")]
}

# Listas para inserts SQL
insert_paises = []
insert_estados = []
insert_voos = []
insert_passagens = []

# IDs auxiliares
estado_id_counter = 1
voo_id_counter = 1
passagem_id_counter = 1
voo_ids = []

# Inserção de países
for i, (nome, codigo) in enumerate(paises, start=1):
    insert_paises.append(f"INSERT INTO Paises (Nome, Codigo) VALUES ('{nome}', '{codigo}');")
    for nome_estado, uf in estados[codigo]:
        insert_estados.append(
            f"INSERT INTO Estados (PaisID, Nome, UF) VALUES ({i}, '{nome_estado}', '{uf}');")
        estado_id_counter += 1

# Simular 120 voos
for _ in range(120):
    origem = random.randint(1, estado_id_counter - 1)
    destino = random.randint(1, estado_id_counter - 1)
    while destino == origem:
        destino = random.randint(1, estado_id_counter - 1)
    partida = datetime(2025, 4, 10) + timedelta(days=random.randint(1, 90))
    chegada = partida + timedelta(hours=random.randint(2, 15))
    capacidade = random.randint(120, 280)
    codigo = str(uuid.uuid4())
    insert_voos.append(
        f"INSERT INTO Voos (Codigo, OrigemID, DestinoID, DataPartida, DataChegada, Capacidade) "
        f"VALUES ('{codigo}', {origem}, {destino}, '{partida}', '{chegada}', {capacidade});"
    )
    voo_ids.append(voo_id_counter)
    voo_id_counter += 1

# Simular 350 passagens distribuídas nos voos
for _ in range(350):
    voo_id = random.choice(voo_ids)
    preco = random.randint(300, 7000)
    dias_antes = random.randint(1, 90)
    data_compra = datetime(2025, 4, 10) - timedelta(days=dias_antes)
    insert_passagens.append(
        f"INSERT INTO Passagens (VooID, DataCompra, PrecoPago) "
        f"VALUES ({voo_id}, '{data_compra}', {preco});"
    )
    passagem_id_counter += 1

# Mostrar exemplos

os.system('cls' if os.name == 'nt' else 'clear')
print(insert_paises)
print("\n\n")
input()
print(insert_estados)
print("\n\n")
input()
print(insert_voos)
print("\n\n")   
input()
print(insert_passagens)
