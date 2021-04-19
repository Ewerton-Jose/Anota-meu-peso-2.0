def lin(x = '-', y = 40):
    print(x * y)

def cabeçalho(x = "nome"):
    lin()
    print(f'{x:-^40}')
    lin()

def menuo(x = []):
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