import random as rd

# variáveis 

sinalizadorVermmelho = False #define se o sinalizador será ativado ou não
numeroMensageirosVermelhos = 5
numeroMensageirosAzuis = 10
mensageiroVermelho = True
mensageiroAzul = False
tempo = 0 #em segundos


#FUNÇÕES

def enviarMensageiro (mensageiro, tempo, nMensageiros):
    probabilidadeSerPego = rd.randrange(0,101)

    if(probabilidadeSerPego <= 45):
        return False, tempo, nMensageiros - 1 #Define se o mensageiro será morto ou não, o tempo atual e o número de mensageiros disponíveis
    else:

        tempo+= rd.randrange(3600, 4201)

        return True, tempo



#MAIN CODE

enviarMensageiro(mensageiroVermelho, tempo, numeroMensageirosVermelhos)

if mensageiroVermelho == True:
    enviarMensageiro(mensageiroAzul, tempo, numeroMensageirosAzuis)