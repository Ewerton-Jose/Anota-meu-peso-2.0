# Importações
import matplotlib.pyplot as plt
from datetime import date

#Variáveis
data_atual = f'{date.today()}'.replace('-','/')
dias = ['15/10/2021','26/10/2021','01/11/2021','10/11/2021','15/11/2021']
dias.append(data_atual)
peso = [78.5,82.2,80.0,75.5,72.56]

# Contato usuario
while True:
    try:
        peso.append(float(input('Digite seu peso: ')))
    except:
        print('Dado inválido: ')
    else:
        break

# Mostrar na tela
plt.xlabel('Dias')
plt.ylabel('Pesos')
plt.plot(dias,peso)
plt.show()