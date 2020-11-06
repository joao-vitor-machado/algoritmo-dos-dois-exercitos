import random as rd

# variáveis 

sinalizadorVermmelho = False #define se o sinalizador será ativado ou não
numeroMensageirosVermelhos = 5
numeroMensageirosAzuis = 10
mensageiroVermelho = False
mensageiroAzul = False
tempo = 0 #em segundos
aceitouHorario = False


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


#MAIN CODE

while sinalizadorVermmelho == False:

    if mensageiroVermelho == False:
        enviarMensageiroVermelho(mensageiroVermelho, tempo, numeroMensageirosVermelhos)

    if mensageiroVermelho:
        enviarMensageiroAzul(mensageiroAzul, tempo, numeroMensageirosAzuis)
