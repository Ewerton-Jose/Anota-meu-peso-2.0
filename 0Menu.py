from aFunções import *

cabeçalho("Menu")
op = ['Exercícios Diarios', 'Cronograma da alimentação', 'IMC',"Registra Meu Peso",'litros diários']
menuo(op)
escolha = analiseInteiro('Sua escolha: ')
while escolha < 1 or escolha > 5:
    print('\033[31mopção inválida\033[m')
    escolha = analiseInteiro('Sua escolha: ')

if escolha == 1:
    print('x1')
elif escolha == 2:
    print('x2')
elif escolha == 3:
    print('x3')
elif escolha == 4:
    print('x4')
else:
    print('x5')