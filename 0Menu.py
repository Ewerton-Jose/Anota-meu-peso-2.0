from time import sleep
from datetime import date
# ------------- Funções ------------

def lin(x = '-', y = 40):
    print(x * y)

def cabeçalho(x = "nome"):
    lin()
    print(f'{x.center(40, "-")}')
    lin()

def menu(x = []):
    s = 1
    for e in x:
        print(f'Opção {s} = {e}')
        s += 1
    lin()

def analiseInteiro(nome = 'str'):
    while True:
        try:
            n = int(input(f'{nome}'))
        except:
            print('\033[31mErro, numero inválido\033[m')
        else:
            return n
            break

def analiseFloat(nome = 'str'):
    while True:
        try:
            n = float(input(f"{nome}"))
        except:
            print('\033[31mErro, Numero inválido\033[m')
        else:
            return n
            break
    
# ------------------ Memu --------------------
data_de_hoje = date.today()
arq = "Registro Peso"
try:
    b = open(arq, 'rt')
    b.close()
except:
    b = open(arq, 'wt+')
else:
    pass

while True:
    cabeçalho("Menu")
    op = [ 'IMC','Exercícios Diarios', 'Cronograma da alimentação',"Registra Meu Peso",'litros diários']
    menu(op)
    escolha = analiseInteiro('Sua escolha: ')
    while escolha < 1 or escolha > 5:
        print('\033[31mopção inválida\033[m')
        escolha = analiseInteiro('Sua escolha: ')

    # ------------------ IMC ----------------------
    if escolha == 1:
        cabeçalho("Veja com está o seu IMC")
        Altura = analiseFloat('Digite sua altura: ')
        Peso = analiseFloat('Digite seu peso: ')
        IMC = Peso / (Altura * Altura)
        Classificação = ""
        if IMC < 18.5:
            Classificação = "Magreza"
        elif IMC > 18.5 and IMC < 24.9:
            Classificação = "Normal"
        elif IMC > 24.9 and IMC < 29.9:
            Classificação = "acima do peso"
        elif IMC > 30 and IMC < 39.9:
            Classificação = "Obsidade"
        elif IMC > 39.9:
            Classificação = "Obsidade morbida"
        print(f'Seu IMC é de {IMC} e sua classificação é {Classificação}')

    # --------------Exercícios Diarios---------------
    elif escolha == 2:
            cabeçalho("Exercícios Diarios")
            print('Analísando o IMC...')
            sleep(2)
            try:
                print(f"Seu IMC é de {IMC}, Você está {classificação}")
            except:
                print("\033[31mIMC não localizado, tente fazer a opção 1!\033[m")
            else:
                pass

    # ------------------ Cronograma da Alimentação -------------
    elif escolha == 3:
        print('x3')
    
    # ----------------- Registra meu peso ------------------
    elif escolha == 4:
        pseo = analiseFloat("Quanto você está pesando hoje: ")
        a = open(arq, 'at')
        a.write(f"No Dia {data_de_hoje.strftime('%d/%m/%Y')} você estava pesando {pseo}\n")
        print(f"{pseo} Kilos no dia {data_de_hoje.strftime('%d/%m/%Y')}")

    # ------------------- Litros Diarios ----------------
    else:
        olol = 2500
        cabeçalho("Litros Diários")
        print('Quantos ML seu copo principal tem: ')
        xy = ['100ml','150ml','200ml','250ml','400mm']
        menu(xy)
        esc = analiseInteiro("Escolha sua opção: ")
        while esc < 1 or esc > 5:
            print('\033[31mopção inválida\033[m')
            esc = analiseInteiro('Sua escolha: ')
        if esc == 1:
            cp = olol // 100
        elif esc == 2:
            cp = olol // 150
        elif esc == 3:
            cp = olol // 200
        elif esc == 4:
            cp = olol // 250
        else:
            cp = olol // 400
        print(f'Você precisa beber {cp} copos por dia')

