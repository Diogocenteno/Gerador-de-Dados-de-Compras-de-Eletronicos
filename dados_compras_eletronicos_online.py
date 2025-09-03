#%% dados_compras_eletronicos_online.py
# -*- coding: utf-8 -*-

import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import string
import locale
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog, Menu, Listbox
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledText, ScrolledFrame
import time
import threading

# --- Dados Iniciais e Configurações Globais (Constantes) ---

# Gerador de dados fictícios
FAKE_GENERATOR = Faker("pt_BR")

# Listas de dados pré-definidas
ENTREGADORES = [
    "Correios", "Jadlog", "Loggi", "Azul Cargo", "Total Express", "DHL Brasil",
    "FedEx Brasil", "Tegma", "Viamais", "Mercado Envios", "Mercado Livre",
    "DHL", "FedEx", "UPS", "Amazon Logistics", "USPS", "Royal Mail",
    "SF Express", "TNT Express", "Yamato Transport", "DPD"
]
CATEGORIAS = ["Corporativo", "Doméstico", "Industrial", "Educacional", "Entretenimento"]
FABRICANTES = [ "LG", "NVIDEA", "BRASTEMP", "Samsung", "Apple", "Sony", "HP", "Dell", "Xiaomi", "Huawei", 
    "Asus", "Acer", "Lenovo", "Microsoft", "Toshiba", "Panasonic", "Philips", "Intel", "AMD", 
    "Canon", "Epson", "Logitech", "Razer", "Motorola", "Nokia", "Google", "OnePlus", "OPPO", 
    "Vivo", "Realme", "Zebra", "Seagate", "Western Digital", "Kingston", "Corsair", "Gigabyte", 
    "MSI", "IBM", "Qualcomm", "Nintendo", "Siemens", "Bosch", "Whirlpool", "Electrolux", 
    "Haier", "Hitachi", "Sharp", "JBL", "Bose", "Sennheiser", "GoPro", "Fitbit", "Garmin",
    "AOC", "BenQ", "ViewSonic", "Thermaltake", "Cooler Master", "EVGA", "Arduino", "Raspberry Pi", 
    "BlackBerry", "Alcatel", "TCL", "HTC", "ASRock", "Biostar", "Fujitsu", " NEC", "Kyocera", 
    "Lexmark", "Brother", "Pioneer", "Yamaha", "Denon", "Marantz", "Onkyo", "Klipsch", "HyperX", 
    "SteelSeries", "Redragon", "Ducky", "Akko", "Anker", "Belkin", "TP-Link", "Netgear", 
    "D-Link", "Synology", "QNAP", "Western Digital", "SanDisk", "Crucial", "Patriot", "ADATA", 
    "PNY", "Zotac", "Sapphire", "PowerColor", "XFX", "InWin", "Lian Li", "Fractal Design", 
    "NZXT", "Phanteks", "SilverStone", "Deepcool", "Noctua", "Be Quiet!", "Arctic", "EKWB", 
    "CableMod", "Elgato", "Blue Microphones", "Shure", "Audio-Technica", "AKG", "Focal", 
    "KEF", "Bang & Olufsen", "Sonos", "Harman Kardon", "Marshall", "Devialet", "Dyson", 
    "iRobot", "Shark", "Rowenta", "Tefal", "Miele", "KitchenAid", "GE Appliances", "Frigidaire", 
    "Maytag", "LG Chem", "CATL", "Panasonic Energy", "Tesla", "BYD", "Rivian", "Lucid Motors", 
    "NIO", "XPeng", "Faraday Future", "Roku", "Amazon Basics", "Ubiquiti", "Ring", "Blink", 
    "Wyze", "Eufy", "Arlo", "SimpliSafe", "August", "Nest", "Ecobee", "Honeywell", "Schlage", 
    "Yale", "Kwikset", "Ring", "Blink", "Wyze", "Eufy", "Arlo", "SimpliSafe", "August", 
    "Nest", "Ecobee", "Honeywell", "Schlage", "Yale" ]
COMISSOES = ["5%", "8%", "10%", "12%", "15%", "18%"]
DOMINIOS_EMAIL = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "icloud.com", "aol.com", "zoho.com", "org.br"]
LOJAS = [
    "Magazine Luiza", "Lojas Americanas", "Ponto Frio", "Casas Bahia", "Submarino", 
    "Carrefour", "Extra", "Fast Shop", "Havan", "Mercado Livre", 
    "Walmart", "Amazon", "Apple Store", "Samsung Store", "Sony Store", 
    "LG Store", "Microsoft Store", "Dell Store", "HP Store", 
    "Acer Store", "Xiaomi Store", "Huawei Store", "Motorola", "Nokia", 
    "Best Buy", "Carrefour Brasil", "Walmart Brasil", 
    "AliExpress", "Target", "Urban Outfitters", "Macy's", 
    "Bershka", "Stradivarius", "Pull&Bear", "Nike Store", "Adidas Store", 
    "Puma", "Under Armour", "New Balance", "Asics", "Reebok", 
    "Foot Locker", "Champion", "Vans", "Converse", "Dr. Martens", 
    "Sapatella", "Dafiti", "Zattini", "Netshoes", "Kanui", 
    "ShoeStock", "Sephora Brasil", "Boticário", "Avon", "Jequiti", 
    "L'Occitane en Provence", "The Body Shop", "Nyx", "Maybelline", "MAC Cosmetics", 
    "Sally Hansen", "Revlon", "Estée Lauder", "Clinique", "Lancôme", 
    "Charlotte Tilbury", "Riachuelo Online", "C&A Online", "Renner Online", "Marisa Online", 
    "Fast Shop Online", "Americanas Online", "Magazine Luiza Online", "Carrefour Online", 
    "Extra Online", "Submarino Online", "Mercado Livre Online", "AliExpress Brasil", "Wish", 
    "Zara Online", "H&M Online", "Forever 21 Online", "Uniqlo", "Urban Outfitters Online", 
    "Amazon Fashion", "Lojas Centauro Online", "Centauro Brasil", "Decathlon", "Leroy Merlin Online", 
    "Casa&Video", "Tok&Stok Online", "Lojas Renner Online", "Loja do Mecânico", "Tenda Online", 
    "Ponto Frio Online", "Ricardo Eletro Online", "Extra Online", "Walmart Online", "Target Online", 
    "Best Buy Online", "GameStop Online", "Apple Online Store", "Samsung Store", "Sony Store", 
    "LG Store", "Microsoft Store", "Lenovo", "Dell Store", "HP Store", 
    "Acer Store", "Xiaomi Store", "Huawei Store", "Motorola", "Nokia", 
    "Sears", "Kohl's", "Nordstrom", "Macy's Online", "J.C. Penney", 
    "Bloomingdale's", "Neiman Marcus", "Saks Fifth Avenue", "Barneys New York", "Burlington Coat Factory", 
    "TJ Maxx", "Ross Dress for Less", "Kirkland's", "Bed Bath & Beyond", "The Home Depot", 
    "Lowe's", "IKEA", "Costco", "Sam's Club", "BJ's Wholesale Club", 
    "Lidl", "Aldi", "Trader Joe's", "Whole Foods Market Online", "Sprouts Farmers Market", 
    "Fresh Market", "Earth Fare", "Harris Teeter", "Safeway", "Albertsons", 
    "Publix", "Wegmans", "Stop & Shop", "Food Lion", "ShopRite", 
    "Giant Food", "Food4Less", "Ralphs", "Vons", "Pavilions", 
    "Albertsons Companies", "FreshDirect", "Peapod", "Instacart", "Shipt",
    "AliExpress", "B&H Photo Video", "Newegg", "Adorama", "Fry's Electronics", 
    "Micro Center", "PC Componentes", "Gearbest", "Banggood", "Rakuten", 
    "Overstock", "Kogan", "Currys", "Maplin", "PC World", 
    "John Lewis", "Darty", "Euronics", "MediaMarkt", "Conforama", 
    "Saturn", "Cdiscount", "FNAC", "Carrefour Electronics", "Fnac Darty", 
    "Kaufland", "Real", "Toys'R'Us", "Gadget Flow", "Woot", 
    "Best Buy Canada", "Pyramid Computer", "Snapdeal", "Flipkart", "Vishal Megamart", 
    "Sears Canada", "The Source", "Lenovo Official Store", "Microsoft Store Online", 
    "Razer Store", "CyberPowerPC", "Alienware", "iBuyPower", "Tigerdirect", 
    "Ebuyer", "Walmart Canada", "Costco Electronics", "LaptopsDirect", 
    "Lazada", "Gearbest Electronics", "Jumia", "ShopClues", "Slickdeals", 
    "TigerDirect", "Walmart International", "Sainsbury's", "Argos", "HomeDepot Canada", "ASOS", "Boohoo", "PrettyLittleThing", "Missguided", "Romwe", "Zalando", "Sandro", "Maje", "The Kooples", "Reiss",
    "Ted Baker", "Jigsaw", "Whistles", "Levi's", "Wrangler", "Lee", "TOMMY Jeans", "Gant", "Fred Perry", "Benetton",
    "Pepe Jeans", "Aritzia", "Anthropologie", "Free People", "Revolve", "Boscov's", "Old Navy", "Gap", "Marks & Spencer", "Debenhams",
    "House of Fraser", "Next", "River Island", "Topshop", "The Outnet", "MyTheresa", "Net-a-Porter", "Farfetch", "Matches Fashion",
    "Saks OFF 5th", "Harrods", "Selfridges", "Fortnum & Mason", "TK Maxx", "Costco UK", "B&Q", "Dunelm", "Argos", "IKEA",
    "Homebase", "Currys PC World", "Lidl UK", "Aldi UK", "Matalan", "Kmart Australia", "Big W", "Harvey Norman", "The Good Guys",
    "Officeworks", "Peters of Kensington", "Sportsgirl", "Supre", "Sussan", "Witchery", "Petbarn", "Chemist Warehouse", "Priceline Pharmacy",
    "FoodWorks", "Harris Farm Markets", "Lincraft", "Autobarn", "Supercheap Auto", "Repco", "The Reject Shop", "Fantastic Furniture",
    "Mattress Firm", "Wayfair", "Pier 1", "Crate & Barrel", "Pottery Barn", "Williams-Sonoma", "Sur La Table", "World Market",
    "West Elm", "CB2", "Z Gallerie", "HomeGoods", "Bed Bath & Beyond", "Target Home", "Costco Home", "IKEA Home", "Ace Hardware",
    "RONA", "Cabela's", "Bass Pro Shops", "L.L. Bean", "Patagonia", "Columbia Sportswear", "Arc'teryx", "Mountain Hardwear",
    "Marmot", "REI", "Dick's Sporting Goods", "Academy Sports + Outdoors", "Hoka One One", "Saucony", "Brooks Running",
    "Fila", "Converse", "Vans", "Dr. Martens", "Skechers", "Crocs", "Birkenstock", "Steve Madden", "Nine West",
    "Jessica Simpson", "Schutz", "Tory Burch", "Marc Jacobs", "Saint Laurent", "Balenciaga", "Versace", "Fendi",
    "Celine", "Burberry", "Moncler", "Tiffany & Co.", "Cartier" ]
PRODUTOS_ELETRONICOS = [
"Leitor de Cartão SD", "Drone com Câmera", "Projetor 3D", "Placa de Vídeo para PC", "Sensor de Pressão Arterial",
"Receptor Bluetooth", "Smartphone Dobrável", "Câmera 360 graus", "Mini Projetor", "Óculos de Realidade Aumentada",
"Impressora 3D", "Tablet Android", "Câmera de Vigilância IP", "Placa de Som para PC", "Escova de Dentes Elétrica",
"Carregador Rápido", "Aparelho de DVD", "Assinatura de Streaming de Música", "Caixa de Som Resistente à Água",
"Home Cinema", "Controlador de Console", "Teclado de Violinista", "Câmera de Segurança Wireless", "Microfone de Estúdio",
"Ventilador USB", "Carregador de Celular Wireless", "Interruptor de Luz Inteligente", "Termômetro Digital",
"Processador Intel", "Câmera de Reverso para Carro", "Balança Digital Inteligente", "Luminária LED", "Roteador Mesh",
"Carregador de Carro", "Relógio Inteligente Infantil", "Chuveiro Inteligente", "Câmera Digital Profissional",
"Rádio Digital", "Power Bank Solar", "Detector de Fumaça Inteligente", "Câmera de Ação 4K", "Câmera de Segurança Sem Fio",
"Caixa de Som com Subwoofer", "Ar Condicionado Inteligente", "Drone com Controle Remoto", "Aparelho de Som Portátil",
"Smartphone 5G", "Controle de Acesso Digital", "Smartphone com Tela Curva", "Computador All-in-One", "Monitor com Tela OLED",
"Batedeira Elétrica Inteligente", "Dínamo Portátil", "Monitor 4K Ultra HD", "Tablet Infantil", "Sistema de Som Surround",
"Airfryer Digital", "Compressor de Ar Digital", "Câmera de Segurança 4K", "Óculos de Realidade Virtual",
"Óculos de Sol com Bluetooth", "Teclado sem Fio", "Fone de Ouvido com Cancelamento de Ruído", "Máquina de Cortar Cabelo Elétrica",
"Lixeira Inteligente", "Barra de Som", "Console de Vídeo Game Retrô", "Ventilador Inteligente", "Alarme Inteligente",
"Relógio de Pulso Inteligente", "Impressora 3D de Resina", "Máquina de Café Inteligente", "Aparelho de Jogo Portátil",
"Teclado Multifuncional", "Roteador 5G", "Assinatura de Streaming de Vídeos", "Smartphone com Câmera de Alta Resolução",
"Luz de Mesa LED", "Aquecedor Inteligente", "Câmera de Segurança para Bebês", "Carregador Rápido para iPhone",
"Painel Solar para Carro", "Controle de Temperatura Inteligente", "Sistema de Som Bluetooth", "Microfone Sem Fio",
"Alto-Falante de Carro", "Caixa de Som com Rádio FM", "Smartwatch Esportivo", "Teclado Retroiluminado",
"Câmera de Vigilância em Nuvem", "Carregador Rápido para Notebook", "Projetor de Tela Grande", "Antena Digital",
"Air Purifier Inteligente", "Fone de Ouvido Gaming", "Sistema de Automação Residencial", "Espelho Inteligente",
"Leitor de Impressão Digital", "Aquecedor de Água Inteligente", "Fone de Ouvido com Microfone", "Roteador 4G",
"Câmera de Segurança com Inteligência Artificial", "Fone de Ouvido Fitness", "Relógio Despertador com Projeção",
"Lâmpada Inteligente", "Som Portátil Bluetooth", "Teclado Compacto", "Rádio Bluetooth", "Mini Câmera Espiã",
"Máscara de Realidade Virtual", "Carregador de Celular Solar", "Luminária Inteligente", "Alarme de Portão Inteligente",
"Controle de Temperatura para Sala", "Sistema de Som de Alta Definição", "Compressor de Ar Inteligente", "Câmera de Segurança Sem Fio 4K",
"Tomada Inteligente", "Microfone de Podcaster", "Câmera de Segurança para Escritório", "Kit de Vídeo Conferência",
"Powerbank Inteligente", "Chaveiro Localizador Bluetooth", "Despertador Inteligente com Luz", "Carregador de Bateria de Carro",
"Balança Digital com Bluetooth", "Monitor com Tela Curva 32", "Alarme para Casa", "Placa de Expansão USB", 
"Escova de Cabelo Inteligente", "Controle Remoto Bluetooth", "Amplificador de Som Portátil", "Secador de Cabelo Inteligente",
"Aquecedor de Ambiente Inteligente", "Leitor de Código de Barras", "Cartão de Memória de Alta Velocidade", "Carregador de Bateria Sem Fio",
"Aspirador de Pó Inteligente", "Placa de Captura de Vídeo", "Carregador Turbo para Android", "Estabilizador para Câmera",
"Lâmpada LED RGB Inteligente", "Fechadura Digital com Biometria", "Controle Remoto Universal Wi-Fi", "Mouse Gamer RGB",
"Switch HDMI 4K", "Console de Jogos Portátil Retrô", "Smartwatch com Monitor Cardíaco", "Termostato Inteligente",
"Projetor Portátil HD", "Chaleira Elétrica Inteligente", "Gravador de Voz Digital", "Monitor Ultrawide",
"Roteador com VPN Integrada", "Fritadeira Sem Óleo Inteligente", "Hub USB-C Multiporta", "Luminária de Mesa Dobrável",
"Cortina Inteligente com Wi-Fi", "Mochila com Carregador USB", "Carregador de Pilhas Inteligente", "Scanner de Documentos Portátil",
"Teclado Mecânico Bluetooth", "Controle de Som Ambiente", "Suporte de Celular com Carregador Wireless", "Headset VR para PC",
"Caixa de Som Inteligente com Assistente Virtual", "Detector de Monóxido de Carbono Inteligente", "TV 8K OLED",
"Carregador Magnético para Smartwatch", "Câmera para Streaming com 4K", "Câmera Térmica Portátil", "Sensor de Movimento Inteligente",
"Impressora de Fotos Instantânea", "Projetor Laser 4K", "Chave Inteligente NFC", "Gravador de Chamadas Bluetooth",
"Monitor Gamer com 240Hz", "Purificador de Água Inteligente", "Cortador de Cabelo a Vácuo", "Bomba de Ar Elétrica",
"Microfone Lapela Wireless", "Adaptador de Rede USB-C", "Caixa de Som com Iluminação RGB", "Smart TV 120Hz",
"Ventilador de Torre Inteligente", "Torneira Digital com Temperatura", "Carregador de Carro com Display LED",
"Câmera de Vigilância Solar", "Relógio Inteligente para Idosos", "Projetor Holográfico", "Gravador de Vídeo para Carro",
"Teclado Dobrável Bluetooth", "Balança de Cozinha Digital", "Adaptador HDMI para Celular", "Placa Mãe Gamer",
"Power Bank com Display Digital", "Impressora Multifuncional Wi-Fi", "Câmera de Vídeo Conferência 1080p",
"Fone de Ouvido com Assistente de Voz", "Garrafa Térmica Inteligente", "Placa de Áudio Externa", "Suporte para Notebook com Cooler",
"Luminária de Chão Inteligente", "Carregador de Parede com Múltiplas Saídas", "Aparelho de Medição de Glicose Bluetooth",
"Campainha Inteligente com Câmera", "Detector de Gás Inteligente", "Papel Fotográfico para Impressora Portátil",
"Controle de Iluminação RGB", "Bicicleta Elétrica com Bluetooth", "Câmera Instantânea Digital", "Gravador de Áudio USB",
"Smart Ring (Anel Inteligente)", "Mochila com Energia Solar", "Fone de Ouvido de Condução Óssea", "Adaptador de Tomada Universal",
"Relógio Solar Inteligente", "Drone Subaquático", "Placa de Vídeo Externa para Notebook", "Console de Jogos em Nuvem","Fone de Ouvido Sem Fio", "Microfone de Estúdio Profissional", "Balança Digital de Cozinha", "Chaveiro Inteligente com Localizador", "Máquina de Massagem Portátil", "Detector de Radiação UV", "Óculos de Sol com Câmera", "Câmera com Visão Noturna", "Luminária LED com Carregador", "Carregador Rápido USB-C","Smartphone com Tela dobrável", "Balança de Precisão Digital", "Câmera de Ação com Wi-Fi", "Aspirador de Pó Vertical", "Monitor 144Hz", "Teclado Ergonomico", "Relógio com GPS Integrado", "Carregador Solar para Smartphone", "Amplificador de Sinal Wi-Fi", "Notebook 2 em 1","Carro Elétrico Infantil", "Câmera de Segurança com Detecção de Movimento", "Espelho com Iluminação LED", "Telefone Sem Fio Bluetooth", "Mouse Wireless para Gamer", "Tablet com Tela Retina", "Câmera com Zoom Óptico", "Controle Remoto para TV Inteligente", "Lâmpada de Emergência Inteligente", "Ventilador com Ionizador","Smartwatch com Monitor de Pressão Arterial", "Receptor de Áudio Bluetooth", "Impressora Compacta", "Placa de Expansão de Som", "Headset com Microfone para PC", "Rádio Inteligente com Bluetooth", "Carregador Rápido para Carro", "Câmera de Vigilância 1080p", "Máscara Facial com LED", "Fritadeira Sem Óleo Portátil","Power Bank para Notebook", "Assinatura de Streaming de Vídeos", "Óculos de Realidade Virtual 3D", "Leitor de Cartões MicroSD", "Chave Digital de Segurança", "Câmera de Vídeo Profissional", "Lâmpada de Mesa com Carregador Wireless", "Drone de Corrida", "Bateria Externa para Celular", "Fone de Ouvido In-ear",
"Placa de Captura para Transmissão ao Vivo", "Smartphone com Tela AMOLED", "Carregador Automático para Bateria", "Impressora Fotográfica Portátil", "Mouse Gamer com Botões Programáveis", "Roteador Wi-Fi 6", "Kit de Iluminação para Vídeos", "Câmera com Tripé Integrado", "Projetor de Cinema Pessoal", "Carregador sem Fio para AirPods",
"Relógio Inteligente com Monitoramento de Sono", "Controle de Console para PC", "Monitor Full HD Curvo", "Fone de Ouvido com Bluetooth", "Alarme de Fumaça Inteligente", "Espelho de Maquiagem com Iluminação LED", "Câmera de Vídeo 360 graus", "Câmera de Carro com Visão 360", "Câmera PTZ para Escritório", "Tablet com Teclado Removível",
"Power Bank com Carregamento Solar", "Roteador Mesh Wi-Fi", "Suporte para Celular para Carro", "Fone de Ouvido para Exercícios", "Câmera Instantânea com Filme", "Filtro de Ar Inteligente", "Câmera de Segurança com Áudio", "Secador de Cabelo Profissional", "Câmera para Monitoramento de Bebê", "Máquina de Café Espresso",
"Teclado Bluetooth para Tablet", "Projetor de Slides", "Monitor Touchscreen", "Barra de Som com Bluetooth", "Controlador de Jogo para Smartphone", "Smartphone Dual SIM", "Relógio Digital com Função de Alarme", "Máquina de Cortar Cabelo sem Fio", "Fritadeira a Ar", "Câmera de Segurança com Alerta de Movimento",
"Carregador USB de Parede", "Máscara de Proteção com Filtro", "Ventilador com Controle Remoto", "Placa de Captura HDMI", "Carregador Solar Portátil", "Smartwatch com Funções Esportivas", "Microfone para YouTube", "Câmera de Reverso sem Fio", "Sensor de Temperatura e Umidade", "Gravador de Vídeos Full HD",
"Teclado e Mouse sem Fio", "Drone para Iniciantes", "Impressora Térmica Portátil", "Kit de Vídeo Conferência com Webcam", "Balança de Peso Corporal", "Alarme de Segurança para Casa", "Câmera de Códigos QR", "Sensor de Movimento para Casa", "Fone de Ouvido Bluetooth com Microfone", "Carregador Rápido com Display",
"Power Bank para Celular e Notebook", "Roteador Wi-Fi Inteligente", "Suporte de Mesa para Tablet", "Câmera para Captura de Vídeos Profissionais", "Kit de Iluminação LED para Estúdio", "Monitor com Suporte Articulado", "Receptor Bluetooth de Áudio", "Ventilador Portátil com Bateria", "Espelho com Tela LCD", "Placa de Vídeo com Ray Tracing",
"Projetor com Conexão Sem Fio", "Carregador com Entrada USB-C", "Fone de Ouvido com Bluetooth 5.0", "Tablet com Conectividade 4G", "Câmera de Segurança 4K com Wi-Fi", "Chave de Carro Inteligente", "Teclado Mecânico com RGB", "Mouse Óptico Gamer", "Câmera de Ação Resistente à Água", "Fone de Ouvido Bluetooth Para Corrida",
"Controle Remoto para Equipamentos Inteligentes", "Placa Mãe para PC Gamer", "Controle de TV com Comando de Voz", "Fone de Ouvido para Jogo", "Suporte para Notebook com Ajuste de Altura", "Carregador de Bateria Inteligente", "Câmera de Segurança com Reconhecimento Facial", "Gravador de Áudio Digital", "Fone de Ouvido com Controle de Volume",
"Drone com Controle Remoto Profissional", "Projetor para Apresentações", "Lâmpada de Mesa com Carregador USB", "Telefone Celular com 5G", "Microfone Condensador para Estúdio", "Carregador de Smartphone com Qi", "Câmera de Vigilância com Gravação em Nuvem", "Mochila Inteligente com Painel Solar", "Câmera com Estabilização de Imagem",
"Kit de Som para Streaming", "Headset Gaming com Microfone", "Carregador de Parede com 4 Portas USB", "Tablet com 128GB de Memória", "Lâmpada RGB com Controle Remoto", "Fone de Ouvido com Cancelamento de Ruído Ativo", "Receptor de TV Digital", "Câmera para Monitoramento de Casa", "Placa de Expansão de Rede", "Impressora Fotográfica para Smartphone",
"Hub USB para Notebook", "Fone de Ouvido Over-Ear", "Carregador com Função de Bateria Externa", "Relógio Inteligente com Notificações", "Fone de Ouvido com Fio para PC", "Carregador de Carro Sem Fio", "Dispositivo de Áudio para PC", "Câmera Instantânea de Filme", "Gravador de Som Digital", "Teclado com Teclas Mecânicas",
"Dispositivo de Streaming de Vídeos", "Câmera para Videochamadas", "Mouse Sem Fio Ergonômico", "Câmera de Segurança 1080p", "Smartphone com Câmera 48MP", "Aparelho de Áudio Portátil", "Monitor LED 4K", "Fone de Ouvido com Tecnologia NFC", "Impressora Térmica de Etiquetas", "Carregador Wireless para iPhone",
"Controle de Iluminação RGB para TV", "Gravador de Áudio Portátil", "Câmera de Segurança com Zoom Digital", "Ventilador USB", "Placa de Som Externa para PC", "Roteador Wi-Fi com Alta Velocidade", "Smartwatch com GPS", "Câmera de Segurança com Detecção de Som", "Drone com Câmera 4K", "Carregador de Carro com Qi",
"Dispositivo de Áudio para Celular", "Placa de Áudio USB para PC", "Fone de Ouvido para Vídeo Conferência", "Smartwatch com Monitoramento de Saúde", "Câmera de Reverso para Carro com Visão Noturna", "Câmera de Vigilância com Alerta de Intrusão", "Fone de Ouvido com Som 3D", "Câmera de Ação à Prova d'Água", "Sistema de Som em Miniatura", "Impressora a Laser Multifuncional"
]

# Listas de personalização que podem ser modificadas pelo usuário
VENDEDORES_PERSONALIZADOS = []
CLIENTES_PERSONALIZADOS = []

