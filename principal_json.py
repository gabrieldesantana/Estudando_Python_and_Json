from funcoes_json import *

if input('Sua primeira vez rodando o programa? [S/N]: ') == 'S'.upper():
    listaClientes = []
    dicioClientes = {}
else:
    listaClientes = jsonParaPython()
    dicioClientes = {}

mostrar_menu()

while True:
    opcao = int(input('Informe a opção: '))

    if opcao == 1:
        listaClientes = cadastrar_cliente(listaClientes, dicioClientes)
        pythonParaJson(listaClientes)
        mostrar_menu()
    
    if opcao == 2:
        mostrar_clientes(listaClientes)
        mostrar_menu()

    if opcao == 3:
        excluir_cliente(listaClientes)
        pythonParaJson(listaClientes)
        mostrar_menu()

    if opcao == 0:
        print('Até logo!')
        break