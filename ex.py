import random as rd

# variáveis 

sinalizadorVermmelho = False #define se o sinalizador será ativado ou não
numeroMensageirosVermelhos = 5
numeroMensageirosAzuis = 10
mensageiroVermelho = False
mensageiroAzul = False
tempo = 0 #em segundos
aceitouHorario = True


#FUNÇÕES

def enviarMensageiroVermelho (mensageiro, tempo, nMensageiros):
    probabilidadeSerPego = rd.randrange(0,101)

    if(probabilidadeSerPego <= 45):
        return False, tempo + 12601, nMensageiros - 1 #Define se o mensageiro será morto ou não, o tempo atual e o número de mensageiros disponíveis
    else:

        tempo+= rd.randrange(3600, 4201)

        return True, tempo

def enviarMensageiroAzul (mensageiro, tempo, nMensageiros):
    probabilidadeSerPego = rd.randrange(0,101)

    if(probabilidadeSerPego <= 45):
        return False, tempo + 4201, nMensageiros - 1 #Define se o mensageiro será morto ou não, o tempo atual e o número de mensageiros disponíveis
    else:

        tempo+= rd.randrange(3600, 4201)

        return True, tempo

def mostrarHorario (tempo):
    seg  = 0
    minu = 0
    hora = 0


    minu = int((tempo / 60) % 60)
    hora = int((tempo / 60) / 60)
    seg  = int(tempo % 60)

    print(f'{hora} : {minu} : {seg}')


#MAIN CODE
    sinalizadorVermmelho = False #define se o sinalizador será ativado ou não
    while sinalizadorVermmelho == False:

        if mensageiroVermelho == False:
            enviarMensageiroVermelho(mensageiroVermelho, tempo, numeroMensageirosVermelhos)

        if mensageiroVermelho:
            possibilidadeImpossibilitar = rd.randrange(0,101)
            if possibilidadeImpossibilitar <= 1:
                aceitouHorario = False

            enviarMensageiroAzul(mensageiroAzul, tempo, numeroMensageirosAzuis)

        if mensageiroAzul == True and aceitouHorario == True:
            sinalizadorVermmelho = True