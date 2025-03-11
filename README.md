# Sistema Bancário em Python

## Funcionalidades

- **Criar Usuário**: Permite criar um novo usuário com nome, data de nascimento, CPF e endereço.
- **Criar Conta Corrente**: Permite criar uma nova conta corrente para um usuário existente.
- **Depositar**: Permite realizar depósitos em uma conta corrente.
- **Sacar**: Permite realizar saques de uma conta corrente, respeitando o limite de saldo e o limite de saques.
- **Mostrar Extrato**: Exibe o extrato de transações de uma conta corrente.
- **Listar Contas**: Lista todas as contas correntes criadas.

## Classes

### Cliente

Representa um cliente do banco.

#### Atributos

- `nome`: Nome do cliente.
- `data_nascimento`: Data de nascimento do cliente.
- `cpf`: CPF do cliente.
- `endereco`: Endereço do cliente.

### Historico

Armazena o histórico de transações de uma conta.

#### Atributos

- `transacoes`: Lista de transações realizadas.

#### Métodos

- `adicionar_transacao(transacao)`: Adiciona uma transação ao histórico.

### Conta

Representa uma conta bancária.

#### Atributos

- `saldo`: Saldo da conta.
- `numero`: Número da conta.
- `agencia`: Agência da conta.
- `cliente`: Cliente associado à conta.
- `historico`: Histórico de transações da conta.

#### Métodos

- `saldo()`: Retorna o saldo da conta.
- `nova_conta(cliente, numero)`: Cria uma nova conta para um cliente.
- `sacar(valor)`: Realiza um saque na conta.
- `depositar(valor)`: Realiza um depósito na conta.

### Conta_Corrente (herda de Conta)

Representa uma conta corrente com limite de saque.

#### Atributos

- `limite`: Limite de crédito da conta.
- `limite_saques`: Limite de saques permitidos.
- `numero_saques`: Número de saques realizados.

#### Métodos

- `sacar(valor)`: Realiza um saque na conta, considerando o limite de crédito e o limite de saques.

## Exemplo de Uso

```plaintext
====================Operações====================
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] CRIAR USUÁRIO
[5] CRIAR CONTA CORRENTE
[6] LISTAR CONTAS
[0] SAIR
=> 4
Digite o nome do usuário: João Silva
Digite a data de nascimento do usuário (DD/MM/AAAA): 01/01/1980
Digite o CPF do usuário: 123.456.789-00
Digite o endereço do usuário (logradouro, número, bairro, cidade/sigla do estado): Rua A, 123, Centro, São Paulo/SP
Usuário criado com sucesso!
