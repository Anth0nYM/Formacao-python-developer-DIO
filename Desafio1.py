import time
menu = """
************************************
*       Banco Dio              *
************************************

Escolha uma opção:
  d -> Depositar
  s -> Sacar
  e -> Extrato
  q -> Sair

Opção: 
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'q':
        break
    elif opcao == 'd':
        valor = float(input("Valor do depósito: "))
        saldo += valor
        extrato += f"Depósito: {valor}\n"
        print("Depósito realizado com sucesso")
        time.sleep(2)
        print('\n'*50)
    elif opcao == 's':
        valor = float(input("Valor do saque: "))
        if numero_saques < LIMITE_SAQUES:
            if valor <= saldo + limite:
                saldo -= valor
                extrato += f"Saque: {valor}\n"
                numero_saques += 1
                time.sleep(2)
                print('\n'*50)
            else:
                print("Saldo insuficiente")
                time.sleep(2)
                print('\n'*50)
        else:
            print("Limite de saques atingido")
            time.sleep(2)
            print('\n'*50)
    elif opcao == 'e':
        print(f"Saldo: {saldo}")
        print(f"Limite: {limite}")
        print(extrato)
        input("Pressione enter para voltar ao menu")
    else:
        print("Opção inválida")
        time.sleep(2)
        print('\n'*50)
