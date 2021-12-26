import json

# Algum Json
x = '{"nome": "Gabriel", "idade":20, "cidade": "Aracaju"}'

# parse x:
y = json.loads(x) # 

# O resultado é um dicionario python
print(y)
print(y['idade'])


###########
# ARQUIVOS
###########

#Lendo um json
print('Lendo um Json')
with open('test.json', 'r') as f:
    json_object = json.loads(f.read())

print(json_object)
print(json_object['cidade'])