menu = """
SISTEMA BANCÁRIO

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

Depositos = []
Saques = []
Extrato = {}



opcao = 0
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = int(input(menu))

    
    if opcao == 1:

        #ESTRUTURA DE REPETIÇÃO PARA FAZER DEPÓSITOS SUCESSIVOS
        while True:
            valor = float(input('Informe o valor que deseja depositar: '))

                #se o valor for zero ou negativo, ele da erro e fica pedindo um valor válido.
            while valor <= 0:
                valor = float(input('Informe um valor válido:'))

            Depositos.append(valor)

                #saldo vai somando o valor de cada deposito
            saldo += valor
            print(f'O Depósito de R$ {valor:.2f} foi efetuado com sucesso.')

            Continuar_Deposito = str(input('Deseja continuar a depositar?:[S/N] ')).upper().strip()

            #Se na variavel estiver dentro não, entao o loop irá parar e volta para o menu, pois encerra um ciclo do laço.
            if Continuar_Deposito in ["N", "NÃO", "NAO"]:
                break 


    if opcao == 2:
        #foi criado condições para realizar o saque

        while True:
            if numero_saques < LIMITE_SAQUES:          
                if saldo == 0:
                    print('Sem saldo disponível.')

                valor = float(input('Informe o valor que deseja sacar: '))
                while valor <= 0:
                    valor = float(input('Informe um valor válido:'))

                if valor <= saldo:
                    if valor <= 500:     
                        saldo -= valor 
                        #a lista de saques recebe o valor sacado
                        Saques.append(valor)
                        print(f'O Saque de R$ {valor:.2f} foi efetuado com sucesso.')

                    else:
                        print('O valor informado é maior do que o limite diário de R$ 500 reais.')

                numero_saques += 1

                #Laço para continuar sacando dinheiro
                Continuar_Saque = str(input('Deseja sacar novamente?: [S/N] ')).upper().strip()
                if Continuar_Saque in ["N", "NÃO", "NAO"]:
                    break
            else:
                print('LIMITE DE SAQUE DIÁRIOS: 3.\nVocê já utilizou o limite diário disponível.')
                break   
        
    if opcao == 3:

        #Passando os dados da lista Depositos e Saques para dentro do Dicionário Extrato 
        Extrato['depositos'] = Depositos.copy()
        Extrato['saques'] = Saques.copy()
        Extrato['saldo_final'] = saldo 

        print('-'*30)
        print('EXTRATO:')

        #ENTRANDO NAS LISTAS PARA EXIBIR NA TELA AS MOVIMENTAÇÕES

        for Tipo_Movimentacao, Lista_Valores in Extrato.items():
            if Tipo_Movimentacao == 'depositos':
                for posicao, valor in enumerate(Lista_Valores): 
                    print(f'Deposito {posicao+1}° deposito: R${valor:.2f}')
            if Tipo_Movimentacao == 'saques':
                for posicao, valor in enumerate(Lista_Valores):
                    print(f'Saque {posicao+1}° R${valor:.2f}')
        print(f'Saldo: R${Extrato["saldo_final"]:.2f}')
        print('-'*30)
    
    if opcao == 4:
        print('SISTEMA ENCERRADO.')
        break 



