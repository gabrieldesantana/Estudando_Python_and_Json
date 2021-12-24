# Estudando Json + Python

## Convertendo Json para Python

    1 - import json

### Algum Json
    2 - x = '{"nome": "Gabriel", "idade":20, "cidade": "Aracaju"}'

parse x:

    3 - y = json.loads(x)

### O resultado é um dicionario python
    4 - print(y) -> Mostra um dicionario python
    
    5 - print(y['idade']) -> Mostra um valor do dicionario Python

#

## Convertendo de Python para Json

    1 - import json

### Um dicionario Python (dict):
    2 - x = {
    "nome": "Gabriel",
    "age": 20,
    "city": "Aracaju"
    }

### Convertendo em Json
    3 - y = json.dumps(x, indent=4)

### O resultado é uma string Json
    4 - print(y)

#

# Trabalhando com Arquivos .json

## Lendo um json

#

    1 - print('Lendo um Json') 

    2 - with open('test.json', 'r') as f:
            json_object = json.loads(f.read())

    4 - print(json_object)

    5 - print(json_object['city'])

#

## Escrevendo um json

#

    1 - json_string = json.dumps(x,indent=4)
 
    2 -  with open('test.json', 'w') as f:
            f.write(json_string)

    3 - print(json_string)

    4 - print(json_string['city'])