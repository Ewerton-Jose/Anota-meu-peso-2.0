from time import sleep

# ------------- Funções ------------

def lin(x = '-', y = 40):
    print(x * y)

def cabeçalho(x = "nome"):
    lin()
    print(f'{x:-^40}')
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
        print('x4')

    # ------------------- Litros Diarios ----------------
    else:
        print('x5')