# Dicionário com estados e cidades para cada país (pode ser expandido pelo usuário)
ESTADOS_CIDADES = {
    "Brazil": {
    "Acre": ["Rio Branco", "Cruzeiro do Sul", "Sena Madureira", "Tarauacá", "Feijó", "Brasiléia", "Plácido de Castro", "Epitaciolândia", "Xapuri", "Mâncio Lima", "Capixaba", "Rodrigues Alves", "Marechal Thaumaturgo", "Porto Acre", "Assis Brasil", "Santa Rosa do Purus", "Jordão", "Porto Walter", "Manoel Urbano", "Bujari", "Acrelândia", "Senador Guiomard"],
    "Alagoas": ["Maceió", "Arapiraca", "Rio Largo", "Palmeira dos Índios", "União dos Palmares", "Penedo", "São Miguel dos Campos", "Santana do Ipanema", "Coruripe", "Delmiro Gouveia", "Campo Alegre", "Teotônio Vilela", "São Luís do Quitunde", "Atalaia", "Maragogi", "Murici", "Pilar", "São Sebastião", "Viçosa", "Mata Grande"],
    "Amapá": ["Macapá", "Santana", "Laranjal do Jari", "Oiapoque", "Porto Grande", "Mazagão", "Tartarugalzinho", "Pedra Branca do Amapari", "Vitória do Jari", "Calçoene", "Amapá", "Ferreira Gomes", "Cutias", "Itaubal", "Pracuúba", "Serra do Navio", "Porto Santana", "Tartarugal", "Laranjal do Jari", "Pedra Branca do Amapari"],
    "Amazonas": ["Manaus", "Parintins", "Itacoatiara", "Manacapuru", "Coari", "Tefé", "Maués", "Tabatinga", "Humaitá", "São Gabriel da Cachoeira", "Iranduba", "Manicoré", "Borba", "Benjamin Constant", "Eirunepé", "Carauari", "Novo Airão", "Autazes", "Careiro", "Nhamundá"],
    "Bahia": ["Salvador", "Feira de Santana", "Vitória da Conquista", "Camaçari", "Ilhéus", "Itabuna", "Juazeiro", "Lauro de Freitas", "Barreiras", "Porto Seguro", "Alagoinhas", "Teixeira de Freitas", "Eunápolis", "Paulo Afonso", "Santo Antônio de Jesus", "Valença", "Candeias", "Guanambi", "Brumado", "Jequié"],
    "Ceará": ["Fortaleza", "Caucaia", "Juazeiro do Norte", "Maracanaú", "Sobral", "Crato", "Itapipoca", "Maranguape", "Iguatu", "Quixadá", "Pacatuba", "Cascavel", "Horizonte", "Aquiraz", "Russas", "Limoeiro do Norte", "Aracati", "Canindé", "Icó", "Barbalha"],
    "Distrito Federal": ["Brasília", "Ceilândia", "Taguatinga", "Samambaia", "Gama", "Planaltina", "Sobradinho", "Santa Maria", "São Sebastião", "Paranoá", "Recanto das Emas", "Lago Sul", "Guará", "Núcleo Bandeirante", "Cruzeiro", "Riacho Fundo", "Águas Claras", "Sudoeste/Octogonal", "Varjão", "Jardim Botânico"],
    "Espírito Santo": ["Vitória", "Vila Velha", "Cariacica", "Serra", "Linhares", "Cachoeiro de Itapemirim", "Colatina", "Guarapari", "Aracruz", "São Mateus", "Viana", "Nova Venécia", "Barra de São Francisco", "Santa Maria de Jetibá", "Domingos Martins", "Marataízes", "Afonso Cláudio", "Itapemirim", "Conceição da Barra", "Jaguaré"],
    "Goiás": ["Goiânia", "Aparecida de Goiânia", "Anápolis", "Rio Verde", "Luziânia", "Águas Lindas de Goiás", "Valparaíso de Goiás", "Trindade", "Formosa", "Jataí", "Senador Canedo", "Catalão", "Itumbiara", "Novo Gama", "Santo Antônio do Descoberto", "Caldas Novas", "Rio Verde", "Mineiros", "Morrinhos", "Itaberaí"],
    "Maranhão": ["São Luís", "Imperatriz", "Timon", "Caxias", "Codó", "São José de Ribamar", "Paço do Lumiar", "Açailândia", "Bacabal", "Santa Inês", "Barra do Corda", "Pinheiro", "Chapadinha", "Buriticupu", "Grajaú", "Itapecuru Mirim", "Zé Doca", "Coroatá", "Tutóia", "Viana"],
    "Mato Grosso": ["Cuiabá", "Várzea Grande", "Rondonópolis", "Sinop", "Tangará da Serra", "Cáceres", "Sorriso", "Lucas do Rio Verde", "Primavera do Leste", "Barra do Garças", "Alta Floresta", "Juína", "Campo Verde", "Pontes e Lacerda", "Mirassol d'Oeste", "Nova Mutum", "Peixoto de Azevedo", "Poconé", "Campo Novo do Parecis", "Comodoro"],
    "Mato Grosso do Sul": ["Campo Grande", "Dourados", "Três Lagoas", "Corumbá", "Ponta Porã", "Naviraí", "Nova Andradina", "Aquidauana", "Sidrolândia", "Paranaíba", "Maracaju", "Rio Brilhante", "Caarapó", "Coxim", "Amambai", "Jardim", "Bataguassu", "São Gabriel do Oeste", "Fátima do Sul", "Iguatemi"],
    "Minas Gerais": ["Belo Horizonte", "Contagem", "Juiz de Fora", "Uberlândia", "Betim", "Montes Claros", "Ribeirão das Neves", "Uberaba", "Governador Valadares", "Ipatinga", "Divinópolis", "Sete Lagoas", "Poços de Caldas", "Patos de Minas", "Teófilo Otoni", "Pouso Alegre", "Barbacena", "Sabará", "Varginha", "Conselheiro Lafaiete"],
    "Pará": ["Belém", "Ananindeua", "Santarém", "Marabá", "Castanhal", "Parauapebas", "Abaetetuba", "Itaituba", "Cametá", "Bragança", "Altamira", "Tucuruí", "Barcarena", "Redenção", "Tailândia", "São Félix do Xingu", "Breves", "Moju", "Capanema", "Mãe do Rio"],
    "Paraíba": ["João Pessoa", "Campina Grande", "Santa Rita", "Patos", "Bayeux", "Sousa", "Cajazeiras", "Guarabira", "Cabedelo", "Sapé", "Mamanguape", "Monteiro", "Catolé do Rocha", "Esperança", "Pombal", "Solânea", "Areia", "Alagoa Grande", "Itabaiana", "Conde"],
    "Paraná": ["Curitiba", "Londrina", "Maringá", "Ponta Grossa", "Cascavel", "Foz do Iguaçu", "Colombo", "São José dos Pinhais", "Guarapuava", "Paranaguá", "Arapongas", "Apucarana", "Campo Largo", "Araucária", "Pinhais", "Toledo", "Cambé", "Umuarama", "Francisco Beltrão", "Pato Branco"],
    "Pernambuco": ["Recife", "Jaboatão dos Guararapes", "Olinda", "Caruaru", "Petrolina", "Paulista", "Cabo de Santo Agostinho", "Garanhuns", "Vitória de Santo Antão", "Igarassu", "Camaragibe", "São Lourenço da Mata", "Abreu e Lima", "Santa Cruz do Capibaribe", "Serra Talhada", "Gravatá", "Carpina", "Belo Jardim", "Goiana", "Arcoverde"],
    "Piauí": ["Teresina", "Parnaíba", "Picos", "Piripiri", "Floriano", "Campo Maior", "Barras", "Altos", "Esperantina", "União", "José de Freitas", "Oeiras", "Miguel Alves", "São Raimundo Nonato", "Uruçuí", "Corrente", "Valença do Piauí", "Pedro II", "Luís Correia", "Angical do Piauí"],
    "Rio de Janeiro": ["Rio de Janeiro", "Niterói", "Duque de Caxias", "São Gonçalo", "Belford Roxo", "Nova Iguaçu", "Campos dos Goytacazes", "Petrópolis", "Volta Redonda", "Magé", "Itaboraí", "São João de Meriti", "Macaé", "Mesquita", "Queimados", "Cabo Frio", "Angra dos Reis", "Barra Mansa", "Nova Friburgo", "Teresópolis"],
    "Rio Grande do Norte": ["Natal", "Mossoró", "Parnamirim", "São Gonçalo do Amarante", "Macaíba", "Ceará-Mirim", "Caicó", "Açu", "Currais Novos", "Santa Cruz", "João Câmara", "Apodi", "Pau dos Ferros", "São Miguel", "Touros", "Nova Cruz", "Areia Branca", "Canguaretama", "Macaíba", "Monte Alegre"],
    "Rio Grande do Sul": ["Porto Alegre", "Caxias do Sul", "Pelotas", "Canoas", "Santa Maria", "Gravataí", "Novo Hamburgo", "São Leopoldo", "Rio Grande", "Passo Fundo", "Uruguaiana", "Bagé", "Bento Gonçalves", "Erechim", "Sapucaia do Sul", "Guaíba", "Cachoeirinha", "Santana do Livramento", "Esteio", "Alegrete"],
    "Rondônia": ["Porto Velho", "Ji-Paraná", "Ariquemes", "Vilhena", "Cacoal", "Rolim de Moura", "Guajará-Mirim", "Jaru", "Ouro Preto do Oeste", "Pimenta Bueno", "Presidente Médici", "Buritis", "Machadinho d'Oeste", "Nova Mamoré", "Alta Floresta d'Oeste", "Candeias do Jamari", "Espigão d'Oeste", "São Miguel do Guaporé", "Colorado do Oeste", "Cerejeiras"],
    "Roraima": ["Boa Vista", "Rorainópolis", "Caracaraí", "Alto Alegre", "Mucajaí", "Cantá", "Pacaraima", "Bonfim", "Normandia", "São Luiz", "Amajari", "Iracema", "Uiramutã", "Caroebe", "São João da Baliza", "Cristalândia do Piauí", "Manoel Emídio", "Avelino Lopes", "Landri Sales", "Pio IX"],
    "Santa Catarina": ["Florianópolis", "Joinville", "Blumenau", "São José", "Criciúma", "Chapecó", "Itajaí", "Lages", "Jaraguá do Sul", "Palhoça", "Balneário Camboriú", "Brusque", "Tubarão", "Camboriú", "São Bento do Sul", "Caçador", "Navegantes", "Concórdia", "Rio do Sul", "Araranguá"],
    "São Paulo": ["São Paulo", "Campinas", "Santos", "Sorocaba", "Ribeirão Preto", "São Bernardo do Campo", "Osasco", "São José dos Campos", "Mauá", "Mogi das Cruzes", "Diadema", "Carapicuíba", "Piracicaba", "Bauru", "Itaquaquecetuba", "São Vicente", "Franca", "Praia Grande", "Guarujá", "Taubaté"],
    "Sergipe": ["Aracaju", "Nossa Senhora do Socorro", "Lagarto", "Itabaiana", "São Cristóvão", "Estância", "Tobias Barreto", "Itaporanga d'Ajuda", "Simão Dias", "Nossa Senhora da Glória", "Capela", "Poço Redondo", "Propriá", "Nossa Senhora das Dores", "Poço Verde", "Boquim", "Canindé de São Francisco", "Riachão do Dantas", "Salgado", "Japaratuba"],
    "Tocantins": ["Palmas", "Araguaína", "Gurupi", "Porto Nacional", "Paraíso do Tocantins", "Colinas do Tocantins", "Guaraí", "Dianópolis", "Formoso do Araguaia", "Miracema do Tocantins", "Augustinópolis", "Taguatinga", "Xambioá", "Wanderlândia", "Gurupi", "Pedro Afonso", "Lagoa da Confusão", "Brejinho de Nazaré", "Araguatins", "Buriti do Tocantins"]
    
  },
"United States": {
  "California": ["Los Angeles", "San Francisco", "San Diego", "Sacramento", "Fresno", "Oakland", "San Jose", "Long Beach", "Santa Ana", "Anaheim"],
  "Texas": ["Houston", "Dallas", "Austin", "San Antonio", "Fort Worth", "El Paso", "Arlington", "Corpus Christi", "Plano", "Laredo"],
  "Florida": ["Miami", "Orlando", "Tampa", "Jacksonville", "Fort Lauderdale", "St. Petersburg", "Port St. Lucie", "Cape Coral", "Hialeah", "Tallahassee"],
  "New York": ["New York", "Buffalo", "Rochester", "Syracuse", "Albany", "Yonkers", "New Rochelle", "Mount Vernon", "Schenectady", "Utica"],
  "Illinois": ["Chicago", "Aurora", "Naperville", "Joliet", "Rockford", "Elgin", "Peoria", "Springfield", "Champaign", "Bloomington"],
  "Arizona": ["Phoenix", "Tucson", "Mesa", "Chandler", "Glendale", "Scottsdale", "Gilbert", "Tempe", "Peoria", "Surprise"],
  "Ohio": ["Columbus", "Cleveland", "Cincinnati", "Toledo", "Akron", "Dayton", "Parma", "Canton", "Youngstown", "Lorain"],
  "Georgia": ["Atlanta", "Augusta", "Columbus", "Savannah", "Athens", "Sandy Springs", "Macon", "Roswell", "Albany", "Johns Creek"],
  "Pennsylvania": ["Philadelphia", "Pittsburgh", "Allentown", "Erie", "Reading", "Scranton", "Bethlehem", "Lancaster", "Harrisburg", "Altoona"],
  "Washington": ["Seattle", "Spokane", "Tacoma", "Vancouver", "Bellevue", "Everett", "Kent", "Yakima", "Renton", "Federal Way"]
},
"Japan": {
  "Tokyo": ["Tokyo", "Shibuya", "Shinjuku", "Chiyoda", "Minato", "Taito", "Shinagawa", "Meguro", "Ota", "Setagaya"],
  "Osaka": ["Osaka", "Sakai", "Higashiosaka", "Yao", "Suita", "Neyagawa", "Toyonaka", "Ibaraki", "Hirakata", "Takatsuki"],
  "Kyoto": ["Kyoto", "Uji", "Kameoka", "Muko", "Nagaokakyo", "Yawata", "Fushimi", "Nishikyō", "Yamashina", "Kameoka"],
  "Hokkaido": ["Sapporo", "Hakodate", "Asahikawa", "Kushiro", "Obihiro", "Tomakomai", "Ebetsu", "Kitami", "Iwamizawa", "Abashiri"],
  "Okinawa": ["Naha", "Okinawa", "Uruma", "Urasoe", "Ginowan", "Ishigaki", "Urasoe", "Nago", "Itoman", "Tomigusuku"],
  "Aichi": ["Nagoya", "Toyota", "Okazaki", "Ichinomiya", "Seto", "Kasugai", "Anjo", "Kariya", "Toyohashi", "Komaki"],
  "Kanagawa": ["Yokohama", "Kawasaki", "Sagamihara", "Yokosuka", "Fujisawa", "Hiratsuka", "Chigasaki", "Atsugi", "Yamato", "Ebina"],
  "Fukuoka": ["Fukuoka", "Kitakyushu", "Kurume", "Omuta", "Iizuka", "Kasuya", "Nogata", "Tagawa", "Yanagawa", "Yame"],
  "Hyogo": ["Kobe", "Himeji", "Nishinomiya", "Amagasaki", "Akashi", "Kakogawa", "Takarazuka", "Itami", "Sanda", "Ashiya"],
  "Saitama": ["Saitama", "Kawaguchi", "Koshigaya", "Kawagoe", "Tokorozawa", "Hanyu", "Ageo", "Sayama", "Asaka", "Wako"]
},
"France": {
  "Île-de-France": ["Paris", "Boulogne-Billancourt", "Saint-Denis", "Versailles", "Créteil", "Nanterre", "Montreuil", "Argenteuil", "Colombes", "Aubervilliers"],
  "Provence-Alpes-Côte d'Azur": ["Marseille", "Nice", "Toulon", "Aix-en-Provence", "Avignon", "Cannes", "Antibes", "La Seyne-sur-Mer", "Hyères", "Fréjus"],
  "Auvergne-Rhône-Alpes": ["Lyon", "Grenoble", "Saint-Étienne", "Villeurbanne", "Clermont-Ferrand", "Valence", "Annecy", "Chambéry", "Vénissieux", "Roanne"],
  "Occitanie": ["Toulouse", "Montpellier", "Nîmes", "Perpignan", "Béziers", "Montauban", "Narbonne", "Carcassonne", "Albi", "Castres"],
  "Nouvelle-Aquitaine": ["Bordeaux", "Limoges", "Poitiers", "Pau", "La Rochelle", "Mérignac", "Bayonne", "Pessac", "Talence", "Angoulême"],
  "Hauts-de-France": ["Lille", "Amiens", "Roubaix", "Tourcoing", "Dunkerque", "Calais", "Villeneuve-d'Ascq", "Valenciennes", "Boulogne-sur-Mer", "Arras"],
  "Grand Est": ["Strasbourg", "Reims", "Metz", "Nancy", "Mulhouse", "Colmar", "Troyes", "Charleville-Mézières", "Châlons-en-Champagne", "Épinal"],
  "Pays de la Loire": ["Nantes", "Angers", "Le Mans", "Saint-Nazaire", "La Roche-sur-Yon", "Cholet", "Laval", "Les Sables-d'Olonne", "Saumur", "Saint-Herblain"],
  "Bretagne": ["Rennes", "Brest", "Quimper", "Lorient", "Vannes", "Saint-Malo", "Saint-Brieuc", "Fougères", "Concarneau", "Morlaix"],
  "Normandie": ["Rouen", "Le Havre", "Caen", "Cherbourg-en-Cotentin", "Évreux", "Dieppe", "Saint-Étienne-du-Rouvray", "Sotteville-lès-Rouen", "Alençon", "Lisieux"]
},
"Germany": {
  "Berlin": ["Berlin", "Charlottenburg", "Kreuzberg", "Pankow", "Spandau", "Tempelhof", "Neukölln", "Lichtenberg", "Marzahn", "Reinickendorf"],
  "Bavaria": ["Munich", "Nuremberg", "Augsburg", "Regensburg", "Ingolstadt", "Würzburg", "Fürth", "Erlangen", "Bayreuth", "Bamberg"],
  "North Rhine-Westphalia": ["Cologne", "Düsseldorf", "Dortmund", "Essen", "Bonn", "Aachen", "Duisburg", "Bochum", "Wuppertal", "Bielefeld"],
  "Baden-Württemberg": ["Stuttgart", "Mannheim", "Karlsruhe", "Freiburg", "Heidelberg", "Ulm", "Heilbronn", "Pforzheim", "Reutlingen", "Tübingen"],
  "Hesse": ["Frankfurt", "Wiesbaden", "Darmstadt", "Kassel", "Offenbach", "Hanau", "Gießen", "Marburg", "Fulda", "Rüsselsheim"],
  "Saxony": ["Dresden", "Leipzig", "Chemnitz", "Zwickau", "Plauen", "Görlitz", "Freiberg", "Bautzen", "Pirna", "Radebeul"],
  "Lower Saxony": ["Hanover", "Braunschweig", "Osnabrück", "Oldenburg", "Wolfsburg", "Göttingen", "Salzgitter", "Hildesheim", "Delmenhorst", "Wilhelmshaven"],
  "Rhineland-Palatinate": ["Mainz", "Ludwigshafen", "Koblenz", "Trier", "Kaiserslautern", "Worms", "Neuwied", "Speyer", "Frankenthal", "Pirmasens"],
  "Schleswig-Holstein": ["Kiel", "Lübeck", "Flensburg", "Neumünster", "Norderstedt", "Elmshorn", "Pinneberg", "Itzehoe", "Wedel", "Ahrensburg"],
  "Saxony-Anhalt": ["Magdeburg", "Halle", "Dessau-Roßlau", "Wittenberg", "Halberstadt", "Stendal", "Bitterfeld-Wolfen", "Merseburg", "Bernburg", "Naumburg"]
},
"China": {
  "Beijing": ["Beijing", "Haidian", "Chaoyang", "Fengtai", "Shijingshan", "Tongzhou", "Changping", "Daxing", "Fangshan", "Mentougou"],
  "Shanghai": ["Shanghai", "Pudong", "Xuhui", "Changning", "Jing'an", "Putuo", "Hongkou", "Yangpu", "Minhang", "Baoshan"],
  "Guangdong": ["Guangzhou", "Shenzhen", "Dongguan", "Foshan", "Zhuhai", "Shantou", "Huizhou", "Zhongshan", "Jiangmen", "Zhaoqing"],
  "Zhejiang": ["Hangzhou", "Ningbo", "Wenzhou", "Shaoxing", "Huzhou", "Jiaxing", "Jinhua", "Quzhou", "Zhoushan", "Taizhou"],
  "Sichuan": ["Chengdu", "Mianyang", "Leshan", "Panzhihua", "Yibin", "Dazhou", "Nanchong", "Luzhou", "Suining", "Neijiang"],
  "Jiangsu": ["Nanjing", "Suzhou", "Wuxi", "Changzhou", "Zhenjiang", "Yangzhou", "Nantong", "Xuzhou", "Huai'an", "Yancheng"],
  "Shandong": ["Jinan", "Qingdao", "Yantai", "Weifang", "Zibo", "Tai'an", "Weihai", "Rizhao", "Linyi", "Dezhou"],
  "Fujian": ["Fuzhou", "Xiamen", "Quanzhou", "Zhangzhou", "Putian", "Nanping", "Longyan", "Sanming", "Ningde", "Fujian"],
  "Hunan": ["Changsha", "Zhuzhou", "Xiangtan", "Hengyang", "Yueyang", "Chenzhou", "Shaoyang", "Yiyang", "Loudi", "Zhangjiajie"],
  "Hubei": ["Wuhan", "Xiangyang", "Yichang", "Jingzhou", "Shiyan", "Huangshi", "Xiaogan", "Ezhou", "Jingmen", "Huanggang"]
},
"India": {
  "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Solapur", "Thane", "Pimpri-Chinchwad", "Kalyan-Dombivli", "Vasai-Virar"],
  "Delhi": ["New Delhi", "Delhi Cantonment", "Narela", "Sultanpur Majra", "Najafgarh", "Mehrauli", "Rohini", "Dwarka", "Pitampura", "Vasant Vihar"],
  "Karnataka": ["Bangalore", "Mysore", "Hubli", "Mangalore", "Belgaum", "Gulbarga", "Davanagere", "Bellary", "Shimoga", "Tumkur"],
  "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli", "Tiruppur", "Vellore", "Erode", "Thoothukudi"],
  "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Agra", "Allahabad", "Meerut", "Ghaziabad", "Noida", "Aligarh", "Moradabad"],
  "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar", "Junagadh", "Gandhinagar", "Anand", "Navsari"],
  "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Bikaner", "Ajmer", "Bhilwara", "Alwar", "Bharatpur", "Pali"],
  "West Bengal": ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri", "Malda", "Bardhaman", "Habra", "Kharagpur", "Shantipur"],
  "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Darbhanga", "Arrah", "Bihar Sharif", "Katihar", "Chapra", "Sasaram"],
  "Andhra Pradesh": ["Hyderabad", "Visakhapatnam", "Vijayawada", "Guntur", "Nellore", "Kurnool", "Rajahmundry", "Kakinada", "Tirupati", "Anantapur"]
},
"Russia": {
  "Moscow": ["Moscow", "Zelenograd", "Khimki", "Balashikha", "Lyubertsy", "Podolsk", "Mytishchi", "Korolyov", "Odintsovo", "Krasnogorsk"],
  "Saint Petersburg": ["Saint Petersburg", "Kolpino", "Pushkin", "Kronstadt", "Peterhof", "Sestroretsk", "Gatchina", "Vyborg", "Tosno", "Sosnovy Bor"],
  "Novosibirsk Oblast": ["Novosibirsk", "Berds", "Iskitim", "Kuybyshev", "Ob", "Toguchin", "Berdsk", "Karasuk", "Tatarsk", "Barabinsk"],
  "Sverdlovsk Oblast": ["Yekaterinburg", "Nizhny Tagil", "Kamensk-Uralsky", "Pervouralsk", "Serov", "Asbest", "Revda", "Polevskoy", "Krasnoturinsk", "Karpinsk"],
  "Krasnodar Krai": ["Krasnodar", "Sochi", "Novorossiysk", "Armavir", "Yeysk", "Kropotkin", "Slavyansk-na-Kubani", "Tikhoretsk", "Tuapse", "Labinsk"],
  "Tatarstan": ["Kazan", "Naberezhnye Chelny", "Nizhnekamsk", "Almetyevsk", "Zelenodolsk", "Bugulma", "Yelabuga", "Leninogorsk", "Chistopol", "Zainsk"],
  "Chelyabinsk Oblast": ["Chelyabinsk", "Magnitogorsk", "Zlatoust", "Miass", "Kopeysk", "Troitsk", "Snezhinsk", "Ozyorsk", "Satka", "Kartaly"],
  "Rostov Oblast": ["Rostov-on-Don", "Taganrog", "Shakhty", "Volgodonsk", "Novocherkassk", "Bataysk", "Novoshakhtinsk", "Kamensk-Shakhtinsky", "Azov", "Gukovo"],
  "Samara Oblast": ["Samara", "Tolyatti", "Syzran", "Novokuybyshevsk", "Chapayevsk", "Zhigulyovsk", "Oktyabrsk", "Neftegorsk", "Kinel", "Otradny"],
  "Bashkortostan": ["Ufa", "Sterlitamak", "Salavat", "Neftekamsk", "Oktyabrsky", "Beloretsk", "Ishimbay", "Kumertau", "Sibay", "Belebey"]
},
"Australia": {
  "New South Wales": ["Sydney", "Newcastle", "Wollongong", "Parramatta", "Penrith", "Liverpool", "Blacktown", "Campbelltown", "Albury", "Tamworth"],
  "Victoria": ["Melbourne", "Geelong", "Ballarat", "Bendigo", "Mildura", "Wodonga", "Shepparton", "Warrnambool", "Sunbury", "Traralgon"],
  "Queensland": ["Brisbane", "Gold Coast", "Sunshine Coast", "Townsville", "Cairns", "Toowoomba", "Mackay", "Rockhampton", "Bundaberg", "Hervey Bay"],
  "Western Australia": ["Perth", "Mandurah", "Bunbury", "Geraldton", "Kalgoorlie", "Albany", "Karratha", "Broome", "Port Hedland", "Busselton"],
  "South Australia": ["Adelaide", "Mount Gambier", "Whyalla", "Murray Bridge", "Port Lincoln", "Port Pirie", "Gawler", "Victor Harbor", "Roxby Downs", "Renmark"],
  "Tasmania": ["Hobart", "Launceston", "Devonport", "Burnie", "Ulverstone", "Sorell", "Kingston", "New Norfolk", "George Town", "Wynyard"],
  "Northern Territory": ["Darwin", "Alice Springs", "Palmerston", "Katherine", "Nhulunbuy", "Tennant Creek", "Wadeye", "Jabiru", "Yulara", "Borroloola"],
  "Australian Capital Territory": ["Canberra", "Belconnen", "Gungahlin", "Tuggeranong", "Woden", "Queanbeyan", "Yass", "Murrumbateman", "Bungendore", "Goulburn"],
  "Norfolk Island": ["Kingston", "Burnt Pine", "Cascade", "Anson Bay", "Ball Bay", "Headstone", "Middlegate", "Rocky Point", "Steeles Point", "Taylors Road"],
  "Christmas Island": ["Flying Fish Cove", "Poon Saan", "Silver City", "Drumsite", "South Point", "Waterfall", "Egeria Point", "Greta Beach", "West White Beach", "Dolly Beach"]
},
"Canada": {
  "Ontario": ["Toronto", "Ottawa", "Mississauga", "Brampton", "Hamilton", "London", "Markham", "Vaughan", "Kitchener", "Windsor"],
  "Quebec": ["Montreal", "Quebec City", "Laval", "Gatineau", "Longueuil", "Sherbrooke", "Saguenay", "Levis", "Trois-Rivières", "Terrebonne"],
  "British Columbia": ["Vancouver", "Surrey", "Burnaby", "Richmond", "Abbotsford", "Coquitlam", "Kelowna", "Langley", "Saanich", "Delta"],
  "Alberta": ["Calgary", "Edmonton", "Red Deer", "Lethbridge", "St. Albert", "Medicine Hat", "Grande Prairie", "Airdrie", "Spruce Grove", "Leduc"],
  "Manitoba": ["Winnipeg", "Brandon", "Steinbach", "Thompson", "Portage la Prairie", "Winkler", "Selkirk", "Morden", "Dauphin", "Flin Flon"],
  "Saskatchewan": ["Saskatoon", "Regina", "Prince Albert", "Moose Jaw", "Swift Current", "Yorkton", "North Battleford", "Estevan", "Weyburn", "Lloydminster"],
  "Nova Scotia": ["Halifax", "Sydney", "Dartmouth", "Truro", "New Glasgow", "Glace Bay", "Kentville", "Bridgewater", "Yarmouth", "Amherst"],
  "New Brunswick": ["Fredericton", "Saint John", "Moncton", "Dieppe", "Miramichi", "Edmundston", "Bathurst", "Campbellton", "Oromocto", "Shediac"],
  "Newfoundland and Labrador": ["St. John's", "Conception Bay South", "Mount Pearl", "Corner Brook", "Paradise", "Grand Falls-Windsor", "Gander", "Happy Valley-Goose Bay", "Labrador City", "Stephenville"],
  "Prince Edward Island": ["Charlottetown", "Summerside", "Stratford", "Cornwall", "Montague", "Kensington", "Souris", "Alberton", "Tignish", "Georgetown"]
},
"Mexico": {
  "Mexico City": ["Mexico City", "Iztapalapa", "Gustavo A. Madero", "Alvaro Obregon", "Coyoacan", "Cuauhtemoc", "Tlalpan", "Xochimilco", "Miguel Hidalgo", "Benito Juarez"],
  "Jalisco": ["Guadalajara", "Zapopan", "Tlaquepaque", "Tonala", "Tlajomulco de Zuniga", "Puerto Vallarta", "Lagos de Moreno", "Tepatitlan de Morelos", "Ocotlan", "Tequila"],
  "Nuevo León": ["Monterrey", "Guadalupe", "San Nicolas de los Garza", "Apodaca", "General Escobedo", "Santa Catarina", "San Pedro Garza Garcia", "Escobedo", "Garcia", "Juarez"],
  "Puebla": ["Puebla", "Tehuacan", "San Martin Texmelucan", "Heroica Puebla de Zaragoza", "Atlixco", "San Pedro Cholula", "Cholula", "Huauchinango", "Zacatlan", "San Andres Cholula"],
  "Veracruz": ["Veracruz", "Xalapa", "Coatzacoalcos", "Cordoba", "Poza Rica", "Minatitlan", "Orizaba", "Boca del Rio", "Tuxpan", "Martinez de la Torre"],
  "Baja California": ["Tijuana", "Mexicali", "Ensenada", "Rosarito", "Tecate", "Playas de Rosarito", "San Felipe", "La Paz", "Los Cabos", "San Jose del Cabo"],
  "Chihuahua": ["Chihuahua", "Juarez", "Cuauhtemoc", "Delicias", "Parral", "Camargo", "Nuevo Casas Grandes", "Jimenez", "Aldama", "Meoqui"],
  "Michoacán": ["Morelia", "Uruapan", "Zamora", "Lazaro Cardenas", "Apatzingan", "Zitacuaro", "La Piedad", "Sahuayo", "Hidalgo", "Patzcuaro"],
  "Guanajuato": ["Leon", "Guanajuato", "Irapuato", "Celaya", "Salamanca", "Silao", "San Miguel de Allende", "Dolores Hidalgo", "Acambaro", "San Francisco del Rincon"],
  "Yucatán": ["Merida", "Valladolid", "Progreso", "Tizimin", "Ticul", "Tekax", "Hunucma", "Oxkutzcab", "Izamal", "Motul"]
},
"Argentina": {
  "Buenos Aires": ["Buenos Aires", "La Plata", "Mar del Plata", "Quilmes", "Banfield", "Merlo", "Morón", "Avellaneda", "San Isidro", "Tigre"],
  "Córdoba": ["Córdoba", "Río Cuarto", "Villa María", "San Francisco", "Alta Gracia", "Villa Carlos Paz", "Río Tercero", "Bell Ville", "Jesús María", "Cosquín"],
  "Santa Fe": ["Rosario", "Santa Fe", "Rafaela", "Venado Tuerto", "Reconquista", "Santo Tomé", "Esperanza", "Villa Gobernador Gálvez", "San Lorenzo", "Funes"],
  "Mendoza": ["Mendoza", "San Rafael", "Godoy Cruz", "Guaymallén", "Las Heras", "Luján de Cuyo", "Maipú", "Rivadavia", "Tunuyán", "San Martín"],
  "Tucumán": ["San Miguel de Tucumán", "Yerba Buena", "Concepción", "Aguilares", "Banda del Río Salí", "Tafí Viejo", "Monteros", "Famaillá", "Lules", "Simoca"],
  "Salta": ["Salta", "San Ramón de la Nueva Orán", "Tartagal", "Cafayate", "Metán", "Rosario de la Frontera", "Cerrillos", "General Güemes", "Chicoana", "La Caldera"],
  "Entre Ríos": ["Paraná", "Concordia", "Gualeguaychú", "Concepción del Uruguay", "Gualeguay", "Victoria", "Villaguay", "Nogoyá", "Federación", "Colón"],
  "Chaco": ["Resistencia", "Barranqueras", "Presidencia Roque Sáenz Peña", "Villa Ángela", "Charata", "General San Martín", "Quitilipi", "Machagai", "Las Breñas", "Tres Isletas"],
  "Corrientes": ["Corrientes", "Goya", "Mercedes", "Curuzú Cuatiá", "Paso de los Libres", "Monte Caseros", "Esquina", "Santo Tomé", "Ituzaingó", "Bella Vista"],
  "Misiones": ["Posadas", "Oberá", "Eldorado", "Puerto Iguazú", "Apóstoles", "Leandro N. Alem", "San Vicente", "Jardín América", "Aristóbulo del Valle", "Puerto Rico"]
},
"United Kingdom": {
  "England": ["London", "Birmingham", "Manchester", "Liverpool", "Leeds", "Sheffield", "Bristol", "Nottingham", "Leicester", "Coventry"],
  "Scotland": ["Edinburgh", "Glasgow", "Aberdeen", "Dundee", "Inverness", "Perth", "Stirling", "Ayr", "Paisley", "Dunfermline"],
  "Wales": ["Cardiff", "Swansea", "Newport", "Bangor", "St Asaph", "St Davids", "Wrexham", "Barry", "Neath", "Cwmbran"],
  "Northern Ireland": ["Belfast", "Derry", "Lisburn", "Newry", "Bangor", "Ballymena", "Coleraine", "Newtownabbey", "Carrickfergus", "Craigavon"],
  "Greater London": ["London", "Croydon", "Bromley", "Ealing", "Hounslow", "Harrow", "Brent", "Barnet", "Enfield", "Redbridge"],
  "West Midlands": ["Birmingham", "Coventry", "Wolverhampton", "Solihull", "Walsall", "Dudley", "Sandwell", "Stourbridge", "Halesowen", "West Bromwich"],
  "Greater Manchester": ["Manchester", "Salford", "Bolton", "Stockport", "Oldham", "Rochdale", "Bury", "Wigan", "Trafford", "Tameside"],
  "West Yorkshire": ["Leeds", "Bradford", "Wakefield", "Huddersfield", "Halifax", "Keighley", "Dewsbury", "Batley", "Brighouse", "Pontefract"],
  "Merseyside": ["Liverpool", "Birkenhead", "St Helens", "Bootle", "Wallasey", "Southport", "Crosby", "Formby", "Huyton", "Kirkby"],
  "Tyne and Wear": ["Newcastle upon Tyne", "Sunderland", "Gateshead", "South Shields", "Jarrow", "Wallsend", "Tynemouth", "Whitley Bay", "Washington", "Hebburn"]
},
"Italy": {
  "Lazio": ["Rome", "Latina", "Fiumicino", "Tivoli", "Viterbo", "Civitavecchia", "Anzio", "Nettuno", "Rieti", "Frosinone"],
  "Lombardy": ["Milan", "Brescia", "Monza", "Bergamo", "Como", "Pavia", "Cremona", "Lecco", "Lodi", "Sondrio"],
  "Veneto": ["Venice", "Verona", "Padua", "Vicenza", "Treviso", "Rovigo", "Belluno", "Chioggia", "Bassano del Grappa", "Mira"],
  "Campania": ["Naples", "Salerno", "Caserta", "Torre del Greco", "Pozzuoli", "Giugliano in Campania", "Benevento", "Aversa", "Castellammare di Stabia", "Afragola"],
  "Sicily": ["Palermo", "Catania", "Messina", "Syracuse", "Trapani", "Marsala", "Gela", "Ragusa", "Agrigento", "Caltanissetta"],
  "Piedmont": ["Turin", "Novara", "Alessandria", "Asti", "Cuneo", "Biella", "Vercelli", "Verbania", "Casale Monferrato", "Chivasso"],
  "Emilia-Romagna": ["Bologna", "Modena", "Parma", "Reggio Emilia", "Ravenna", "Ferrara", "Rimini", "Forlì", "Piacenza", "Cesena"],
  "Tuscany": ["Florence", "Pisa", "Livorno", "Arezzo", "Prato", "Lucca", "Pistoia", "Grosseto", "Massa", "Carrara"],
  "Apulia": ["Bari", "Taranto", "Foggia", "Lecce", "Brindisi", "Andria", "Barletta", "Trani", "Altamura", "Molfetta"],
  "Calabria": ["Reggio Calabria", "Catanzaro", "Lamezia Terme", "Cosenza", "Crotone", "Vibo Valentia", "Corigliano-Rossano", "Locri", "Rende", "Amantea"]
},
"Spain": {
  "Madrid": ["Madrid", "Alcalá de Henares", "Getafe", "Leganés", "Alcorcón", "Móstoles", "Fuenlabrada", "Coslada", "Pozuelo de Alarcón", "Las Rozas"],
  "Catalonia": ["Barcelona", "L'Hospitalet de Llobregat", "Badalona", "Sabadell", "Terrassa", "Tarragona", "Lleida", "Mataró", "Santa Coloma de Gramenet", "Reus"],
  "Andalusia": ["Seville", "Malaga", "Cordoba", "Granada", "Jerez de la Frontera", "Almeria", "Huelva", "Cadiz", "Jaén", "Marbella"],
  "Valencia": ["Valencia", "Alicante", "Elche", "Castellón de la Plana", "Torrevieja", "Orihuela", "Benidorm", "Alcoy", "Elda", "Sagunto"],
  "Galicia": ["Vigo", "A Coruña", "Ourense", "Lugo", "Santiago de Compostela", "Pontevedra", "Ferrol", "Oleiros", "Carballo", "Ribeira"],
  "Basque Country": ["Bilbao", "Vitoria-Gasteiz", "San Sebastián", "Barakaldo", "Getxo", "Irun", "Portugalete", "Santurtzi", "Basauri", "Errenteria"],
  "Castile and León": ["Valladolid", "Burgos", "Salamanca", "León", "Palencia", "Zamora", "Ávila", "Segovia", "Soria", "Ponferrada"],
  "Castile-La Mancha": ["Toledo", "Albacete", "Guadalajara", "Ciudad Real", "Cuenca", "Talavera de la Reina", "Puertollano", "Alcázar de San Juan", "Tomelloso", "Hellín"],
  "Canary Islands": ["Las Palmas de Gran Canaria", "Santa Cruz de Tenerife", "San Cristóbal de La Laguna", "Telde", "Arona", "Santa Lucía de Tirajana", "Arrecife", "Puerto del Rosario", "Los Llanos de Aridane", "La Orotava"],
  "Balearic Islands": ["Palma de Mallorca", "Ibiza", "Manacor", "Mahón", "Ciutadella de Menorca", "Inca", "Llucmajor", "Calvià", "Alcúdia", "Santa Eulària des Riu"]
},
"South Africa": {
  "Gauteng": ["Johannesburg", "Pretoria", "Vereeniging", "Soweto", "Randburg", "Roodepoort", "Benoni", "Boksburg", "Brakpan", "Krugersdorp"],
  "Western Cape": ["Cape Town", "Stellenbosch", "Paarl", "Worcester", "George", "Knysna", "Mossel Bay", "Oudtshoorn", "Swellendam", "Hermanus"],
  "KwaZulu-Natal": ["Durban", "Pietermaritzburg", "Ulundi", "Richards Bay", "Newcastle", "Ladysmith", "Empangeni", "Ballito", "Margate", "Port Shepstone"],
  "Eastern Cape": ["Port Elizabeth", "East London", "Bhisho", "Mthatha", "Graaff-Reinet", "Queenstown", "Uitenhage", "Grahamstown", "Butterworth", "Aliwal North"],
  "Limpopo": ["Polokwane", "Thohoyandou", "Musina", "Phalaborwa", "Lephalale", "Mokopane", "Bela-Bela", "Modimolle", "Tzaneen", "Hoedspruit"],
  "Mpumalanga": ["Nelspruit", "Witbank", "Secunda", "Standerton", "Ermelo", "Piet Retief", "Malalane", "Barberton", "Hazyview", "White River"],
  "North West": ["Rustenburg", "Mahikeng", "Potchefstroom", "Klerksdorp", "Brits", "Vryburg", "Lichtenburg", "Zeerust", "Wolmaransstad", "Stilfontein"],
  "Free State": ["Bloemfontein", "Welkom", "Kroonstad", "Bethlehem", "Sasolburg", "Virginia", "Parys", "Phuthaditjhaba", "Harrismith", "QwaQwa"],
  "Northern Cape": ["Kimberley", "Upington", "Springbok", "De Aar", "Kuruman", "Postmasburg", "Colesberg", "Prieska", "Calvinia", "Port Nolloth"],
  "Western Transvaal": ["Klerksdorp", "Potchefstroom", "Rustenburg", "Lichtenburg", "Ventersdorp", "Wolmaransstad", "Orkney", "Stilfontein", "Hartbeesfontein", "Koster"]
},
"Nigeria": {
  "Lagos": ["Lagos", "Ikeja", "Surulere", "Apapa", "Mushin", "Agege", "Ikorodu", "Badagry", "Epe", "Ojo"],
  "Kano": ["Kano", "Fagge", "Dala", "Gwale", "Nasarawa", "Tarauni", "Kumbotso", "Ungogo", "Dawakin Tofa", "Bichi"],
  "Rivers": ["Port Harcourt", "Obio-Akpor", "Okrika", "Eleme", "Oyigbo", "Opobo", "Bonny", "Degema", "Ahoada", "Omoku"],
  "Oyo": ["Ibadan", "Ogbomosho", "Iseyin", "Oyo", "Saki", "Eruwa", "Igboho", "Kisi", "Igbeti", "Ibarapa"],
  "Enugu": ["Enugu", "Nsukka", "Agbani", "Awgu", "Udi", "Oji River", "Nkanu", "Ezeagu", "Igbo-Etiti", "Uzo-Uwani"],
  "Kaduna": ["Kaduna", "Zaria", "Kafanchan", "Soba", "Ikara", "Makarf", "Kachia", "Kajuru", "Jema'a", "Lere"],
  "Delta": ["Asaba", "Warri", "Sapele", "Ughelli", "Agbor", "Oghara", "Burutu", "Koko", "Ozoro", "Patani"],
  "Ogun": ["Abeokuta", "Sagamu", "Ijebu-Ode", "Ilaro", "Ifo", "Ota", "Ijebu-Igbo", "Aiyetoro", "Imeko", "Ipokia"],
  "Anambra": ["Awka", "Onitsha", "Nnewi", "Aguata", "Ihiala", "Nkpor", "Uli", "Ogidi", "Ekwulobia", "Umunze"],
  "Borno": ["Maiduguri", "Bama", "Gwoza", "Dikwa", "Biram", "Kukawa", "Monguno", "Askira", "Damboa", "Gubio"]
},
"Egypt": {
  "Cairo": ["Cairo", "Giza", "Shubra El-Kheima", "Helwan", "6th of October City", "Nasr City", "Maadi", "Zamalek", "Dokki", "New Cairo"],
  "Alexandria": ["Alexandria", "Borg El Arab", "Damanhur", "Kafr El Dawwar", "Rosetta", "Abu Qir", "El Montaza", "El Amreya", "El Agami", "El Gomrok"],
  "Giza": ["Giza", "6th of October City", "Sheikh Zayed City", "Al Hawamidiyah", "Al Badrashin", "Atfih", "Imbaba", "Bulaq", "El Haram", "El Warraq"],
  "Sharkia": ["Zagazig", "10th of Ramadan City", "Bilbeis", "Abu Hammad", "Minya Al Qamh", "Al Husayniyah", "Faqous", "Mashtool El Souk", "Kafr Saqr", "El Ibrahimiya"],
  "Luxor": ["Luxor", "Armant", "Esna", "Tiba", "Al Qarna", "Al Bayadiyah", "Al Karnak", "Al Tod", "Al Zayniya", "Al Qusair"],
  "Aswan": ["Aswan", "Kom Ombo", "Edfu", "Abu Simbel", "Daraw", "Kalabsha", "Nasr Al Nuba", "Al Khazan", "Al Radisia", "Al Shalal"],
  "Port Said": ["Port Said", "Port Fouad", "Al Arab", "Al Zohour", "Al Manakh", "Al Ganoub", "Al Sharq", "Al Dawahi", "Al Manasra", "Al Gharb"],
  "Suez": ["Suez", "Al Arbaeen", "Al Ganayen", "Al Sawa", "Faisal", "Al Adabiya", "Al Ataka", "Al Zaytoun", "Al Salam", "Al Ataqa"],
  "Ismailia": ["Ismailia", "Fayed", "Al Qantara", "Al Tal Al Kabir", "Al Qantara Gharb", "Al Qantara Sharq", "Al Salheya", "Al Kasaseen", "Al Abaseya", "Al Sawah"],
  "Red Sea": ["Hurghada", "Safaga", "El Gouna", "Marsa Alam", "Shalateen", "Ras Ghareb", "Al Quseir", "Abu Ramad", "Halayeb", "Sharm El Sheikh"]
},
"Kenya": {
  "Nairobi": ["Nairobi", "Eastleigh", "Kasarani", "Embakasi", "Dagoretti", "Karen", "Langata", "Westlands", "Ruiru", "Thika"],
  "Mombasa": ["Mombasa", "Likoni", "Kisauni", "Changamwe", "Nyali", "Mtwapa", "Bamburi", "Shanzu", "Mikindani", "Mariakani"],
  "Kisumu": ["Kisumu", "Maseno", "Ahero", "Muhoroni", "Kondele", "Kibos", "Dunga", "Nyalenda", "Manyatta", "Obunga"],
  "Nakuru": ["Nakuru", "Naivasha", "Molo", "Njoro", "Gilgil", "Rongai", "Bahati", "Subukia", "Mau Narok", "Elburgon"],
  "Eldoret": ["Eldoret", "Burnt Forest", "Kapsabet", "Iten", "Moiben", "Soy", "Kipkaren", "Cheptiret", "Kesses", "Ziwa"],
  "Machakos": ["Machakos", "Athi River", "Kathiani", "Kangundo", "Mwala", "Yatta", "Matungulu", "Masinga", "Mavoko", "Kalama"],
  "Kakamega": ["Kakamega", "Mumias", "Malava", "Butere", "Khwisero", "Shinyalu", "Lugari", "Likuyani", "Matungu", "Navakholo"],
  "Meru": ["Meru", "Maua", "Nkubu", "Mitunguu", "Kianjai", "Laare", "Muthara", "Kibirichia", "Gatimbi", "Kiegoi"],
  "Nyeri": ["Nyeri", "Karatina", "Othaya", "Mweiga", "Endarasha", "Chaka", "Mukurweini", "Kiganjo", "Gatitu", "Naro Moru"],
  "Kisii": ["Kisii", "Ogembo", "Suneka", "Keroka", "Nyamache", "Tabaka", "Nyamarambe", "Rigoma", "Nyansiongo", "Marani"]
},
"Turkey": {
  "Istanbul": ["Istanbul", "Kadikoy", "Besiktas", "Uskudar", "Beyoglu", "Bagcilar", "Fatih", "Esenyurt", "Kartal", "Maltepe"],
  "Ankara": ["Ankara", "Etimesgut", "Sincan", "Kecioren", "Mamak", "Altindag", "Cankaya", "Yenimahalle", "Golbasi", "Pursaklar"],
  "Izmir": ["Izmir", "Karsiyaka", "Bornova", "Konak", "Buca", "Bayrakli", "Karabağlar", "Aliaga", "Menemen", "Torbali"],
  "Bursa": ["Bursa", "Inegol", "Gemlik", "Mustafakemalpasa", "Karacabey", "Orhangazi", "Yildirim", "Osmangazi", "Nilufer", "Gursu"],
  "Antalya": ["Antalya", "Alanya", "Manavgat", "Kemer", "Serik", "Kas", "Konyaalti", "Muratpasa", "Kepez", "Dosemealti"],
  "Adana": ["Adana", "Ceyhan", "Kozan", "Tufanbeyli", "Feke", "Saimbeyli", "Yumurtalik", "Karaisali", "Pozanti", "Imamoglu"],
  "Gaziantep": ["Gaziantep", "Nizip", "Islahiye", "Araban", "Oguzeli", "Yavuzeli", "Nurdagi", "Karkamis", "Sahinbey", "Sehitkamil"],
  "Konya": ["Konya", "Eregli", "Aksehir", "Beysehir", "Cumra", "Ilgin", "Karatay", "Meram", "Selcuklu", "Seydisehir"],
  "Mersin": ["Mersin", "Tarsus", "Erdemli", "Silifke", "Anamur", "Mut", "Gulnar", "Bozzyurt", "Yenisehir", "Mezitli"],
  "Diyarbakir": ["Diyarbakir", "Bismil", "Cermik", "Cinar", "Cungus", "Dicle", "Egil", "Ergani", "Hani", "Hazro"]
},
"South Korea": {
  "Seoul": ["Seoul", "Gangnam", "Mapo", "Jongno", "Yongsan", "Seocho", "Gwanak", "Songpa", "Gangdong", "Nowon"],
  "Busan": ["Busan", "Haeundae", "Sasang", "Dongnae", "Geumjeong", "Busanjin", "Yeongdo", "Jung-gu", "Suyeong", "Gijang"],
  "Incheon": ["Incheon", "Bupyeong", "Gyeyang", "Namdong", "Seo-gu", "Yeonsu", "Michuhol", "Jung-gu", "Dong-gu", "Ganghwa"],
  "Daegu": ["Daegu", "Dalseo", "Jung-gu", "Suseong", "Nam-gu", "Buk-gu", "Dong-gu", "Seo-gu", "Suseong", "Dalseong"],
  "Gwangju": ["Gwangju", "Gwangsan", "Dong-gu", "Seo-gu", "Nam-gu", "Buk-gu", "Gwangsan", "Dong-gu", "Seo-gu", "Nam-gu"],
  "Daejeon": ["Daejeon", "Yuseong", "Seo-gu", "Dong-gu", "Jung-gu", "Daedeok", "Yuseong", "Seo-gu", "Dong-gu", "Jung-gu"],
  "Ulsan": ["Ulsan", "Nam-gu", "Buk-gu", "Dong-gu", "Jung-gu", "Ulju", "Nam-gu", "Buk-gu", "Dong-gu", "Jung-gu"],
  "Gyeonggi": ["Suwon", "Yongin", "Seongnam", "Goyang", "Bucheon", "Ansan", "Anyang", "Namyangju", "Hwaseong", "Pyeongtaek"],
  "Gangwon": ["Chuncheon", "Wonju", "Gangneung", "Donghae", "Sokcho", "Samcheok", "Hongcheon", "Cheorwon", "Hoengseong", "Pyeongchang"],
  "Jeju": ["Jeju", "Seogwipo", "Jeju City", "Aewol", "Hallim", "Jocheon", "Gujwa", "Daejeong", "Andeok", "Namwon"]
},
"Indonesia": {
  "Jakarta": ["Jakarta", "South Jakarta", "East Jakarta", "West Jakarta", "North Jakarta", "Central Jakarta", "Tangerang", "Depok", "Bekasi", "Bogor"],
  "East Java": ["Surabaya", "Malang", "Kediri", "Madiun", "Blitar", "Pasuruan", "Probolinggo", "Mojokerto", "Jember", "Banyuwangi"],
  "West Java": ["Bandung", "Bekasi", "Depok", "Bogor", "Cimahi", "Tasikmalaya", "Cirebon", "Sukabumi", "Karawang", "Subang"],
  "Central Java": ["Semarang", "Surakarta", "Tegal", "Pekalongan", "Magelang", "Salatiga", "Purwokerto", "Kudus", "Pati", "Blora"],
  "Banten": ["Serang", "Tangerang", "South Tangerang", "Cilegon", "Pandeglang", "Lebak", "Ciputat", "Balaraja", "Tigaraksa", "Curug"],
  "Bali": ["Denpasar", "Badung", "Gianyar", "Tabanan", "Singaraja", "Kuta", "Ubud", "Nusa Dua", "Sanur", "Seminyak"],
  "Sumatra": ["Medan", "Palembang", "Padang", "Pekanbaru", "Bandar Lampung", "Jambi", "Bengkulu", "Dumai", "Binjai", "Pematangsiantar"],
  "Sulawesi": ["Makassar", "Manado", "Palu", "Kendari", "Gorontalo", "Bitung", "Palopo", "Bau-Bau", "Ternate", "Tidore"],
  "Kalimantan": ["Pontianak", "Balikpapan", "Samarinda", "Banjarmasin", "Palangka Raya", "Tarakan", "Singkawang", "Bontang", "Sampit", "Loa Janan"],
  "Papua": ["Jayapura", "Merauke", "Biak", "Nabire", "Wamena", "Timika", "Sorong", "Manokwari", "Fakfak", "Kaimana"]
},
"Pakistan": {
  "Punjab": ["Lahore", "Faisalabad", "Rawalpindi", "Multan", "Gujranwala", "Sialkot", "Bahawalpur", "Sargodha", "Sheikhupura", "Jhelum"],
  "Sindh": ["Karachi", "Hyderabad", "Sukkur", "Larkana", "Nawabshah", "Mirpur Khas", "Thatta", "Badin", "Khairpur", "Shikarpur"],
  "Khyber Pakhtunkhwa": ["Peshawar", "Abbottabad", "Mardan", "Swat", "Nowshera", "Charsadda", "Mansehra", "Kohat", "Haripur", "Dera Ismail Khan"],
  "Balochistan": ["Quetta", "Gwadar", "Turbat", "Khuzdar", "Chaman", "Sibi", "Zhob", "Loralai", "Dera Bugti", "Ziarat"],
  "Islamabad Capital Territory": ["Islamabad", "Rawalpindi", "Murree", "Taxila", "Kahuta", "Golra Sharif", "Tarnol", "Bhara Kahu", "Sihala", "Koral"],
  "Azad Kashmir": ["Muzaffarabad", "Mirpur", "Rawalakot", "Kotli", "Bagh", "Bhimber", "Hattian", "Neelum", "Haveli", "Sudhnuti"],
  "Gilgit-Baltistan": ["Gilgit", "Skardu", "Hunza", "Nagar", "Ghizer", "Shigar", "Astore", "Ghanche", "Kharmang", "Diamer"],
  "Federally Administered Tribal Areas": ["Khyber", "Kurram", "Mohmand", "Bajaur", "Orakzai", "North Waziristan", "South Waziristan", "Dera Ismail Khan", "Tank", "Bannu"],
  "Sindh Coastal Areas": ["Thatta", "Badin", "Tharparkar", "Umerkot", "Mirpur Khas", "Sanghar", "Khairpur", "Shikarpur", "Jacobabad", "Kashmore"],
  "Northern Areas": ["Gilgit", "Skardu", "Hunza", "Nagar", "Ghizer", "Shigar", "Astore", "Ghanche", "Kharmang", "Diamer"]
},
"Bangladesh": {
  "Dhaka": ["Dhaka", "Narayanganj", "Gazipur", "Savar", "Tangail", "Manikganj", "Narsingdi", "Munshiganj", "Kishoreganj", "Faridpur"],
  "Chittagong": ["Chittagong", "Cox's Bazar", "Comilla", "Brahmanbaria", "Noakhali", "Feni", "Chandpur", "Lakshmipur", "Rangamati", "Bandarban"],
  "Khulna": ["Khulna", "Jessore", "Satkhira", "Bagerhat", "Kushtia", "Chuadanga", "Meherpur", "Narail", "Magura", "Jhenaidah"],
  "Rajshahi": ["Rajshahi", "Bogra", "Pabna", "Sirajganj", "Natore", "Naogaon", "Chapainawabganj", "Joypurhat", "Kushtia", "Meherpur"],
  "Sylhet": ["Sylhet", "Moulvibazar", "Habiganj", "Sunamganj", "Sreemangal", "Bishwanath", "Beanibazar", "Golapganj", "Jaintiapur", "Kanaighat"],
  "Barisal": ["Barisal", "Patuakhali", "Pirojpur", "Bhola", "Jhalokati", "Barguna", "Amtali", "Bakerganj", "Gaurnadi", "Mehendiganj"],
  "Rangpur": ["Rangpur", "Dinajpur", "Gaibandha", "Kurigram", "Lalmonirhat", "Nilphamari", "Panchagarh", "Thakurgaon", "Pirganj", "Badarganj"],
  "Mymensingh": ["Mymensingh", "Jamalpur", "Netrokona", "Sherpur", "Kishoreganj", "Tangail", "Fulbaria", "Gafargaon", "Trishal", "Bhaluka"],
  "Comilla": ["Comilla", "Brahmanbaria", "Chandpur", "Lakshmipur", "Noakhali", "Feni", "Haimchar", "Kachua", "Meghna", "Titas"],
  "Faridpur": ["Faridpur", "Rajbari", "Madaripur", "Shariatpur", "Gopalganj", "Kashiani", "Boalmari", "Alfadanga", "Bhanga", "Nagarkanda"]
},
"Philippines": {
  "Metro Manila": ["Manila", "Quezon City", "Makati", "Taguig", "Pasig", "Mandaluyong", "San Juan", "Parañaque", "Las Piñas", "Muntinlupa"],
  "Cebu": ["Cebu City", "Lapu-Lapu", "Mandaue", "Talisay", "Danao", "Toledo", "Minglanilla", "Naga", "Consolacion", "Liloan"],
  "Davao": ["Davao City", "Tagum", "Panabo", "Digos", "Mati", "Samal", "Sta. Cruz", "Malita", "Bansalan", "Don Marcelino"],
  "Bulacan": ["Malolos", "Meycauayan", "San Jose del Monte", "Santa Maria", "Baliuag", "Plaridel", "Marilao", "Guiguinto", "Pulilan", "Calumpit"],
  "Laguna": ["Santa Rosa", "Calamba", "San Pablo", "Biñan", "Los Baños", "Cabuyao", "San Pedro", "Sta. Cruz", "Nagcarlan", "Calauan"],
  "Pampanga": ["Angeles City", "San Fernando", "Mabalacat", "Mexico", "Guagua", "Apalit", "Lubao", "Arayat", "Floridablanca", "Porac"],
  "Batangas": ["Batangas City", "Lipa", "Tanauan", "Nasugbu", "Bauan", "San Jose", "Calaca", "Balayan", "Lemery", "Taal"],
  "Iloilo": ["Iloilo City", "Passi", "Oton", "Santa Barbara", "Miagao", "San Joaquin", "Leganes", "Tigbauan", "Guimbal", "Tubungan"],
  "Negros Occidental": ["Bacolod", "Silay", "Kabankalan", "Bago", "Cadiz", "Talisay", "Himamaylan", "Victorias", "Sagay", "La Carlota"],
  "Zamboanga": ["Zamboanga City", "Dipolog", "Pagadian", "Isabela", "Dapitan", "Molave", "Labason", "Siocon", "Ipil", "Aurora"]
},
"Vietnam": {
  "Hanoi": ["Hanoi", "Ha Dong", "Cau Giay", "Long Bien", "Tay Ho", "Hoan Kiem", "Ba Dinh", "Dong Da", "Hai Ba Trung", "Thanh Xuan"],
  "Ho Chi Minh City": ["Ho Chi Minh City", "Thu Duc", "Binh Thanh", "Go Vap", "Tan Binh", "Phu Nhuan", "District 1", "District 3", "District 5", "District 7"],
  "Da Nang": ["Da Nang", "Lien Chieu", "Thanh Khe", "Hai Chau", "Son Tra", "Ngu Hanh Son", "Cam Le", "Hoa Vang", "Lien Chieu", "Thanh Khe"],
  "Hai Phong": ["Hai Phong", "Hong Bang", "Le Chan", "Ngo Quyen", "Kien An", "Do Son", "Duong Kinh", "Hai An", "Thuy Nguyen", "An Duong"],
  "Can Tho": ["Can Tho", "Ninh Kieu", "Binh Thuy", "Cai Rang", "O Mon", "Thot Not", "Phong Dien", "Co Do", "Vinh Thanh", "Thoi Lai"],
  "Hue": ["Hue", "Phu Vang", "Huong Thuy", "Huong Tra", "Phu Loc", "Quang Dien", "A Luoi", "Nam Dong", "Phong Dien", "Quang Dien"],
  "Nha Trang": ["Nha Trang", "Cam Ranh", "Ninh Hoa", "Dien Khanh", "Van Ninh", "Khanh Vinh", "Truc Lam", "Nha Trang Beach", "Hon Chong", "Doc Let"],
  "Vung Tau": ["Vung Tau", "Ba Ria", "Long Dien", "Dat Do", "Xuyen Moc", "Chau Duc", "Con Dao", "Tan Thanh", "Phu My", "Long Hai"],
  "Hai Duong": ["Hai Duong", "Chi Linh", "Kinh Mon", "Nam Sach", "Thanh Ha", "Cam Giang", "Binh Giang", "Gia Loc", "Tu Ky", "Ninh Giang"],
  "Quang Ninh": ["Ha Long", "Cam Pha", "Uong Bi", "Mong Cai", "Quang Yen", "Dong Trieu", "Yen Hung", "Hoanh Bo", "Van Don", "Co To"]
},
"Thailand": {
  "Bangkok": ["Bangkok", "Chatuchak", "Bang Na", "Lat Phrao", "Phra Khanong", "Sathon", "Pathum Wan", "Ratchathewi", "Sukhumvit", "Thonburi"],
  "Chiang Mai": ["Chiang Mai", "Mae Rim", "San Sai", "Hang Dong", "Saraphi", "Doi Saket", "Mae Taeng", "Chom Thong", "Hot", "Samoeng"],
  "Phuket": ["Phuket", "Kathu", "Thalang", "Patong", "Karon", "Kamala", "Rawai", "Chalong", "Mai Khao", "Nai Harn"],
  "Krabi": ["Krabi", "Ao Nang", "Klong Thom", "Koh Lanta", "Plai Phraya", "Khao Phanom", "Khlong Muang", "Nuea Khlong", "Lam Thap", "Ko Phi Phi"],
  "Pattaya": ["Pattaya", "Jomtien", "Nong Prue", "Bang Lamung", "Na Kluea", "Huai Yai", "Sattahip", "Ban Chang", "Phan Thong", "Si Racha"],
  "Surat Thani": ["Surat Thani", "Koh Samui", "Koh Phangan", "Koh Tao", "Chaiya", "Tha Chana", "Kanchanadit", "Ban Na San", "Phunphin", "Tha Kham"],
  "Udon Thani": ["Udon Thani", "Ban Dung", "Kumphawapi", "Nong Han", "Prachaksinlapakhom", "Ban Phue", "Si That", "Wang Sam Mo", "Nong Wua So", "Nam Som"],
  "Khon Kaen": ["Khon Kaen", "Ban Phai", "Chum Phae", "Nam Phong", "Phra Yuen", "Mancha Khiri", "Ban Haet", "Nong Ruea", "Ubolratana", "Waeng Yai"],
  "Songkhla": ["Songkhla", "Hat Yai", "Sadao", "Chana", "Na Thawi", "Thepha", "Ranot", "Krasae Sin", "Sathing Phra", "Singhanakhon"],
  "Nakhon Ratchasima": ["Nakhon Ratchasima", "Pak Chong", "Sikhio", "Pak Thong Chai", "Non Sung", "Bua Yai", "Chok Chai", "Khon Buri", "Soeng Sang", "Wang Nam Khiao"]
},
"Malaysia": {
  "Kuala Lumpur": ["Kuala Lumpur", "Ampang", "Cheras", "Segambut", "Setapak", "Batu", "Kepong", "Titiwangsa", "Lembah Pantai", "Bandar Tun Razak"],
  "Selangor": ["Shah Alam", "Petaling Jaya", "Subang Jaya", "Klang", "Kajang", "Selayang", "Ampang Jaya", "Sungai Buloh", "Puchong", "Rawang"],
  "Penang": ["George Town", "Butterworth", "Bukit Mertajam", "Bayan Lepas", "Jelutong", "Tanjung Tokong", "Air Itam", "Gelugor", "Balik Pulau", "Tanjung Bungah"],
  "Johor": ["Johor Bahru", "Iskandar Puteri", "Pasir Gudang", "Muar", "Batu Pahat", "Kluang", "Segamat", "Kulai", "Pontian", "Tangkak"],
  "Sabah": ["Kota Kinabalu", "Sandakan", "Tawau", "Lahad Datu", "Keningau", "Semporna", "Kudat", "Ranau", "Beaufort", "Papar"],
  "Sarawak": ["Kuching", "Miri", "Sibu", "Bintulu", "Limbang", "Sri Aman", "Sarikei", "Kapit", "Mukah", "Betong"],
  "Perak": ["Ipoh", "Taiping", "Teluk Intan", "Sitiawan", "Kampar", "Batu Gajah", "Kuala Kangsar", "Tapah", "Parit Buntar", "Lumut"],
  "Kedah": ["Alor Setar", "Sungai Petani", "Kulim", "Langkawi", "Jitra", "Pendang", "Baling", "Yan", "Gurun", "Pokok Sena"],
  "Kelantan": ["Kota Bharu", "Pasir Mas", "Tumpat", "Tanah Merah", "Pasir Puteh", "Bachok", "Machang", "Kuala Krai", "Jeli", "Gua Musang"],
  "Terengganu": ["Kuala Terengganu", "Kemaman", "Dungun", "Marang", "Hulu Terengganu", "Setiu", "Besut", "Kuala Berang", "Chukai", "Ajil"]
},
"Singapore": {
  "Central Singapore": ["Singapore", "Marina Bay", "Orchard", "Raffles Place", "Bugis", "Chinatown", "Clarke Quay", "Dhoby Ghaut", "Little India", "Rochor"],
  "North East": ["Serangoon", "Hougang", "Punggol", "Sengkang", "Ang Mo Kio", "Seletar", "Buangkok", "Compassvale", "Rivervale", "Anchorvale"],
  "North West": ["Woodlands", "Bukit Panjang", "Choa Chu Kang", "Yishun", "Sembawang", "Lim Chu Kang", "Sungei Kadut", "Kranji", "Mandai", "Tengah"],
  "South East": ["Bedok", "Tampines", "Pasir Ris", "Changi", "Geylang", "Kallang", "Eunos", "Kembangan", "Simei", "Ubi"],
  "South West": ["Jurong", "Clementi", "Bukit Batok", "Tuas", "Boon Lay", "Pioneer", "Taman Jurong", "Yuhua", "Hong Kah", "Choa Chu Kang"],
  "East Coast": ["Marine Parade", "Katong", "Joo Chiat", "Bedok Reservoir", "Siglap", "Frankel", "Opera Estate", "Kembangan", "Chai Chee", "Eastwood"],
  "West Coast": ["Clementi", "West Coast", "Pandan Gardens", "Jurong East", "Jurong West", "Bukit Batok", "Choa Chu Kang", "Tengah", "Boon Lay", "Pioneer"],
  "North Coast": ["Woodlands", "Sembawang", "Yishun", "Admiralty", "Canberra", "Marsiling", "Kranji", "Sungei Kadut", "Lim Chu Kang", "Mandai"],
  "Central North": ["Ang Mo Kio", "Bishan", "Toa Payoh", "Serangoon", "Hougang", "Punggol", "Sengkang", "Seletar", "Buangkok", "Compassvale"],
  "Central South": ["Bukit Merah", "Queenstown", "Tiong Bahru", "Outram", "Telok Blangah", "HarbourFront", "Pasir Panjang", "Kent Ridge", "Clementi", "Dover"]
},
"Saudi Arabia": {
  "Riyadh": ["Riyadh", "Diriyah", "Al Kharj", "Al Majma'ah", "Al Zulfi", "Thadiq", "Huraymila", "Rumah", "Dawadmi", "Afif"],
  "Mecca": ["Mecca", "Jeddah", "Taif", "Al Qunfudhah", "Al Lith", "Al Jumum", "Khulais", "Rabiq", "Turubah", "Al Muwayh"],
  "Medina": ["Medina", "Yanbu", "Badr", "Khaybar", "Al Ula", "Mahd adh Dhahab", "Al Henakiyah", "Wadi al-Fara", "Al Jafr", "Al Suwayriqiyah"],
  "Eastern Province": ["Dammam", "Khobar", "Dhahran", "Jubail", "Qatif", "Hafr Al Batin", "Ras Tanura", "Abqaiq", "Udhailiyah", "Al Khafji"],
  "Asir": ["Abha", "Khamis Mushait", "Bisha", "Najran", "Sarawat", "Rijal Almaa", "Tathlith", "Muhayil", "Balqarn", "Al Namas"],
  "Tabuk": ["Tabuk", "Al Wajh", "Duba", "Umluj", "Haql", "Al Bad", "Tayma", "Al Khurma", "Sharma", "Al Muzeilmiya"],
  "Jazan": ["Jazan", "Sabya", "Abu Arish", "Samtah", "Al Harth", "Baish", "Farasan", "Al Dayer", "Al Reeth", "Al Edabi"],
  "Hail": ["Hail", "Baqaa", "Al Ghazalah", "Al Shinan", "Al Makhwah", "Al Sulaimi", "Al Kharma", "Al Aqiq", "Al Qaisumah", "Al Qarah"],
  "Najran": ["Najran", "Sharurah", "Hubuna", "Badr Al Janub", "Yadamah", "Thar", "Kharkhir", "Al Kharkhir", "Al Wadeen", "Al Aqeeq"],
  "Al Jawf": ["Sakakah", "Qurayyat", "Dumat al-Jandal", "Al Isawiyah", "Tabarjal", "Al Qurayyat", "Al Haditha", "Al Khuraybah", "Al Qaryatayn", "Al Mithnab"]
},
"United Arab Emirates": {
  "Dubai": ["Dubai", "Deira", "Bur Dubai", "Jumeirah", "Al Barsha", "Downtown Dubai", "Dubai Marina", "Al Qusais", "Al Karama", "Al Nahda"],
  "Abu Dhabi": ["Abu Dhabi", "Al Ain", "Al Dhafra", "Al Gharbia", "Al Shamkha", "Baniyas", "Khalifa City", "Mohammed Bin Zayed City", "Al Reef", "Al Raha"],
  "Sharjah": ["Sharjah", "Al Khan", "Al Qasimiya", "Al Nahda", "Al Majaz", "Al Taawun", "Al Rolla", "Al Qulayaa", "Al Mujarrah", "Al Heera"],
  "Ajman": ["Ajman", "Al Hamriyah", "Al Jurf", "Al Manama", "Al Zorah", "Masfout", "Al Rashidiya", "Al Nuaimiya", "Al Mowaihat", "Al Tallah"],
  "Ras Al Khaimah": ["Ras Al Khaimah", "Al Jazirah Al Hamra", "Al Marjan Island", "Al Rams", "Digdaga", "Khatt", "Al Ghail", "Al Hamra", "Al Huwaylat", "Al Mairid"],
  "Fujairah": ["Fujairah", "Dibba Al Fujairah", "Al Bidya", "Al Aqah", "Masafi", "Al Hala", "Al Bithnah", "Al Faseel", "Al Hayl", "Al Taween"],
  "Umm Al Quwain": ["Umm Al Quwain", "Al Salamah", "Al Raas", "Al Ramlah", "Al Aahad", "Al Haditha", "Al Khor", "Al Sawan", "Al Shabakah", "Al Zorah"],
  "Al Dhafra": ["Madinat Zayed", "Ghayathi", "Ruwais", "Sila", "Liwa Oasis", "Marawah", "Delma Island", "Al Mirfa", "Al Ruwais", "Al Dhafra"],
  "Al Ain": ["Al Ain", "Al Jimi", "Al Mutaredh", "Al Masoudi", "Al Foah", "Al Khrair", "Al Yahar", "Al Maqam", "Al Hayer", "Al Qattara"],
  "Western Region": ["Ghantoot", "Al Mirfa", "Al Sila", "Al Ruwais", "Al Dhafra", "Madinat Zayed", "Ghayathi", "Liwa Oasis", "Marawah", "Delma Island"]
},
"Israel": {
  "Jerusalem": ["Jerusalem", "Beit Hanina", "Ramot", "Gilo", "Har Homa", "East Jerusalem", "Talpiot", "Ein Karem", "Mamilla", "Mea Shearim"],
  "Tel Aviv": ["Tel Aviv", "Jaffa", "Ramat Gan", "Herzliya", "Bat Yam", "Holon", "Bnei Brak", "Givatayim", "Rishon LeZion", "Petah Tikva"],
  "Haifa": ["Haifa", "Nesher", "Tirat Carmel", "Kiryat Ata", "Kiryat Bialik", "Kiryat Motzkin", "Kiryat Yam", "Kiryat Haim", "Dalia", "Carmel"],
  "Central District": ["Rishon LeZion", "Petah Tikva", "Netanya", "Rehovot", "Kfar Saba", "Modiin", "Ramla", "Lod", "Ness Ziona", "Yavne"],
  "Southern District": ["Beersheba", "Ashkelon", "Ashdod", "Eilat", "Dimona", "Sderot", "Ofakim", "Netivot", "Arad", "Kiryat Gat"],
  "Northern District": ["Nazareth", "Afula", "Tiberias", "Kiryat Shmona", "Carmiel", "Nahariya", "Migdal HaEmek", "Safed", "Yokneam", "Ma'alot-Tarshiha"],
  "Judea and Samaria": ["Ariel", "Ma'ale Adumim", "Beitar Illit", "Modiin Illit", "Efrat", "Kiryat Arba", "Kedumim", "Karnie Shomron", "Oranit", "Elkana"],
  "Golan Heights": ["Katzrin", "Majdal Shams", "Buq'ata", "Ein Qiniyye", "Neve Ativ", "Ramat Magshimim", "Ani'am", "Givat Yoav", "Haspin", "Natur"],
  "Sharon Plain": ["Herzliya", "Ra'anana", "Hod HaSharon", "Kfar Saba", "Rosh HaAyin", "Tira", "Tayibe", "Qalansawe", "Kafr Qasim", "Jaljulia"],
  "Negev": ["Beersheba", "Dimona", "Eilat", "Arad", "Mitzpe Ramon", "Yeruham", "Netivot", "Ofakim", "Sderot", "Rahat"]
},
"Iran": {
  "Tehran": ["Tehran", "Karaj", "Eslamshahr", "Shahriar", "Qods", "Varamin", "Rey", "Damavand", "Pakdasht", "Robat Karim"],
  "Isfahan": ["Isfahan", "Kashan", "Najafabad", "Shahin Shahr", "Golpayegan", "Mobarakeh", "Falavarjan", "Natanz", "Khomeyni Shahr", "Zarrin Shahr"],
  "Fars": ["Shiraz", "Marvdasht", "Jahrom", "Kazerun", "Fasa", "Abadeh", "Estahban", "Neyriz", "Darab", "Lar"],
  "Khorasan": ["Mashhad", "Neyshabur", "Sabzevar", "Torbat-e Heydarieh", "Kashmar", "Torbat-e Jam", "Quchan", "Bojnord", "Gonabad", "Chenaran"],
  "East Azerbaijan": ["Tabriz", "Maragheh", "Marand", "Mianeh", "Ahar", "Sarab", "Shabestar", "Osku", "Bonab", "Jolfa"],
  "West Azerbaijan": ["Urmia", "Khoy", "Mahabad", "Miandoab", "Bukan", "Piranshahr", "Salmas", "Naqadeh", "Takab", "Shahin Dezh"],
  "Kerman": ["Kerman", "Sirjan", "Rafsanjan", "Bam", "Jiroft", "Zarand", "Shahr-e Babak", "Bardsir", "Kahnuj", "Manujan"],
  "Khuzestan": ["Ahvaz", "Abadan", "Khorramshahr", "Dezful", "Andimeshk", "Shushtar", "Masjed Soleyman", "Mahshahr", "Izeh", "Behbahan"],
  "Gilan": ["Rasht", "Bandar Anzali", "Lahijan", "Langrud", "Astara", "Rudsar", "Fuman", "Masuleh", "Shaft", "Talesh"],
  "Mazandaran": ["Sari", "Babol", "Amol", "Qaem Shahr", "Behshahr", "Chalus", "Noor", "Tonekabon", "Ramsar", "Neka"]
},
"Iraq": {
  "Baghdad": ["Baghdad", "Sadr City", "Kadhimiya", "Al Mansour", "Al Rashid", "Al Amiriya", "Al Karrada", "Al Dora", "Al Shaab", "Al Adhamiya"],
  "Basra": ["Basra", "Az Zubayr", "Al Qurnah", "Abu Al Khasib", "Shatt Al Arab", "Al Faw", "Umm Qasr", "Al Midaina", "Al Haritha", "Al Tannuma"],
  "Nineveh": ["Mosul", "Sinjar", "Tal Afar", "Al Hamdaniya", "Shekhan", "Tel Kaif", "Bashiqa", "Al Baaj", "Al Qosh", "Bartella"],
  "Erbil": ["Erbil", "Soran", "Koysinjaq", "Shaqlawa", "Choman", "Mergasor", "Rawanduz", "Makhmur", "Khabat", "Pirde"],
  "Sulaymaniyah": ["Sulaymaniyah", "Halabja", "Darbandikhan", "Ranya", "Pshdar", "Qaladiza", "Chamchamal", "Kalar", "Dukan", "Said Sadiq"],
  "Diyala": ["Baqubah", "Khanaqin", "Jalawla", "Balad Ruz", "Khalis", "Muqdadiyah", "Al Miqdadiyah", "Al Mansuriyah", "Al Khalis", "Al Muqdadiyah"],
  "Anbar": ["Ramadi", "Fallujah", "Al Qaim", "Haditha", "Hit", "Rutba", "Anah", "Khalidiya", "Habbaniyah", "Baghdadi"],
  "Karbala": ["Karbala", "Ain Al-Tamur", "Al Hindiyah", "Al Hur", "Al Khidhir", "Al Mahawil", "Al Mashkhab", "Al Musayyib", "Al Qasim", "Al Tarmiyah"],
  "Najaf": ["Najaf", "Kufa", "Manathera", "Al Mishkhab", "Al Qadisiyah", "Al Hamza", "Al Muwaffaqiyah", "Al Qasim", "Al Tarmiyah", "Al Zubayr"],
  "Dohuk": ["Dohuk", "Zakho", "Amedi", "Sumel", "Bardarash", "Sharya", "Batifa", "Faysh Khabur", "Sarsang", "Mangesh"]
},
"Afghanistan": {
  "Kabul": ["Kabul", "Deh Sabz", "Bagrami", "Char Asiab", "Paghman", "Mir Bacha Kot", "Qarabagh", "Shakardara", "Istalif", "Kalakan"],
  "Herat": ["Herat", "Ghoryan", "Kushk", "Karukh", "Guzara", "Zinda Jan", "Obe", "Kohsan", "Adraskan", "Shindand"],
  "Kandahar": ["Kandahar", "Spin Boldak", "Arghandab", "Daman", "Panjwayi", "Zhari", "Shah Wali Kot", "Maiwand", "Khakrez", "Takhtapu"],
  "Balkh": ["Mazar-i-Sharif", "Balkh", "Sholgara", "Chimtal", "Dawlatabad", "Kaldar", "Kholm", "Marmul", "Nahr-e Shahi", "Shulgara"],
  "Nangarhar": ["Jalalabad", "Behsud", "Kama", "Dara-i-Nur", "Surkh Rod", "Pachir wa Agam", "Khogyani", "Shinwar", "Lal Pur", "Achin"],
  "Kunduz": ["Kunduz", "Khanabad", "Imam Sahib", "Aliabad", "Archi", "Chahar Dara", "Dasht-e Archi", "Qalay-I-Zal", "Qalay-I-Zal", "Qalay-I-Zal"],
  "Bamyan": ["Bamyan", "Yakawlang", "Panjab", "Shibar", "Kahmard", "Waras", "Saighan", "Shahristan", "Yakawlang", "Kahmard"],
  "Helmand": ["Lashkargah", "Sangin", "Nad Ali", "Nawa", "Marjah", "Garmsir", "Kajaki", "Washir", "Nahr-e Saraj", "Khanashin"],
  "Badakhshan": ["Fayzabad", "Baharak", "Jurm", "Ishkashim", "Khash", "Kuf Ab", "Ragh", "Shighnan", "Wakhan", "Zebak"],
  "Ghazni": ["Ghazni", "Andar", "Deh Yak", "Gelan", "Jaghori", "Malistan", "Nawa", "Qarabagh", "Waghaz", "Zana Khan"]
},
"Nepal": {
  "Kathmandu": ["Kathmandu", "Lalitpur", "Bhaktapur", "Kirtipur", "Madhyapur Thimi", "Budhanilkantha", "Gokarneshwar", "Shankharapur", "Tarakeshwar", "Nagarjun"],
  "Pokhara": ["Pokhara", "Lekhnath", "Bagar", "Bijayapur", "Dhapakhel", "Batulechaur", "Hemja", "Sarangkot", "Pumdi Bhumdi", "Kahun"],
  "Lumbini": ["Lumbini", "Siddharthanagar", "Butwal", "Tilottama", "Gulariya", "Kapilvastu", "Taulihawa", "Banganga", "Kotahimai", "Suddhodhan"],
  "Janakpur": ["Janakpur", "Dhanusha", "Mahottari", "Sarlahi", "Siraha", "Bara", "Parsa", "Rautahat", "Bara", "Parsa"],
  "Bagmati": ["Hetauda", "Chitwan", "Makwanpur", "Dhading", "Nuwakot", "Rasuwa", "Sindhuli", "Ramechhap", "Dolakha", "Sindhupalchok"],
  "Gandaki": ["Pokhara", "Kaski", "Lamjung", "Tanahu", "Syangja", "Gorkha", "Manang", "Mustang", "Myagdi", "Nawalpur"],
  "Karnali": ["Birendranagar", "Surkhet", "Dailekh", "Jajarkot", "Dolpa", "Humla", "Kalikot", "Mugu", "Jumla", "Rukum"],
  "Sudurpashchim": ["Dhangadhi", "Kailali", "Kanchanpur", "Dadeldhura", "Baitadi", "Darchula", "Bajhang", "Bajura", "Achham", "Doti"],
  "Province 1": ["Biratnagar", "Morang", "Sunsari", "Jhapa", "Ilam", "Panchthar", "Taplejung", "Dhankuta", "Terhathum", "Sankhuwasabha"],
  "Province 2": ["Janakpur", "Dhanusha", "Mahottari", "Sarlahi", "Siraha", "Bara", "Parsa", "Rautahat", "Bara", "Parsa"]
},
"Sri Lanka": {
  "Colombo": ["Colombo", "Dehiwala-Mount Lavinia", "Moratuwa", "Sri Jayawardenepura Kotte", "Negombo", "Kaduwela", "Kolonnawa", "Homagama", "Maharagama", "Kesbewa"],
  "Kandy": ["Kandy", "Gampola", "Nuwara Eliya", "Matale", "Dambulla", "Wattegama", "Kadugannawa", "Pilimatalawa", "Akurana", "Harispattuwa"],
  "Galle": ["Galle", "Ambalangoda", "Hikkaduwa", "Weligama", "Matara", "Tangalle", "Hambantota", "Balapitiya", "Ahangama", "Mirissa"],
  "Jaffna": ["Jaffna", "Chavakachcheri", "Point Pedro", "Nallur", "Chankanai", "Karainagar", "Uduvil", "Sandilipay", "Tellippalai", "Maruthankerny"],
  "Anuradhapura": ["Anuradhapura", "Polonnaruwa", "Mihintale", "Kekirawa", "Habarana", "Galenbindunuwewa", "Nochchiyagama", "Thambuttegama", "Talawa", "Rambewa"],
  "Trincomalee": ["Trincomalee", "Kinniya", "Kantalai", "Seruvila", "Gomarankadawala", "Muttur", "Kuchchaveli", "Thambalagamuwa", "Morawewa", "Padavi Sri Pura"],
  "Batticaloa": ["Batticaloa", "Kalkudah", "Valaichchenai", "Eravur", "Vakarai", "Kattankudy", "Chenkalady", "Kiran", "Paddiruppu", "Vellavely"],
  "Ratnapura": ["Ratnapura", "Balangoda", "Embilipitiya", "Pelmadulla", "Kuruwita", "Eheliyagoda", "Nivithigala", "Kahawatta", "Godakawela", "Ayagama"],
  "Badulla": ["Badulla", "Bandarawela", "Haputale", "Welimada", "Ella", "Passara", "Mahiyanganaya", "Haldummulla", "Diyatalawa", "Soranathota"],
  "Mannar": ["Mannar", "Nanattan", "Madhu", "Murunkan", "Tharapuram", "Pesalai", "Vankalai", "Silavathurai", "Erukkalampiddy", "Periyamadhu"]
},
"Myanmar": {
  "Yangon": ["Yangon", "Bago", "Mawlamyine", "Pathein", "Monywa", "Sittwe", "Pyay", "Taungoo", "Hinthada", "Tharyarwady"],
  "Mandalay": ["Mandalay", "Meiktila", "Pyin Oo Lwin", "Myingyan", "Kyaukse", "Sagaing", "Yamethin", "Mogok", "Nyaung-U", "Maha Aungmye"],
  "Naypyidaw": ["Naypyidaw", "Lewe", "Pyinmana", "Tatkon", "Zeyathiri", "Ottarathiri", "Pobbathiri", "Dekkhinathiri", "Zabuthiri", "Poppathiri"],
  "Shan State": ["Taunggyi", "Lashio", "Kengtung", "Muse", "Kyaukme", "Nyaungshwe", "Hsipaw", "Tachileik", "Namhsan", "Mong Hsat"],
  "Ayeyarwady": ["Pathein", "Hinthada", "Myaungmya", "Maubin", "Pyapon", "Labutta", "Kyaiklat", "Danubyu", "Wakema", "Kyonpyaw"],
  "Bago": ["Bago", "Taungoo", "Pyay", "Tharrawaddy", "Nattalin", "Letpadan", "Paungde", "Shwedaung", "Oktwin", "Thanatpin"],
  "Magway": ["Magway", "Pakokku", "Minbu", "Thayet", "Gangaw", "Sidoktaya", "Pwintbyu", "Natmauk", "Taungdwingyi", "Chauk"],
  "Sagaing": ["Sagaing", "Monywa", "Shwebo", "Katha", "Kale", "Mawlaik", "Hkamti", "Yinmabin", "Khin-U", "Wetlet"],
  "Tanintharyi": ["Dawei", "Myeik", "Kawthaung", "Thayetchaung", "Yebyu", "Launglon", "Palaw", "Tanintharyi", "Kyunsu", "Bokpyin"],
  "Kachin": ["Myitkyina", "Bhamo", "Putao", "Mohnyin", "Shwegu", "Mansi", "Waingmaw", "Chipwi", "Tanai", "Khaunglanhpu"]
},
"Cambodia": {
  "Phnom Penh": ["Phnom Penh", "Dangkao", "Meanchey", "Russey Keo", "Sen Sok", "Chbar Ampov", "Por Sen Chey", "Prek Pnov", "Chroy Changvar", "Boeng Keng Kang"],
  "Siem Reap": ["Siem Reap", "Siem Reap Town", "Angkor Chum", "Angkor Thom", "Banteay Srei", "Kralanh", "Puok", "Prasat Bakong", "Soutr Nikom", "Chi Kraeng"],
  "Battambang": ["Battambang", "Banon", "Thmor Kol", "Ek Phnom", "Moung Ruessei", "Sangkae", "Bavel", "Kamrieng", "Phnum Proek", "Koas Krala"],
  "Sihanoukville": ["Sihanoukville", "Kampong Seila", "Prey Nob", "Stung Hav", "Koh Rong", "Koh Rong Samloem", "Veal Renh", "Ream", "Otres", "Kampong Som"],
  "Kampong Cham": ["Kampong Cham", "Tbong Khmum", "Krouch Chhmar", "Memot", "Ou Reang Ov", "Cheung Prey", "Kampong Siem", "Prey Chhor", "Srey Santhor", "Kampong Thom"],
  "Kampong Thom": ["Kampong Thom", "Stueng Saen", "Baray", "Prasat Balangk", "Prasat Sambour", "Sandan", "Santuk", "Stoung", "Taing Kouk", "Kampong Svay"],
  "Kampot": ["Kampot", "Bokor", "Chhouk", "Dang Tong", "Kampong Trach", "Tuek Chhou", "Angkor Chey", "Banteay Meas", "Chum Kiri", "Kampong Bay"],
  "Kandal": ["Ta Khmau", "Kien Svay", "Ang Snuol", "Koh Thom", "Leuk Daek", "Lvea Aem", "Mukh Kampul", "Ponhea Lueu", "Sa'ang", "Kandal Stueng"],
  "Prey Veng": ["Prey Veng", "Ba Phnum", "Kamchay Mear", "Kampong Leav", "Kampong Trabaek", "Kanhchriech", "Me Sang", "Peam Chor", "Peam Ro", "Sithor Kandal"],
  "Takeo": ["Takeo", "Angkor Borei", "Bati", "Bourei Cholsar", "Kirivong", "Koh Andet", "Prey Kabbas", "Samraong", "Doun Kaev", "Tram Kak"]
},
"Laos": {
  "Vientiane": ["Vientiane", "Xaysetha", "Sikhottabong", "Chanthabuly", "Hadxayfong", "Xaythany", "Sisattanak", "Naxaithong", "Mayparkngum", "Sangthong"],
  "Luang Prabang": ["Luang Prabang", "Chomphet", "Xiengngeun", "Pak Ou", "Nambak", "Nane", "Pak Seng", "Phonxay", "Phoukhoune", "Viengkham"],
  "Savannakhet": ["Savannakhet", "Outhoumphone", "Xayphouthong", "Phalanxay", "Xonboury", "Champhone", "Atsaphangthong", "Atsaphone", "Xaybouly", "Thapangthong"],
  "Pakse": ["Pakse", "Champasak", "Sanasomboun", "Bachiengchaleunsouk", "Paksong", "Pathoumphone", "Phonthong", "Soukhoumma", "Mounlapamok", "Khong"],
  "Vang Vieng": ["Vang Vieng", "Thoulakhom", "Kasi", "Phou Kout", "Vang Vieng Town", "Ban Na Hin", "Ban Tha Heua", "Ban Pakpo", "Ban Pha Tang", "Ban Pha Khao"],
  "Xieng Khouang": ["Phonsavan", "Pek", "Kham", "Nong Het", "Khoun", "Mok May", "Phou Kout", "Thathom", "Nong Haet", "Paek"],
  "Champasak": ["Pakse", "Champasak", "Sanasomboun", "Bachiengchaleunsouk", "Paksong", "Pathoumphone", "Phonthong", "Soukhoumma", "Mounlapamok", "Khong"],
  "Luang Namtha": ["Luang Namtha", "Long", "Viengphoukha", "Na Le", "Sing", "Nalae", "Vieng Phoukha", "Long District", "Namtha District", "Sing District"],
  "Oudomxay": ["Muang Xay", "La", "Namor", "Nga", "Pakbeng", "Beng", "Houn", "Xay", "Nga District", "La District"],
  "Bolikhamxay": ["Paksan", "Thaphabat", "Pakxan", "Bolikhan", "Khamkeut", "Viengthong", "Borikhane", "Khamkeut District", "Pakxan District", "Thaphabat District"]
},
"Mongolia": {
  "Ulaanbaatar": ["Ulaanbaatar", "Khan-Uul", "Bayanzürkh", "Sükhbaatar", "Songino Khairkhan", "Chingeltei", "Baganuur", "Bagakhangai", "Nalaikh", "Bayangol"],
  "Darkhan-Uul": ["Darkhan", "Orkhon", "Sharyngol", "Khongor", "Erdenet", "Bulgan", "Khongor District", "Orkhon District", "Sharyngol District", "Darkhan District"],
  "Khovd": ["Khovd", "Altai", "Bulgan", "Buyant", "Chandmani", "Darvi", "Durgun", "Duut", "Mankhan", "Mönkhkhairkhan"],
  "Uvs": ["Ulaangom", "Baruunturuun", "Zavkhan", "Khovd", "Ölgii", "Tosontsengel", "Naranbulag", "Malchin", "Ömnögovi", "Tarialan"],
  "Dornod": ["Choibalsan", "Bayankhongor", "Khentii", "Sukhbaatar", "Dornogovi", "Govi-Sümber", "Bayandelger", "Bayandun", "Bayankhutag", "Bayantsagaan"],
  "Arkhangai": ["Tsetserleg", "Bulgan", "Erdenemandal", "Ikh-Tamir", "Jargalant", "Khashaat", "Khotont", "Ögii nuur", "Ölziit", "Tariat"],
  "Bayankhongor": ["Bayankhongor", "Bogd", "Büren", "Galuut", "Gurvanbulag", "Jinst", "Khureemaral", "Ölziit", "Shinejinst", "Zag"],
  "Gobi-Altai": ["Altai", "Bayantsagaan", "Biger", "Bugat", "Darvi", "Delger", "Erdene", "Jargalant", "Sharga", "Taishir"],
  "Khentii": ["Öndörkhaan", "Batshireet", "Bayan-Adarga", "Bayankhutag", "Bayanmönkh", "Bayan-Ovoo", "Binder", "Dadal", "Darkhan", "Delgerkhaan"],
  "Zavkhan": ["Uliastai", "Aldarkhaan", "Asgat", "Bayantes", "Bayankhairkhan", "Bulnai", "Durvuljin", "Erdenekhaijkhan", "Ider", "Ikh-Uul"]
},
"New Zealand": {
  "Auckland": ["Auckland", "Manukau", "North Shore", "Waitakere", "Papakura", "Franklin", "Rodney", "Howick", "Pakuranga", "Botany Downs"],
  "Wellington": ["Wellington", "Lower Hutt", "Upper Hutt", "Porirua", "Kapiti Coast", "Masterton", "Carterton", "Featherston", "Greytown", "Martinborough"],
  "Christchurch": ["Christchurch", "Selwyn", "Waimakariri", "Ashburton", "Timaru", "Rangiora", "Kaiapoi", "Rolleston", "Lincoln", "Leeston"],
  "Hamilton": ["Hamilton", "Cambridge", "Te Awamutu", "Huntly", "Ngaruawahia", "Raglan", "Morrinsville", "Matamata", "Otorohanga", "Tokoroa"],
  "Dunedin": ["Dunedin", "Mosgiel", "Port Chalmers", "Oamaru", "Balclutha", "Queenstown", "Wanaka", "Alexandra", "Cromwell", "Milton"],
  "Tauranga": ["Tauranga", "Mount Maunganui", "Papamoa", "Te Puke", "Katikati", "Waihi", "Whakatane", "Opotiki", "Rotorua", "Taupo"],
  "Napier-Hastings": ["Napier", "Hastings", "Havelock North", "Taradale", "Flaxmere", "Wairoa", "Central Hawke's Bay", "Waipukurau", "Waipawa", "Clive"],
  "Palmerston North": ["Palmerston North", "Feilding", "Levin", "Foxton", "Shannon", "Ashhurst", "Bulls", "Marton", "Pahiatua", "Woodville"],
  "Nelson": ["Nelson", "Richmond", "Motueka", "Wakefield", "Brightwater", "Mapua", "Stoke", "Tahunanui", "Moutere", "Riwaka"],
  "Invercargill": ["Invercargill", "Bluff", "Gore", "Winton", "Te Anau", "Riverton", "Otautau", "Tuatapere", "Edendale", "Wyndham"]
},
"Fiji": {
  "Central Division": ["Suva", "Nausori", "Navua", "Lami", "Nakasi", "Sigatoka", "Nadi", "Lautoka", "Ba", "Tavua"],
  "Western Division": ["Lautoka", "Nadi", "Ba", "Tavua", "Rakiraki", "Vatukoula", "Sigatoka", "Nadroga", "Navosa", "Tavua"],
  "Northern Division": ["Labasa", "Savusavu", "Taveuni", "Bua", "Seaqaqa", "Nabouwalu", "Taveuni", "Bua", "Seaqaqa", "Nabouwalu"],
  "Eastern Division": ["Levuka", "Tubou", "Lakeba", "Ovalau", "Koro", "Vanuabalavu", "Lakeba", "Ovalau", "Koro", "Vanuabalavu"],
  "Rotuma": ["Ahau", "Motusa", "Oinafa", "Malhaha", "Pepjei", "Juju", "Itu'ti'u", "Noa'tau", "Faguta", "Itumuta"],
  "Lomaiviti": ["Levuka", "Ovalau", "Koro", "Batiki", "Gau", "Nairai", "Moala", "Totoya", "Matuku", "Vanuabalavu"],
  "Kadavu": ["Vunisea", "Nabukelevu", "Galoa", "Daviqele", "Nalotu", "Naceva", "Tavuki", "Nabukelevu", "Galoa", "Daviqele"],
  "Lau": ["Tubou", "Lakeba", "Ovalau", "Koro", "Vanuabalavu", "Lakeba", "Ovalau", "Koro", "Vanuabalavu", "Lakeba"],
  "Vanua Levu": ["Labasa", "Savusavu", "Taveuni", "Bua", "Seaqaqa", "Nabouwalu", "Taveuni", "Bua", "Seaqaqa", "Nabouwalu"],
  "Viti Levu": ["Suva", "Nausori", "Navua", "Lami", "Nakasi", "Sigatoka", "Nadi", "Lautoka", "Ba", "Tavua"]
},
"Papua New Guinea": {
  "National Capital District": ["Port Moresby", "Boroko", "Gerehu", "Waigani", "Konedobu", "Badili", "Gordon", "Koki", "Hohola", "Ela Beach"],
  "Morobe": ["Lae", "Bulolo", "Wau", "Finschhafen", "Menyamya", "Kaiapit", "Tewae-Siassi", "Nawae", "Markham", "Kabwum"],
  "Eastern Highlands": ["Goroka", "Kainantu", "Okapa", "Henganofi", "Unggai-Bena", "Lufa", "Obura-Wonenara", "Daulo", "Asaro", "Bena"],
  "Western Highlands": ["Mount Hagen", "Kundiawa", "Banz", "Minj", "Tari", "Mendi", "Tambul", "Nebilyer", "Mul", "Kompiam"],
  "East New Britain": ["Kokopo", "Rabaul", "Kerevat", "Vunapope", "Duke of York", "Gazelle", "Pomio", "Kokopo-Vunamami", "Raluana", "Bitapaka"],
  "West New Britain": ["Kimbe", "Hoskins", "Bialla", "Kandrian", "Talasea", "Gloucester", "Mosa", "Gasmata", "Kandrian-Gloucester", "Bali-Vitu"],
  "Madang": ["Madang", "Bogia", "Sumkar", "Rai Coast", "Middle Ramu", "Usino-Bundi", "Madang", "Bogia", "Sumkar", "Rai Coast"],
  "Milne Bay": ["Alotau", "Esa'ala", "Kiriwina-Goodenough", "Samarai-Murua", "Esa'ala", "Kiriwina-Goodenough", "Samarai-Murua", "Esa'ala", "Kiriwina-Goodenough", "Samarai-Murua"],
  "Enga": ["Wabag", "Laiagam", "Kandep", "Wapenamanda", "Kompiam", "Porgera", "Wapenamanda", "Kompiam", "Porgera", "Wapenamanda"],
  "Simbu": ["Kundiawa", "Gumine", "Kerowagi", "Sinasina-Yonggomugl", "Chuave", "Salt-Nomane-Karamui", "Gumine", "Kerowagi", "Sinasina-Yonggomugl", "Chuave"]
},
"Nicaragua": {
  "Managua": ["Managua", "Ciudad Sandino", "Tipitapa", "San Rafael del Sur", "Ticuantepe", "El Crucero", "Villa El Carmen", "Mateare", "San Francisco Libre", "Valle de Ticuantep"],
  "León": ["León", "La Paz Centro", "Nagarote", "El Sauce", "Larreynaga", "Achuapa", "Santa Rosa del Peñón", "El Jicaral", "Quezalguaque", "Telica"],
  "Chinandega": ["Chinandega", "El Viejo", "Corinto", "Chichigalpa", "Posoltega", "El Realejo", "Villanueva", "Somotillo", "Santo Tomás del Norte", "Cinco Pinos"],
  "Masaya": ["Masaya", "Nindirí", "Catarina", "San Juan de Oriente", "Niquinohomo", "Tisma", "La Concepción", "Masatepe", "Nandasmo", "San Marcos"],
  "Granada": ["Granada", "Nandaime", "Diriomo", "Diriá", "El Rosario", "Santa Teresa", "Nandaime", "Diriomo", "Diriá", "El Rosario"],
  "Carazo": ["Jinotepe", "Diriamba", "San Marcos", "Santa Teresa", "Dolores", "La Paz de Carazo", "El Rosario", "La Conquista", "Jinotepe", "Diriamba"],
  "Rivas": ["Rivas", "San Jorge", "San Juan del Sur", "Cárdenas", "Moyogalpa", "Altagracia", "Belén", "Buenos Aires", "Potosí", "Tola"],
  "Matagalpa": ["Matagalpa", "San Ramón", "Matiguás", "Muy Muy", "Esquipulas", "San Dionisio", "Sébaco", "Ciudad Darío", "Terrabona", "San Isidro"],
  "Jinotega": ["Jinotega", "San Rafael del Norte", "San Sebastián de Yalí", "La Concordia", "El Cuá", "Wiwilí", "Santa María de Pantasma", "San José de Bocay", "El Cua", "Wiwilí"],
  "Estelí": ["Estelí", "Condega", "Pueblo Nuevo", "San Juan de Limay", "La Trinidad", "San Nicolás", "Estelí", "Condega", "Pueblo Nuevo", "San Juan de Limay"]
},
"Honduras": {
  "Tegucigalpa": ["Tegucigalpa", "Comayagüela", "Santa Lucía", "Valle de Ángeles", "Ojojona", "San Juancito", "Tatumbla", "Curarén", "San Antonio de Oriente", "Cedros"],
  "San Pedro Sula": ["San Pedro Sula", "Choloma", "Villanueva", "La Lima", "El Progreso", "Puerto Cortés", "Omoa", "Pimienta", "Potrerillos", "Santa Cruz de Yojoa"],
  "La Ceiba": ["La Ceiba", "Tela", "Trujillo", "Olanchito", "Juticalpa", "Roatán", "Utila", "Guanaja", "Sonaguera", "Tocoa"],
  "Choluteca": ["Choluteca", "El Triunfo", "Marcovia", "Namasigüe", "Pespire", "San Lorenzo", "Duyure", "Morolica", "Apacilagua", "Concepción de María"],
  "Comayagua": ["Comayagua", "Siguatepeque", "La Paz", "Santa Rosa de Copán", "Gracias", "San Pedro Sula", "La Esperanza", "Yarumela", "Esquías", "Lejamaní"],
  "Copán": ["Santa Rosa de Copán", "Copán Ruinas", "La Entrada", "Cabañas", "Dulce Nombre", "San Agustín", "San Antonio", "San Jerónimo", "San José", "San Juan de Opoa"],
  "Olancho": ["Juticalpa", "Catacamas", "Campamento", "San Esteban", "Gualaco", "Guata", "Jano", "La Unión", "Mangulile", "Patuca"],
  "Cortés": ["San Pedro Sula", "Choloma", "Villanueva", "La Lima", "El Progreso", "Puerto Cortés", "Omoa", "Pimienta", "Potrerillos", "Santa Cruz de Yojoa"],
  "Yoro": ["Yoro", "El Progreso", "Olanchito", "Jocón", "Morazán", "Victoria", "El Negrito", "Santa Rita", "Sulaco", "Yorito"],
  "Atlántida": ["La Ceiba", "Tela", "Trujillo", "Olanchito", "Juticalpa", "Roatán", "Utila", "Guanaja", "Sonaguera", "Tocoa"]
},
"El Salvador": {
  "San Salvador": ["San Salvador", "Soyapango", "Santa Tecla", "Mejicanos", "Apopa", "Delgado", "Cuscatancingo", "Ayutuxtepeque", "Ilopango", "San Marcos"],
  "Santa Ana": ["Santa Ana", "Chalchuapa", "Metapán", "Coatepeque", "El Congo", "Texistepeque", "Candelaria de la Frontera", "Masahuat", "San Sebastián Salitrillo", "Santiago de la Frontera"],
  "San Miguel": ["San Miguel", "Usulután", "Chinameca", "Santiago de María", "Quelepa", "Moncagua", "Chapeltique", "Lolotique", "Nueva Guadalupe", "San Jorge"],
  "La Libertad": ["Santa Tecla", "Antiguo Cuscatlán", "Nuevo Cuscatlán", "Zaragoza", "Colón", "Quezaltepeque", "San Juan Opico", "Ciudad Arce", "Huizúcar", "Jayaque"],
  "Sonsonate": ["Sonsonate", "Acajutla", "Izalco", "Nahuizalco", "Armenia", "Juayúa", "Santo Domingo de Guzmán", "Sonzacate", "Caluco", "Santa Catarina Masahuat"],
  "Ahuachapán": ["Ahuachapán", "Atiquizaya", "Apaneca", "Concepción de Ataco", "Tacuba", "Turín", "Guaymango", "Jujutla", "San Francisco Menéndez", "San Lorenzo"],
  "Cuscatlán": ["Cojutepeque", "Suchitoto", "San Pedro Perulapán", "San Rafael Cedros", "San Bartolomé Perulapía", "San José Guayabal", "Santa Cruz Michapa", "Tenancingo", "El Carmen", "Monte San Juan"],
  "La Paz": ["Zacatecoluca", "Olocuilta", "San Pedro Masahuat", "San Luis La Herradura", "San Juan Nonualco", "Santiago Nonualco", "San Miguel Tepezontes", "Mercedes La Ceiba", "San Juan Talpa", "San Rafael Obrajuelo"],
  "Usulután": ["Usulután", "Jucuapa", "Santiago de María", "Jiquilisco", "Ozatlán", "Santa Elena", "Ereguayquín", "Concepción Batres", "San Dionisio", "San Francisco Javier"],
  "Morazán": ["San Francisco Gotera", "Cacaopera", "Chilanga", "Jocoro", "Sociedad", "El Divisadero", "Guatajiagua", "Osicala", "San Carlos", "San Simón"]
},
"Guatemala": {
  "Guatemala City": ["Guatemala City", "Mixco", "Villa Nueva", "San Miguel Petapa", "Santa Catarina Pinula", "San José Pinula", "Fraijanes", "Amatitlán", "Chinautla", "San Pedro Ayampuc"],
  "Quetzaltenango": ["Quetzaltenango", "Salcajá", "Olintepeque", "Cantel", "Almolonga", "Zunil", "San Mateo", "La Esperanza", "Concepción Chiquirichapa", "San Juan Ostuncalco"],
  "Escuintla": ["Escuintla", "Santa Lucía Cotzumalguapa", "Puerto San José", "Tiquisate", "La Gomera", "Siquinalá", "Masagua", "Nueva Concepción", "Palín", "San Vicente Pacaya"],
  "Sacatepéquez": ["Antigua Guatemala", "Jocotenango", "Sumpango", "Santiago Sacatepéquez", "San Lucas Sacatepéquez", "Santa María de Jesús", "Pastores", "San Bartolomé Milpas Altas", "San Miguel Dueñas", "Santa Lucía Milpas Altas"],
  "Petén": ["Flores", "Santa Elena", "San Benito", "Melchor de Mencos", "Poptún", "Sayaxché", "Dolores", "La Libertad", "San Francisco", "San Andrés"],
  "Huehuetenango": ["Huehuetenango", "Chiantla", "Malacatancito", "La Democracia", "San Pedro Necta", "San Ildefonso Ixtahuacán", "Santa Bárbara", "Todos Santos Cuchumatán", "San Juan Atitán", "San Rafael Petzal"],
  "Alta Verapaz": ["Cobán", "San Pedro Carchá", "San Juan Chamelco", "Tactic", "Santa Cruz Verapaz", "Tamahú", "Tucurú", "Panzós", "Senahú", "Cahabón"],
  "Izabal": ["Puerto Barrios", "Morales", "Livingston", "Los Amates", "El Estor", "Santo Tomás de Castilla", "Rio Dulce", "El Estor", "Santo Tomás de Castilla", "Rio Dulce"],
  "Chimaltenango": ["Chimaltenango", "San Martín Jilotepeque", "Comalapa", "Tecpán Guatemala", "Patzicía", "Patzún", "San José Poaquil", "San Juan Comalapa", "Santa Apolonia", "Zaragoza"],
  "Sololá": ["Sololá", "Panajachel", "San José Chacayá", "Santa María Visitación", "Santa Lucía Utatlán", "Nahualá", "Santa Catarina Ixtahuacán", "Santa Clara La Laguna", "San Juan La Laguna", "San Pablo La Laguna"]
},
"Iceland": {
  "Capital Region": ["Reykjavík", "Kópavogur", "Hafnarfjörður", "Garðabær", "Mosfellsbær", "Seltjarnarnes", "Álftanes", "Reykjanesbær", "Vogar", "Grindavík"],
  "Southern Peninsula": ["Keflavík", "Reykjanesbær", "Grindavík", "Sandgerði", "Vogar", "Garður", "Reykjanesbær", "Grindavík", "Sandgerði", "Vogar"],
  "West": ["Akranes", "Borgarnes", "Grundarfjörður", "Stykkishólmur", "Ólafsvík", "Reykholt", "Hvanneyri", "Bifröst", "Húsafell", "Flúðir"],
  "Westfjords": ["Ísafjörður", "Bolungarvík", "Patreksfjörður", "Hólmavík", "Suðureyri", "Flateyri", "Tálknafjörður", "Bíldudalur", "Þingeyri", "Súðavík"],
  "Northeast": ["Akureyri", "Húsavík", "Siglufjörður", "Dalvík", "Hjalteyri", "Grenivík", "Ólafsfjörður", "Reykjahlíð", "Mývatn", "Húsavík"],
  "East": ["Egilsstaðir", "Reyðarfjörður", "Fáskrúðsfjörður", "Neskaupstaður", "Eskifjörður", "Seyðisfjörður", "Vopnafjörður", "Bakkafjörður", "Mjóifjörður", "Breiðdalsvík"],
  "South": ["Selfoss", "Hveragerði", "Hella", "Vík", "Kirkjubæjarklaustur", "Höfn", "Eyrarbakki", "Stokkseyri", "Þorlákshöfn", "Hvolsvöllur"],
  "Northwest": ["Sauðárkrókur", "Blönduós", "Skagaströnd", "Hólar", "Varmahlíð", "Hvammstangi", "Staður", "Reykhólar", "Búðardalur", "Laugar"],
  "Central Highlands": ["Laugarvatn", "Geysir", "Gullfoss", "Kerlingarfjöll", "Hveravellir", "Landmannalaugar", "Þórsmörk", "Eyjafjallajökull", "Langjökull", "Hofsjökull"],
  "Reykjanes": ["Reykjanesbær", "Grindavík", "Sandgerði", "Vogar", "Garður", "Reykjanesbær", "Grindavík", "Sandgerði", "Vogar", "Garður"]
},
"Ireland": {
  "Leinster": ["Dublin", "Dún Laoghaire", "Bray", "Drogheda", "Dundalk", "Kilkenny", "Wexford", "Portlaoise", "Mullingar", "Naas"],
  "Munster": ["Cork", "Limerick", "Waterford", "Tralee", "Ennis", "Clonmel", "Tipperary", "Killarney", "Youghal", "Cobh"],
  "Connacht": ["Galway", "Sligo", "Castlebar", "Ballina", "Roscommon", "Tuam", "Westport", "Loughrea", "Athenry", "Clifden"],
  "Ulster": ["Belfast", "Derry", "Lisburn", "Newry", "Bangor", "Ballymena", "Coleraine", "Omagh", "Enniskillen", "Armagh"],
  "Midlands": ["Athlone", "Tullamore", "Portlaoise", "Mullingar", "Longford", "Birr", "Edenderry", "Moate", "Ballymahon", "Abbeyleix"],
  "Dublin": ["Dublin", "Dún Laoghaire", "Bray", "Drogheda", "Dundalk", "Kilkenny", "Wexford", "Portlaoise", "Mullingar", "Naas"],
  "Cork": ["Cork", "Kinsale", "Cobh", "Youghal", "Midleton", "Fermoy", "Mallow", "Bandon", "Clonakilty", "Skibbereen"],
  "Galway": ["Galway", "Salthill", "Oranmore", "Clifden", "Tuam", "Loughrea", "Athenry", "Ballinasloe", "Gort", "Portumna"],
  "Limerick": ["Limerick", "Adare", "Newcastle West", "Kilmallock", "Rathkeale", "Askeaton", "Abbeyfeale", "Croom", "Bruff", "Patrickswell"],
  "Waterford": ["Waterford", "Dungarvan", "Tramore", "Lismore", "Portlaw", "Kilmacthomas", "Clonmel", "Carrick-on-Suir", "Cahir", "Cashel"]
},
"Norway": {
  "Oslo": ["Oslo", "Bærum", "Lørenskog", "Skedsmo", "Eidsvoll", "Nesodden", "Asker", "Rælingen", "Lillestrøm", "Ski"],
  "Bergen": ["Bergen", "Os", "Fana", "Ytrebygda", "Fyllingsdalen", "Arna", "Åsane", "Laksevåg", "Fana", "Ytrebygda"],
  "Trondheim": ["Trondheim", "Stjørdal", "Steinkjer", "Levanger", "Malvik", "Orkdal", "Melhus", "Klæbu", "Selbu", "Tydal"],
  "Stavanger": ["Stavanger", "Sandnes", "Haugesund", "Sola", "Randaberg", "Klepp", "Time", "Gjesdal", "Sokndal", "Lund"],
  "Tromsø": ["Tromsø", "Harstad", "Narvik", "Finnsnes", "Bardufoss", "Lyngen", "Storslett", "Skjervøy", "Kåfjord", "Kvænangen"],
  "Kristiansand": ["Kristiansand", "Mandal", "Farsund", "Flekkefjord", "Vennesla", "Søgne", "Songdalen", "Lindesnes", "Lyngdal", "Hægebostad"],
  "Drammen": ["Drammen", "Lier", "Øvre Eiker", "Nedre Eiker", "Kongsberg", "Røyken", "Hurum", "Svelvik", "Holmestrand", "Tønsberg"],
  "Fredrikstad": ["Fredrikstad", "Sarpsborg", "Moss", "Hvaler", "Råde", "Rygge", "Våler", "Skiptvet", "Askim", "Eidsberg"],
  "Stavanger": ["Stavanger", "Sandnes", "Haugesund", "Sola", "Randaberg", "Klepp", "Time", "Gjesdal", "Sokndal", "Lund"],
  "Bodø": ["Bodø", "Fauske", "Sørfold", "Saltdal", "Gildeskål", "Beiarn", "Meløy", "Rødøy", "Rana", "Lurøy"]
},
"Sweden": {
  "Stockholm": ["Stockholm", "Södertälje", "Solna", "Uppsala", "Västerås", "Örebro", "Nyköping", "Eskilstuna", "Sigtuna", "Täby"],
  "Gothenburg": ["Gothenburg", "Mölndal", "Kungsbacka", "Borås", "Trollhättan", "Alingsås", "Lerum", "Partille", "Kungälv", "Märsta"],
  "Malmö": ["Malmö", "Lund", "Helsingborg", "Kristianstad", "Landskrona", "Trelleborg", "Ystad", "Höör", "Eslöv", "Svedala"],
  "Uppsala": ["Uppsala", "Enköping", "Bålsta", "Sigtuna", "Knivsta", "Tierp", "Östhammar", "Älvkarleby", "Heby", "Håbo"],
  "Västerbotten": ["Umeå", "Skellefteå", "Lycksele", "Vilhelmina", "Robertsfors", "Nordmaling", "Bjurholm", "Vindeln", "Norsjö", "Malå"],
  "Skåne": ["Malmö", "Lund", "Helsingborg", "Kristianstad", "Landskrona", "Trelleborg", "Ystad", "Höör", "Eslöv", "Svedala"],
  "Dalarna": ["Falun", "Borlänge", "Avesta", "Ludvika", "Mora", "Leksand", "Smedjebacken", "Säter", "Vansbro", "Gagnef"],
  "Östergötland": ["Linköping", "Norrköping", "Motala", "Mjölby", "Finspång", "Åtvidaberg", "Söderköping", "Valdemarsvik", "Boxholm", "Kisa"],
  "Västmanland": ["Västerås", "Köping", "Sala", "Fagersta", "Arboga", "Hallstahammar", "Surahammar", "Kungsör", "Norberg", "Skinnskatteberg"],
  "Jönköping": ["Jönköping", "Värnamo", "Nässjö", "Tranås", "Vetlanda", "Gislaved", "Sävsjö", "Habo", "Mullsjö", "Aneby"]
},
"Finland": {
  "Helsinki": ["Helsinki", "Espoo", "Vantaa", "Kauniainen", "Kerava", "Kirkkonummi", "Sipoo", "Tuusula", "Nurmijärvi", "Järvenpää"],
  "Tampere": ["Tampere", "Nokia", "Kangasala", "Ylöjärvi", "Pirkkala", "Valkeakoski", "Lempäälä", "Vesilahti", "Mänttä-Vilppula", "Orivesi"],
  "Turku": ["Turku", "Kaarina", "Raisio", "Naantali", "Lieto", "Masku", "Paimio", "Sauvo", "Rusko", "Nousiainen"],
  "Oulu": ["Oulu", "Kempele", "Haukipudas", "Kiiminki", "Oulunsalo", "Ylikiiminki", "Liminka", "Tyrnävä", "Utajärvi", "Muhos"],
  "Lapland": ["Rovaniemi", "Kemi", "Tornio", "Sodankylä", "Kemijärvi", "Inari", "Utsjoki", "Kittilä", "Salla", "Enontekiö"],
  "Uusimaa": ["Helsinki", "Espoo", "Vantaa", "Kauniainen", "Kerava", "Kirkkonummi", "Sipoo", "Tuusula", "Nurmijärvi", "Järvenpää"],
  "Pirkanmaa": ["Tampere", "Nokia", "Kangasala", "Ylöjärvi", "Pirkkala", "Valkeakoski", "Lempäälä", "Vesilahti", "Mänttä-Vilppula", "Orivesi"],
  "Varsinais-Suomi": ["Turku", "Kaarina", "Raisio", "Naantali", "Lieto", "Masku", "Paimio", "Sauvo", "Rusko", "Nousiainen"],
  "North Karelia": ["Joensuu", "Kitee", "Lieksa", "Nurmes", "Outokumpu", "Ilomantsi", "Kontiolahti", "Polvijärvi", "Tohmajärvi", "Valtimo"],
  "Kymenlaakso": ["Kotka", "Kouvola", "Hamina", "Anjalankoski", "Loviisa", "Pyhtää", "Miehikkälä", "Virolahti", "Iitti", "Jaala"]
},
"Denmark": {
  "Copenhagen": ["Copenhagen", "Frederiksberg", "Gentofte", "Gladsaxe", "Hvidovre", "Rødovre", "Ballerup", "Herlev", "Hørsholm", "Lyngby"],
  "Aarhus": ["Aarhus", "Silkeborg", "Randers", "Horsens", "Viborg", "Skanderborg", "Hedensted", "Favrskov", "Norddjurs", "Syddjurs"],
  "Odense": ["Odense", "Svendborg", "Nyborg", "Middelfart", "Assens", "Kerteminde", "Faaborg", "Bogense", "Otterup", "Munkebo"],
  "Aalborg": ["Aalborg", "Hjørring", "Frederikshavn", "Thisted", "Brønderslev", "Sæby", "Nibe", "Løgstør", "Farsø", "Aars"],
  "Esbjerg": ["Esbjerg", "Varde", "Ribe", "Grindsted", "Bramming", "Oksbøl", "Tjæreborg", "Henne", "Gørding", "Bramming"],
  "Vejle": ["Vejle", "Kolding", "Horsens", "Fredericia", "Hedensted", "Juelsminde", "Brædstrup", "Børkop", "Give", "Egtved"],
  "Roskilde": ["Roskilde", "Køge", "Greve", "Solrød", "Ishøj", "Hvalsø", "Lejre", "Skibby", "Jyllinge", "Gundsømagle"],
  "Helsingør": ["Helsingør", "Hillerød", "Fredensborg", "Hørsholm", "Espergærde", "Hornbæk", "Snekkersten", "Tikøb", "Græsted", "Gilleleje"],
  "Bornholm": ["Rønne", "Nexø", "Aakirkeby", "Svaneke", "Gudhjem", "Allinge", "Hasle", "Østerlars", "Snogebæk", "Nylars"],
  "Funen": ["Odense", "Svendborg", "Nyborg", "Middelfart", "Assens", "Kerteminde", "Faaborg", "Bogense", "Otterup", "Munkebo"]
},
"Netherlands": {
  "North Holland": ["Amsterdam", "Haarlem", "Zaanstad", "Hilversum", "Alkmaar", "Amstelveen", "Purmerend", "Hoorn", "Velsen", "Heerhugowaard"],
  "South Holland": ["Rotterdam", "The Hague", "Leiden", "Dordrecht", "Delft", "Gouda", "Zoetermeer", "Schiedam", "Vlaardingen", "Alphen aan den Rijn"],
  "Utrecht": ["Utrecht", "Amersfoort", "Zeist", "Nieuwegein", "Veenendaal", "Houten", "Woerden", "De Bilt", "IJsselstein", "Soest"],
  "North Brabant": ["Eindhoven", "Tilburg", "Breda", "Helmond", "Den Bosch", "Roosendaal", "Oss", "Bergen op Zoom", "Veldhoven", "Waalwijk"],
  "Gelderland": ["Arnhem", "Nijmegen", "Apeldoorn", "Ede", "Doetinchem", "Zutphen", "Harderwijk", "Tiel", "Wageningen", "Zevenaar"],
  "Overijssel": ["Enschede", "Zwolle", "Deventer", "Almelo", "Hengelo", "Kampen", "Oldenzaal", "Raalte", "Ommen", "Steenwijk"],
  "Limburg": ["Maastricht", "Eindhoven", "Heerlen", "Venlo", "Sittard", "Roermond", "Geleen", "Weert", "Kerkrade", "Brunssum"],
  "Friesland": ["Leeuwarden", "Drachten", "Sneek", "Heerenveen", "Harlingen", "Franeker", "Joure", "Wolvega", "Lemmer", "Bolsward"],
  "Groningen": ["Groningen", "Assen", "Emmen", "Hoogezand", "Veendam", "Winschoten", "Stadskanaal", "Delfzijl", "Leek", "Zuidhorn"],
  "Zeeland": ["Middelburg", "Vlissingen", "Goes", "Terneuzen", "Hulst", "Sluis", "Veere", "Tholen", "Kapelle", "Zierikzee"]
},
"Belgium": {
  "Brussels": ["Brussels", "Schaerbeek", "Molenbeek-Saint-Jean", "Anderlecht", "Ixelles", "Uccle", "Etterbeek", "Woluwe-Saint-Lambert", "Forest", "Saint-Gilles"],
  "Flanders": ["Antwerp", "Ghent", "Bruges", "Leuven", "Mechelen", "Aalst", "Kortrijk", "Hasselt", "Ostend", "Genk"],
  "Wallonia": ["Liège", "Charleroi", "Namur", "Mons", "Tournai", "Verviers", "La Louvière", "Seraing", "Mouscron", "Herstal"],
  "East Flanders": ["Ghent", "Aalst", "Sint-Niklaas", "Dendermonde", "Oudenaarde", "Eeklo", "Zottegem", "Ninove", "Deinze", "Lokeren"],
  "West Flanders": ["Bruges", "Ostend", "Kortrijk", "Roeselare", "Ypres", "Waregem", "Diksmuide", "Poperinge", "Menen", "Wevelgem"],
  "Antwerp": ["Antwerp", "Mechelen", "Turnhout", "Lier", "Herentals", "Mol", "Geel", "Boom", "Heist-op-den-Berg", "Hoogstraten"],
  "Limburg": ["Hasselt", "Genk", "Tongeren", "Sint-Truiden", "Bilzen", "Maasmechelen", "Lanaken", "Diepenbeek", "Beringen", "Leopoldsburg"],
  "Hainaut": ["Charleroi", "Mons", "Tournai", "La Louvière", "Mouscron", "Soignies", "Ath", "Binche", "Châtelet", "Thuin"],
  "Liège": ["Liège", "Verviers", "Seraing", "Herstal", "Eupen", "Waremme", "Soumagne", "Ans", "Flémalle", "Grâce-Hollogne"],
  "Namur": ["Namur", "Dinant", "Philippeville", "Andenne", "Gembloux", "Ciney", "Rochefort", "Floreffe", "Profondeville", "Fosses-la-Ville"]
},
"Switzerland": {
  "Zurich": ["Zurich", "Winterthur", "Uster", "Dübendorf", "Dietikon", "Wädenswil", "Horgen", "Kloten", "Thalwil", "Bülach"],
  "Bern": ["Bern", "Biel/Bienne", "Thun", "Köniz", "Ostermundigen", "Burgdorf", "Muri bei Bern", "Spiez", "Langenthal", "Interlaken"],
  "Geneva": ["Geneva", "Carouge", "Vernier", "Lancy", "Meyrin", "Onex", "Plan-les-Ouates", "Thônex", "Chêne-Bougeries", "Grand-Saconnex"],
  "Vaud": ["Lausanne", "Montreux", "Yverdon-les-Bains", "Nyon", "Renens", "Vevey", "Pully", "Morges", "Gland", "Aigle"],
  "Ticino": ["Lugano", "Bellinzona", "Locarno", "Mendrisio", "Chiasso", "Ascona", "Biasca", "Minusio", "Losone", "Capriasca"],
  "Basel": ["Basel", "Allschwil", "Riehen", "Bettingen", "Muttenz", "Pratteln", "Binningen", "Birsfelden", "Münchenstein", "Reinach"],
  "Lucerne": ["Lucerne", "Kriens", "Emmen", "Horw", "Ebikon", "Sursee", "Stans", "Hochdorf", "Sempach", "Wolhusen"],
  "St. Gallen": ["St. Gallen", "Rapperswil-Jona", "Wil", "Gossau", "Buchs", "Uzwil", "Altstätten", "Flawil", "Wittenbach", "Sargans"],
  "Valais": ["Sion", "Martigny", "Monthey", "Sierre", "Brig-Glis", "Visp", "Leuk", "Saint-Maurice", "Conthey", "Savièse"],
  "Fribourg": ["Fribourg", "Bulle", "Villars-sur-Glâne", "Marly", "Düdingen", "Estavayer-le-Lac", "Châtel-Saint-Denis", "Romont", "Murten", "Tafers"]
},
"Austria": {
  "Vienna": ["Vienna", "Döbling", "Favoriten", "Floridsdorf", "Hietzing", "Leopoldstadt", "Liesing", "Meidling", "Neubau", "Ottakring"],
  "Styria": ["Graz", "Leoben", "Kapfenberg", "Bruck an der Mur", "Feldbach", "Knittelfeld", "Köflach", "Liezen", "Mürzzuschlag", "Weiz"],
  "Tyrol": ["Innsbruck", "Kufstein", "Telfs", "Schwaz", "Hall in Tirol", "Wörgl", "Lienz", "Imst", "Rum", "St. Johann in Tirol"],
  "Salzburg": ["Salzburg", "Hallein", "Saalfelden", "Zell am See", "Bischofshofen", "St. Johann im Pongau", "Neumarkt am Wallersee", "Oberndorf bei Salzburg", "Mittersill", "Tamsweg"],
  "Carinthia": ["Klagenfurt", "Villach", "Wolfsberg", "Spittal an der Drau", "Feldkirchen", "St. Veit an der Glan", "Völkermarkt", "Hermagor", "Friesach", "Sankt Andrä"],
  "Upper Austria": ["Linz", "Wels", "Steyr", "Leonding", "Traun", "Braunau am Inn", "Ansfelden", "Gmunden", "Vöcklabruck", "Ried im Innkreis"],
  "Lower Austria": ["St. Pölten", "Wiener Neustadt", "Krems an der Donau", "Amstetten", "Baden", "Mödling", "Klosterneuburg", "Tulln", "Schwechat", "Neunkirchen"],
  "Vorarlberg": ["Dornbirn", "Feldkirch", "Bregenz", "Lustenau", "Hohenems", "Bludenz", "Hard", "Rankweil", "Götzis", "Lauterach"],
  "Burgenland": ["Eisenstadt", "Rust", "Neusiedl am See", "Mattersburg", "Oberpullendorf", "Oberwart", "Güssing", "Jennersdorf", "Pinkafeld", "Neudörfl"],
  "Salzkammergut": ["Bad Ischl", "Gmunden", "Hallstatt", "St. Wolfgang", "Ebensee", "Mondsee", "Attersee", "St. Gilgen", "Traunkirchen", "Altmünster"]
},
"Czech Republic": {
  "Prague": ["Prague", "Prague 1", "Prague 2", "Prague 3", "Prague 4", "Prague 5", "Prague 6", "Prague 7", "Prague 8", "Prague 9"],
  "Brno": ["Brno", "Černovice", "Královo Pole", "Líšeň", "Modřice", "Židenice", "Bystrc", "Komín", "Starý Lískovec", "Kohoutovice"],
  "Ostrava": ["Ostrava", "Poruba", "Slezská Ostrava", "Mariánské Hory", "Vítkovice", "Hrabůvka", "Michálkovice", "Přívoz", "Zábřeh", "Hrabová"],
  "Plzeň": ["Plzeň", "Doubravka", "Bory", "Lochotín", "Skvrňany", "Křimice", "Božkov", "Černice", "Doudlevce", "Lobzy"],
  "Liberec": ["Liberec", "Jablonec nad Nisou", "Turnov", "Česká Lípa", "Frýdlant", "Nový Bor", "Hrádek nad Nisou", "Chrastava", "Tanvald", "Semily"],
  "Olomouc": ["Olomouc", "Prostějov", "Přerov", "Šternberk", "Hranice", "Litovel", "Uničov", "Jeseník", "Zábřeh", "Mohelnice"],
  "Ústí nad Labem": ["Ústí nad Labem", "Děčín", "Teplice", "Most", "Chomutov", "Litvínov", "Jirkov", "Kadaň", "Bílina", "Varnsdorf"],
  "Hradec Králové": ["Hradec Králové", "Pardubice", "Jičín", "Náchod", "Trutnov", "Rychnov nad Kněžnou", "Dvůr Králové nad Labem", "Vrchlabí", "Jaroměř", "Nové Město nad Metují"],
  "Zlín": ["Zlín", "Otrokovice", "Kroměříž", "Uherské Hradiště", "Valašské Meziříčí", "Vsetín", "Rožnov pod Radhoštěm", "Holešov", "Bystřice pod Hostýnem", "Napajedla"],
  "Karlovy Vary": ["Karlovy Vary", "Sokolov", "Cheb", "Ostrov", "Mariánské Lázně", "Aš", "Horní Slavkov", "Kraslice", "Nejdek", "Františkovy Lázně"]
},
"Poland": {
  "Warsaw": ["Warsaw", "Praga-Północ", "Praga-Południe", "Mokotów", "Ursynów", "Wola", "Śródmieście", "Bielany", "Targówek", "Bemowo"],
  "Kraków": ["Kraków", "Nowa Huta", "Podgórze", "Krowodrza", "Bronowice", "Zwierzyniec", "Dębniki", "Łagiewniki", "Bieżanów", "Prądnik Czerwony"],
  "Łódź": ["Łódź", "Bałuty", "Polesie", "Górna", "Widzew", "Śródmieście", "Zgierz", "Pabianice", "Tomaszów Mazowiecki", "Bełchatów"],
  "Wrocław": ["Wrocław", "Psie Pole", "Krzyki", "Fabryczna", "Śródmieście", "Stare Miasto", "Biskupin", "Ołbin", "Karłowice", "Gaj"],
  "Poznań": ["Poznań", "Grunwald", "Jeżyce", "Wilda", "Stare Miasto", "Nowe Miasto", "Ławica", "Rataje", "Winogrady", "Piątkowo"],
  "Gdańsk": ["Gdańsk", "Sopot", "Gdynia", "Pruszcz Gdański", "Rumia", "Wejherowo", "Tczew", "Starogard Gdański", "Chojnice", "Kwidzyn"],
  "Szczecin": ["Szczecin", "Police", "Stargard", "Świnoujście", "Goleniów", "Gryfino", "Nowogard", "Choszczno", "Myślibórz", "Pyrzyce"],
  "Bydgoszcz": ["Bydgoszcz", "Toruń", "Włocławek", "Grudziądz", "Inowrocław", "Brodnica", "Świecie", "Chełmno", "Nakło nad Notecią", "Solec Kujawski"],
  "Lublin": ["Lublin", "Zamość", "Chełm", "Biała Podlaska", "Puławy", "Świdnik", "Kraśnik", "Łuków", "Biłgoraj", "Tomaszów Lubelski"],
  "Katowice": ["Katowice", "Sosnowiec", "Gliwice", "Zabrze", "Bytom", "Ruda Śląska", "Tychy", "Dąbrowa Górnicza", "Chorzów", "Jaworzno"]
},
"Hungary": {
  "Budapest": ["Budapest", "Pest", "Buda", "Óbuda", "Kispest", "Újpest", "Ferencváros", "Kőbánya", "Csepel", "Erzsébetváros"],
  "Debrecen": ["Debrecen", "Hajdúböszörmény", "Nyíregyháza", "Hajdúszoboszló", "Tiszavasvári", "Balmazújváros", "Hajdúnánás", "Hajdúdorog", "Hajdúhadház", "Hajdúbagos"],
  "Szeged": ["Szeged", "Hódmezővásárhely", "Makó", "Sándorfalva", "Deszk", "Algyő", "Szatymaz", "Kistelek", "Mindszent", "Mórahalom"],
  "Miskolc": ["Miskolc", "Szerencs", "Ozd", "Kazincbarcika", "Tiszaújváros", "Sajószentpéter", "Sajóvámos", "Sajókeresztúr", "Sajólád", "Sajóecseg"],
  "Pécs": ["Pécs", "Komló", "Szigetvár", "Mohács", "Siklós", "Bóly", "Pécsvárad", "Szentlőrinc", "Harkány", "Kozármisleny"],
  "Győr": ["Győr", "Mosonmagyaróvár", "Sopron", "Kapuvár", "Csorna", "Tét", "Pannonhalma", "Fertőd", "Fertőszentmiklós", "Bőny"],
  "Nyíregyháza": ["Nyíregyháza", "Mátészalka", "Kisvárda", "Tiszavasvári", "Baktalórántháza", "Vásárosnamény", "Záhony", "Fehérgyarmat", "Kemecse", "Nyírbátor"],
  "Kecskemét": ["Kecskemét", "Kiskunfélegyháza", "Kiskunhalas", "Kiskőrös", "Kiskunmajsa", "Lajosmizse", "Tiszakécske", "Kerekegyháza", "Soltvadkert", "Kunszentmiklós"],
  "Székesfehérvár": ["Székesfehérvár", "Bicske", "Dunaújváros", "Enying", "Gárdony", "Martonvásár", "Polgárdi", "Sárbogárd", "Sárkeresztúr", "Sárszentmihály"],
  "Eger": ["Eger", "Füzesabony", "Gyöngyös", "Hatvan", "Heves", "Kisköre", "Pétervására", "Recsk", "Szarvasgede", "Verpelét"]
},
"Romania": {
  "Bucharest": ["Bucharest", "Sector 1", "Sector 2", "Sector 3", "Sector 4", "Sector 5", "Sector 6", "Ilfov", "Otopeni", "Voluntari"],
  "Cluj-Napoca": ["Cluj-Napoca", "Florești", "Turda", "Dej", "Câmpia Turzii", "Gherla", "Huedin", "Cojocna", "Apahida", "Feleacu"],
  "Timișoara": ["Timișoara", "Lugoj", "Sânnicolau Mare", "Jimbolia", "Recaș", "Buziaș", "Giroc", "Săcălaz", "Racovița", "Deta"],
  "Iași": ["Iași", "Pașcani", "Hârlău", "Podu Iloaiei", "Târgu Frumos", "Valea Lupului", "Tomești", "Mironeasa", "Șipote", "Ungheni"],
  "Constanța": ["Constanța", "Mangalia", "Medgidia", "Năvodari", "Ovidiu", "Eforie", "Techirghiol", "Cernavodă", "Murfatlar", "Limanu"],
  "Brașov": ["Brașov", "Săcele", "Codlea", "Râșnov", "Predeal", "Zărnești", "Făgăraș", "Ghimbav", "Victoria", "Sânpetru"],
  "Craiova": ["Craiova", "Băilești", "Calafat", "Filiași", "Segarcea", "Dăbuleni", "Plenița", "Podari", "Șimnicu de Sus", "Valea Stanciului"],
  "Galați": ["Galați", "Tecuci", "Târgu Bujor", "Berești", "Barcea", "Pechea", "Tudor Vladimirescu", "Liești", "Oancea", "Smârdan"],
  "Ploiești": ["Ploiești", "Câmpina", "Băicoi", "Mizil", "Urlați", "Boldești-Scăeni", "Valea Călugărească", "Blejoi", "Păulești", "Târgșoru Vechi"],
  "Oradea": ["Oradea", "Săcueni", "Salonta", "Beiuș", "Aleșd", "Marghita", "Ștei", "Nucet", "Valea lui Mihai", "Tinca"]
},
"Bulgaria": {
  "Sofia": ["Sofia", "Krasno Selo", "Mladost", "Vitosha", "Lozenets", "Nadezhda", "Ovcha Kupel", "Slatina", "Studentski Grad", "Lyulin"],
  "Plovdiv": ["Plovdiv", "Karshiyaka", "Maritsa", "Rakovski", "Asenovgrad", "Perushtitsa", "Stamboliyski", "Parvomay", "Sadovo", "Kuklen"],
  "Varna": ["Varna", "Asparuhovo", "Galata", "Vinitsa", "Dolni Chiflik", "Byala", "Provadia", "Devnya", "Suvorovo", "Aksakovo"],
  "Burgas": ["Burgas", "Pomorie", "Nesebar", "Sozopol", "Kameno", "Ruen", "Sredets", "Primorsko", "Aytos", "Karnobat"],
  "Ruse": ["Ruse", "Byala", "Dve Mogili", "Slivo Pole", "Tsenovo", "Vetovo", "Borovo", "Ivanovo", "Aleksandrovo", "Senovo"],
  "Stara Zagora": ["Stara Zagora", "Kazanlak", "Chirpan", "Nova Zagora", "Radnevo", "Gurkovo", "Opan", "Galabovo", "Muglizh", "Pavel Banya"],
  "Pleven": ["Pleven", "Levski", "Nikopol", "Belene", "Cherven Bryag", "Dolni Dabnik", "Pordim", "Gulyantsi", "Knezha", "Iskar"],
  "Veliko Tarnovo": ["Veliko Tarnovo", "Gorna Oryahovitsa", "Svishtov", "Elena", "Lyaskovets", "Pavlikeni", "Strazhitsa", "Polski Trambesh", "Debelets", "Zlataritsa"],
  "Blagoevgrad": ["Blagoevgrad", "Bansko", "Sandanski", "Petrich", "Gotse Delchev", "Razlog", "Simitli", "Kresna", "Belitsa", "Yakoruda"],
  "Gabrovo": ["Gabrovo", "Sevlievo", "Dryanovo", "Tryavna", "Plachkovtsi", "Devin", "Smolyan", "Chepelare", "Zlatograd", "Nedelino"]
},
"Greece": {
  "Attica": ["Athens", "Piraeus", "Peristeri", "Kallithea", "Acharnes", "Nikaia", "Glyfada", "Ilion", "Nea Smyrni", "Marousi"],
  "Central Macedonia": ["Thessaloniki", "Kalamaria", "Evosmos", "Serres", "Drama", "Kavala", "Veroia", "Giannitsa", "Naousa", "Edessa"],
  "Crete": ["Heraklion", "Chania", "Rethymno", "Agios Nikolaos", "Ierapetra", "Sitia", "Archanes", "Malia", "Neapoli", "Anogeia"],
  "Peloponnese": ["Patras", "Kalamata", "Corinth", "Tripoli", "Argos", "Sparta", "Nafplio", "Pyrgos", "Aigio", "Megalopoli"],
  "Thessaly": ["Larissa", "Volos", "Trikala", "Karditsa", "Farsala", "Tyrnavos", "Elassona", "Kalambaka", "Nea Ionia", "Almyros"],
  "Epirus": ["Ioannina", "Arta", "Preveza", "Igoumenitsa", "Paramythia", "Filiates", "Konitsa", "Parga", "Metsovo", "Zagori"],
  "Western Greece": ["Patras", "Agrinio", "Messolonghi", "Aigio", "Pyrgos", "Amaliada", "Nafpaktos", "Loutraki", "Thermo", "Astakos"],
  "Central Greece": ["Lamia", "Chalcis", "Livadeia", "Amfissa", "Thebes", "Karpenisi", "Atalanti", "Karystos", "Istiaia", "Aidipsos"],
  "South Aegean": ["Rhodes", "Heraklion", "Chania", "Rethymno", "Agios Nikolaos", "Ierapetra", "Sitia", "Archanes", "Malia", "Neapoli"],
  "North Aegean": ["Mytilene", "Chios", "Samos", "Lemnos", "Lesbos", "Ikaria", "Symi", "Kos", "Kalymnos", "Patmos"]
},
"Portugal": {
  "Lisbon": ["Lisbon", "Sintra", "Cascais", "Loures", "Amadora", "Oeiras", "Vila Franca de Xira", "Almada", "Seixal", "Barreiro"],
  "Porto": ["Porto", "Vila Nova de Gaia", "Matosinhos", "Maia", "Gondomar", "Valongo", "Póvoa de Varzim", "Vila do Conde", "Espinho", "Santa Maria da Feira"],
  "Braga": ["Braga", "Guimarães", "Barcelos", "Famalicão", "Vila Nova de Famalicão", "Esposende", "Vizela", "Amares", "Celorico de Basto", "Fafe"],
  "Aveiro": ["Aveiro", "Ílhavo", "Ovar", "Águeda", "Oliveira de Azeméis", "São João da Madeira", "Estarreja", "Anadia", "Vagos", "Sever do Vouga"],
  "Coimbra": ["Coimbra", "Figueira da Foz", "Cantanhede", "Montemor-o-Velho", "Lousã", "Mira", "Penacova", "Condeixa-a-Nova", "Mealhada", "Tábua"],
  "Faro": ["Faro", "Loulé", "Portimão", "Albufeira", "Olhão", "Lagos", "Silves", "Tavira", "Vila Real de Santo António", "São Brás de Alportel"],
  "Setúbal": ["Setúbal", "Palmela", "Barreiro", "Montijo", "Sesimbra", "Alcochete", "Moita", "Seixal", "Almada", "Sines"],
  "Madeira": ["Funchal", "Câmara de Lobos", "Machico", "Santa Cruz", "Santana", "Ponta do Sol", "Ribeira Brava", "Calheta", "Porto Moniz", "São Vicente"],
  "Azores": ["Ponta Delgada", "Angra do Heroísmo", "Horta", "Ribeira Grande", "Lagoa", "Vila Franca do Campo", "Praia da Vitória", "Vila do Porto", "Povoação", "Nordeste"],
  "Viseu": ["Viseu", "Lamego", "Vila Real", "Chaves", "Mangualde", "Castro Daire", "Tondela", "Santa Comba Dão", "São Pedro do Sul", "Oliveira de Frades"]
},
"Croatia": {
  "Zagreb": ["Zagreb", "Sesvete", "Velika Gorica", "Zaprešić", "Samobor", "Dugo Selo", "Sveta Nedelja", "Jastrebarsko", "Vrbovec", "Ivanić-Grad"],
  "Split-Dalmatia": ["Split", "Kaštela", "Solin", "Omiš", "Makarska", "Trogir", "Sinj", "Imotski", "Vrgorac", "Hvar"],
  "Dubrovnik-Neretva": ["Dubrovnik", "Korčula", "Metković", "Ploče", "Opuzen", "Ston", "Orebić", "Trpanj", "Slivno", "Župa Dubrovačka"],
  "Istria": ["Pula", "Rovinj", "Poreč", "Umag", "Labin", "Buzet", "Novigrad", "Buje", "Vodnjan", "Motovun"],
  "Osijek-Baranja": ["Osijek", "Đakovo", "Našice", "Valpovo", "Belišće", "Donji Miholjac", "Beli Manastir", "Čepin", "Vinkovci", "Slavonski Brod"],
  "Primorje-Gorski Kotar": ["Rijeka", "Opatija", "Crikvenica", "Kastav", "Bakar", "Kraljevica", "Novi Vinodolski", "Delnice", "Čabar", "Vrbovsko"],
  "Zadar": ["Zadar", "Biograd na Moru", "Benkovac", "Nin", "Obrovac", "Pag", "Gračac", "Starigrad", "Vir", "Sukošan"],
  "Šibenik-Knin": ["Šibenik", "Knin", "Drniš", "Vodice", "Rogoznica", "Skradin", "Pirovac", "Murter", "Tisno", "Primošten"],
  "Varaždin": ["Varaždin", "Čakovec", "Ludbreg", "Ivanec", "Lepoglava", "Novi Marof", "Varaždinske Toplice", "Breznički Hum", "Mali Bukovec", "Donja Voća"],
  "Lika-Senj": ["Gospić", "Otočac", "Senj", "Novalja", "Perušić", "Lovinac", "Brinje", "Plitvička Jezera", "Udbina", "Donji Lapac"]
},
"Serbia": {
  "Belgrade": ["Belgrade", "Zemun", "New Belgrade", "Čukarica", "Zvezdara", "Palilula", "Voždovac", "Savski Venac", "Rakovica", "Obrenovac"],
  "Vojvodina": ["Novi Sad", "Subotica", "Zrenjanin", "Pančevo", "Sombor", "Kikinda", "Sremska Mitrovica", "Vršac", "Bačka Palanka", "Temerin"],
  "Šumadija and Western Serbia": ["Kragujevac", "Čačak", "Jagodina", "Kraljevo", "Kruševac", "Užice", "Valjevo", "Loznica", "Šabac", "Aranđelovac"],
  "Southern and Eastern Serbia": ["Niš", "Leskovac", "Vranje", "Pirot", "Zaječar", "Bor", "Prokuplje", "Negotin", "Knjaževac", "Aleksinac"],
  "Kosovo and Metohija": ["Pristina", "Prizren", "Peć", "Mitrovica", "Gnjilane", "Đakovica", "Podujevo", "Kosovska Mitrovica", "Uroševac", "Orahovac"],
  "Mačva": ["Šabac", "Loznica", "Bogatić", "Vladimirci", "Koceljeva", "Mali Zvornik", "Krupanj", "Ljubovija", "Loznica", "Šabac"],
  "Pomoravlje": ["Ćuprija", "Jagodina", "Paraćin", "Svilajnac", "Despotovac", "Rekovac", "Ćuprija", "Jagodina", "Paraćin", "Svilajnac"],
  "Rasina": ["Kruševac", "Varvarin", "Ćićevac", "Trstenik", "Aleksandrovac", "Brus", "Kruševac", "Varvarin", "Ćićevac", "Trstenik"],
  "Raška": ["Kraljevo", "Novi Pazar", "Vrnjačka Banja", "Raška", "Tutin", "Brus", "Aleksandrovac", "Kraljevo", "Novi Pazar", "Vrnjačka Banja"],
  "Zlatibor": ["Užice", "Čajetina", "Kosjerić", "Arilje", "Požega", "Nova Varoš", "Priboj", "Sjenica", "Bajina Bašta", "Zlatibor"]
},
"Ukraine": {
  "Kyiv": ["Kyiv", "Brovary", "Bila Tserkva", "Irpin", "Vyshhorod", "Vasylkiv", "Boryspil", "Fastiv", "Obukhiv", "Boyarka"],
  "Lviv": ["Lviv", "Drohobych", "Stryi", "Chervonohrad", "Truskavets", "Sambir", "Novyi Rozdil", "Zhovkva", "Yavoriv", "Mykolaiv"],
  "Kharkiv": ["Kharkiv", "Lozova", "Chuhuiv", "Pervomaiskyi", "Balakliia", "Izium", "Kupiansk", "Vovchansk", "Derhachi", "Merefa"],
  "Odesa": ["Odesa", "Chornomorsk", "Izmail", "Bilhorod-Dnistrovskyi", "Yuzhne", "Podilsk", "Reni", "Balta", "Rozdilna", "Kiliia"],
  "Dnipropetrovsk": ["Dnipro", "Kryvyi Rih", "Kamianske", "Nikopol", "Pavlohrad", "Novomoskovsk", "Zhovti Vody", "Marhanets", "Synelnykove", "Pershotravensk"],
  "Donetsk": ["Donetsk", "Mariupol", "Makiivka", "Horlivka", "Kramatorsk", "Sloviansk", "Bakhmut", "Kostiantynivka", "Druzhkivka", "Yasynuvata"],
  "Zaporizhzhia": ["Zaporizhzhia", "Melitopol", "Berdiansk", "Enerhodar", "Tokmak", "Polohy", "Dniprorudne", "Vilniansk", "Orikhiv", "Huliaipole"],
  "Ivano-Frankivsk": ["Ivano-Frankivsk", "Kalush", "Kolomyia", "Nadvirna", "Dolyna", "Yaremche", "Burshtyn", "Sniatyn", "Tysmenytsia", "Rohatyn"],
  "Chernihiv": ["Chernihiv", "Nizhyn", "Pryluky", "Bakhmach", "Novhorod-Siverskyi", "Koriukivka", "Ichnia", "Mena", "Horodnia", "Sosnytsia"],
  "Vinnytsia": ["Vinnytsia", "Zhmerynka", "Mohyliv-Podilskyi", "Khmilnyk", "Haisyn", "Ladyzhyn", "Bar", "Tulchyn", "Kalynivka", "Bershad"]
},
"Kazakhstan": {
  "Nur-Sultan": ["Nur-Sultan", "Kokshetau", "Stepnogorsk", "Atbasar", "Shchuchinsk", "Akkol", "Zerenda", "Ereymentau", "Makinsk", "Shortandy"],
  "Almaty": ["Almaty", "Taldykorgan", "Kapchagay", "Tekeli", "Ushtobe", "Sarkand", "Zharkent", "Esik", "Kaskelen", "Talgar"],
  "Shymkent": ["Shymkent", "Turkistan", "Kentau", "Arys", "Saryagash", "Zhetisai", "Shardara", "Lenger", "Tole Bi", "Ordabasy"],
  "Karaganda": ["Karaganda", "Temirtau", "Zhezkazgan", "Balkhash", "Saran", "Shakhtinsk", "Priozersk", "Abay", "Karkaraly", "Osakarovka"],
  "Aktobe": ["Aktobe", "Kandyagash", "Khromtau", "Emba", "Shalkar", "Martuk", "Alga", "Komsomolsk", "Kargaly", "Shubarkuduk"],
  "Pavlodar": ["Pavlodar", "Ekibastuz", "Aksu", "Kurchatov", "Bayanaul", "Zhelezinka", "Irtyshsk", "Kachiry", "Sharbakty", "Terenkol"],
  "Taraz": ["Taraz", "Shu", "Kulan", "Sarykemer", "Merke", "Moyynkum", "Baurzhan Momyshuly", "Tole Bi", "Zhanatas", "Shuysk"],
  "Ust-Kamenogorsk": ["Ust-Kamenogorsk", "Semei", "Ridder", "Ayagoz", "Zaysan", "Kurchatov", "Shemonaikha", "Zyryanovsk", "Glubokoye", "Tarbagatay"],
  "Kyzylorda": ["Kyzylorda", "Aral", "Baikonur", "Shieli", "Zhosaly", "Kazaly", "Zhanakorgan", "Shardara", "Terenozek", "Aiteke Bi"],
  "Atyrau": ["Atyrau", "Kulsary", "Makat", "Dossor", "Inderborskiy", "Kurmangazy", "Miyaly", "Zhylyoi", "Tengiz", "Kyzylkoga"]
},
"Uzbekistan": {
  "Tashkent": ["Tashkent", "Angren", "Chirchiq", "Olmaliq", "Bekabad", "Yangiyul", "Gazalkent", "Keles", "Parkent", "Chinoz"],
  "Samarkand": ["Samarkand", "Kattakurgan", "Urgut", "Bulungur", "Jomboy", "Pastdargom", "Narpay", "Payariq", "Tayloq", "Chelak"],
  "Bukhara": ["Bukhara", "Kagan", "Gijduvon", "Romitan", "Shafirkan", "Vobkent", "Olot", "Gazli", "Karakul", "Qorako'l"],
  "Khorezm": ["Urgench", "Khiva", "Gurlan", "Shovot", "Xonqa", "Hazorasp", "Yangibozor", "Bogot", "Qoshkopir", "Yangiariq"],
  "Fergana": ["Fergana", "Margilan", "Kokand", "Quvasoy", "Rishton", "Beshariq", "Qo'qon", "Yaypan", "Bog'dod", "Dang'ara"],
  "Andijan": ["Andijan", "Asaka", "Shahrixon", "Marhamat", "Jalalkuduk", "Izboskan", "Paxtaobod", "Qo'rg'ontepa", "Xo'jaobod", "Baliqchi"],
  "Namangan": ["Namangan", "Chust", "Kosonsoy", "Uychi", "Pop", "To'raqo'rg'on", "Mingbuloq", "Norin", "Uchqo'rg'on", "Yangiqo'rg'on"],
  "Qashqadaryo": ["Qarshi", "Shahrisabz", "Kitob", "Koson", "Muborak", "G'uzor", "Dehqonobod", "Kasbi", "Chiroqchi", "Yakkabog"],
  "Surxondaryo": ["Termez", "Denov", "Sherobod", "Sho'rchi", "Qumqo'rg'on", "Jarqo'rg'on", "Bandixon", "Angor", "Boysun", "Muzrabot"],
  "Navoiy": ["Navoiy", "Zarafshon", "Uchquduq", "Qiziltepa", "Nurota", "Tomdi", "Karmana", "Xatirchi", "Konimex", "Yangirabot"]
},
"Belarus": {
  "Minsk": ["Minsk", "Barysaw", "Salihorsk", "Maladzyechna", "Zhodzina", "Slutsk", "Vileyka", "Dzyarzhynsk", "Marina Horka", "Fanipol"],
  "Gomel": ["Gomel", "Mazyr", "Zhlobin", "Svetlahorsk", "Rechytsa", "Kalinkavichy", "Rahachow", "Dobrush", "Zhytkavichy", "Buda-Kashalyova"],
  "Mogilev": ["Mogilev", "Babruysk", "Asipovichy", "Horki", "Krychaw", "Bykhaw", "Shklow", "Klimavichy", "Mstsislaw", "Chavusy"],
  "Vitebsk": ["Vitebsk", "Orsha", "Navapolatsk", "Polatsk", "Pastavy", "Hlybokaye", "Lepel", "Novalukoml", "Haradok", "Braslaw"],
  "Grodno": ["Grodno", "Lida", "Slonim", "Vawkavysk", "Smarhon", "Ashmyany", "Shchuchyn", "Iwie", "Dziatlava", "Svislach"],
  "Brest": ["Brest", "Baranavichy", "Pinsk", "Kobryn", "Byaroza", "Ivatsevichy", "Luninets", "Pruzhany", "Ivanava", "Drahichyn"],
  "Minsk Region": ["Minsk", "Barysaw", "Salihorsk", "Maladzyechna", "Zhodzina", "Slutsk", "Vileyka", "Dzyarzhynsk", "Marina Horka", "Fanipol"],
  "Gomel Region": ["Gomel", "Mazyr", "Zhlobin", "Svetlahorsk", "Rechytsa", "Kalinkavichy", "Rahachow", "Dobrush", "Zhytkavichy", "Buda-Kashalyova"],
  "Mogilev Region": ["Mogilev", "Babruysk", "Asipovichy", "Horki", "Krychaw", "Bykhaw", "Shklow", "Klimavichy", "Mstsislaw", "Chavusy"],
  "Vitebsk Region": ["Vitebsk", "Orsha", "Navapolatsk", "Polatsk", "Pastavy", "Hlybokaye", "Lepel", "Novalukoml", "Haradok", "Braslaw"]
},
"Azerbaijan": {
  "Baku": ["Baku", "Sumqayit", "Khirdalan", "Qaraçuxur", "Binəqədi", "Nəsimi", "Narimanov", "Yasamal", "Sabunçu", "Xətai"],
  "Ganja": ["Ganja", "Naftalan", "Samukh", "Goranboy", "Goygol", "Dashkasan", "Gadabay", "Tovuz", "Shamkir", "Goychay"],
  "Shirvan": ["Shirvan", "Bilasuvar", "Jalilabad", "Neftchala", "Salyan", "Hajigabul", "Agjabadi", "Imishli", "Saatli", "Sabirabad"],
  "Lankaran": ["Lankaran", "Astara", "Lerik", "Masalli", "Yardimli", "Jalilabad", "Bilasuvar", "Lankaran", "Astara", "Lerik"],
  "Mingachevir": ["Mingachevir", "Yevlakh", "Shaki", "Zaqatala", "Qabala", "Oghuz", "Gakh", "Balakan", "Shamakhi", "Ismayilli"],
  "Nakhchivan": ["Nakhchivan", "Ordubad", "Julfa", "Sharur", "Babek", "Shahbuz", "Kangarli", "Sadarak", "Shahbuz", "Babek"],
  "Quba": ["Quba", "Qusar", "Khachmaz", "Shabran", "Siyazan", "Quba", "Qusar", "Khachmaz", "Shabran", "Siyazan"],
  "Shaki": ["Shaki", "Zaqatala", "Qabala", "Oghuz", "Gakh", "Balakan", "Shamakhi", "Ismayilli", "Shaki", "Zaqatala"],
  "Gabala": ["Gabala", "Oghuz", "Gakh", "Balakan", "Shamakhi", "Ismayilli", "Gabala", "Oghuz", "Gakh", "Balakan"],
  "Shamakhi": ["Shamakhi", "Ismayilli", "Gabala", "Oghuz", "Gakh", "Balakan", "Shamakhi", "Ismayilli", "Gabala", "Oghuz"]
},
"Cuba": {
  "Havana": ["Havana", "Guanabacoa", "Regla", "San Miguel del Padrón", "Boyeros", "Arroyo Naranjo", "La Lisa", "Playa", "Plaza de la Revolución", "Marianao"],
  "Santiago de Cuba": ["Santiago de Cuba", "Palma Soriano", "San Luis", "Contramaestre", "Guamá", "Mella", "Segundo Frente", "Songo-La Maya", "Tercer Frente", "El Cobre"],
  "Camagüey": ["Camagüey", "Florida", "Guáimaro", "Jimaguayú", "Minas", "Najasa", "Nuevitas", "Santa Cruz del Sur", "Sibanicú", "Vertientes"],
  "Holguín": ["Holguín", "Banes", "Antilla", "Cacocum", "Calixto García", "Cueto", "Frank País", "Gibara", "Mayarí", "Moa"],
  "Villa Clara": ["Santa Clara", "Placetas", "Sagua la Grande", "Remedios", "Caibarién", "Camajuaní", "Cifuentes", "Corralillo", "Encrucijada", "Manicaragua"],
  "Pinar del Río": ["Pinar del Río", "Consolación del Sur", "Guane", "La Palma", "Los Palacios", "Mantua", "Minas de Matahambre", "San Juan y Martínez", "San Luis", "Viñales"],
  "Matanzas": ["Matanzas", "Cárdenas", "Colón", "Jagüey Grande", "Jovellanos", "Limonar", "Los Arabos", "Martí", "Pedro Betancourt", "Perico"],
  "Cienfuegos": ["Cienfuegos", "Aguada de Pasajeros", "Cruces", "Cumanayagua", "Lajas", "Palmira", "Rodas", "Santa Isabel de las Lajas", "Abreus", "Cienfuegos"],
  "Granma": ["Bayamo", "Manzanillo", "Bartolomé Masó", "Campechuela", "Cauto Cristo", "Guisa", "Jiguaní", "Media Luna", "Niquero", "Pilón"],
  "Las Tunas": ["Las Tunas", "Amancio", "Colombia", "Jesús Menéndez", "Jobabo", "Majibacoa", "Manatí", "Puerto Padre", "Las Tunas", "Amancio"]
},
"Dominican Republic": {
  "Santo Domingo": ["Santo Domingo", "Boca Chica", "Los Alcarrizos", "San Antonio de Guerra", "Pedro Brand", "San Cristóbal", "Baní", "Bajos de Haina", "Villa Altagracia", "San Gregorio de Nigua"],
  "Santiago": ["Santiago de los Caballeros", "Tamboril", "Villa González", "Jánico", "San José de las Matas", "Puñal", "Licey al Medio", "Sabana Iglesia", "Bisonó", "Villa Bisonó"],
  "La Vega": ["La Vega", "Constanza", "Jarabacoa", "Moca", "San Víctor", "Rincón", "Cotuí", "Fantino", "Cevicos", "Piedra Blanca"],
  "Puerto Plata": ["Puerto Plata", "Sosúa", "Cabarete", "Imbert", "Altamira", "Luperón", "Villa Isabela", "Guananico", "Los Hidalgos", "Villa Montellano"],
  "San Pedro de Macorís": ["San Pedro de Macorís", "Guayacanes", "Quisqueya", "Consuelo", "Los Llanos", "Ramón Santana", "Juan Dolio", "San José de los Llanos", "La Romana", "Boca Chica"],
  "La Altagracia": ["Higüey", "Punta Cana", "Bávaro", "Verón", "La Otra Banda", "San Rafael del Yuma", "Bayahibe", "La Romana", "Boca de Yuma", "Miches"],
  "San Juan": ["San Juan de la Maguana", "Bohechío", "El Cercado", "Juan de Herrera", "Las Matas de Farfán", "Vallejuelo", "San Juan", "Bohechío", "El Cercado", "Juan de Herrera"],
  "Duarte": ["San Francisco de Macorís", "Arenoso", "Castillo", "Hostos", "Las Guáranas", "Pimentel", "Villa Riva", "San Francisco de Macorís", "Arenoso", "Castillo"],
  "Espaillat": ["Moca", "Cayetano Germosén", "Gaspar Hernández", "Jamao al Norte", "San Víctor", "Moca", "Cayetano Germosén", "Gaspar Hernández", "Jamao al Norte", "San Víctor"],
  "Barahona": ["Barahona", "Cabral", "El Peñón", "Enriquillo", "Fundación", "Jaquimeyes", "La Ciénaga", "Las Salinas", "Paraíso", "Polo"]
},
"Haiti": {
  "Ouest": ["Port-au-Prince", "Carrefour", "Delmas", "Pétion-Ville", "Gressier", "Kenscoff", "Tabarre", "Cité Soleil", "Croix-des-Bouquets", "Léogâne"],
  "Artibonite": ["Gonaïves", "Saint-Marc", "Verrettes", "Dessalines", "Petite-Rivière-de-l'Artibonite", "Gros-Morne", "Anse-Rouge", "Marmelade", "Saint-Michel-de-l'Attalaye", "Ennery"],
  "Nord": ["Cap-Haïtien", "Limbé", "Fort-Liberté", "Grande-Rivière-du-Nord", "Acul-du-Nord", "Milot", "Plaine-du-Nord", "Quartier-Morin", "Dondon", "Limonade"],
  "Nord-Est": ["Ouanaminthe", "Trou-du-Nord", "Fort-Liberté", "Ferrier", "Caracol", "Terrier-Rouge", "Mombin-Crochu", "Capotille", "Mont-Organisé", "Carice"],
  "Sud": ["Les Cayes", "Aquin", "Cavaillon", "Saint-Louis-du-Sud", "Port-Salut", "Chantal", "Torbeck", "Île-à-Vache", "Camp-Perrin", "Chardonnières"],
  "Sud-Est": ["Jacmel", "Marigot", "Bainet", "Belle-Anse", "Côtes-de-Fer", "Thiotte", "La Vallée", "Grand-Gosier", "Anse-à-Pitre", "Belle-Anse"],
  "Centre": ["Hinche", "Mirebalais", "Lascahobas", "Cerca-la-Source", "Boucan-Carré", "Savanette", "Thomassique", "Cerca-Cavajal", "Maïssade", "Belladère"],
  "Grand'Anse": ["Jérémie", "Anse-d'Hainault", "Dame-Marie", "Les Irois", "Corail", "Beaumont", "Pestel", "Moron", "Chambellan", "Bonbon"],
  "Nippes": ["Miragoâne", "Baradères", "Petite-Rivière-de-Nippes", "Fonds-des-Nègres", "Paillant", "L'Asile", "Arnaud", "Plaisance", "Petite-Rivière-de-Nippes", "Fonds-des-Nègres"],
  "Nord-Ouest": ["Port-de-Paix", "Saint-Louis-du-Nord", "Jean-Rabel", "Môle-Saint-Nicolas", "Bombardopolis", "Anse-à-Foleur", "Chansolme", "La Tortue", "Baie-de-Henne", "Bassin-Bleu"]
},
"Jamaica": {
  "Kingston": ["Kingston", "Portmore", "Spanish Town", "Half Way Tree", "New Kingston", "Cross Roads", "Stony Hill", "Constant Spring", "Duhaney Park", "Papine"],
  "St. Andrew": ["Kingston", "Half Way Tree", "Papine", "Mona", "Hope Pastures", "Beverly Hills", "Barbican", "Constant Spring", "Stony Hill", "Golden Spring"],
  "St. Catherine": ["Spanish Town", "Portmore", "Old Harbour", "Linstead", "Bog Walk", "Ewarton", "Old Harbour Bay", "Greater Portmore", "Caymanas", "Gregory Park"],
  "Clarendon": ["May Pen", "Chapelton", "Frankfield", "Kellits", "Rock River", "Alston", "Mocho", "Toll Gate", "Race Course", "Hayes"],
  "Manchester": ["Mandeville", "Christiana", "Williamsfield", "Porus", "Alligator Pond", "Spaldings", "Greenvale", "Gutters", "Pike", "Crawford"],
  "St. Elizabeth": ["Black River", "Santa Cruz", "Malvern", "Junction", "Lacovia", "Nain", "Bamboo", "Balaclava", "Maggotty", "Southfield"],
  "Westmoreland": ["Savanna-la-Mar", "Negril", "Frome", "Bluefields", "Grange Hill", "Bethel Town", "Darliston", "Whitehouse", "Little London", "Petersfield"],
  "St. James": ["Montego Bay", "Falmouth", "Irwin", "Cambridge", "Adelphi", "Granville", "Reading", "Catherine Hall", "Rose Hall", "Bogue"],
  "Trelawny": ["Falmouth", "Duncans", "Wakefield", "Clarks Town", "Albert Town", "Ulster Spring", "Windsor", "Rio Bueno", "Martha Brae", "Bounty Hall"],
  "Portland": ["Port Antonio", "Buff Bay", "Hope Bay", "Manchioneal", "Long Bay", "Moore Town", "Boston", "Fairy Hill", "St. Margaret's Bay", "Boundbrook"]
},
"Trinidad and Tobago": {
  "Port of Spain": ["Port of Spain", "San Juan", "Laventille", "Tunapuna", "Arouca", "Arima", "Chaguanas", "Couva", "Point Fortin", "Diego Martin"],
  "San Fernando": ["San Fernando", "Marabella", "Princes Town", "Debe", "Penal", "Siparia", "La Brea", "Fyzabad", "Point Fortin", "Couva"],
  "Chaguanas": ["Chaguanas", "Couva", "Preysal", "California", "Felicity", "Enterprise", "Charlieville", "Longdenville", "Cunupia", "Caroni"],
  "Arima": ["Arima", "Arouca", "Tunapuna", "D'Abadie", "Maloney", "O'Meara", "Piarco", "Caura", "Tacarigua", "St. Augustine"],
  "Tobago": ["Scarborough", "Roxborough", "Charlotteville", "Plymouth", "Buccoo", "Crown Point", "Black Rock", "Moriah", "Bethel", "Pembroke"],
  "Couva-Tabaquite-Talparo": ["Couva", "Tabaquite", "Talparo", "Preysal", "California", "Felicity", "Enterprise", "Charlieville", "Longdenville", "Cunupia"],
  "Diego Martin": ["Diego Martin", "Petit Valley", "Carenage", "Glencoe", "Maraval", "St. Lucien", "Moka", "Westmoorings", "Goodwood Park", "Diamond Vale"],
  "Penal-Debe": ["Penal", "Debe", "Siparia", "Fyzabad", "La Brea", "Point Fortin", "Rousillac", "San Francique", "Vistabella", "Claxton Bay"],
  "Sangre Grande": ["Sangre Grande", "Manzanilla", "Guayaguayare", "Toco", "Matura", "Rio Claro", "Biche", "Mayaro", "Cumuto", "Tamarind Tree"],
  "Princes Town": ["Princes Town", "Moruga", "Tableland", "Palo Seco", "Barrackpore", "New Grant", "Claxton Bay", "Rousillac", "San Francique", "Vistabella"]
},
"Costa Rica": {
  "San José": ["San José", "Escazú", "Desamparados", "Puriscal", "Tarrazú", "Aserrí", "Mora", "Goicoechea", "Santa Ana", "Alajuelita"],
  "Alajuela": ["Alajuela", "San Ramón", "Grecia", "San Mateo", "Atenas", "Naranjo", "Palmares", "Poás", "Orotina", "San Carlos"],
  "Cartago": ["Cartago", "Paraíso", "La Unión", "Jiménez", "Turrialba", "Alvarado", "Oreamuno", "El Guarco", "Cartago", "Paraíso"],
  "Heredia": ["Heredia", "Barva", "Santo Domingo", "Santa Bárbara", "San Rafael", "San Isidro", "Belén", "Flores", "San Pablo", "Sarapiquí"],
  "Guanacaste": ["Liberia", "Nicoya", "Santa Cruz", "Bagaces", "Carrillo", "Cañas", "Abangares", "Tilarán", "Nandayure", "La Cruz"],
  "Puntarenas": ["Puntarenas", "Esparza", "Buenos Aires", "Montes de Oro", "Osa", "Quepos", "Golfito", "Coto Brus", "Parrita", "Corredores"],
  "Limón": ["Limón", "Pococí", "Siquirres", "Talamanca", "Matina", "Guácimo", "Limón", "Pococí", "Siquirres", "Talamanca"],
  "San José Province": ["San José", "Escazú", "Desamparados", "Puriscal", "Tarrazú", "Aserrí", "Mora", "Goicoechea", "Santa Ana", "Alajuelita"],
  "Alajuela Province": ["Alajuela", "San Ramón", "Grecia", "San Mateo", "Atenas", "Naranjo", "Palmares", "Poás", "Orotina", "San Carlos"],
  "Cartago Province": ["Cartago", "Paraíso", "La Unión", "Jiménez", "Turrialba", "Alvarado", "Oreamuno", "El Guarco", "Cartago", "Paraíso"]
},
"Panama": {
  "Panamá": ["Panamá City", "San Miguelito", "Tocumen", "Las Cumbres", "Pacora", "Chilibre", "Arraiján", "La Chorrera", "Capira", "Chame"],
  "Colón": ["Colón", "Portobelo", "Chagres", "Donoso", "Santa Isabel", "Omar Torrijos Herrera", "Colón", "Portobelo", "Chagres", "Donoso"],
  "Darién": ["La Palma", "Yaviza", "Chepigana", "Pinogana", "Santa Fe", "Chepigana", "Pinogana", "Santa Fe", "La Palma", "Yaviza"],
  "Chiriquí": ["David", "Boquete", "Volcán", "Gualaca", "Bugaba", "Dolega", "Alanje", "Barú", "Renacimiento", "Tierras Altas"],
  "Veraguas": ["Santiago", "Atalaya", "Calobre", "Cañazas", "La Mesa", "Las Palmas", "Mariato", "Montijo", "Río de Jesús", "San Francisco"],
  "Bocas del Toro": ["Bocas del Toro", "Changuinola", "Almirante", "Bastimentos", "Chiriquí Grande", "Bocas del Toro", "Changuinola", "Almirante", "Bastimentos", "Chiriquí Grande"],
  "Coclé": ["Penonomé", "Aguadulce", "Antón", "La Pintada", "Natá", "Olá", "Coclé", "Penonomé", "Aguadulce", "Antón"],
  "Herrera": ["Chitré", "Las Minas", "Los Pozos", "Ocú", "Parita", "Pesé", "Santa María", "Chitré", "Las Minas", "Los Pozos"],
  "Los Santos": ["Las Tablas", "Guararé", "Tonosí", "Macaracas", "Pedasí", "Pocrí", "Los Santos", "Las Tablas", "Guararé", "Tonosí"],
  "Ngäbe-Buglé": ["Chichica", "Kankintú", "Kusapín", "Mironó", "Müna", "Nole Düima", "Ñürüm", "Besiko", "Kädri", "Nidori"]
},
"El Salvador": {
  "San Salvador": ["San Salvador", "Soyapango", "Santa Tecla", "Mejicanos", "Apopa", "Delgado", "Cuscatancingo", "Ayutuxtepeque", "Ilopango", "San Marcos"],
  "Santa Ana": ["Santa Ana", "Chalchuapa", "Metapán", "Coatepeque", "El Congo", "Texistepeque", "Candelaria de la Frontera", "Masahuat", "San Sebastián Salitrillo", "Santiago de la Frontera"],
  "San Miguel": ["San Miguel", "Usulután", "Chinameca", "Santiago de María", "Quelepa", "Moncagua", "Chapeltique", "Lolotique", "Nueva Guadalupe", "San Jorge"],
  "La Libertad": ["Santa Tecla", "Antiguo Cuscatlán", "Nuevo Cuscatlán", "Zaragoza", "Colón", "Quezaltepeque", "San Juan Opico", "Ciudad Arce", "Huizúcar", "Jayaque"],
  "Sonsonate": ["Sonsonate", "Acajutla", "Izalco", "Nahuizalco", "Armenia", "Juayúa", "Santo Domingo de Guzmán", "Sonzacate", "Caluco", "Santa Catarina Masahuat"],
  "Ahuachapán": ["Ahuachapán", "Atiquizaya", "Apaneca", "Concepción de Ataco", "Tacuba", "Turín", "Guaymango", "Jujutla", "San Francisco Menéndez", "San Lorenzo"],
  "Cuscatlán": ["Cojutepeque", "Suchitoto", "San Pedro Perulapán", "San Rafael Cedros", "San Bartolomé Perulapía", "San José Guayabal", "Santa Cruz Michapa", "Tenancingo", "El Carmen", "Monte San Juan"],
  "La Paz": ["Zacatecoluca", "Olocuilta", "San Pedro Masahuat", "San Luis La Herradura", "San Juan Nonualco", "Santiago Nonualco", "San Miguel Tepezontes", "Mercedes La Ceiba", "San Juan Talpa", "San Rafael Obrajuelo"],
  "Usulután": ["Usulután", "Jucuapa", "Santiago de María", "Jiquilisco", "Ozatlán", "Santa Elena", "Ereguayquín", "Concepción Batres", "San Dionisio", "San Francisco Javier"],
  "Morazán": ["San Francisco Gotera", "Cacaopera", "Chilanga", "Jocoro", "Sociedad", "El Divisadero", "Guatajiagua", "Osicala", "San Carlos", "San Simón"]
},
"Honduras": {
  "Tegucigalpa": ["Tegucigalpa", "Comayagüela", "Santa Lucía", "Valle de Ángeles", "Ojojona", "San Juancito", "Tatumbla", "Curarén", "San Antonio de Oriente", "Cedros"],
  "San Pedro Sula": ["San Pedro Sula", "Choloma", "Villanueva", "La Lima", "El Progreso", "Puerto Cortés", "Omoa", "Pimienta", "Potrerillos", "Santa Cruz de Yojoa"],
  "La Ceiba": ["La Ceiba", "Tela", "Trujillo", "Olanchito", "Juticalpa", "Roatán", "Utila", "Guanaja", "Sonaguera", "Tocoa"],
  "Choluteca": ["Choluteca", "El Triunfo", "Marcovia", "Namasigüe", "Pespire", "San Lorenzo", "Duyure", "Morolica", "Apacilagua", "Concepción de María"],
  "Comayagua": ["Comayagua", "Siguatepeque", "La Paz", "Santa Rosa de Copán", "Gracias", "San Pedro Sula", "La Esperanza", "Yarumela", "Esquías", "Lejamaní"],
  "Copán": ["Santa Rosa de Copán", "Copán Ruinas", "La Entrada", "Cabañas", "Dulce Nombre", "San Agustín", "San Antonio", "San Jerónimo", "San José", "San Juan de Opoa"],
  "Olancho": ["Juticalpa", "Catacamas", "Campamento", "San Esteban", "Gualaco", "Guata", "Jano", "La Unión", "Mangulile", "Patuca"],
  "Cortés": ["San Pedro Sula", "Choloma", "Villanueva", "La Lima", "El Progreso", "Puerto Cortés", "Omoa", "Pimienta", "Potrerillos", "Santa Cruz de Yojoa"],
  "Yoro": ["Yoro", "El Progreso", "Olanchito", "Jocón", "Morazán", "Victoria", "El Negrito", "Santa Rita", "Sulaco", "Yorito"],
  "Atlántida": ["La Ceiba", "Tela", "Trujillo", "Olanchito", "Juticalpa", "Roatán", "Utila", "Guanaja", "Sonaguera", "Tocoa"]
},
"Nicaragua": {
  "Managua": ["Managua", "Ciudad Sandino", "Tipitapa", "San Rafael del Sur", "Ticuantepe", "El Crucero", "Villa El Carmen", "Mateare", "San Francisco Libre", "Valle de Ticuantep"],
  "León": ["León", "La Paz Centro", "Nagarote", "El Sauce", "Larreynaga", "Achuapa", "Santa Rosa del Peñón", "El Jicaral", "Quezalguaque", "Telica"],
  "Chinandega": ["Chinandega", "El Viejo", "Corinto", "Chichigalpa", "Posoltega", "El Realejo", "Villanueva", "Somotillo", "Santo Tomás del Norte", "Cinco Pinos"],
  "Masaya": ["Masaya", "Nindirí", "Catarina", "San Juan de Oriente", "Niquinohomo", "Tisma", "La Concepción", "Masatepe", "Nandasmo", "San Marcos"],
  "Granada": ["Granada", "Nandaime", "Diriomo", "Diriá", "El Rosario", "Santa Teresa", "Nandaime", "Diriomo", "Diriá", "El Rosario"],
  "Carazo": ["Jinotepe", "Diriamba", "San Marcos", "Santa Teresa", "Dolores", "La Paz de Carazo", "El Rosario", "La Conquista", "Jinotepe", "Diriamba"],
  "Rivas": ["Rivas", "San Jorge", "San Juan del Sur", "Cárdenas", "Moyogalpa", "Altagracia", "Belén", "Buenos Aires", "Potosí", "Tola"],
  "Matagalpa": ["Matagalpa", "San Ramón", "Matiguás", "Muy Muy", "Esquipulas", "San Dionisio", "Sébaco", "Ciudad Darío", "Terrabona", "San Isidro"],
  "Jinotega": ["Jinotega", "San Rafael del Norte", "San Sebastián de Yalí", "La Concordia", "El Cuá", "Wiwilí", "Santa María de Pantasma", "San José de Bocay", "El Cua", "Wiwilí"],
  "Estelí": ["Estelí", "Condega", "Pueblo Nuevo", "San Juan de Limay", "La Trinidad", "San Nicolás", "Estelí", "Condega", "Pueblo Nuevo", "San Juan de Limay"]
},
"Paraguay": {
  "Asunción": ["Asunción", "Lambaré", "Fernando de la Mora", "Luque", "San Lorenzo", "Capiatá", "Ñemby", "Mariano Roque Alonso", "Villa Elisa", "Itauguá"],
  "Concepción": ["Concepción", "Horqueta", "Belén", "Loreto", "San Lázaro", "Azotey", "Yby Yaú", "Bella Vista", "San Carlos", "Arroyito"],
  "San Pedro": ["San Pedro de Ycuamandiyú", "Antequera", "Choré", "General Elizardo Aquino", "Guayaibí", "Itacurubí del Rosario", "Lima", "Nueva Germania", "San Estanislao", "Tacuatí"],
  "Cordillera": ["Caacupé", "Atyrá", "Caraguatay", "Emboscada", "Eusebio Ayala", "Isla Pucú", "Itacurubí de la Cordillera", "Juan de Mena", "Loma Grande", "Piribebuy"],
  "Guairá": ["Villarrica", "Borja", "Colonia Independencia", "Itapé", "Iturbe", "Mbocayaty", "Natalicio Talavera", "Ñumí", "Paso Yobái", "San Salvador"],
  "Caaguazú": ["Coronel Oviedo", "Caaguazú", "Carayaó", "Doctor Cecilio Báez", "Doctor Juan Manuel Frutos", "José Domingo Ocampos", "La Pastora", "Marechal Estigarribia", "Nueva Londres", "Raúl Arsenio Oviedo"],
  "Itapúa": ["Encarnación", "Bella Vista", "Cambyretá", "Capitán Miranda", "Carlos Antonio López", "Carmen del Paraná", "Coronel Bogado", "Fram", "General Artigas", "General Delgado"],
  "Misiones": ["San Juan Bautista", "Ayolas", "San Ignacio", "Santa María", "Santa Rosa", "Santiago", "Villa Florida", "Yabebyry", "San Miguel", "San Patricio"],
  "Paraguarí": ["Paraguarí", "Acahay", "Caapucú", "Carapeguá", "Escobar", "La Colmena", "Mbuyapey", "Pirayú", "Quiindy", "Sapucai"],
  "Alto Paraná": ["Ciudad del Este", "Hernandarias", "Minga Guazú", "Presidente Franco", "San Alberto", "San Cristóbal", "Santa Rita", "Yguazú", "Naranjal", "Juan León Mallorquín"]
},
"Uruguay": {
  "Montevideo": ["Montevideo", "Ciudad Vieja", "Pocitos", "Punta Carretas", "Carrasco", "Malvín", "Parque Rodó", "Cerro", "Prado", "Buceo"],
  "Canelones": ["Canelones", "Santa Lucía", "Las Piedras", "Pando", "La Paz", "Barros Blancos", "Progreso", "Tala", "San Ramón", "Aguas Corrientes"],
  "Maldonado": ["Maldonado", "Punta del Este", "San Carlos", "Piriápolis", "Pan de Azúcar", "Aiguá", "Solis de Mataojo", "Cerro Pelado", "Gregorio Aznárez", "Garzón"],
  "Salto": ["Salto", "Belén", "Constitución", "Daymán", "San Antonio", "Colonia Lavalleja", "Pueblo Fernández", "Rincón de Valentín", "Saucedo", "Cerro de Vera"],
  "Colonia": ["Colonia del Sacramento", "Carmelo", "Nueva Helvecia", "Rosario", "Juan Lacaze", "Florencio Sánchez", "Tarariras", "Ombúes de Lavalle", "Colonia Valdense", "Conchillas"],
  "Paysandú": ["Paysandú", "Guichón", "Quebracho", "Porvenir", "Tambores", "Piedras Coloradas", "Lorenzo Geyres", "Chapicuy", "Nico Pérez", "Cerro Chato"],
  "Rocha": ["Rocha", "Chuy", "Castillos", "Lascano", "La Paloma", "Cebollatí", "18 de Julio", "Velázquez", "San Luis al Medio", "La Coronilla"],
  "Rivera": ["Rivera", "Tranqueras", "Vichadero", "Minas de Corrales", "La Pedrera", "Mandubí", "Masoller", "Santa Teresa", "Laguna del Sauce", "Cerro Pelado"],
  "Tacuarembó": ["Tacuarembó", "Paso de los Toros", "San Gregorio de Polanco", "Ansina", "Curtina", "Tambores", "Achar", "Piedras Coloradas", "Laureles", "Valle Edén"],
  "Artigas": ["Artigas", "Bella Unión", "Tomás Gomensoro", "Baltasar Brum", "Sequeira", "Las Piedras", "Pintadito", "Cerro de las Cuentas", "Cerro Chato", "Cerro de Vera"]
},
"Bolivia": {
  "La Paz": ["La Paz", "El Alto", "Viacha", "Achocalla", "Mecapaca", "Palca", "Laja", "Pucarani", "Batallas", "Caranavi"],
  "Santa Cruz": ["Santa Cruz de la Sierra", "Montero", "Warnes", "La Guardia", "Cotoca", "El Torno", "Portachuelo", "San Ignacio de Velasco", "San José de Chiquitos", "Roboré"],
  "Cochabamba": ["Cochabamba", "Quillacollo", "Sacaba", "Colcapirhua", "Tiquipaya", "Vinto", "Sipe Sipe", "Punata", "Aiquile", "Cliza"],
  "Oruro": ["Oruro", "Caracollo", "Challapata", "Huanuni", "Pazña", "Poopó", "Santiago de Huari", "Totora", "Machacamarca", "El Choro"],
  "Potosí": ["Potosí", "Uyuni", "Tupiza", "Villazón", "Colchani", "Llallagua", "Betanzos", "Atocha", "Tinguipaya", "Cotagaita"],
  "Tarija": ["Tarija", "Yacuiba", "Bermejo", "Villamontes", "Padcaya", "Entre Ríos", "San Lorenzo", "El Puente", "Uriondo", "Caraparí"],
  "Chuquisaca": ["Sucre", "Monteagudo", "Yotala", "Tarabuco", "Camargo", "Villa Serrano", "Zudañez", "Padilla", "Tarabuco", "Yotala"],
  "Beni": ["Trinidad", "Riberalta", "Guayaramerín", "San Borja", "Santa Ana de Yacuma", "San Ignacio de Moxos", "San Joaquín", "Magdalena", "Baures", "Loreto"],
  "Pando": ["Cobija", "Porvenir", "Bella Flor", "Filadelfia", "Santos Mercado", "Nueva Esperanza", "Villa Nueva", "El Sena", "San Lorenzo", "San Pedro"],
  "Tarija": ["Tarija", "Yacuiba", "Bermejo", "Villamontes", "Padcaya", "Entre Ríos", "San Lorenzo", "El Puente", "Uriondo", "Caraparí"]
},
"Ecuador": {
  "Pichincha": ["Quito", "Cayambe", "Machachi", "Sangolquí", "Tabacundo", "Pedro Moncayo", "Rumiñahui", "Mejía", "Puerto Quito", "San Miguel de los Bancos"],
  "Guayas": ["Guayaquil", "Durán", "Samborondón", "Daule", "Milagro", "Yaguachi", "Nobol", "Salitre", "Santa Lucía", "El Triunfo"],
  "Azuay": ["Cuenca", "Gualaceo", "Paute", "Sigsig", "Chordeleg", "Girón", "Santa Isabel", "Oña", "Pucará", "San Fernando"],
  "Manabí": ["Portoviejo", "Manta", "Montecristi", "Jaramijó", "Chone", "Bahía de Caráquez", "Rocafuerte", "Calceta", "Jipijapa", "Pedernales"],
  "El Oro": ["Machala", "Santa Rosa", "Pasaje", "Huaquillas", "Arenillas", "Piñas", "Zaruma", "Portovelo", "Balsas", "Marcabelí"],
  "Tungurahua": ["Ambato", "Baños", "Pelileo", "Píllaro", "Cevallos", "Quero", "Mocha", "Tisaleo", "Patate", "Huambaló"],
  "Loja": ["Loja", "Catamayo", "Zapotillo", "Cariamanga", "Calvas", "Paltas", "Puyango", "Macará", "Saraguro", "Chaguarpamba"],
  "Imbabura": ["Ibarra", "Otavalo", "Cotacachi", "Atuntaqui", "Urcuquí", "Pimampiro", "Antonio Ante", "San Miguel de Urcuquí", "Cotacachi", "Otavalo"],
  "Esmeraldas": ["Esmeraldas", "Atacames", "Muisne", "Quinindé", "San Lorenzo", "Río Verde", "Eloy Alfaro", "Montalvo", "La Concordia", "Valdez"],
  "Santo Domingo de los Tsáchilas": ["Santo Domingo", "La Concordia", "Alluriquín", "Luz de América", "Valle Hermoso", "San Jacinto del Búa", "El Carmen", "La Independencia", "Quinindé", "La Concordia"]
},
"Venezuela": {
  "Caracas": ["Caracas", "Petare", "Baruta", "Chacao", "El Hatillo", "Caucagüita", "Guarenas", "Guatire", "Los Teques", "San Antonio de los Altos"],
  "Zulia": ["Maracaibo", "Cabimas", "Ciudad Ojeda", "Santa Bárbara del Zulia", "Machiques", "La Concepción", "San Francisco", "Lagunillas", "Mene Grande", "Villa del Rosario"],
  "Miranda": ["Los Teques", "Guarenas", "Guatire", "Ocumare del Tuy", "Santa Teresa del Tuy", "Cúa", "Charallave", "San Antonio de los Altos", "Baruta", "El Hatillo"],
  "Lara": ["Barquisimeto", "Carora", "Quíbor", "El Tocuyo", "Cabudare", "Duaca", "Sanare", "Sarare", "Siquisique", "Urdaneta"],
  "Aragua": ["Maracay", "Turmero", "La Victoria", "El Limón", "Cagua", "Villa de Cura", "Palo Negro", "San Mateo", "Santa Cruz", "Tocorón"],
  "Carabobo": ["Valencia", "Puerto Cabello", "Guacara", "Los Guayos", "Mariara", "San Diego", "Bejuma", "Tocuyito", "Naguanagua", "Montalbán"],
  "Bolívar": ["Ciudad Guayana", "Ciudad Bolívar", "Upata", "El Callao", "Santa Elena de Uairén", "Tumeremo", "Guasipati", "El Dorado", "Maripa", "Kavanayén"],
  "Táchira": ["San Cristóbal", "Rubio", "Táriba", "La Fría", "Colón", "Palmira", "San Antonio del Táchira", "Ureña", "Capacho", "Santa Ana del Táchira"],
  "Mérida": ["Mérida", "El Vigía", "Tovar", "Ejido", "Lagunillas", "Santa Cruz de Mora", "Bailadores", "Zea", "Mucuchíes", "Timotes"],
  "Anzoátegui": ["Barcelona", "Puerto La Cruz", "Lechería", "El Tigre", "Anaco", "Cantaura", "Guanta", "Pariaguán", "San José de Guanipa", "Santa Ana"]
},
"Chile": {
  "Santiago": ["Santiago", "Puente Alto", "Maipú", "Las Condes", "Providencia", "La Florida", "Ñuñoa", "San Bernardo", "Peñalolén", "La Pintana"],
  "Valparaíso": ["Valparaíso", "Viña del Mar", "Quilpué", "Villa Alemana", "San Antonio", "Quillota", "Los Andes", "La Calera", "Limache", "Concón"],
  "Biobío": ["Concepción", "Talcahuano", "Chillán", "Los Ángeles", "Coronel", "San Pedro de la Paz", "Lota", "Lebu", "Arauco", "Cañete"],
  "Maule": ["Talca", "Curicó", "Linares", "Constitución", "Cauquenes", "Parral", "San Javier", "Molina", "Rauco", "Longaví"],
  "Araucanía": ["Temuco", "Padre Las Casas", "Villarrica", "Angol", "Pucón", "Victoria", "Lautaro", "Nueva Imperial", "Collipulli", "Pitrufquén"],
  "Los Lagos": ["Puerto Montt", "Osorno", "Puerto Varas", "Ancud", "Castro", "Quellón", "Frutillar", "Calbuco", "Llanquihue", "Purranque"],
  "Coquimbo": ["La Serena", "Coquimbo", "Ovalle", "Illapel", "Vicuña", "Salamanca", "Los Vilos", "Andacollo", "Combarbalá", "Monte Patria"],
  "Antofagasta": ["Antofagasta", "Calama", "Tocopilla", "Mejillones", "San Pedro de Atacama", "Taltal", "Maria Elena", "Sierra Gorda", "Ollagüe", "Antofagasta"],
  "Atacama": ["Copiapó", "Vallenar", "Caldera", "Chañaral", "Diego de Almagro", "Tierra Amarilla", "Huasco", "Alto del Carmen", "Freirina", "Caldera"],
  "Magallanes": ["Punta Arenas", "Puerto Natales", "Porvenir", "Puerto Williams", "Cabo de Hornos", "Timaukel", "Río Verde", "San Gregorio", "Laguna Blanca", "Primavera"]
},
"Peru": {
  "Lima": ["Lima", "Callao", "Ate", "Barranco", "Comas", "Chorrillos", "La Molina", "Lince", "Miraflores", "San Isidro"],
  "Arequipa": ["Arequipa", "Camaná", "Mollendo", "Chivay", "Cayma", "Cerro Colorado", "Characato", "Yanahuara", "Socabaya", "Jesús María"],
  "Cusco": ["Cusco", "Sacsayhuamán", "Ollantaytambo", "Pisac", "Urubamba", "Machu Picchu", "Calca", "Chinchero", "Maras", "Yucay"],
  "La Libertad": ["Trujillo", "Chepén", "Pacasmayo", "Guadalupe", "Virú", "Otuzco", "Sánchez Carrión", "Julcán", "Gran Chimú", "Santiago de Chuco"],
  "Piura": ["Piura", "Sullana", "Paita", "Talara", "Catacaos", "Chulucanas", "Sechura", "La Unión", "Morropón", "Huancabamba"],
  "Lambayeque": ["Chiclayo", "Lambayeque", "Ferreñafe", "Monsefú", "Santa Rosa", "Eten", "Picsi", "Túcume", "Pimentel", "Olmos"],
  "Ancash": ["Huaraz", "Chimbote", "Caraz", "Yungay", "Casma", "Huaraz", "Carhuaz", "Recuay", "Aija", "Bolognesi"],
  "Junín": ["Huancayo", "Jauja", "Tarma", "La Oroya", "Satipo", "Chanchamayo", "Concepción", "San Jerónimo de Tunán", "Chupaca", "Junín"],
  "Puno": ["Puno", "Juliaca", "Ilave", "Azángaro", "Yunguyo", "Lampa", "Huancané", "Chucuito", "San Román", "Melgar"],
  "Ica": ["Ica", "Chincha Alta", "Pisco", "Nazca", "Palpa", "Paracas", "San Juan Bautista", "Santiago", "Subtanjalla", "Tate"]
},
"Colombia": {
  "Bogotá": ["Bogotá", "Usaquén", "Chapinero", "Santa Fe", "San Cristóbal", "Usme", "Tunjuelito", "Bosa", "Kennedy", "Fontibón"],
  "Antioquia": ["Medellín", "Bello", "Itagüí", "Envigado", "Rionegro", "La Estrella", "Sabaneta", "Copacabana", "Girardota", "Barbosa"],
  "Valle del Cauca": ["Cali", "Palmira", "Buenaventura", "Tuluá", "Cartago", "Buga", "Yumbo", "Jamundí", "Florida", "Pradera"],
  "Cundinamarca": ["Soacha", "Facatativá", "Girardot", "Fusagasugá", "Zipaquirá", "Chía", "Mosquera", "Madrid", "Funza", "Cajicá"],
  "Santander": ["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta", "Barrancabermeja", "San Gil", "Socorro", "Málaga", "Barbosa", "Rionegro"],
  "Bolívar": ["Cartagena", "Magangué", "Turbaco", "Arjona", "Carmen de Bolívar", "San Juan Nepomuceno", "El Carmen de Bolívar", "Santa Rosa del Sur", "San Jacinto", "María la Baja"],
  "Atlántico": ["Barranquilla", "Soledad", "Malambo", "Sabanalarga", "Puerto Colombia", "Baranoa", "Galapa", "Palmar de Varela", "Santo Tomás", "Ponedera"],
  "Nariño": ["Pasto", "Tumaco", "Ipiales", "Samaniego", "La Unión", "Sandona", "Túquerres", "Buesaco", "Chachagüí", "Yacuanquer"],
  "Córdoba": ["Montería", "Cereté", "Sahagún", "Lorica", "Planeta Rica", "Tierralta", "Montelíbano", "Puerto Libertador", "San Andrés de Sotavento", "Chinú"],
  "Tolima": ["Ibagué", "Espinal", "Honda", "Mariquita", "Líbano", "Fresno", "Chaparral", "Melgar", "Guamo", "Armero"]
},
"Argentina": {
  "Buenos Aires": ["Buenos Aires", "La Plata", "Mar del Plata", "Quilmes", "Banfield", "Merlo", "Morón", "Avellaneda", "San Isidro", "Tigre"],
  "Córdoba": ["Córdoba", "Río Cuarto", "Villa María", "San Francisco", "Alta Gracia", "Villa Carlos Paz", "Río Tercero", "Bell Ville", "Jesús María", "Cosquín"],
  "Santa Fe": ["Rosario", "Santa Fe", "Rafaela", "Venado Tuerto", "Reconquista", "Santo Tomé", "Esperanza", "Villa Gobernador Gálvez", "San Lorenzo", "Funes"],
  "Mendoza": ["Mendoza", "San Rafael", "Godoy Cruz", "Guaymallén", "Las Heras", "Luján de Cuyo", "Maipú", "Rivadavia", "Tunuyán", "San Martín"],
  "Tucumán": ["San Miguel de Tucumán", "Yerba Buena", "Concepción", "Aguilares", "Banda del Río Salí", "Tafí Viejo", "Monteros", "Famaillá", "Lules", "Simoca"],
  "Salta": ["Salta", "San Ramón de la Nueva Orán", "Tartagal", "Cafayate", "Metán", "Rosario de la Frontera", "Cerrillos", "General Güemes", "Chicoana", "La Caldera"],
  "Entre Ríos": ["Paraná", "Concordia", "Gualeguaychú", "Concepción del Uruguay", "Gualeguay", "Victoria", "Villaguay", "Nogoyá", "Federación", "Colón"],
  "Chaco": ["Resistencia", "Barranqueras", "Presidencia Roque Sáenz Peña", "Villa Ángela", "Charata", "General San Martín", "Quitilipi", "Machagai", "Las Breñas", "Tres Isletas"],
  "Corrientes": ["Corrientes", "Goya", "Mercedes", "Curuzú Cuatiá", "Paso de los Libres", "Monte Caseros", "Esquina", "Santo Tomé", "Ituzaingó", "Bella Vista"],
  "Misiones": ["Posadas", "Oberá", "Eldorado", "Puerto Iguazú", "Apóstoles", "Leandro N. Alem", "San Vicente", "Jardín América", "Aristóbulo del Valle", "Puerto Rico"]
},
"Cyprus": {
  "Nicosia": ["Nicosia", "Strovolos", "Lakatamia", "Latsia", "Aglandjia", "Engomi", "Morphou", "Kyrenia", "Kythrea", "Tseri"],
  "Limassol": ["Limassol", "Germasogeia", "Agios Athanasios", "Mesa Geitonia", "Kato Polemidia", "Ypsonas", "Parekklisha", "Episkopi", "Kolossi", "Erimi"],
  "Larnaca": ["Larnaca", "Aradippou", "Livadia", "Dromolaxia", "Kiti", "Pervolia", "Oroklini", "Xylofagou", "Athienou", "Lefkara"],
  "Paphos": ["Paphos", "Peyia", "Polis Chrysochous", "Geroskipou", "Tala", "Tsada", "Kissonerga", "Emba", "Chloraka", "Akoursos"],
  "Famagusta": ["Famagusta", "Paralimni", "Deryneia", "Ayia Napa", "Protaras", "Sotira", "Avgorou", "Liopetri", "Frenaros", "Acheritou"],
  "Kyrenia": ["Kyrenia", "Karavas", "Lapithos", "Bellapais", "Alsancak", "Ozanköy", "Çatalköy", "Lapta", "Ağırdağ", "Taşkent"],
  "Trikomo": ["Trikomo", "Lysi", "Vatili", "Ardana", "Galinoporni", "Koma tou Gialou", "Sinde", "Agios Iakovos", "Rizokarpaso", "Agios Andronikos"],
  "Lefka": ["Lefka", "Morphou", "Kato Zodeia", "Pano Zodeia", "Kato Pyrgos", "Pomos", "Kato Koutrafas", "Pano Koutrafas", "Kato Lefkara", "Pano Lefkara"],
  "Ammochostos": ["Famagusta", "Paralimni", "Deryneia", "Ayia Napa", "Protaras", "Sotira", "Avgorou", "Liopetri", "Frenaros", "Acheritou"],
  "Pitsilia": ["Agros", "Pelendri", "Platanistasa", "Alona", "Kyperounta", "Polystypos", "Dymes", "Kato Mylos", "Palaichori", "Askas"]
},
"Malta": {
  "Valletta": ["Valletta", "Floriana", "Marsa", "Paola", "Hamrun", "Sliema", "St. Julian's", "Gżira", "Ta' Xbiex", "Pembroke"],
  "Northern Region": ["St. Paul's Bay", "Mellieħa", "Mġarr", "Naxxar", "Mosta", "Għargħur", "Burmarrad", "Qawra", "Buġibba", "Xemxija"],
  "Southern Region": ["Żabbar", "Żejtun", "Birżebbuġa", "Marsaskala", "Marsaxlokk", "Gudja", "Għaxaq", "Kirkop", "Luqa", "Mqabba"],
  "Gozo": ["Victoria", "Xagħra", "Nadur", "Xewkija", "Għajnsielem", "Qala", "San Lawrenz", "Għarb", "Sannat", "Munxar"],
  "Central Region": ["Birkirkara", "Qormi", "Żebbuġ", "Attard", "Balzan", "Lija", "Iklin", "Swieqi", "San Ġwann", "Msida"],
  "South Eastern Region": ["Birżebbuġa", "Marsaskala", "Marsaxlokk", "Żejtun", "Gudja", "Għaxaq", "Kirkop", "Luqa", "Mqabba", "Safi"],
  "Western Region": ["Rabat", "Mdina", "Siġġiewi", "Żebbuġ", "Attard", "Balzan", "Lija", "Iklin", "Swieqi", "San Ġwann"],
  "Eastern Region": ["Sliema", "St. Julian's", "Gżira", "Ta' Xbiex", "Pembroke", "San Ġwann", "Swieqi", "Msida", "Birkirkara", "Qormi"],
  "Northern Harbour": ["Valletta", "Floriana", "Marsa", "Paola", "Hamrun", "Sliema", "St. Julian's", "Gżira", "Ta' Xbiex", "Pembroke"],
  "Southern Harbour": ["Birżebbuġa", "Marsaskala", "Marsaxlokk", "Żejtun", "Gudja", "Għaxaq", "Kirkop", "Luqa", "Mqabba", "Safi"]
},
"Luxembourg": {
  "Luxembourg": ["Luxembourg City", "Esch-sur-Alzette", "Differdange", "Dudelange", "Ettelbruck", "Diekirch", "Wiltz", "Echternach", "Rumelange", "Grevenmacher"],
  "Diekirch": ["Diekirch", "Ettelbruck", "Wiltz", "Vianden", "Clervaux", "Redange", "Mersch", "Bissen", "Larochette", "Bettendorf"],
  "Grevenmacher": ["Grevenmacher", "Echternach", "Remich", "Wormeldange", "Bech", "Rosport", "Manternach", "Wasserbillig", "Mertert", "Berdorf"],
  "Esch-sur-Alzette": ["Esch-sur-Alzette", "Differdange", "Dudelange", "Sanem", "Schifflange", "Bettembourg", "Kayl", "Rumelange", "Pétange", "Bascharage"],
  "Capellen": ["Capellen", "Mamer", "Koerich", "Kehlen", "Kopstal", "Steinfort", "Hobscheid", "Septfontaines", "Garnich", "Dippach"],
  "Remich": ["Remich", "Wormeldange", "Bech", "Rosport", "Manternach", "Wasserbillig", "Mertert", "Berdorf", "Remich", "Wormeldange"],
  "Vianden": ["Vianden", "Putscheid", "Tandel", "Vianden", "Putscheid", "Tandel", "Vianden", "Putscheid", "Tandel", "Vianden"],
  "Clervaux": ["Clervaux", "Wincrange", "Weiswampach", "Troisvierges", "Clervaux", "Wincrange", "Weiswampach", "Troisvierges", "Clervaux", "Wincrange"],
  "Redange": ["Redange", "Ell", "Rambrouch", "Saeul", "Useldange", "Vichten", "Redange", "Ell", "Rambrouch", "Saeul"],
  "Wiltz": ["Wiltz", "Esch-sur-Sûre", "Boulaide", "Lac de la Haute-Sûre", "Winseler", "Wiltz", "Esch-sur-Sûre", "Boulaide", "Lac de la Haute-Sûre", "Winseler"]
},
"Andorra": {
  "Andorra la Vella": ["Andorra la Vella", "Santa Coloma", "La Margineda", "Escaldes-Engordany", "Pas de la Casa", "Encamp", "Canillo", "Ordino", "La Massana", "Arinsal"],
  "Escaldes-Engordany": ["Escaldes-Engordany", "Les Escaldes", "Engordany", "Vila", "Escaldes-Engordany", "Les Escaldes", "Engordany", "Vila", "Escaldes-Engordany", "Les Escaldes"],
  "Encamp": ["Encamp", "Pas de la Casa", "Grau Roig", "El Tarter", "Encamp", "Pas de la Casa", "Grau Roig", "El Tarter", "Encamp", "Pas de la Casa"],
  "Canillo": ["Canillo", "Soldeu", "El Tarter", "Ransol", "Canillo", "Soldeu", "El Tarter", "Ransol", "Canillo", "Soldeu"],
  "Ordino": ["Ordino", "La Cortinada", "Arans", "El Serrat", "Ordino", "La Cortinada", "Arans", "El Serrat", "Ordino", "La Cortinada"],
  "La Massana": ["La Massana", "Arinsal", "Pal", "Erts", "La Massana", "Arinsal", "Pal", "Erts", "La Massana", "Arinsal"],
  "Sant Julià de Lòria": ["Sant Julià de Lòria", "Aixovall", "Aixirivall", "Sant Julià de Lòria", "Aixovall", "Aixirivall", "Sant Julià de Lòria", "Aixovall", "Aixirivall", "Sant Julià de Lòria"],
  "Escaldes": ["Escaldes", "Engordany", "Les Escaldes", "Escaldes", "Engordany", "Les Escaldes", "Escaldes", "Engordany", "Les Escaldes", "Escaldes"],
  "Pas de la Casa": ["Pas de la Casa", "Grau Roig", "El Tarter", "Pas de la Casa", "Grau Roig", "El Tarter", "Pas de la Casa", "Grau Roig", "El Tarter", "Pas de la Casa"],
  "Arinsal": ["Arinsal", "Pal", "Erts", "Arinsal", "Pal", "Erts", "Arinsal", "Pal", "Erts", "Arinsal"]
},
"Liechtenstein": {
  "Vaduz": ["Vaduz", "Schaan", "Triesen", "Balzers", "Eschen", "Mauren", "Triesenberg", "Ruggell", "Gamprin", "Schellenberg"],
  "Schaan": ["Schaan", "Vaduz", "Triesen", "Balzers", "Eschen", "Mauren", "Triesenberg", "Ruggell", "Gamprin", "Schellenberg"],
  "Triesen": ["Triesen", "Vaduz", "Schaan", "Balzers", "Eschen", "Mauren", "Triesenberg", "Ruggell", "Gamprin", "Schellenberg"],
  "Balzers": ["Balzers", "Vaduz", "Schaan", "Triesen", "Eschen", "Mauren", "Triesenberg", "Ruggell", "Gamprin", "Schellenberg"],
  "Eschen": ["Eschen", "Vaduz", "Schaan", "Triesen", "Balzers", "Mauren", "Triesenberg", "Ruggell", "Gamprin", "Schellenberg"],
  "Mauren": ["Mauren", "Vaduz", "Schaan", "Triesen", "Balzers", "Eschen", "Triesenberg", "Ruggell", "Gamprin", "Schellenberg"],
  "Triesenberg": ["Triesenberg", "Vaduz", "Schaan", "Triesen", "Balzers", "Eschen", "Mauren", "Ruggell", "Gamprin", "Schellenberg"],
  "Ruggell": ["Ruggell", "Vaduz", "Schaan", "Triesen", "Balzers", "Eschen", "Mauren", "Triesenberg", "Gamprin", "Schellenberg"],
  "Gamprin": ["Gamprin", "Vaduz", "Schaan", "Triesen", "Balzers", "Eschen", "Mauren", "Triesenberg", "Ruggell", "Schellenberg"],
  "Schellenberg": ["Schellenberg", "Vaduz", "Schaan", "Triesen", "Balzers", "Eschen", "Mauren", "Triesenberg", "Ruggell", "Gamprin"]
},
"Greenland": {
  "Nuuk": ["Nuuk", "Qeqertarsuatsiaat", "Paamiut", "Maniitsoq", "Sisimiut", "Kangaamiut", "Qasigiannguit", "Aasiaat", "Qeqertarsuaq", "Uummannaq"],
  "Sisimiut": ["Sisimiut", "Kangerlussuaq", "Itilleq", "Sarfannguit", "Kangaamiut", "Maniitsoq", "Nuuk", "Qeqertarsuatsiaat", "Paamiut", "Qasigiannguit"],
  "Ilulissat": ["Ilulissat", "Qasigiannguit", "Qeqertarsuaq", "Uummannaq", "Upernavik", "Aasiaat", "Kangaatsiaq", "Niaqornat", "Oqaatsut", "Saqqaq"],
  "Qaqortoq": ["Qaqortoq", "Narsaq", "Nanortalik", "Alluitsup Paa", "Qassimiut", "Tasiusaq", "Aappilattoq", "Eqalugaarsuit", "Igaliku", "Qassiarsuk"],
  "Maniitsoq": ["Maniitsoq", "Kangaamiut", "Sisimiut", "Kangerlussuaq", "Nuuk", "Qeqertarsuatsiaat", "Paamiut", "Qasigiannguit", "Aasiaat", "Qeqertarsuaq"],
  "Tasiilaq": ["Tasiilaq", "Kuummiut", "Kulusuk", "Isortoq", "Sermiligaaq", "Tiniteqilaaq", "Ikkatteq", "Kangerlussuaq", "Ittoqqortoormiit", "Scoresbysund"],
  "Uummannaq": ["Uummannaq", "Qaarsut", "Ikerasak", "Saattut", "Niaqornat", "Illorsuit", "Nuugaatsiaq", "Qaanaaq", "Siorapaluk", "Savissivik"],
  "Aasiaat": ["Aasiaat", "Qasigiannguit", "Qeqertarsuaq", "Ilulissat", "Kangaatsiaq", "Niaqornat", "Oqaatsut", "Saqqaq", "Aasiaat", "Qasigiannguit"],
  "Narsaq": ["Narsaq", "Qaqortoq", "Nanortalik", "Alluitsup Paa", "Qassimiut", "Tasiusaq", "Aappilattoq", "Eqalugaarsuit", "Igaliku", "Qassiarsuk"],
  "Ittoqqortoormiit": ["Ittoqqortoormiit", "Scoresbysund", "Tasiilaq", "Kuummiut", "Kulusuk", "Isortoq", "Sermiligaaq", "Tiniteqilaaq", "Ikkatteq", "Kangerlussuaq"]
},
"Faroe Islands": {
  "Tórshavn": ["Tórshavn", "Argir", "Hoyvík", "Kollafjørður", "Streymnes", "Kvívík", "Vestmanna", "Sørvágur", "Miðvágur", "Sandavágur"],
  "Klaksvík": ["Klaksvík", "Hvannasund", "Árnafjørður", "Norðdepil", "Hvítanes", "Haraldssund", "Svínoy", "Fuglafjørður", "Leirvík", "Gøta"],
  "Runavík": ["Runavík", "Saltangará", "Glyvrar", "Skarvanes", "Søldarfjørður", "Lambareiði", "Elduvík", "Funningsfjørður", "Oyndarfjørður", "Skipanes"],
  "Tvøroyri": ["Tvøroyri", "Froðba", "Trongisvágur", "Hvalba", "Sandvík", "Fámjin", "Vágur", "Porkeri", "Hov", "Øravík"],
  "Fuglafjørður": ["Fuglafjørður", "Hellur", "Kirkja", "Hattarvík", "Svínoy", "Fugloy", "Hvannasund", "Árnafjørður", "Norðdepil", "Hvítanes"],
  "Vestmanna": ["Vestmanna", "Kvívík", "Kollafjørður", "Streymnes", "Saksun", "Hvalvík", "Haldarsvík", "Hósvík", "Langasandur", "Tjørnuvík"],
  "Sørvágur": ["Sørvágur", "Miðvágur", "Sandavágur", "Bøur", "Gásadalur", "Mykines", "Vatnsoyrar", "Bour", "Gásadalur", "Mykines"],
  "Eiði": ["Eiði", "Ljósá", "Elduvík", "Funningur", "Gjógv", "Funningsfjørður", "Oyndarfjørður", "Skipanes", "Eiði", "Ljósá"],
  "Sandur": ["Sandur", "Skálavík", "Húsavík", "Dalur", "Skopun", "Skúvoy", "Hestur", "Nólsoy", "Stóra Dímun", "Lítla Dímun"],
  "Skopun": ["Skopun", "Sandur", "Skálavík", "Húsavík", "Dalur", "Skúvoy", "Hestur", "Nólsoy", "Stóra Dímun", "Lítla Dímun"]
},
"Monaco": {
  "Monaco-Ville": ["Monaco-Ville", "La Condamine", "Monte-Carlo", "Fontvieille", "Larvotto", "La Rousse", "Saint Michel", "Moneghetti", "Jardin Exotique", "Les Révoires"],
  "Monte-Carlo": ["Monte-Carlo", "La Condamine", "Monaco-Ville", "Fontvieille", "Larvotto", "La Rousse", "Saint Michel", "Moneghetti", "Jardin Exotique", "Les Révoires"],
  "La Condamine": ["La Condamine", "Monte-Carlo", "Monaco-Ville", "Fontvieille", "Larvotto", "La Rousse", "Saint Michel", "Moneghetti", "Jardin Exotique", "Les Révoires"],
  "Fontvieille": ["Fontvieille", "Monte-Carlo", "La Condamine", "Monaco-Ville", "Larvotto", "La Rousse", "Saint Michel", "Moneghetti", "Jardin Exotique", "Les Révoires"],
  "Larvotto": ["Larvotto", "Monte-Carlo", "La Condamine", "Monaco-Ville", "Fontvieille", "La Rousse", "Saint Michel", "Moneghetti", "Jardin Exotique", "Les Révoires"],
  "La Rousse": ["La Rousse", "Monte-Carlo", "La Condamine", "Monaco-Ville", "Fontvieille", "Larvotto", "Saint Michel", "Moneghetti", "Jardin Exotique", "Les Révoires"],
  "Saint Michel": ["Saint Michel", "Monte-Carlo", "La Condamine", "Monaco-Ville", "Fontvieille", "Larvotto", "La Rousse", "Moneghetti", "Jardin Exotique", "Les Révoires"],
  "Moneghetti": ["Moneghetti", "Monte-Carlo", "La Condamine", "Monaco-Ville", "Fontvieille", "Larvotto", "La Rousse", "Saint Michel", "Jardin Exotique", "Les Révoires"],
  "Jardin Exotique": ["Jardin Exotique", "Monte-Carlo", "La Condamine", "Monaco-Ville", "Fontvieille", "Larvotto", "La Rousse", "Saint Michel", "Moneghetti", "Les Révoires"],
  "Les Révoires": ["Les Révoires", "Monte-Carlo", "La Condamine", "Monaco-Ville", "Fontvieille", "Larvotto", "La Rousse", "Saint Michel", "Moneghetti", "Jardin Exotique"]
},
"San Marino": {
  "San Marino": ["San Marino", "Borgo Maggiore", "Serravalle", "Domagnano", "Fiorentino", "Acquaviva", "Chiesanuova", "Montegiardino", "Faetano", "Poggio di Chiesanuova"],
  "Borgo Maggiore": ["Borgo Maggiore", "San Marino", "Serravalle", "Domagnano", "Fiorentino", "Acquaviva", "Chiesanuova", "Montegiardino", "Faetano", "Poggio di Chiesanuova"],
  "Serravalle": ["Serravalle", "San Marino", "Borgo Maggiore", "Domagnano", "Fiorentino", "Acquaviva", "Chiesanuova", "Montegiardino", "Faetano", "Poggio di Chiesanuova"],
  "Domagnano": ["Domagnano", "San Marino", "Borgo Maggiore", "Serravalle", "Fiorentino", "Acquaviva", "Chiesanuova", "Montegiardino", "Faetano", "Poggio di Chiesanuova"],
  "Fiorentino": ["Fiorentino", "San Marino", "Borgo Maggiore", "Serravalle", "Domagnano", "Acquaviva", "Chiesanuova", "Montegiardino", "Faetano", "Poggio di Chiesanuova"],
  "Acquaviva": ["Acquaviva", "San Marino", "Borgo Maggiore", "Serravalle", "Domagnano", "Fiorentino", "Chiesanuova", "Montegiardino", "Faetano", "Poggio di Chiesanuova"],
  "Chiesanuova": ["Chiesanuova", "San Marino", "Borgo Maggiore", "Serravalle", "Domagnano", "Fiorentino", "Acquaviva", "Montegiardino", "Faetano", "Poggio di Chiesanuova"],
  "Montegiardino": ["Montegiardino", "San Marino", "Borgo Maggiore", "Serravalle", "Domagnano", "Fiorentino", "Acquaviva", "Chiesanuova", "Faetano", "Poggio di Chiesanuova"],
  "Faetano": ["Faetano", "San Marino", "Borgo Maggiore", "Serravalle", "Domagnano", "Fiorentino", "Acquaviva", "Chiesanuova", "Montegiardino", "Poggio di Chiesanuova"],
  "Poggio di Chiesanuova": ["Poggio di Chiesanuova", "San Marino", "Borgo Maggiore", "Serravalle", "Domagnano", "Fiorentino", "Acquaviva", "Chiesanuova", "Montegiardino", "Faetano"]
},

}

