#DECLARAÇÃO DA CLASSE
class ContaBancaria():
    """
    A classe ContaBancaria cria um conta com número, nome do titular e saldo.
    """

    def __init__(self, numeroconta, nome, saldo=0): #Método Construtor
        #Inicializa uma nova instância da classe ContaBancaria.
        #Atributos:
        '''
        id (int): O número de identificação da conta bancária.
        titular (str): O nome do titular da conta.
        saldo (float): O saldo disponível na conta (padrão é 0.0).
        '''
        self.id = numeroconta
        self.titular = nome
        self.saldo = saldo
        print(f'\033[34mConta {self.id} criada com sucesso!!!\033[m')

        #Métodos
    def __str__(self):
        '''Retorna uma representação legível em texto dos dados da conta.
            str: Texto formatado contendo número da conta, titular e saldo atual.
        '''
        return f'C/C: {self.id} ; TITULAR: {self.titular} ; SALDO: R${self.saldo:.2f}'

    def depositar(self, valor):
        #Adiciona um valor ao saldo atual da conta.
        self.saldo = self.saldo + valor
        print(f'\033[33mDepósito de R${valor:.2f} na conta de {self.titular},'
              f' efetuado com sucesso!!!\033[m')

    def sacar(self, valor):
        '''
            Realiza a retirada de um valor da conta, respeitando o saldo disponível.
            Se o valor solicitado for maior que o saldo atual, a operação é cancelada
            e um aviso de saldo insuficiente é exibido.
        '''
        if valor > self.saldo:
            print(f'\033[31mSaque de R${valor:.2f} não efetuado na conta de {self.titular}. SALDO INSUFICIENTE!\033[m')
        else:
            self.saldo = self.saldo - valor
            print(f'\033[33mSaque de R${valor:.2f} na conta de {self.titular},'
                    f'realizado com sucesso!!\033[m')




# EXECUÇÃO E TESTES DA CLASSE (INSTANCIAÇÃO DE OBJETOS)
# Criando objetos da classe ContaBancaria
cf1 = ContaBancaria(13000100, 'Alexandre', 1000)
cf2 = ContaBancaria(13000101, 'Rosangela', 2500)
cf3 = ContaBancaria(13000102,'Arthur')
print(cf1)
print(cf2)
print(cf3)
cf2.sacar(600)
print(cf2)
cf3.sacar(100)
print(cf3)




