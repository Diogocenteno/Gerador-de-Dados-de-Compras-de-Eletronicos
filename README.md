Gerador de Dados de Compras de Eletrônicos

Descrição

Este script gera um conjunto de dados fictícios de compras de produtos eletrônicos. Ele utiliza as bibliotecas pandas e faker para criar e exportar um arquivo Excel contendo informações de 50.000 compras, distribuídas entre 100 tipos de produtos eletrônicos e 40 países com seus respectivos estados e cidades.

Funcionalidades

Geração de um grande volume de dados fictícios (50.000 registros)

Inclusão de 100 tipos de produtos eletrônicos

Distribuição geográfica dos dados em 40 países

Formatação da data e preços para um formato legível

Exportação dos dados para um arquivo Excel

Tecnologias Utilizadas

Python

Pandas

Faker

Random

Datetime

Como Utilizar

Instale as dependências necessárias utilizando:

pip install pandas faker openpyxl

Execute o script Python.

O arquivo gerado dados_compras_eletronicos_50mil_linhas.xlsx estará disponível no diretório do script.

Estrutura dos Dados

O dataset gerado contém as seguintes colunas:

ID do Cliente: Identificador único para cada cliente

Nome Completo do Cliente: Nome e sobrenome gerados aleatoriamente

ID do Produto: Identificador único do produto

Nome do Produto: Nome do produto eletrônico

Data da Compra: Data formatada no padrão dd/mm/yyyy

Preço: Valor do produto formatado em reais (R$)

País da Compra: País onde a compra foi realizada

Estado da Compra: Estado correspondente ao país

Cidade da Compra: Cidade correspondente ao estado

Autor

Criado para fins de estudo e análise de dados fictícios. Ajuste conforme necessário para seus projetos.

Este README fornece uma visão geral do funcionamento do script e instruções para sua utilização. Qualquer dúvida ou melhoria, sinta-se à vontade para contribuir!