# Configurando locale para exibição correta de moeda
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, '') # Fallback para o locale padrão do sistema

# --- Definição dos Temas ---
THEMES = {
    "Padrão": {
        "root_bg": "#EBF2F9", # Azul muito claro
        "label_bg": "#EBF2F9", "label_fg": "#333333",
        "button_bg": "#4285F4", "button_fg": "white",
        "button_active_bg": "#2196F3", # Azul secundário no hover
        "entry_bg": "#FFFFFF", "entry_fg": "#333333",
        "entry_border": "#BBDEFB", "entry_focus_bg": "#F8FBFF", "entry_focus_border": "#4285F4",
        "checkbutton_bg": "#EBF2F9", "checkbutton_fg": "#333333", "checkbutton_active_bg": "#DDEEFF",
        "notebook_bg": "#EBF2F9",
        "tab_bg": "#DDEEFF", "tab_fg": "#555555",
        "tab_selected_bg": "#4285F4", "tab_selected_fg": "white",
        "labelframe_bg": "#FFFFFF", "labelframe_border": "#BBDEFB", "labelframe_label_fg": "#3F51B5",
        "treeview_heading_bg": "#4285F4", "treeview_heading_fg": "white", "treeview_heading_active_bg": "#2196F3",
        "treeview_bg": "#FFFFFF", "treeview_fg": "#333333", "treeview_field_bg": "#FFFFFF",
        "treeview_selected_bg": "#BBDEFB", "treeview_selected_fg": "#333333",
        "lightframe_bg": "#F8F8FF",
        "listbox_bg": "#FFFFFF", "listbox_fg": "#333333", "listbox_select_bg": "#BBDEFB", "listbox_select_fg": "#333333",
        "scrollbar_bg": "#EEEEEE", "scrollbar_trough_bg": "#F8F8FF", "scrollbar_grip_bg": "#AAAAAA", "scrollbar_active_bg": "#BBDEFB", "scrollbar_active_grip_bg": "#666666",
        "progressbar_trough_bg": "#E0E0E0", "progressbar_fill_bg": "#4CAF50",
        "status_bg": "#D1E7DD", "status_fg": "#0F5132",
        "scrolledtext_bg": "#FFFFFF", "scrolledtext_fg": "#333333"
    },
    "Solar": {
        "root_bg": "#FFF8E1", # Light cream/yellow
        "label_bg": "#FFF8E1", "label_fg": "#424242",
        "button_bg": "#FF8F00", "button_fg": "white", # Darker orange
        "button_active_bg": "#FFB300", # Amber on hover
        "entry_bg": "#FFFFFF", "entry_fg": "#424242",
        "entry_border": "#FFD600", "entry_focus_bg": "#FFFBE5", "entry_focus_border": "#FF8F00",
        "checkbutton_bg": "#FFF8E1", "checkbutton_fg": "#424242", "checkbutton_active_bg": "#FFE0B2",
        "notebook_bg": "#FFF8E1",
        "tab_bg": "#FFE0B2", "tab_fg": "#616161", # Light orange tab, darker grey text
        "tab_selected_bg": "#FFB300", "tab_selected_fg": "white", # Amber selected tab
        "labelframe_bg": "#FFFFFF", "labelframe_border": "#FFD600", "labelframe_label_fg": "#E65100", # Deep orange label
        "treeview_heading_bg": "#FFB300", "treeview_heading_fg": "white", "treeview_heading_active_bg": "#FF8F00",
        "treeview_bg": "#FFFFFF", "treeview_fg": "#424242", "treeview_field_bg": "#FFFFFF",
        "treeview_selected_bg": "#FFE0B2", "treeview_selected_fg": "#424242",
        "lightframe_bg": "#FFFDF0",
        "listbox_bg": "#FFFFFF", "listbox_fg": "#424242", "listbox_select_bg": "#FFE0B2", "listbox_select_fg": "#424242",
        "scrollbar_bg": "#FFECB3", "scrollbar_trough_bg": "#FFFBE5", "scrollbar_grip_bg": "#FFC107", "scrollbar_active_bg": "#FFB300", "scrollbar_active_grip_bg": "#FF8F00",
        "progressbar_trough_bg": "#F5F5DC", "progressbar_fill_bg": "#FFD600",
        "status_bg": "#FFCC80", "status_fg": "#BF360C",
        "scrolledtext_bg": "#FFFFFF", "scrolledtext_fg": "#424242"
    },
    "Dark Mode": {
        "root_bg": "#212121", # Dark grey
        "label_bg": "#212121", "label_fg": "#E0E0E0",
        "button_bg": "#424242", "button_fg": "#E0E0E0",
        "button_active_bg": "#616161", # Lighter grey on hover
        "entry_bg": "#303030", "entry_fg": "#E0E0E0",
        "entry_border": "#424242", "entry_focus_bg": "#3A3A3A", "entry_focus_border": "#BBDEFB",
        "checkbutton_bg": "#212121", "checkbutton_fg": "#E0E0E0", "checkbutton_active_bg": "#303030",
        "notebook_bg": "#212121",
        "tab_bg": "#303030", "tab_fg": "#B0B0B0",
        "tab_selected_bg": "#424242", "tab_selected_fg": "white",
        "labelframe_bg": "#303030", "labelframe_border": "#424242", "labelframe_label_fg": "#BBDEFB",
        "treeview_heading_bg": "#424242", "treeview_heading_fg": "#E0E0E0", "treeview_heading_active_bg": "#616161",
        "treeview_bg": "#303030", "treeview_fg": "#E0E0E0", "treeview_field_bg": "#303030",
        "treeview_selected_bg": "#616161", "treeview_selected_fg": "white",
        "lightframe_bg": "#282828",
        "listbox_bg": "#303030", "listbox_fg": "#E0E0E0", "listbox_select_bg": "#616161", "listbox_select_fg": "white",
        "scrollbar_bg": "#424242", "scrollbar_trough_bg": "#303030", "scrollbar_grip_bg": "#616161", "scrollbar_active_bg": "#757575", "scrollbar_active_grip_bg": "#9E9E9E",
        "progressbar_trough_bg": "#424242", "progressbar_fill_bg": "#4CAF50",
        "status_bg": "#303030", "status_fg": "#E0E0E0",
        "scrolledtext_bg": "#303030", "scrolledtext_fg": "#E0E0E0"
    },
    "Natureza": {
        "root_bg": "#E8F5E9", # Very light green
        "label_bg": "#E8F5E9", "label_fg": "#388E3C", # Dark green
        "button_bg": "#66BB6A", "button_fg": "white", # Light green
        "button_active_bg": "#4CAF50", # Medium green on hover
        "entry_bg": "#FFFFFF", "entry_fg": "#388E3C",
        "entry_border": "#A5D6A7", "entry_focus_bg": "#F0FEE0", "entry_focus_border": "#66BB6A",
        "checkbutton_bg": "#E8F5E9", "checkbutton_fg": "#388E3C", "checkbutton_active_bg": "#C8E6C9",
        "notebook_bg": "#E8F5E9",
        "tab_bg": "#C8E6C9", "tab_fg": "#558B2F", # Greenish tab, darker green text
        "tab_selected_bg": "#4CAF50", "tab_selected_fg": "white", # Medium green selected tab
        "labelframe_bg": "#FFFFFF", "labelframe_border": "#A5D6A7", "labelframe_label_fg": "#33691E", # Deep forest green
        "treeview_heading_bg": "#4CAF50", "treeview_heading_fg": "white", "treeview_heading_active_bg": "#66BB6A",
        "treeview_bg": "#FFFFFF", "treeview_fg": "#388E3C", "treeview_field_bg": "#FFFFFF",
        "treeview_selected_bg": "#A5D6A7", "treeview_selected_fg": "#388E3C",
        "lightframe_bg": "#F5FFF5",
        "listbox_bg": "#FFFFFF", "listbox_fg": "#388E3C", "listbox_select_bg": "#A5D6A7", "listbox_select_fg": "#388E3C",
        "scrollbar_bg": "#DCEDC8", "scrollbar_trough_bg": "#F5FFF5", "scrollbar_grip_bg": "#8BC34A", "scrollbar_active_bg": "#A5D6A7", "scrollbar_active_grip_bg": "#689F38",
        "progressbar_trough_bg": "#DCEDC8", "progressbar_fill_bg": "#8BC34A",
        "status_bg": "#C8E6C9", "status_fg": "#2E7D32",
        "scrolledtext_bg": "#FFFFFF", "scrolledtext_fg": "#388E3C"
    }
}
# Configurando locale para exibição correta de moeda
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, '') # Fallback para o locale padrão do sistema

