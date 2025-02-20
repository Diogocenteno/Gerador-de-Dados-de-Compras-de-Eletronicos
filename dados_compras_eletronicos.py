#%%

import pandas as pd
import random
from faker import Faker
from datetime import datetime
import string

# Gerador de dados fictícios
fake = Faker()

# Listas de exemplos de nomes de lojas
lojas = [
    "Magazine Luiza", "Lojas Americanas", "Ponto Frio", "Casas Bahia", "Submarino", 
    "Carrefour", "Extra", "Fast Shop", "Havan", "Mercado Livre", 
    "Walmart", "Amazon", "Nike", "Adidas", "Apple Store", 
    "Sephora", "Zara", "Leroy Merlin", "Centauro", "C&A", 
    "Renner", "Riachuelo", "H&M", "Forever 21", "Tok&Stok", 
    "Marisa", "Casas Pernambucanas", "Kalunga", "Drogaria São Paulo", "Pague Menos", 
    "L'Occitane", "O Boticário", "Trator 360", "B2W (Americanas.com, Submarino e Shoptime)", "Ricardo Eletro", 
    "Dell", "Best Buy", "Carrefour Brasil", "Carrefour Express", "Walmart Brasil", 
    "Tenda", "Oi", "Casas Bahia Online", "Mercado Livre Brasil", "AliExpress", 
    "Target", "Urban Outfitters", "Pull&Bear", "Mango", "Kmart", 
    "Whole Foods Market", "GameStop", "Gucci", "Prada", "Louis Vuitton", 
    "Chanel", "Mango", "Victoria's Secret", "Bath & Body Works", "Macy's", 
    "Bershka", "Stradivarius", "Pull&Bear", "Nike Store", "Adidas Store", 
    "Puma", "Under Armour", "New Balance", "Asics", "Reebok", 
    "Foot Locker", "Champion", "Vans", "Converse", "Dr. Martens", 
    "Havaianas", "Schutz", "Arezzo", "Melissa", "Toms", 
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
    "Albertsons Companies", "FreshDirect", "Peapod", "Instacart", "Shipt"
]

# Inicializar a lista primeiro
produtos_eletronicos = []

# produtos eletronicos 200
produtos_eletronicos = [
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
    "Aquecedor de Ambiente Inteligente", "Leitor de Código de Barras", "Cartão de Memória de Alta Velocidade", "Carregador de Bateria Sem Fio"
]

