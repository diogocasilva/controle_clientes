from Servico import *
from datetime import datetime, date


def gerar_log(tempo,msg):
    agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open("log.txt", "a") as log:
         log.write(tempo + ' - ' + msg + '\n')
         hoje = date.today()
         hoje.strftime('%d/%m/%y')

# Menu em loop
while True:
    print('#' * 28)
    print('# 1 - Novo cliente            #')
    print('# 2 - Buscar cliente por cpf  #')
    print('# 3 - Buscar cliente por nome #')
    print('# 4 - Mostrar todos           #')
    print('# 5 - Alterar cliente         #')
    print('# 6 - Excluir cliente          #')
    print('# 7 - Sair                    #')
    print('#' * 28)

    op = input('Informe a operação:')

    if op == '1':
        agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        cpf = input('Informe o cpf:')
        nome = input('Informe o nome:')
        sexo = input('Informe o sexo:')
        telefone = input('Informe o telefone:')
        cidade = input('Informe a cidade:')
        estado = input('Informe o estado:')
        endereco = input('Informe o endereco:')
        cep = input('Informe o cep:')
        conta = input('Informe o debito:')
        novo_cliente(cpf, nome, sexo, telefone, cidade, estado, endereco, cep, conta)
        gerar_log(agora, f'cliente {nome} cadastrado')

    elif op == "2":
        agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        cpf = input('Informe o cpf do cliente:')
        print(buscar_cliente_por_cpf(cpf))
        cliente = buscar_cliente_por_cpf(cpf)
        print('')
        print('cpf:', cliente[0])
        print('nome:', cliente[1])
        print('sexo:', cliente[2])
        print('telefone:', cliente[3])
        print('cidade:', cliente[4])
        print('estado:', cliente[5])
        print('endereco:', cliente[6])
        print('cep:', cliente[7])
        print('conta:', cliente[8])
        print('')
        gerar_log(agora, f'Busca pelo {cpf} realizada com sucesso')

    elif op == "3":
        agora =datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        nome = input('Informe o nome do cliente:')
        cliente = buscar_cliente_por_nome(nome)
        print('cpf:', cliente[0], 'nome:', cliente[1], 'sexo:', cliente[2]
              , 'telefone:', cliente[3], 'cidade:', cliente[4]
              , 'estado:', cliente[5], 'endereco:', cliente[6], 'cep:', cliente[7], 'debito:', cliente[8])
        gerar_log(agora, f'Busca pelo {nome} realizada com sucesso')

    elif op == "4":
        agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        cliente = mostrar_todos()
        for cliente in cliente:
            print('cpf:', cliente[0])
            print('nome:', cliente[1])
            print('sexo:', cliente[2])
            print('telefone:', cliente[3])
            print('cidade:', cliente[4])
            print('estado:', cliente[5])
            print('endereco:', cliente[6])
            print('cep:', cliente[7])
            print('debito:', cliente[8])
            print('')



    elif op == "5":
        agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        cpf_busca = int(input('Informe o cpf do cliente:'))
        nome = input('Informe o nome: ')
        sexo = input('Informe o sexo:')
        telefone = int(input('Informe o telefone:'))
        cidade = input('Informe a cidade:')
        estado = input('Informe o estado:')
        endereco = input('Informe o endereco:')
        cep = int(input('Informe o cep:'))
        conta = int(input('Informe o debito:'))
        alterar_cliente(nome, sexo, telefone, cidade, estado, endereco, cep, conta, cpf_busca)
        gerar_log(agora, f'Cliente alterado com sucesso')

    elif op == "6":
        agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        cpf = int(input('Informe o cpf do cliente para pagar o debito'))
        excluir_cliente(cpf)
        gerar_log(agora, f'Conta paga, obigrado por comprar com a gente')

    elif op == "7":
        print('Obrigado volte sempre!')
        break
    else:
        print('Opção inválida!')
