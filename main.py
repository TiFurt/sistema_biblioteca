from 


if __name__ == '__main__':
    try:
        while True:
            nome = str(input('Nome do cliente(digite 0 para sair): '))
            if nome == '0':
                break
            elif nome in ([cliente.get_nome() for cliente in clientes]):
                print([conta for conta in contas if conta.get_nome() == nome])
                contasCliente = [conta for conta in contas if conta.get_nome() == nome]
                for cliente in contas:
                    if cliente.get_nome() == nome:
                        break
                    id += 1
                print('Escolha uma das opções abaixo:')
                print('1 - Saldo')
                print('2 - Deposito')
                print('3 - Saque')
                print('4 - Transferência')
                opcao = int(input('Digite sua opção: '))
                match opcao:
                    case 1:
                        print('Saldo: {}'.format(contas[id].get_saldo()))
                        break
                    case 2:
                        valor = float(input('Valor do depósito: '))
                        contas[id].depositar(valor)
                        print('Depósito realizado com sucesso!')
                        break
                    case 3:
                        valor = float(input('Valor do saque: '))
                        contas[id].sacar(valor)
                        print('Saque realizado com sucesso!')
                        break
                    case 4:
                        valor = float(input('Valor da transferência: '))
                        conta = int(input('Número da conta: '))
                        contas[id].transferir(valor, contas[conta+1])
                        print('Transferência realizada com sucesso!')
                        break
                if opcao == 1:
                    print(f'Saldo da conta de {nome}: {contas[0].get_saldo()}')
                elif opcao == 2:
                    valor = float(input('Valor do deposito: '))
                    contas[0].deposito(valor)
                    print(f'Saldo da conta de {nome}: {contas[0].get_saldo()}')
                elif opcao == 3:
                    valor = float(input('Valor do saque: '))
                    contas[0].saque(valor)
                    print(f'Saldo da conta de {nome}: {contas[0].get_saldo()}')
                else:
                    print('Opção inválida')
            else:
                print('Cliente não encontrado')

    except ValueError:
        print('Valor invalido')