# Dicionário com estados e cidades para cada país
estados_cidades = {
    "United States": {
        "California": ["Los Angeles", "San Francisco", "San Diego", "Sacramento", "San Jose", "Fresno"],
        "Texas": ["Houston", "Dallas", "Austin", "San Antonio", "Fort Worth", "El Paso"],
        "New York": ["New York", "Buffalo", "Rochester", "Albany", "Syracuse", "Yonkers"],
        "Florida": ["Miami", "Orlando", "Tampa", "Jacksonville", "Fort Lauderdale", "Tallahassee"],
        "Illinois": ["Chicago", "Springfield", "Naperville", "Aurora", "Rockford", "Peoria"]
    },
    "Brazil": {
        "São Paulo": ["São Paulo", "Campinas", "Santos", "São Bernardo do Campo", "Sorocaba", "Ribeirão Preto"],
        "Rio de Janeiro": ["Rio de Janeiro", "Niterói", "Petrópolis", "Campos dos Goytacazes", "Nova Iguaçu", "Volta Redonda"],
        "Minas Gerais": ["Belo Horizonte", "Uberlândia", "Juiz de Fora", "Montes Claros", "Betim", "Contagem"],
        "Paraná": ["Curitiba", "Londrina", "Maringá", "Cascavel", "Ponta Grossa", "Foz do Iguaçu"],
        "Rio Grande do Sul": ["Porto Alegre", "Caxias do Sul", "Pelotas", "Santa Maria", "Canoas", "Novo Hamburgo"]
    },
    "Canada": {
        "Ontario": ["Toronto", "Ottawa", "Hamilton", "Mississauga", "Kitchener", "Windsor"],
        "British Columbia": ["Vancouver", "Victoria", "Kelowna", "Burnaby", "Surrey", "Richmond"],
        "Quebec": ["Montreal", "Quebec City", "Laval", "Sherbrooke", "Gatineau", "Trois-Rivières"],
        "Alberta": ["Calgary", "Edmonton", "Red Deer", "Lethbridge", "Medicine Hat", "Grande Prairie"],
        "Manitoba": ["Winnipeg", "Brandon", "Steinbach", "Thompson", "Selkirk", "Portage la Prairie"]
    },
    "Mexico": {
        "CDMX": ["Mexico City", "Coyoacán", "Xochimilco", "Tlalpan", "Iztapalapa", "Azcapotzalco"],
        "Jalisco": ["Guadalajara", "Zapopan", "Puerto Vallarta", "Tlaquepaque", "Tonala", "Tepatitlán"],
        "Nuevo León": ["Monterrey", "San Pedro", "Guadalupe", "Apodaca", "Santa Catarina", "San Nicolás"],
        "Puebla": ["Puebla", "Tehuacán", "San Martín Texmelucan", "Atlixco", "Cholula", "Amozoc"],
        "Veracruz": ["Veracruz", "Xalapa", "Coatzacoalcos", "Orizaba", "Poza Rica", "Córdoba"]
    },
    "Argentina": {
        "Buenos Aires": ["Buenos Aires", "La Plata", "Mar del Plata", "Quilmes", "Bahía Blanca", "Tigre"],
        "Córdoba": ["Córdoba", "Villa Carlos Paz", "Río Cuarto", "Alta Gracia", "San Francisco", "Jesús María"],
        "Santa Fe": ["Rosario", "Santa Fe", "Rafaela", "Venado Tuerto", "Reconquista", "Sunchales"],
        "Mendoza": ["Mendoza", "San Rafael", "Godoy Cruz", "Luján de Cuyo", "Guaymallén", "Malargüe"],
        "Tucumán": ["San Miguel de Tucumán", "Tafí Viejo", "Yerba Buena", "Concepción", "Monteros", "Banda del Río Salí"]
    },
    "Chile": {
        "Santiago": ["Santiago", "Las Condes", "Providencia", "Puente Alto", "Maipú", "Ñuñoa"],
        "Valparaíso": ["Valparaíso", "Viña del Mar", "Quilpué", "Concón", "Villa Alemana", "Los Andes"],
        "Biobío": ["Concepción", "Talcahuano", "Los Ángeles", "Coronel", "San Pedro de la Paz", "Chillán"],
        "Antofagasta": ["Antofagasta", "Calama", "Tocopilla", "Mejillones", "San Pedro de Atacama", "Taltal"],
        "Araucanía": ["Temuco", "Villarrica", "Angol", "Padre Las Casas", "Pucón", "Lautaro"]
    },
    "Germany": {
        "Bavaria": ["Munich", "Nuremberg", "Augsburg", "Regensburg", "Ingolstadt", "Würzburg"],
        "Berlin": ["Berlin", "Potsdam", "Oranienburg", "Neuruppin", "Königs Wusterhausen", "Bernau"],
        "Hesse": ["Frankfurt", "Wiesbaden", "Darmstadt", "Kassel", "Offenbach", "Marburg"],
        "Hamburg": ["Hamburg", "Lübeck", "Kiel", "Flensburg", "Elmshorn", "Neumünster"],
        "Baden-Württemberg": ["Stuttgart", "Karlsruhe", "Mannheim", "Freiburg", "Heidelberg", "Ulm"]
    },
    "France": {
        "Île-de-France": ["Paris", "Versailles", "Boulogne-Billancourt", "Montreuil", "Argenteuil", "Créteil"],
        "Provence-Alpes-Côte d'Azur": ["Marseille", "Nice", "Toulon", "Aix-en-Provence", "Avignon", "Cannes"],
        "Auvergne-Rhône-Alpes": ["Lyon", "Saint-Étienne", "Grenoble", "Villeurbanne", "Clermont-Ferrand", "Chambéry"],
        "Nouvelle-Aquitaine": ["Bordeaux", "Limoges", "Pau", "La Rochelle", "Bayonne", "Angoulême"],
        "Hauts-de-France": ["Lille", "Amiens", "Roubaix", "Tourcoing", "Dunkerque", "Calais"]
    },
    "Italy": {
        "Lazio": ["Rome", "Latina", "Tivoli", "Frosinone", "Velletri", "Guidonia Montecelio"],
        "Lombardy": ["Milan", "Bergamo", "Brescia", "Monza", "Como", "Varese"],
        "Tuscany": ["Florence", "Pisa", "Siena", "Livorno", "Prato", "Arezzo"],
        "Campania": ["Naples", "Salerno", "Caserta", "Sorrento", "Pompeii", "Avellino"],
        "Sicily": ["Palermo", "Catania", "Messina", "Syracuse", "Trapani", "Agrigento"]
    },
    "Australia": {
        "New South Wales": ["Sydney", "Newcastle", "Wollongong", "Maitland", "Coffs Harbour", "Tamworth"],
        "Victoria": ["Melbourne", "Geelong", "Ballarat", "Bendigo", "Shepparton", "Melton"],
        "Queensland": ["Brisbane", "Gold Coast", "Cairns", "Townsville", "Mackay", "Rockhampton"],
        "Western Australia": ["Perth", "Mandurah", "Bunbury", "Geraldton", "Kalgoorlie", "Albany"],
        "South Australia": ["Adelaide", "Mount Gambier", "Whyalla", "Port Lincoln", "Victor Harbor", "Murray Bridge"]
    },
    "Japan": {
        "Tokyo": ["Tokyo", "Chiba", "Yokohama", "Saitama", "Kawasaki", "Koshigaya"],
        "Osaka": ["Osaka", "Kobe", "Sakai", "Hirakata", "Takarazuka", "Toyonaka"],
        "Hokkaido": ["Sapporo", "Hakodate", "Asahikawa", "Obihiro", "Muroran", "Kitami"],
        "Kyoto": ["Kyoto", "Uji", "Maizuru", "Kameoka", "Fushimi", "Kizugawa"],
        "Okinawa": ["Naha", "Okinawa City", "Uruma", "Ishigaki", "Nago", "Miyakojima"]
    },
    "United Kingdom": {
        "England": ["London", "Manchester", "Birmingham", "Liverpool", "Leeds", "Sheffield"],
        "Scotland": ["Edinburgh", "Glasgow", "Aberdeen", "Dundee", "Inverness", "Perth"],
        "Wales": ["Cardiff", "Swansea", "Newport", "Wrexham", "Bangor", "Carmarthen"],
        "Northern Ireland": ["Belfast", "Derry", "Lisburn", "Newtownabbey", "Craigavon", "Ballymena"],
        "Cornwall": ["Truro", "Penzance", "Falmouth", "Newquay", "St Ives", "Camborne"]
    },
    "Spain": {
        "Madrid": ["Madrid", "Getafe", "Alcalá de Henares", "Leganés", "Fuenlabrada", "Móstoles"],
        "Catalonia": ["Barcelona", "Girona", "Tarragona", "Lleida", "Reus", "Mataró"],
        "Andalusia": ["Seville", "Malaga", "Granada", "Córdoba", "Jerez de la Frontera", "Almería"],
        "Valencia": ["Valencia", "Alicante", "Castellón de la Plana", "Elche", "Orihuela", "Torrent"],
        "Basque Country": ["Bilbao", "San Sebastián", "Vitoria-Gasteiz", "Getxo", "Barakaldo", "Irun"]
    },
    "South Korea": {
        "Seoul": ["Seoul", "Incheon", "Gwangmyeong", "Suwon", "Seongnam", "Yongin"],
        "Busan": ["Busan", "Ulsan", "Changwon", "Tongyeong", "Jinhae", "Geoje"],
        "Daegu": ["Daegu", "Gyeongsan", "Andong", "Pohang", "Gumi", "Yeongcheon"],
        "Gyeonggi": ["Suwon", "Bucheon", "Goyang", "Seongnam", "Ansan", "Yongin"],
        "Jeju": ["Jeju", "Seogwipo", "Jeju City", "Aewol", "Halla", "Sungchang"]
    },
    "South Africa": {
        "Gauteng": ["Johannesburg", "Pretoria", "Centurion", "Sandton", "Midrand", "Ekurhuleni"],
        "Western Cape": ["Cape Town", "Stellenbosch", "Paternoster", "George", "Mossel Bay", "Ceres"],
        "KwaZulu-Natal": ["Durban", "Pietermaritzburg", "Newcastle", "Empangeni", "Umlazi", "Richards Bay"],
        "Eastern Cape": ["Port Elizabeth", "East London", "Grahamstown", "Mthatha", "Queenstown", "King William's Town"],
        "Mpumalanga": ["Nelspruit", "Witrivier", "Barberton", "White River", "Sabie", "Komatipoort"]
    },
    "Sweden": {
        "Stockholm": ["Stockholm", "Uppsala", "Västerås", "Norrköping", "Östersund", "Sundbyberg"],
        "Västra Götaland": ["Gothenburg", "Borås", "Alingsås", "Trollhättan", "Uddevalla", "Kungälv"],
        "Skåne": ["Malmö", "Lund", "Helsingborg", "Kristianstad", "Trelleborg", "Ystad"],
        "Östergötland": ["Linköping", "Norrköping", "Motala", "Finspång", "Söderköping", "Boxholm"],
        "Halland": ["Halmstad", "Varberg", "Kungsbacka", "Laholm", "Falkenberg", "Höganäs"]
    },
    "Russia": {
        "Moscow": ["Moscow", "Khimki", "Podolsk", "Balashikha", "Kolomna", "Serpukhov"],
        "Saint Petersburg": ["Saint Petersburg", "Pushkin", "Pavlovsk", "Gatchina", "Lomonosov", "Vyborg"],
        "Tatarstan": ["Kazan", "Naberezhnye Chelny", "Almetyevsk", "Zelenodolsk", "Bugulma", "Chistopol"],
        "Siberia": ["Novosibirsk", "Omsk", "Krasnoyarsk", "Irkutsk", "Tomsk", "Ulan-Ude"],
        "Far East": ["Vladivostok", "Khabarovsk", "Yakutsk", "Magadan", "Birobidzhan", "Petropavlovsk-Kamchatsky"]
    },
    "Egypt": {
        "Cairo": ["Cairo", "Giza", "Shubra El Kheima", "Helwan", "6th of October City", "Nasr City"],
        "Alexandria": ["Alexandria", "Damanhur", "Kafr el-Dawwar", "Borg El Arab", "Rosetta", "Abu Qir"],
        "Giza": ["Giza", "6th of October City", "El Haram", "Dokki", "Helwan", "Shubra El Kheima"],
        "Luxor": ["Luxor", "Aswan", "Edfu", "Qena", "Kom Ombo", "Esna"],
        "Aswan": ["Aswan", "Abu Simbel", "Kom Ombo", "Aswan High Dam", "New Aswan", "Edfu"]
    }
}

