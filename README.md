# Sistema Bancário em Python

## 📌 Introdução
Este projeto implementa um **sistema bancário simples** utilizando **Python**. Ele permite ao usuário realizar operações de depósito, saque e consulta de extrato, respeitando limites pré-definidos de saque.

## 🚀 Funcionalidades
- **Depósito**: Permite adicionar valores positivos ao saldo.
- **Saque**: Limite de 3 saques diários, com um máximo de R$500,00 por saque.
- **Extrato**: Exibe todas as movimentações e o saldo atual.

## 📂 Estrutura do Código
O código é modular e utiliza funções para cada operação:

| Função          | Descrição |
|----------------|-----------|
| `depositar()`  | Realiza um depósito e atualiza o saldo e extrato |
| `sacar()`      | Permite saques respeitando limite diário e de valor |
| `exibir_extrato()` | Lista todas as transações e o saldo |

## 🎯 Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto
- **Colorama**: Biblioteca para estilizar o terminal com cores

## 🛠️ Como Executar
1. Certifique-se de ter o Python instalado.
2. Instale as dependências com:
   ```bash
   pip install colorama