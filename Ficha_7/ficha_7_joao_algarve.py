"""
Trabalho realizado por:
        João Algarve
        PDM-B
        1º ano
        nº 45304
"""
#--------------------------------1--------------------------------

dic={'Ziggy': 'canario', 'Pluto': 'cao', 'Kitty': 'gato', 'Nemo': 'peixe', 'Mickey': 'rato'}

var=True

while(var):
    nome = input("Insira o nome do animal: ")
    especie = input("Insira a especie do animal: ")

    if nome == 'fim' or especie == 'fim':
        var = False
    else:
        dic.update({nome.capitalize() : especie})

print(dic,'\n')


for chave in dic:
  print(chave)

resposta = input("\nEscreva o nome do animal para saber a sua especie: ")

print(dic[resposta.capitalize()])
#--------------------------------1--------------------------------