fake = Faker()
num_linhas = 200000
dados = []

for i in range(num_linhas):
    id_cliente = i + 1
    nome_completo_cliente = fake.name()
    letras_aleatorias = ''.join(random.choices(string.ascii_uppercase, k=2))
    id_produto = f"{letras_aleatorias}{random.randint(1000, 9999)}"
    nome_produto = random.choice(produtos_eletronicos)
    data_compra = fake.date_between_dates(date_start=datetime(2020, 1, 1), date_end=datetime(2024, 12, 31))
    preco = round(random.uniform(10, 1000), 2)
    pais_compra = random.choice(list(estados_cidades.keys()))
    estado_compra = random.choice(list(estados_cidades[pais_compra].keys()))
    cidade_compra = random.choice(estados_cidades[pais_compra][estado_compra])
    
    # Calculando os valores
    valor_cartao = round(preco * 1.05, 2)  # 5% a mais no preço
    valor_boleto = round(preco * 1.10, 2)  # 10% a mais no preço
    
    # Adicionando o nome da loja
    nome_loja = random.choice(lojas)
    nome_completo_vendedor = fake.name()  # Movido para depois do nome da loja
    
    dados.append([ 
        id_cliente, nome_completo_cliente, id_produto, nome_produto, data_compra.strftime("%d/%m/%Y"),
        f"R$ {preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), 
        f"R$ {valor_cartao:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), 
        f"R$ {valor_boleto:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        nome_loja, nome_completo_vendedor, pais_compra, estado_compra, cidade_compra
    ])

# Criando o DataFrame com a nova ordem de colunas
df = pd.DataFrame(dados, columns=[ 
    'ID do Cliente', 'Nome do Cliente', 'ID do Produto', 'Nome do Produto', 'Data da Compra',
    'Preço à Vista', 'Valor no Cartão 5%', 'Valor no Boleto 10%', 'Nome da Loja', 'Nome do Vendedor', 
    'País da Compra', 'Estado da Compra', 'Cidade da Compra'
])

# Salvando o arquivo Excel
df.to_excel("dados_compras_eletronicos.xlsx", index=False)
print("Planilha gerada com sucesso!")
