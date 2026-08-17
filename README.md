# two_project_august_pair-programming
👥 Cadastro de Clientes

O sistema permite registrar informações dos clientes, como:

Nome
Telefone
Quantidade de pedidos
Total gasto

Também é possível consultar os clientes cadastrados através da interface.

Os dados são armazenados em:

dados/clientes.json
💳 Formas de Pagamento

O sistema possui as seguintes formas de pagamento:

💵 Dinheiro
💳 Débito
💳 Crédito
📱 Pix

No pagamento em dinheiro, o sistema calcula automaticamente o troco.

Caso o valor recebido seja menor que o valor da compra, o pagamento não pode ser confirmado.

🧾 Recibos

Depois da finalização de uma venda, o sistema gera um recibo com informações como:

Nome da padaria
Data e horário
Cliente
Produtos
Quantidades
Valores
Total da compra
Forma de pagamento
Valor recebido
Troco

O recibo pode ser visualizado na aplicação e também salvo em formato .txt.

📊 Relatório de Vendas

O sistema mantém informações sobre as vendas realizadas.

O relatório apresenta:

Quantidade de pedidos.
Quantidade de produtos vendidos.
Faturamento.
Produto mais vendido.

As informações são armazenadas em:

dados/relatorio.json
🔎 Pesquisa de Produtos

O sistema possui uma área de pesquisa para facilitar a localização dos produtos no cardápio.

A pesquisa permite encontrar produtos pelo nome.

🌙 Modo Claro e Escuro

A interface possui dois temas:

☀️ Modo Claro
🌙 Modo Escuro

O usuário pode alternar entre os temas através do botão disponível na interface.

🖥️ Interface Gráfica

A interface foi desenvolvida utilizando:

tkinter
ttk

O sistema possui:

Abas para as categorias.
Cartões de produtos.
Botões de ação.
Campos de entrada.
Seletores de quantidade.
Tela de pagamento.
Tela de recibo.
Tela de clientes.
Tela de relatório.
Modo claro e escuro.
🛠️ Tecnologias Utilizadas
🐍 Python
🖼️ Tkinter
🎨 ttk
📄 JSON
📁 OS
🕐 Datetime

O projeto utiliza apenas recursos da biblioteca padrão do Python, não sendo necessário instalar bibliotecas externas.

📋 Pré-requisitos

Para executar o sistema, é necessário ter:

Python 3 instalado.
Tkinter disponível na instalação do Python.
Windows, Linux ou macOS.
▶️ Como Executar

Primeiro, renomeie o arquivo do código para:

padaria_artes.py

Depois, abra o terminal dentro da pasta do projeto e execute:

python padaria_artes.py

A interface da Padaria Artes será aberta automaticamente.

📁 Estrutura do Projeto

A estrutura do projeto pode ficar assim:

Padaria-Artes/
│
├── padaria_artes.py
│
├── dados/
│   ├── estoque.json
│   ├── clientes.json
│   └── relatorio.json
│
├── ticket/
│   ├── pedido_YYYYMMDD_HHMMSS.json
│   └── pedido_YYYYMMDD_HHMMSS_recibo.txt
│
└── README.md

A pasta dados armazena as informações de estoque, clientes e relatórios.

A pasta ticket armazena os pedidos e recibos gerados pelo sistema.

💰 Funcionamento de uma Venda

O processo de venda funciona da seguinte forma:

Selecionar os produtos.
Escolher as quantidades.
Conferir o total da compra.
Iniciar o processo de pagamento.
Informar os dados do cliente.
Escolher a forma de pagamento.
Confirmar o pagamento.
Atualizar o estoque.
Registrar a venda.
Gerar o pedido em JSON.
Gerar o recibo em TXT.
📄 Arquivos Gerados
estoque.json

Armazena as quantidades disponíveis dos produtos.

clientes.json

Armazena os dados dos clientes e suas informações de compras.

relatorio.json

Armazena os dados das vendas realizadas.

Arquivos .json dos pedidos

Cada pedido pode ser armazenado individualmente com suas informações.

Arquivos .txt

Contêm os recibos das compras realizadas.

📌 Informações do Projeto

Nome: Padaria Artes
Linguagem: Python
Interface gráfica: Tkinter
Tipo: Sistema de vendas
Arquivo principal: padaria_artes.py