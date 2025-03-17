Gerador de Planilha de Compras Eletrônicas
Este projeto é um gerador de dados fictícios para compras eletrônicas, desenvolvido em Python com interface gráfica utilizando a biblioteca tkinter. O programa permite a criação de planilhas personalizadas com informações como clientes, produtos, métodos de pagamento, localização e status de transações. Além disso, oferece a possibilidade de exportar os dados gerados em formatos como Excel (xlsx) e CSV.

Funcionalidades
Geração de Dados Fictícios:

Gera dados de clientes, produtos, métodos de pagamento, localização e status de transações.

Personalização de IDs, nomes, categorias, fabricantes, entregadores, valores, datas, lojas, vendedores, comissões, países, estados e cidades.

Configurações de Geração:

Definição do número de linhas.

Ajuste de porcentagens de acréscimo para diferentes métodos de pagamento (à vista, Pix, cartão, boleto).

Formatação personalizada de IDs de clientes e produtos.

Seleção de intervalos de datas para as compras.

Escolha de colunas e países a serem incluídos na planilha.

Personalização de Dados:

Adição e remoção de produtos, lojas, vendedores, clientes e domínios de email.

Adição e remoção de países, estados e cidades.

Exportação de Dados:

Salvar os dados gerados em formato Excel (xlsx) ou CSV.

Escolha do nome do arquivo e local de salvamento.

Visualização dos Dados:

Exibição dos dados gerados em uma tabela interativa.

Ajuste automático da largura das colunas.

Exportação dos dados visualizados para um arquivo de texto (txt).

Interface Gráfica Amigável:

Abas para configurações, personalização de produtos, lojas, vendedores, clientes, email e região.

Barra de progresso e cronômetro para acompanhamento da geração de dados.

Menu de contexto com opções de copiar e limpar.

Requisitos
Python 3.x

Bibliotecas necessárias:

pandas

faker

tkinter

locale

threading

time

Para instalar as bibliotecas necessárias, execute o seguinte comando:

bash
Copy
pip install pandas faker
Como Usar
Configurações:

Na aba "Configurações", defina o número de linhas, porcentagens de acréscimo, formato dos IDs, intervalo de datas, colunas e países desejados.

Personalização:

Nas abas de "Personalização", adicione ou remova produtos, lojas, vendedores, clientes, domínios de email, países, estados e cidades.

Geração de Dados:

Clique em "Visualizar Dados" para gerar e visualizar os dados em uma tabela interativa.

Use os botões "Salvar como Excel" ou "Salvar como CSV" para exportar os dados.

Visualização:

Na janela de visualização, ajuste as colunas automaticamente com o botão "Ajustar Colunas".

Salve os dados em um arquivo de texto com o botão "Salvar em Bloco de Notas".

Estrutura do Código
O código está organizado em funções que lidam com diferentes aspectos do programa:

Geração de Dados:

gerar_dados: Gera os dados fictícios com base nas configurações definidas.

gerar_id_com_formato: Gera IDs personalizados com base em um formato especificado.

Interface Gráfica:

atualizar_cronometro: Atualiza o cronômetro durante a geração de dados.

marcar_desmarcar_colunas e marcar_desmarcar_paises: Permitem marcar ou desmarcar todas as colunas ou países de uma vez.

adicionar_item e remover_item: Adicionam ou removem itens das listas de personalização.

salvar_planilha: Salva os dados gerados em formato Excel ou CSV.

visualizar_dados: Exibe os dados gerados em uma tabela interativa.

Personalização:

Funções para adicionar e remover produtos, lojas, vendedores, clientes, domínios de email, países, estados e cidades.

Exemplo de Uso
Configurações:

Defina o número de linhas como 1000.

Ajuste as porcentagens de acréscimo para os métodos de pagamento.

Defina o formato dos IDs como ABC-123456 para clientes e XKIOPY-123 para produtos.

Escolha o intervalo de datas de 01/01/2000 a 01/01/2025.

Selecione as colunas desejadas e os países de origem das compras.

Personalização:

Adicione novos produtos eletrônicos à lista de produtos.

Adicione novas lojas e vendedores.

Adicione novos domínios de email.

Geração de Dados:

Clique em "Visualizar Dados" para gerar e visualizar os dados.

Use os botões "Salvar como Excel" ou "Salvar como CSV" para exportar os dados.

Visualização:

Na janela de visualização, ajuste as colunas automaticamente com o botão "Ajustar Colunas".

Salve os dados em um arquivo de texto com o botão "Salvar em Bloco de Notas".

Agradecimentos
Este projeto foi desenvolvido por Diogo Centeno como uma ferramenta para gerar dados fictícios de compras eletrônicas. Se precisar de suporte ou tiver sugestões, entre em contato.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
