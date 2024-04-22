![campus_marica](https://github.com/Quezia-Moura/PEI.V---Ciclista-Legal/assets/125207561/0fe91225-a24b-4bf4-a161-8f04de855327)
<h1>Trabalho P1</h1>

Curso: Engenharia de Software <br>
Período: 5º <br>
Disciplina: Banco de Dados NoSQL <br>
Professor: Fabrício Tadeu Dias 
<hr>

## Tecnologias Utilizadas

- Node.js
- Flask
- MongoDB
- Mongoose (para modelagem de dados no MongoDB)

## Pré-requisitos

- Node.js instalado
- Python e Flask instalados
- MongoDB instalado ou uma instância na nuvem (como MongoDB Atlas)

# 👩‍💻 Resumo sobre a Aplicação
<strong><i>Obs.: O projeto não está funcionando como pedido. Pretendo arrumar os erros futuramente.</i></strong>

1. **Estrutura do Projeto:**
   - O projeto consiste em uma aplicação Node.js com um servidor Flask em Python que se comunica com um banco de dados MongoDB.
   - MVC <br>
     ![trabalho_node_mvc](https://github.com/Quezia-Moura/Banco-de-Dados-NoSQL_Trabalho-P1/assets/125207561/1ce259b6-e30a-4eaf-80ad-c6dd6a56a85c)


2. **Flask (app.py):**
   - O Flask atua como uma camada intermediária entre a aplicação Node.js e o banco de dados MongoDB.
   - Ele possui rotas para lidar com requisições HTTP, como GET, POST, PUT e DELETE, para interagir com os usuários na aplicação Node.js.
   - Quando uma requisição é recebida, o Flask faz requisições HTTP para a aplicação Node.js para executar as operações no banco de dados.

3. **Node.js (src/server.js):**
   - O Node.js fornece uma API RESTful para gerenciar usuários.
   - Ele usa o Express.js para lidar com as rotas e controladores para processar as requisições.
   - Os controladores interagem com o banco de dados MongoDB usando o Mongoose para realizar operações como criar, listar, atualizar e excluir usuários.

4. **MongoDB (src/models/User.js):**
   - O arquivo `User.js` define o modelo de dados para usuários na aplicação.
   - Ele usa o Mongoose para definir um esquema e interagir com o banco de dados MongoDB.
   - As operações CRUD (Create, Read, Update, Delete) são realizadas neste arquivo para manipular os documentos de usuário no MongoDB.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
