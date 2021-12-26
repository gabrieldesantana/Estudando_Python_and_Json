import json

def mostrar_menu():
    print("""

             CADASTRO DE CLIENTES

        1 - Cadastrar um novo cliente
        2 - Mostrar os clientes cadastrados
        3 - Excluir um cliente
        0 - Encerrar
    
    """)


def cadastrar_cliente(lista,dicio):
    dicio['Nome'] = str(input('Nome: ')).capitalize()
    dicio['Cpf'] = str(input('Cpf: '))

    lista.append(dicio.copy())

    return lista


def mostrar_clientes(lista):
    if len(lista) == 0:
        print("="*40)
        print('')
        print('      Não há clientes cadastrados')
        print('')
        print("="*40)
    else:
        print("="*40)
        for cliente in range(len(lista)):
            print(f" {cliente + 1} - {lista[cliente]}")
            print('-'*40)
        print("="*40)


def excluir_cliente(lista):

    cpf = str(input('Informe o Cpf do cliente: '))
    
    for c in range(len(lista)):
        if lista[c]['Cpf'] == cpf:
            print('-'*40)
            print(f"Cliente {lista[c]['Nome']} foi excluido com sucesso")
            print('-'*40)
            del(lista[c])
            break

def pythonParaJson(lista):

    json_string = json.dumps(lista)

    with open('clientes.json', 'w') as arq:
        arq.write(json_string)


def jsonParaPython():
    with open ('clientes.json', 'r') as arq:
        json_objeto = json.loads(arq.read())
        
        return json_objeto

