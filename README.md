# 🏦 Sistema Simples de Conta Bancária em Python

Este projeto é uma implementação em **Python** voltada para a prática de **Programação Orientada a Objetos (POO)**. Ele simula o gerenciamento básico de uma conta bancária, permitindo criar contas, efetuar depósitos, realizar saques e verificar saldos com validações de regras de negócio.

---

## 📌 Funcionalidades

- **Criação de Conta**: Instancia uma nova conta com número identificador (id), nome do titular e saldo inicial (padrão 0.00).
- **Depósitos**: Adiciona valores ao saldo da conta com confirmação visual.
- **Saques com Validação**: Realiza saques apenas se houver saldo suficiente. Em caso de saldo insuficiente, exibe uma mensagem de alerta.
- **Representação Textual**: Método especial `__str__` customizado para exibir os dados da conta de forma clara e formatada.
- **Feedback Visual no Terminal**: Uso de códigos de cores ANSI no console para destacar operações (sucesso, alertas, erros).

---

## 🛠️ Conceitos de POO Aplicados

Neste projeto foram aplicados os seguintes conceitos fundamentais:
- **Classes e Objetos**: Estruturação do molde ContaBancaria e instanciação dos objetos (cf1, cf2, cf3).
- **Método Construtor (`__init__`)**: Inicialização dos atributos do objeto.
- **Encapsulamento e Estado**: Gerenciamento do estado interno do saldo através dos métodos da classe.
- **Dunder Methods / Special Methods**: Implementação do `__str__` para representação em string.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Ter o **Python 3.x** instalado na sua máquina.

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)

2. **Navegue até a pasta do projeto:**
   cd nome-do-repositorio

3.**Execute o arquivo Python:**
   conta_bancaria.py

## 💻 Exemplo de Uso no Código

# Criando uma conta com saldo inicial de R$ 1000.00
cf1 = ContaBancaria(13000100, 'Alexandre', 1000)

# Efetuando um saque
cf1.sacar(200)

# Exibindo os dados da conta
print(cf1)
# Saída: C/C: 13000100 ; TITULAR: Alexandre ; SALDO: R$800.00
