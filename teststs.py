arq = "Rolúcias"
def arqexiste(arq):
    try:
        a = open(arq, 'rt')
        a.close
    except:
        return False
    else:
        return False

if arqexiste(arq) == True:
    a = open(arq, "wt+")