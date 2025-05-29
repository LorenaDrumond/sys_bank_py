# 🏦 Sistema Bancário em Python

---

## Sumário

1. [Introdução](#introdução)  
2. [Funcionalidades](#funcionalidades)  
3. [Estrutura do Código](#estrutura-do-código)  
4. [Conceitos e Práticas](#conceitos-e-práticas)  
5. [Tecnologias Utilizadas](#tecnologias-utilizadas)  
6. [Como Executar](#como-executar)  
7. [Requisitos](#requisitos)  
8. [Próximos Passos](#próximos-passos)  
9. [Referências](#referências)  
10. [Contato](#contato)  

---

## Introdução

Este projeto implementa um **sistema bancário simples** utilizando a linguagem **Python**. Ele permite que o usuário realize operações básicas como depósito, saque e consulta de extrato, respeitando limites pré-definidos para segurança e controle, como o número máximo de saques diários e limite por saque.

O objetivo é aplicar conceitos básicos de programação procedural e modularização, criando uma aplicação que pode ser facilmente estendida e melhorada.

---

## Funcionalidades

- **Depósito**: Permite adicionar valores positivos ao saldo da conta, registrando a operação no extrato.  
- **Saque**: Possibilita até 3 saques diários, com limite máximo de R$ 500,00 por saque, assegurando o saldo suficiente antes da operação.  
- **Extrato**: Exibe um histórico completo das movimentações (depósitos e saques) e o saldo atual da conta.  

---

## Estrutura do Código

O sistema é organizado em funções modulares, cada uma responsável por uma tarefa específica:

| Função             | Descrição                                                             |
|--------------------|---------------------------------------------------------------------|
| `depositar()`      | Realiza depósitos, atualizando saldo e adicionando registro no extrato |
| `sacar()`          | Executa o saque respeitando os limites diários e valores máximos    |
| `exibir_extrato()` | Mostra o histórico de todas as transações e o saldo atual          |

O código está estruturado para facilitar a leitura, manutenção e futuras expansões, adotando boas práticas de programação procedural.

---

## Conceitos e Práticas

- **Modularização**: O código está dividido em funções para melhorar a organização e reutilização.  
- **Controle de fluxo**: Uso de condicionais para validar operações financeiras (saldo, limite de saque, número de saques).  
- **Entrada e saída de dados**: Interação com o usuário via terminal, exibindo informações claras e formatadas.  
- **Persistência temporária**: As transações são armazenadas em variáveis durante a execução, sem banco de dados.  

---

## Tecnologias Utilizadas

- **Python** (versão 3.x): Linguagem principal do projeto, pela sua simplicidade e popularidade.  
- **Colorama**: Biblioteca para colorir e estilizar a saída do terminal, melhorando a experiência do usuário.  

---

## Como Executar

1. Certifique-se de ter o Python 3 instalado em sua máquina.  
2. Instale a biblioteca necessária com o comando:  
   ```bash
   pip install colorama
3. Clone ou faça o download do repositório.
4. Execute o arquivo principal do sistema com:
   ```bash
python nome_do_arquivo.py
5. Siga as instruções exibidas no terminal para realizar depósitos, saques e consultar o extrato.

## Requisitos

- Python 3.x instalado ([Download Python](https://www.python.org/downloads/))
- Biblioteca Colorama instalada (`pip install colorama`)
- Ambiente de execução em terminal/console compatível

## Referências

- Documentação Python - [https://docs.python.org/3/](https://docs.python.org/3/)
- Bootcamp Dio. - [NTT DATA - Engenharia de Dados com Python](https://web.dio.me/track/engenharia-dados-python)

