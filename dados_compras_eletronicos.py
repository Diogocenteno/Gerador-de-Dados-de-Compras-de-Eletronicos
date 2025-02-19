#%%

import pandas as pd
import random
from faker import Faker
from datetime import datetime

# Gerador de dados fictícios
fake = Faker()

# Lista de produtos eletrônicos ampliada para 100 itens
produtos_eletronicos = [
    "Smartphone", "Laptop", "Tablet", "Câmera Digital", "Fone de Ouvido", "Relógio Inteligente", "Monitor",
    "Teclado", "Mouse", "Smart TV", "Console de Video Game", "Caixa de Som Bluetooth", "Drone", "Projetor",
    "Notebook", "Carregador Portátil", "Console de Jogos", "Processador", "Placa de Vídeo", "Cabo HDMI",
    "Home Theater", "Smartwatch", "Fone de Ouvido Bluetooth", "Roteador Wi-Fi", "Impressora", "Leitor de Cartão",
    "Flash Drive", "Caixa de Som", "E-reader", "Projetor Portátil", "Microfone", "Lente para Câmera",
    "Câmera de Segurança", "Hub USB", "Monitor Curvo", "Sistema de Som", "Placa de Captura", "Mouse Gamer",
    "Teclado Mecânico", "Mousepad Grande", "Fones Over-Ear", "Scanner 3D", "Microfone Lavalier", "Câmera Web 4K",
    "Assinatura Cloud Storage", "Adaptador USB-C", "Placa de Som Externa", "Chave de Rede", "Amplificador de Sinal",
    "Carregador Solar", "Smart Glasses", "Controlador de Jogo", "Fone de Ouvido ANC", "Torre de Som",
    "Câmera Instantânea", "Calculadora Científica", "Notebook Gamer", "Console Portátil", "Soundbar",
    "SSD Externo", "HD Externo", "Switch HDMI", "Cabo USB-C", "Tablet Gráfico", "Leitor de Blu-ray",
    "Carregador sem Fio", "Headset VR", "Placa Mãe", "Gabinete Gamer", "Memória RAM", "Estabilizador de Energia",
    "Nobreak", "Dock Station", "Painel Solar Portátil", "Projetor 4K", "Microfone USB", "Controle Remoto Universal",
    "Monitor Ultrawide", "Extensor de Wi-Fi", "Teclado Bluetooth", "Mouse Sem Fio", "Repetidor de Sinal Wi-Fi",
    "Luminária LED Inteligente", "Relógio Despertador Inteligente", "Webcam Full HD", "Câmera de Ação",
    "Sensor de Movimento", "Interruptor Inteligente", "Central de Automação", "Placa de Rede Wi-Fi",
    "Fone de Ouvido Profissional", "Caixa de Som Inteligente", "Smart Speaker", "HDMI Switcher", "Placa de Video Externa"
]

# Dicionário atualizado para incluir 40 países com estados e cidades
estados_cidades = {
    "United States": {"California": ["Los Angeles", "San Francisco", "San Diego"]},
    "Brazil": {"São Paulo": ["São Paulo", "Campinas", "Santos"]},
    "Canada": {"Ontario": ["Toronto", "Ottawa", "Hamilton"]},
    "Mexico": {"CDMX": ["Mexico City", "Coyoacán", "Xochimilco"]},
    "Argentina": {"Buenos Aires": ["Buenos Aires", "La Plata", "Mar del Plata"]},
    "Chile": {"Santiago": ["Santiago", "Las Condes", "Providencia"]},
    "Colombia": {"Cundinamarca": ["Bogotá", "Chía", "Zipaquirá"]},
    "Germany": {"Bavaria": ["Munich", "Nuremberg", "Augsburg"]},
    "France": {"Île-de-France": ["Paris", "Versailles", "Boulogne"]},
    "Spain": {"Madrid": ["Madrid", "Getafe", "Alcalá"]},
    "Italy": {"Lazio": ["Rome", "Tivoli", "Frosinone"]},
    "United Kingdom": {"England": ["London", "Manchester", "Birmingham"]},
    "Australia": {"New South Wales": ["Sydney", "Newcastle", "Wollongong"]},
    "Japan": {"Tokyo": ["Tokyo", "Shibuya", "Shinjuku"]},
    "South Korea": {"Seoul": ["Seoul", "Incheon", "Suwon"]},
    "India": {"Maharashtra": ["Mumbai", "Pune", "Nagpur"]},
    "Russia": {"Moscow": ["Moscow", "Podolsk", "Khimki"]},
    "Turkey": {"Istanbul": ["Istanbul", "Kadıköy", "Üsküdar"]},
    "Egypt": {"Cairo": ["Cairo", "Giza", "Helwan"]}
}

# Gerando os dados
num_linhas = 50000
dados = []
for i in range(num_linhas):
    id_cliente = i + 1
    nome_completo = fake.name()
    id_produto = random.randint(1000, 9999)
    nome_produto = random.choice(produtos_eletronicos)
    data_compra = fake.date_between_dates(date_start=datetime(2020, 1, 1), date_end=datetime(2024, 12, 31))
    preco = round(random.uniform(10, 1000), 2)
    pais_compra = random.choice(list(estados_cidades.keys()))
    estado_compra = random.choice(list(estados_cidades[pais_compra].keys()))
    cidade_compra = random.choice(estados_cidades[pais_compra][estado_compra])
    
    dados.append([
        id_cliente, nome_completo, id_produto, nome_produto, data_compra.strftime("%d/%m/%Y"),
        f"R$ {preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        pais_compra, estado_compra, cidade_compra
    ])

# Criando o DataFrame
df = pd.DataFrame(dados, columns=[
    'ID do Cliente', 'Nome Completo do Cliente', 'ID do Produto', 'Nome do Produto', 'Data da Compra',
    'Preço', 'País da Compra', 'Estado da Compra', 'Cidade da Compra'
])

# Salvando o arquivo Excel
df.to_excel("dados_compras_eletronicos.xlsx", index=False)
print("Planilha gerada com sucesso!")
