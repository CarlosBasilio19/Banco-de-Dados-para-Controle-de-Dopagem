# 📌 Sistema de Controle de Dopagem  

## 📋 Descrição do Projeto  
Este projeto consiste na modelagem e implementação de um banco de dados relacional para o **Sistema de Controle de Dopagem**. O objetivo é gerenciar o processo de coleta, análise e rastreamento de amostras de atletas submetidos a testes antidoping.  

A base de dados permitirá o armazenamento e consulta de informações essenciais, incluindo:  
✅ Registro de atletas e eventos esportivos.  
✅ Gerenciamento de amostras de dopagem.  
✅ Rastreabilidade de laboratórios responsáveis pela análise.  
✅ Registro de oficiais de controle.  

## 📁 Estrutura do Projeto  
O projeto está organizado da seguinte forma:  

📂 `docs/` → Diagramas e documentação do projeto.  
📂 `sql/` → Scripts SQL para criação e manipulação do banco de dados.  
📂 `scripts/` → Consultas e exemplos de operações com `INSERT`, `UPDATE` e `DELETE`.  

## 📌 Modelagem do Banco de Dados  
O banco de dados foi modelado seguindo os seguintes passos:  

1️⃣ **Diagrama Entidade-Relacionamento (DER):** Modelagem inicial das tabelas e seus relacionamentos.  
2️⃣ **Modelo Relacional:** Conversão do DER para tabelas normalizadas.  
3️⃣ **Implementação Física:** Criação das tabelas no **MySQL** e inserção de dados de teste.  

## 🛠️ Tecnologias Utilizadas  
- **Banco de Dados:** MySQL  
- **Ferramentas de Modelagem:** MySQL Workbench, Draw.io  
- **Linguagem SQL:** Para criação de tabelas, inserção e manipulação de dados  

## 🚀 Como Executar o Projeto  

### 📌 Pré-requisitos  
Antes de começar, certifique-se de ter os seguintes itens instalados:  
- [MySQL Server](https://dev.mysql.com/downloads/)  
- [MySQL Workbench](https://www.mysql.com/products/workbench/)  

### 📌 Passos para Execução  
1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/sistema-controle-dopagem.git
   cd sistema-controle-dopagem