class GeradorPlanilhaApp:
    """
    Uma aplicação Tkinter para gerar planilhas de compras eletrônicas com dados fictícios.
    Permite personalização de colunas, dados e temas visuais usando TTKBootstrap.
    """
    def __init__(self, master):
        self.master = master
        self.master.title("Gerador de Planilha de Compras Eletrônicas - Profissional")
        self.master.geometry("1400x980")

        self.gerando_dados = False
        self.colunas_vars = {}
        self.paises_vars = {}
        self.style = self.master.style
        self.last_generated_data = (None, None)
        self.tk_listboxes = [] # Lista para guardar referência a todos os tk.Listbox

        self.produtos = list(PRODUTOS_ELETRONICOS)
        self.lojas = list(LOJAS)
        self.vendedores = list(VENDEDORES_PERSONALIZADOS)
        self.clientes = list(CLIENTES_PERSONALIZADOS)
        self.dominios = list(DOMINIOS_EMAIL)
        self.estados_cidades_user = {k: {sk: list(sv) for sk, sv in v.items()} for k, v in ESTADOS_CIDADES.items()}

        self._create_widgets()

    def _create_widgets(self):
        """Cria todos os widgets da interface gráfica principal."""
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        menu_arquivo = Menu(menu_bar, tearoff=0)
        menu_arquivo.add_command(label="Sair", command=self.master.quit)
        menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)

        menu_ajuda = Menu(menu_bar, tearoff=0)
        menu_ajuda.add_command(label="Sobre", command=lambda: messagebox.showinfo("Sobre", "Gerador de Planilha de Compras Eletrônicas\nVersão 2.9\nDesenvolvido por Diogo Centeno"))
        menu_ajuda.add_command(label="Ajuda", command=self._exibir_ajuda)
        menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

        self.top_controls_frame = ttk.Frame(self.master, padding=(15, 10, 15, 0))
        self.top_controls_frame.pack(fill="x")

        ttk.Label(self.top_controls_frame, text="Tema:", font=("Segoe UI", 10, "bold")).pack(side="left", padx=(0, 5))
        theme_options = sorted(self.style.theme_names())
        self.theme_var = tk.StringVar(self.master)
        self.theme_var.set(self.style.theme.name)
        
        # FIX: Substituído Combobox por OptionMenu para evitar um bug de estilização
        # que causava a "tela branca" em algumas versões do ttkbootstrap.
        self.theme_menu = ttk.OptionMenu(
            self.top_controls_frame,
            self.theme_var,
            self.style.theme.name, # O primeiro item é o padrão
            *theme_options,
            command=self._change_theme,
            bootstyle="outline"
        )
        self.theme_menu.pack(side="left", padx=(0, 20))

        self.btn_marcar_colunas_top = ttk.Button(self.top_controls_frame, text="Marcar/Desmarcar Colunas", command=self._marcar_desmarcar_colunas, bootstyle="info-outline")
        self.btn_marcar_colunas_top.pack(side="left", padx=(10, 5))

        self.btn_marcar_paises_top = ttk.Button(self.top_controls_frame, text="Marcar/Desmarcar Países", command=self._marcar_desmarcar_paises, bootstyle="info-outline")
        self.btn_marcar_paises_top.pack(side="left", padx=5)

        self.notebook = ttk.Notebook(self.master, padding=(15, 10))
        self.notebook.pack(fill="both", expand=True)

        self._create_tab_config()
        self._create_tab_personalizacao()
        self._create_tab_regiao()

        self.frame_cronometro_progresso = ttk.Frame(self.master, padding=(0, 5, 0, 10))
        self.frame_cronometro_progresso.pack()
        self.frame_cronometro_progresso.grid_columnconfigure(1, weight=1)

        self.cronometro_label = ttk.Label(self.frame_cronometro_progresso, text="Tempo decorrido: 00:00:00", font=("Segoe UI", 11, "bold"))
        self.cronometro_label.grid(row=0, column=0, padx=10)

        self.progress_bar = ttk.Progressbar(self.frame_cronometro_progresso, orient="horizontal", length=400, mode="determinate", bootstyle="success-striped")
        self.progress_bar.grid(row=0, column=1, padx=10)

        self.frame_botoes_acao = ttk.Frame(self.master, padding=(0, 0, 0, 10))
        self.frame_botoes_acao.pack()

        self.btn_csv = ttk.Button(self.frame_botoes_acao, text="Salvar como CSV", command=lambda: self._salvar_planilha("csv"), bootstyle="success")
        self.btn_csv.grid(row=0, column=0, padx=5)
        
        self.btn_xlsx = ttk.Button(self.frame_botoes_acao, text="Salvar como Excel", command=lambda: self._salvar_planilha("xlsx"), bootstyle="success")
        self.btn_xlsx.grid(row=0, column=1, padx=5)

        self.btn_visualizar = ttk.Button(self.frame_botoes_acao, text="Visualizar Dados", command=self._visualizar_dados, bootstyle="info")
        self.btn_visualizar.grid(row=0, column=2, padx=5)

        self.status_label = ttk.Label(self.master, text="Pronto", anchor=tk.W, font=("Segoe UI", 9), bootstyle="primary-inverse", padding=(5, 2))
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

        self._bind_context_menu(self.master)

    def _create_tab_config(self):
        """Cria a aba de configurações com ScrolledFrame para rolagem."""
        config_tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(config_tab_frame, text="Configurações")

        scrolled_frame = ScrolledFrame(config_tab_frame, autohide=True)
        scrolled_frame.pack(fill="both", expand=True, padx=10, pady=5)

        config_params_frame = ttk.LabelFrame(scrolled_frame, text="Parâmetros de Geração", padding=10)
        config_params_frame.pack(fill="x", pady=5)
        config_params_frame.grid_columnconfigure(1, weight=1)

        params = {
            "Número de Linhas:": ("1000", self._validate_numeric),
            "Desconto à Vista (%):": ("-9", self._validate_float),
            "Desconto Pix (%):": ("-7", self._validate_float),
            "Acréscimo Cartão (%):": ("5", self._validate_float),
            "Acréscimo Boleto (%):": ("2", self._validate_float),
            "Formato do ID do Cliente:": ("ABC-123456", None),
            "Formato do ID do Produto:": ("XKIOPY-123", None),
            "Data Inicial (DD/MM/AAAA):": ("01/01/2020", None),
            "Data Final (DD/MM/AAAA):": ("01/01/2025", None)
        }
        self.entries = {}
        for i, (label_text, (default_value, validator)) in enumerate(params.items()):
            ttk.Label(config_params_frame, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky="w")
            entry = ttk.Entry(config_params_frame, width=20)
            entry.insert(0, default_value)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            if validator:
                entry.config(validate="key", validatecommand=(self.master.register(validator), '%P', '%S'))
            self.entries[label_text] = entry

        columns_selection_frame = ttk.LabelFrame(scrolled_frame, text="Seleção de Colunas", padding=10)
        columns_selection_frame.pack(fill="x", pady=5)
        columns_selection_frame.grid_columnconfigure((0,1,2), weight=1)

        COLUNAS = [ "ID do Cliente", "Nome do Cliente", "Email", "ID do Produto", "Nome do Produto", "Categoria", "Fabricante", "Entregador", "Valor da Entrega", "Data da Compra", "Data da Entrega", "Valor do Produto", "Valor à Vista em dinheiro", "Valor no Pix", "Valor no Cartão", "Valor no Boleto", "Nome da Loja", "Nome do Vendedor", "Comissão", "Valor da Comissão", "País da Compra", "Estado da Compra", "Cidade da Compra", "Transação", "Status" ]
        self.colunas_vars = {col: tk.BooleanVar(value=True) for col in COLUNAS}
        for i, col in enumerate(COLUNAS):
            ttk.Checkbutton(columns_selection_frame, text=col, variable=self.colunas_vars[col]).grid(row=i // 3, column=i % 3, padx=10, pady=2, sticky="w")

        countries_selection_frame = ttk.LabelFrame(scrolled_frame, text="Seleção de Países", padding=10)
        countries_selection_frame.pack(fill="x", pady=5)
        countries_selection_frame.grid_columnconfigure((0,1,2), weight=1)

        paises_disponiveis = list(self.estados_cidades_user.keys())
        self.paises_vars = {pais: tk.BooleanVar(value=True) for pais in paises_disponiveis}
        for i, pais in enumerate(paises_disponiveis):
            ttk.Checkbutton(countries_selection_frame, text=pais, variable=self.paises_vars[pais]).grid(row=i // 3, column=i % 3, padx=10, pady=2, sticky="w")
    
    def _create_tab_personalizacao(self):
        """Cria as abas de personalização de dados."""
        dados_personalizaveis = {
            "Produtos": self.produtos, "Lojas": self.lojas,
            "Vendedores": self.vendedores, "Clientes": self.clientes,
            "Domínios de Email": self.dominios
        }
        for nome_aba, lista_dados in dados_personalizaveis.items():
            frame_aba = ttk.Frame(self.notebook, padding=10)
            self.notebook.add(frame_aba, text=nome_aba)
            
            frame_conteudo = ttk.LabelFrame(frame_aba, text=nome_aba, padding=10)
            frame_conteudo.pack(fill="both", expand=True)

            listbox = Listbox(frame_conteudo, relief="flat", borderwidth=1, selectbackground=self.style.colors.primary, selectforeground=self.style.colors.selectfg)
            listbox.pack(padx=5, pady=5, fill="both", expand=True)
            self.tk_listboxes.append(listbox)
            self._atualizar_lista(lista_dados, listbox)
            
            entry = ttk.Entry(frame_conteudo, width=50)
            entry.pack(padx=5, pady=5, fill="x")
            
            btn_frame = ttk.Frame(frame_conteudo)
            btn_frame.pack(pady=5)
            
            singular = nome_aba.replace("ões", "ão").replace("s", "")
            ttk.Button(btn_frame, text=f"Adicionar {singular}", command=lambda l=lista_dados, e=entry, lb=listbox: self._adicionar_item_simples(l, e, lb), bootstyle="primary").pack(side="left", padx=5)
            ttk.Button(btn_frame, text=f"Remover {singular}", command=lambda l=lista_dados, lb=listbox: self._remover_item_simples(l, lb), bootstyle="danger").pack(side="left", padx=5)
            ttk.Button(btn_frame, text="Remover Todos", command=lambda l=lista_dados, lb=listbox: self._remover_todos_itens_simples(l, lb), bootstyle="warning-outline").pack(side="left", padx=5)

    def _create_tab_regiao(self):
        """Cria a aba de gerenciamento de regiões."""
        frame_regiao = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(frame_regiao, text="Região")
        frame_regiao.grid_columnconfigure((0,1,2), weight=1)
        frame_regiao.grid_rowconfigure(0, weight=1)

        # Países
        frame_paises = ttk.LabelFrame(frame_regiao, text="Países", padding=10)
        frame_paises.grid(row=0, column=0, sticky="nsew", padx=5)
        self.lista_paises = Listbox(frame_paises, exportselection=False, relief="flat", borderwidth=1, selectbackground=self.style.colors.primary, selectforeground=self.style.colors.selectfg)
        self.lista_paises.pack(fill="both", expand=True, pady=5)
        self.tk_listboxes.append(self.lista_paises)
        self._atualizar_lista(list(self.estados_cidades_user.keys()), self.lista_paises)
        entry_pais = ttk.Entry(frame_paises)
        entry_pais.pack(fill="x", pady=5)
        btn_paises = ttk.Button(frame_paises, text="Adicionar País", command=lambda: self._adicionar_pais(entry_pais, self.lista_paises), bootstyle="primary-outline")
        btn_paises.pack(fill="x", pady=(0,5))
        
        # Estados
        frame_estados = ttk.LabelFrame(frame_regiao, text="Estados", padding=10)
        frame_estados.grid(row=0, column=1, sticky="nsew", padx=5)
        self.lista_estados = Listbox(frame_estados, exportselection=False, relief="flat", borderwidth=1, selectbackground=self.style.colors.primary, selectforeground=self.style.colors.selectfg)
        self.lista_estados.pack(fill="both", expand=True, pady=5)
        self.tk_listboxes.append(self.lista_estados)
        entry_estado = ttk.Entry(frame_estados)
        entry_estado.pack(fill="x", pady=5)
        btn_estados = ttk.Button(frame_estados, text="Adicionar Estado", command=lambda: self._adicionar_estado(entry_estado), bootstyle="primary-outline")
        btn_estados.pack(fill="x", pady=(0,5))

        # Cidades
        frame_cidades = ttk.LabelFrame(frame_regiao, text="Cidades", padding=10)
        frame_cidades.grid(row=0, column=2, sticky="nsew", padx=5)
        self.lista_cidades = Listbox(frame_cidades, exportselection=False, relief="flat", borderwidth=1, selectbackground=self.style.colors.primary, selectforeground=self.style.colors.selectfg)
        self.lista_cidades.pack(fill="both", expand=True, pady=5)
        self.tk_listboxes.append(self.lista_cidades)
        entry_cidade = ttk.Entry(frame_cidades)
        entry_cidade.pack(fill="x", pady=5)
        btn_cidades = ttk.Button(frame_cidades, text="Adicionar Cidade", command=lambda: self._adicionar_cidade(entry_cidade), bootstyle="primary-outline")
        btn_cidades.pack(fill="x", pady=(0,5))

        self.lista_paises.bind("<<ListboxSelect>>", self._atualizar_estados)
        self.lista_estados.bind("<<ListboxSelect>>", self._atualizar_cidades)
        self.lista_paises.bind("<Button-3>", lambda e: self._menu_regiao(e, "país"))
        self.lista_estados.bind("<Button-3>", lambda e: self._menu_regiao(e, "estado"))
        self.lista_cidades.bind("<Button-3>", lambda e: self._menu_regiao(e, "cidade"))
    
    def _change_theme(self, theme_name: str):
        """Muda o tema da aplicação e atualiza widgets não-ttk manualmente."""
        try:
            self.style.theme_use(theme_name)
            # Atualiza manualmente todos os widgets Listbox (que são do tk, não ttk)
            for listbox in self.tk_listboxes:
                listbox.config(
                    bg=self.style.colors.inputbg, 
                    fg=self.style.colors.inputfg, 
                    selectbackground=self.style.colors.primary, 
                    selectforeground=self.style.colors.selectfg
                )
        except Exception as e:
            messagebox.showerror("Erro de Tema", 
                                 f"Não foi possível aplicar o tema '{theme_name}'.\n\n"
                                 "Isso pode ser causado por uma incompatibilidade com a sua versão da biblioteca 'ttkbootstrap'.\n\n"
                                 f"Detalhes: {e}", parent=self.master)
            # Reverte para o tema anterior se a mudança falhar
            self.theme_var.set(self.style.theme.name)
            self.style.theme_use(self.style.theme.name) # Força a volta ao tema que funcionava

    def _validate_numeric(self, P, S):
        if S == '': return True
        if P.isdigit() and int(P) >= 0: return True
        self.master.bell()
        return False

    def _validate_float(self, P, S):
        if S == '' or P == "-": return True
        try:
            float(P)
            return True
        except ValueError:
            self.master.bell()
            return False

    def _marcar_desmarcar_colunas(self):
        novo_estado = not all(var.get() for var in self.colunas_vars.values())
        for var in self.colunas_vars.values(): var.set(novo_estado)

    def _marcar_desmarcar_paises(self):
        novo_estado = not all(var.get() for var in self.paises_vars.values())
        for var in self.paises_vars.values(): var.set(novo_estado)

    def _adicionar_item_simples(self, lista_referencia, entry, listbox):
        novo_item = entry.get().strip()
        if not novo_item: return messagebox.showwarning("Aviso", "O campo não pode estar vazio.", parent=self.master)
        if novo_item in lista_referencia: return messagebox.showwarning("Aviso", "Este item já existe na lista.", parent=self.master)
        
        lista_referencia.append(novo_item)
        self._atualizar_lista(lista_referencia, listbox)
        entry.delete(0, tk.END)

    def _remover_item_simples(self, lista_referencia, listbox):
        try:
            item_selecionado = listbox.get(listbox.curselection())
            if item_selecionado in lista_referencia:
                lista_referencia.remove(item_selecionado)
                self._atualizar_lista(lista_referencia, listbox)
        except tk.TclError: messagebox.showwarning("Aviso", "Selecione um item para remover.", parent=self.master)

    def _remover_todos_itens_simples(self, lista_referencia, listbox):
        if messagebox.askyesno("Confirmar", f"Deseja remover TODOS os itens de '{listbox.master.cget('text')}'?", parent=self.master):
            lista_referencia.clear()
            listbox.delete(0, tk.END)

    def _atualizar_lista(self, lista_items, listbox):
        listbox.delete(0, tk.END)
        for item in sorted(lista_items):
            listbox.insert(tk.END, item)

    def _adicionar_pais(self, entry, listbox):
        novo_pais = entry.get().strip()
        if not novo_pais: return
        if novo_pais in self.estados_cidades_user: return messagebox.showwarning("Aviso", "Este país já existe.", parent=self.master)
        
        self.estados_cidades_user[novo_pais] = {}
        self._atualizar_lista(self.estados_cidades_user.keys(), listbox)
        entry.delete(0, tk.END)

    def _remover_pais(self):
        try:
            pais = self.lista_paises.get(self.lista_paises.curselection())
            if messagebox.askyesno("Confirmar", f"Remover '{pais}' e todos os seus dados?", parent=self.master):
                del self.estados_cidades_user[pais]
                self._atualizar_lista(self.estados_cidades_user.keys(), self.lista_paises)
                self.lista_estados.delete(0, tk.END)
                self.lista_cidades.delete(0, tk.END)
        except tk.TclError: messagebox.showwarning("Aviso", "Selecione um país.", parent=self.master)

    def _adicionar_estado(self, entry):
        try:
            pais = self.lista_paises.get(self.lista_paises.curselection())
            novo_estado = entry.get().strip()
            if not novo_estado: return
            if novo_estado in self.estados_cidades_user[pais]: return messagebox.showwarning("Aviso", "Este estado já existe.", parent=self.master)
            
            self.estados_cidades_user[pais][novo_estado] = []
            self._atualizar_lista(self.estados_cidades_user[pais].keys(), self.lista_estados)
            entry.delete(0, tk.END)
        except tk.TclError: messagebox.showwarning("Aviso", "Selecione um país.", parent=self.master)

    def _remover_estado(self):
        try:
            pais = self.lista_paises.get(self.lista_paises.curselection())
            estado = self.lista_estados.get(self.lista_estados.curselection())
            if messagebox.askyesno("Confirmar", f"Remover o estado '{estado}' e suas cidades?", parent=self.master):
                del self.estados_cidades_user[pais][estado]
                self._atualizar_lista(self.estados_cidades_user[pais].keys(), self.lista_estados)
                self.lista_cidades.delete(0, tk.END)
        except tk.TclError: messagebox.showwarning("Aviso", "Selecione um estado.", parent=self.master)

    def _adicionar_cidade(self, entry):
        try:
            pais = self.lista_paises.get(self.lista_paises.curselection())
            estado = self.lista_estados.get(self.lista_estados.curselection())
            nova_cidade = entry.get().strip()
            if not nova_cidade: return
            if nova_cidade in self.estados_cidades_user[pais][estado]: return messagebox.showwarning("Aviso", "Esta cidade já existe.", parent=self.master)

            self.estados_cidades_user[pais][estado].append(nova_cidade)
            self._atualizar_lista(self.estados_cidades_user[pais][estado], self.lista_cidades)
            entry.delete(0, tk.END)
        except tk.TclError: messagebox.showwarning("Aviso", "Selecione um país e estado.", parent=self.master)
    
    def _remover_cidade(self):
        try:
            pais = self.lista_paises.get(self.lista_paises.curselection())
            estado = self.lista_estados.get(self.lista_estados.curselection())
            cidade = self.lista_cidades.get(self.lista_cidades.curselection())
            self.estados_cidades_user[pais][estado].remove(cidade)
            self._atualizar_lista(self.estados_cidades_user[pais][estado], self.lista_cidades)
        except (tk.TclError, ValueError): messagebox.showwarning("Aviso", "Selecione uma cidade.", parent=self.master)

    def _atualizar_estados(self, event):
        self.lista_estados.delete(0, tk.END)
        self.lista_cidades.delete(0, tk.END)
        try:
            pais = self.lista_paises.get(self.lista_paises.curselection())
            self._atualizar_lista(self.estados_cidades_user[pais].keys(), self.lista_estados)
        except tk.TclError: pass

    def _atualizar_cidades(self, event):
        self.lista_cidades.delete(0, tk.END)
        try:
            pais = self.lista_paises.get(self.lista_paises.curselection())
            estado = self.lista_estados.get(self.lista_estados.curselection())
            self._atualizar_lista(self.estados_cidades_user[pais][estado], self.lista_cidades)
        except tk.TclError: pass

    def _atualizar_cronometro(self, start_time):
        if self.gerando_dados:
            horas, rem = divmod(time.time() - start_time, 3600)
            minutos, segundos = divmod(rem, 60)
            self.cronometro_label.config(text=f"Tempo: {int(horas):02}:{int(minutos):02}:{int(segundos):02}")
            self.master.after(1000, self._atualizar_cronometro, start_time)

    def _set_ui_state(self, enabled):
        state = "normal" if enabled else "disabled"
        self.master.config(cursor="" if enabled else "wait")
        self._set_widget_state_recursively(self.master, state)
        if enabled:
            self.status_label.config(text="Pronto")

    def _set_widget_state_recursively(self, widget, state):
        """Usa try/except para evitar erros com widgets sem a opção 'state'."""
        try:
            # Não desabilita Labels ou a janela principal
            if widget is not self.master and not isinstance(widget, (ttk.Label, tk.Label, Menu)):
                widget.config(state=state)
        except (tk.TclError, AttributeError):
            # Ignora widgets que não suportam 'state' ou não são widgets padrão
            pass
        
        for child in widget.winfo_children():
            self._set_widget_state_recursively(child, state)

    def _gerar_id_com_formato(self, formato):
        """Gera um ID aleatório baseado em um formato (A=letra, 1=número)."""
        id_gerado = ""
        for caractere in formato:
            if caractere.isalpha():
                id_gerado += random.choice(string.ascii_uppercase)
            elif caractere.isdigit():
                id_gerado += str(random.randint(0, 9))
            else:
                id_gerado += caractere
        return id_gerado
    
    def _start_data_generation_thread(self, callback, **kwargs):
        """Coleta os parâmetros da UI e inicia a geração de dados em uma nova thread."""
        try:
            params = {
                "num_linhas": int(self.entries["Número de Linhas:"].get()),
                "porcentagem_vista": float(self.entries["Desconto à Vista (%):"].get()) / 100,
                "porcentagem_pix": float(self.entries["Desconto Pix (%):"].get()) / 100,
                "porcentagem_cartao": float(self.entries["Acréscimo Cartão (%):"].get()) / 100,
                "porcentagem_boleto": float(self.entries["Acréscimo Boleto (%):"].get()) / 100,
                "formato_id_cliente": self.entries["Formato do ID do Cliente:"].get().strip(),
                "formato_id_produto": self.entries["Formato do ID do Produto:"].get().strip(),
                "data_inicial": datetime.strptime(self.entries["Data Inicial (DD/MM/AAAA):"].get(), "%d/%m/%Y"),
                "data_final": datetime.strptime(self.entries["Data Final (DD/MM/AAAA):"].get(), "%d/%m/%Y"),
                "colunas": [col for col, var in self.colunas_vars.items() if var.get()],
                "paises": [pais for pais, var in self.paises_vars.items() if var.get()]
            }
            if params["num_linhas"] <= 0: raise ValueError("O número de linhas deve ser positivo.")
            if not params["colunas"]: raise ValueError("Selecione pelo menos uma coluna.")
            if not params["paises"]: raise ValueError("Selecione pelo menos um país.")
            if params["data_inicial"] > params["data_final"]: raise ValueError("Data inicial não pode ser maior que a final.")
            if "Email" in params["colunas"] and "Nome do Cliente" not in params["colunas"]: raise ValueError("A coluna 'Email' requer 'Nome do Cliente'.")
            if "Valor da Comissão" in params["colunas"] and "Comissão" not in params["colunas"]: raise ValueError("A coluna 'Valor da Comissão' requer 'Comissão'.")

        except (ValueError, KeyError) as e:
            messagebox.showerror("Erro de Configuração", f"Verifique os parâmetros: {e}", parent=self.master)
            return

        self.gerando_dados = True
        thread = threading.Thread(target=self._worker_gerar_dados, args=(params, callback, kwargs), daemon=True)
        thread.start()

    def _worker_gerar_dados(self, params, callback, kwargs):
        """(Worker Thread) Gera dados com base nos parâmetros e invoca o callback quando concluído."""
        self.master.after(0, self._set_ui_state, False)
        self.master.after(0, self.progress_bar.config, {"maximum": params["num_linhas"], "value": 0})
        
        start_time = time.time()
        self.master.after(0, self._atualizar_cronometro, start_time)
        
        dados_gerados = []
        colunas_selecionadas = params["colunas"]

        for i in range(params["num_linhas"]):
            pais = random.choice(params["paises"])
            estados_do_pais = list(self.estados_cidades_user.get(pais, {}).keys())
            estado = random.choice(estados_do_pais) if estados_do_pais else FAKE_GENERATOR.state()
            cidades_do_estado = self.estados_cidades_user.get(pais, {}).get(estado, [])
            cidade = random.choice(cidades_do_estado) if cidades_do_estado else FAKE_GENERATOR.city()

            preco = round(random.uniform(10, 1000), 2)
            transacao = random.choice(["À vista", "Cartão", "Boleto", "Pix"])
            status = "Aprovado" if transacao in ["À vista", "Pix"] else random.choice(["Aprovado", "Recusado", "Erro", "Não aprovado"])
            id_cliente = self._gerar_id_com_formato(params["formato_id_cliente"])
            id_produto = self._gerar_id_com_formato(params["formato_id_produto"])
            nome_cliente = random.choice(self.clientes) if self.clientes else FAKE_GENERATOR.name()
            
            valor_vista_dinheiro = preco * (1 + params["porcentagem_vista"])
            valor_pix = preco * (1 + params["porcentagem_pix"])
            valor_cartao = preco * (1 + params["porcentagem_cartao"])
            valor_boleto = preco * (1 + params["porcentagem_boleto"])
            data_compra_obj = FAKE_GENERATOR.date_between_dates(params["data_inicial"], params["data_final"])
            comissao_selecionada = random.choice(COMISSOES)

            linha = []
            for col in colunas_selecionadas:
                if col == "ID do Cliente": linha.append(id_cliente)
                elif col == "Nome do Cliente": linha.append(nome_cliente)
                elif col == "Email":
                    dominio = random.choice(self.dominios) if self.dominios else FAKE_GENERATOR.free_email_domain()
                    email = f"{nome_cliente.lower().replace(' ', '.')}{random.randint(1,99)}@{dominio}"
                    linha.append(email)
                elif col == "ID do Produto": linha.append(id_produto)
                elif col == "Nome do Produto": linha.append(random.choice(self.produtos) if self.produtos else "Produto Genérico")
                elif col == "Categoria": linha.append(random.choice(CATEGORIAS))
                elif col == "Fabricante": linha.append(random.choice(FABRICANTES))
                elif col == "Entregador": linha.append(random.choice(ENTREGADORES))
                elif col == "Valor da Entrega": linha.append(locale.currency(preco * 0.10, grouping=True))
                elif col == "Data da Compra": linha.append(data_compra_obj.strftime("%d/%m/%Y"))
                elif col == "Data da Entrega": linha.append((data_compra_obj + timedelta(days=random.randint(3, 30))).strftime("%d/%m/%Y"))
                elif col == "Valor do Produto": linha.append(locale.currency(preco, grouping=True))
                elif col == "Valor à Vista em dinheiro": linha.append(locale.currency(valor_vista_dinheiro, grouping=True))
                elif col == "Valor no Pix": linha.append(locale.currency(valor_pix, grouping=True))
                elif col == "Valor no Cartão": linha.append(locale.currency(valor_cartao, grouping=True))
                elif col == "Valor no Boleto": linha.append(locale.currency(valor_boleto, grouping=True))
                elif col == "Nome da Loja": linha.append(random.choice(self.lojas) if self.lojas else FAKE_GENERATOR.company())
                elif col == "Nome do Vendedor": linha.append(random.choice(self.vendedores) if self.vendedores else FAKE_GENERATOR.name())
                elif col == "Comissão": linha.append(comissao_selecionada)
                elif col == "Valor da Comissão":
                    porcentagem_comissao = float(comissao_selecionada.strip("%")) / 100
                    linha.append(locale.currency(preco * porcentagem_comissao, grouping=True))
                elif col == "País da Compra": linha.append(pais)
                elif col == "Estado da Compra": linha.append(estado)
                elif col == "Cidade da Compra": linha.append(cidade)
                elif col == "Transação": linha.append(transacao)
                elif col == "Status": linha.append(status)
            
            dados_gerados.append(linha)
            
            if i % 100 == 0 or i == params["num_linhas"] - 1:
                progress = i + 1
                self.master.after(0, lambda p=progress: self.progress_bar.config(value=p))
                self.master.after(0, lambda p=progress: self.status_label.config(text=f"Gerando linha {p}/{params['num_linhas']}..."))

        self.gerando_dados = False
        self.last_generated_data = (colunas_selecionadas, dados_gerados)
        self.master.after(0, lambda: callback(**kwargs))

    def _salvar_planilha(self, formato):
        file_path = filedialog.asksaveasfilename(defaultextension=f".{formato}", filetypes=[(f"{formato.upper()} files", f"*.{formato}")], parent=self.master)
        if not file_path: return
        self._start_data_generation_thread(self._do_save, file_path=file_path, formato=formato)

    def _do_save(self, file_path, formato):
        """Callback após os dados serem gerados, para salvar o arquivo."""
        colunas, dados = self.last_generated_data
        if not dados:
            messagebox.showwarning("Aviso", "Nenhum dado foi gerado.", parent=self.master)
            self._set_ui_state(True)
            return

        df = pd.DataFrame(dados, columns=colunas)
        try:
            self.status_label.config(text="Salvando arquivo...")
            if formato == "csv":
                df.to_csv(file_path, index=False, encoding='utf-8-sig')
            else:
                df.to_excel(file_path, index=False)
            messagebox.showinfo("Sucesso", f"Arquivo salvo com sucesso em:\n{file_path}", parent=self.master)
        except Exception as e:
            messagebox.showerror("Erro ao Salvar", f"Não foi possível salvar o arquivo:\n{e}", parent=self.master)
        finally:
            self._set_ui_state(True)

    def _visualizar_dados(self):
        try:
            num_linhas = int(self.entries["Número de Linhas:"].get())
            if num_linhas > 5000:
                if not messagebox.askyesno("Aviso de Desempenho", f"Visualizar {num_linhas} linhas pode ser lento.\nDeseja continuar?", parent=self.master):
                    return
        except (ValueError, KeyError): pass # Validação será feita no início da thread
        self._start_data_generation_thread(self._do_visualize)

    def _do_visualize(self):
        """Callback após os dados serem gerados, para criar a janela de visualização."""
        colunas, dados = self.last_generated_data
        if not dados:
            messagebox.showwarning("Aviso", "Nenhum dado foi gerado.", parent=self.master)
        else:
            self._criar_janela_visualizacao(colunas, dados)
        self._set_ui_state(True)
        
    def _criar_janela_visualizacao(self, colunas, dados):
        janela = tk.Toplevel(self.master)
        janela.title("Visualização dos Dados")
        janela.geometry("1200x700")

        frame_tree = ttk.Frame(janela, padding=10)
        frame_tree.pack(fill="both", expand=True)

        tree = ttk.Treeview(frame_tree, columns=colunas, show="headings")
        tree.pack(side="left", fill="both", expand=True)

        scrollbar_y = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
        scrollbar_y.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar_y.set)
        
        scrollbar_x = ttk.Scrollbar(janela, orient="horizontal", command=tree.xview)
        scrollbar_x.pack(side="bottom", fill="x", padx=10, pady=(0, 10))
        tree.configure(xscrollcommand=scrollbar_x.set)
        
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor='w')

        for row_data in dados:
            tree.insert("", "end", values=row_data)

    def _exibir_ajuda(self):
        janela_ajuda = tk.Toplevel(self.master)
        janela_ajuda.title("Ajuda do Programa")
        janela_ajuda.geometry("800x600")

        texto_ajuda = ScrolledText(janela_ajuda, wrap=tk.WORD, padding=10, autohide=True)
        texto_ajuda.pack(fill="both", expand=True)
        
        ajuda_texto = """ 
 **Ajuda do Programa: Gerador de Planilha de Compras Eletrônicas** Este programa permite gerar dados fictícios de compras eletrônicas para diversas finalidades, como testes de sistemas, simulações ou análise de dados. 

 ### **1. Configurações Principais** * **Número de Linhas:** Define a quantidade de registros a serem gerados na planilha. 
 * **Porcentagem à Vista (%), Pix (%), Cartão (%), Boleto (%):** Ajusta os valores de pagamento de acordo com o método de transação. Use valores negativos para descontos (ex: -5 para 5% de desconto) e positivos para acréscimos (ex: 10 para 10% de acréscimo). 
 * **Formato do ID do Cliente/Produto:** Define um padrão para a geração dos IDs. Use 'A' para letras maiúsculas e '1' para números (ex: ABC-123456). 
 * **Data Inicial/Final:** Define o período para as datas das compras. Use o formato DD/MM/AAAA. 

 ### **2. Seleção de Colunas** * Permite escolher quais colunas serão incluídas na planilha final. Marque ou desmarque as opções conforme sua necessidade. 
 * **Atenção:** A coluna 'Email' requer a seleção de 'Nome do Cliente'. A coluna 'Valor da Comissão' requer a seleção de 'Comissão'. 

 ### **3. Personalização (Produtos, Lojas, Vendedores, Clientes, Email)** * Nessas abas, você pode adicionar ou remover itens das listas usadas na geração de dados. As alterações são mantidas enquanto o programa estiver aberto. 

 ### **4. Região** * Adicione países, estados e cidades específicas. As cidades e estados são hierárquicos: selecione um país para ver/adicionar estados, e um estado para ver/adicionar cidades. 
 * **Importante:** Ao remover um país, todos os seus estados e cidades associados serão removidos. Ao remover um estado, todas as suas cidades associadas serão removidas. 

 ### **5. Como Usar** 1.  Na aba **Configurações**, defina os parâmetros desejados. 
 2.  Nas abas de **Personalização** e **Região**, ajuste as listas de dados conforme sua preferência. 
 3.  Clique em **Visualizar Dados** para gerar e visualizar uma amostra dos dados em uma nova janela. A visualização é limitada para evitar problemas de desempenho, mas o arquivo salvo conterá todas as linhas. 
 4.  Clique em **Salvar como CSV** ou **Salvar como Excel** para exportar todos os dados gerados para um arquivo. 

 --- 

 ### **Agradecimento** Obrigado por utilizar este programa! Desenvolvido por **Diogo Centeno**. 
 """ 
        texto_ajuda.insert(tk.END, ajuda_texto)
        texto_ajuda.configure(state="disabled")

    def _menu_regiao(self, event, tipo):
        menu = Menu(self.master, tearoff=0)
        remover_func = getattr(self, f"_remover_{tipo}")
        menu.add_command(label=f"Remover {tipo.capitalize()}", command=remover_func)
        menu.post(event.x_root, event.y_root)

    def _bind_context_menu(self, widget):
        """Vincula o menu de contexto recursivamente a todos os widgets."""
        widget.bind("<Button-3>", self._menu_contexto)
        for child in widget.winfo_children():
            self._bind_context_menu(child)

    def _menu_contexto(self, event):
        """Cria e exibe um menu de contexto (clique direito) para widgets de entrada."""
        try:
            menu = Menu(self.master, tearoff=0)
            widget = event.widget
            if isinstance(widget, (ttk.Entry, tk.Entry)):
                if widget.selection_present():
                    menu.add_command(label="Copiar", command=lambda: widget.event_generate("<<Copy>>"))
                
                try:
                    if self.master.clipboard_get():
                        menu.add_command(label="Colar", command=lambda: widget.event_generate("<<Paste>>"))
                except tk.TclError:
                    pass # Clipboard is empty
                
                if menu.index(tk.END) is not None:
                     menu.add_separator()
                menu.add_command(label="Limpar", command=lambda: widget.delete(0, tk.END))

            elif isinstance(widget, Listbox):
                 if widget.curselection():
                    selected_text = widget.get(widget.curselection())
                    menu.add_command(label=f"Copiar '{selected_text[:20]}...'", command=lambda: self.master.clipboard_append(selected_text))

            if menu.index(tk.END) is not None:
                menu.post(event.x_root, event.y_root)
        except tk.TclError:
            pass


if __name__ == "__main__":
    # Inicia a aplicação com uma janela TTKBootstrap e um tema padrão
    root = ttk.Window(themename="litera")
    app = GeradorPlanilhaApp(root)
    root.mainloop()

