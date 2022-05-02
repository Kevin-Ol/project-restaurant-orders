# Projeto Restaurant Orders

Projeto feito como critério avaliativo na escola de programação Trybe.

Foi utilizada a linguagem de programação Python.

O objetivo do projeto foi criar um sistema de gerenciamento de uma lanchonete, controlando dados como nome do cliente, menu de lanches, dias de 
funcionamento, pratos mais pedidos, pratos nunca pedidos, e estoque, utilizando as estruturas de dados Hashmap e Conjunto, representados respectivamente 
por dicionário e set na linguagem Python.

## Instruções para reproduzir o projeto

#### Pré Requisitos

Possuir Python instalado

---

1. Clone o repositório
  * `git@github.com:Kevin-Ol/project-restaurant-orders.git`.
  * Entre na pasta do repositório que você acabou de clonar:
    * `cd project-tech-restaurant-orders`

2. Inicie e ative um ambiente virtual
  * `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências
  * `python3 -m pip install -r dev-requirements.txt`

obs: caso haja algum problema na instalação do pacote wheel, reinstale-o com o comando
  * `python3 -m pip install wheel`
---

Os requisitos desenvolvidos no projeto são:

`src/analyze_log.py`

- Função `analyze_log`: possui como parâmetro um caminho para um arquivo csv. Juntamente com outras funções auxiliares criadas no arquivo, a função 
analisa os dados, retorna erros caso não sejam inseridos extensão ou arquivo válidos, e caso tudo esteja correto responde as perguntas: 

  * Qual o prato mais pedido por 'maria'?
  * Quantas vezes 'arnaldo' pediu 'hamburguer'?
  * Quais pratos 'joao' nunca pediu?
  * Quais dias 'joao' nunca foi na lanchonete?

Para este exemplo foi usado o arquivo `data/orders_1.csv`. As respostas são salvas em um arquivo txt localizado em `data/mkt_campaign.txt`.

```bash
hamburguer
1
{'pizza', 'coxinha', 'misto-quente'}
{'sabado', 'segunda-feira'}
```

`src/track_orders.py`

- Classe `TrackOrders`: classe responsável por criar pedidos de forma contínua. Através da criação de sua instância, possui o método `add_new_order` 
capaz de criar pedidos, que são armazenados em seus atributos. Com a lista de pedidos, é possível responder as perguntas:

  * Prato favorito por cliente
    * método `get_most_ordered_dish_per_customer` que recebe o nome do cliente desejado;

  * Pratos nunca pedidos por cada cliente
    * método `get_never_ordered_per_customer` que recebe o nome do cliente desejado;
  
  * Dias nunca visitados por cada cliente
    * método `get_days_never_visited_per_customer` que recebe o nome do cliente desejado;

  * Dia mais movimentado
    * método `get_busiest_day` que não necessita de argumentos;

  * Dia menos movimentado
    * método `get_least_busy_day` que não necessita de argumentos;

`src/inventory_control.py`

- Classe `InventoryControl`: classe responsável pelo controle de estoque da lanchonete. A partir do menu de lanches da lanchonete, e de um inventário
mínimo de ingredientes, é capaz de controlar a quantidade de ingredientes que devem ser comprados para reabastecimento, e controle de quais lanches
estão disponíveis de acordo com o estoque atual. Possui os métodos:

  * `get_days_never_visited_per_customer` recebe o nome do cliente, o pedido, e o dia, e verifica se é possível criar tal pedido, fazendo a redução da
quantidade de ingredientes correspondente;
  * `get_quantities_to_buy`: não recebe parâmetros e retorna a quantidade de cada ingrediente necessária para ser comprada de forma a manter o estoque 
mínimo;
  * `get_available_dishes`: não recebe parâmetros e retorna os lanches disponíveis para serem feitos de acordo com o estoque atual;
