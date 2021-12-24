import json

# Um dicionario Python (dict):
x = {
  "nome": "Gabriel",
  "age": 20,
  "city": "Aracaju",
  "hobby": "Programming"
}

# Convertendo em Json
y = json.dumps(x, indent=4)

# O resultado é uma string Json
print(y)


###########
# ARQUIVOS
###########

#Lendo um json

print('Escrevendo um Json')
json_string = json.dumps(x,indent=4)
with open('test.json', 'w') as f:
    f.write(json_string)

print(json_string)
print(json_string['city'])