import random as rd
#FUNÇÕES

def enviarMensageiroVermelho (mensageiro, tempo, nMensageiros):
    probabilidadeSerPego = rd.randrange(0,101)

    if(probabilidadeSerPego <= 45):
        return False, tempo + 12601, nMensageiros - 1 #Define se o mensageiro será morto ou não, o tempo atual e o número de mensageiros disponíveis
    else:

        tempo+= rd.randrange(3600, 4201)

        return True, tempo, nMensageiros - 1

def enviarMensageiroAzul (mensageiro, tempo, nMensageiros):
    probabilidadeSerPego = rd.randrange(0,101)

    if(probabilidadeSerPego <= 45):
        return False, tempo + 4201, nMensageiros - 1 #Define se o mensageiro será morto ou não, o tempo atual e o número de mensageiros disponíveis
    else:

        tempo+= rd.randrange(3600, 4201)

        return True, tempo, nMensageiros - 1

def mostrarHorario (tempo):
    seg  = 0
    minu = 0
    hora = 0


    minu = int((tempo / 60) % 60)
    hora = int((tempo / 60) / 60)
    seg  = int(tempo % 60)

    return f'{hora} : {minu} : {seg}'


#MAIN CODE

# variáveis 

sinalizadorVermmelho = False #define se o sinalizador será ativado ou não
numeroMensageirosVermelhos = 5
numeroMensageirosAzuis = 10
mensageiroVermelho = False
mensageiroAzul = False
tempo = 0 #em segundos
aceitouHorario = True
vitoria = True
mensagens = []
nmensagens = 0



mensagens.append(f'Início das trocas de mensagem:'  + '\n')
    
while sinalizadorVermmelho == False:
    if numeroMensageirosAzuis == 0 or numeroMensageirosVermelhos == 0:
        vitoria = False
        break

    if mensageiroVermelho == False or aceitouHorario == False:
        mensageiroVermelho, tempo, numeroMensageirosVermelhos = enviarMensageiroVermelho(mensageiroVermelho, tempo, numeroMensageirosVermelhos)
        nmensagens += 1
           
    if mensageiroVermelho:
        possibilidadeImpossibilitar = rd.randrange(0,101)
        nmensagens += 1
        if possibilidadeImpossibilitar <= 1:
            aceitouHorario = False

        mensageiroAzul, tempo, numeroMensageirosAzuis = enviarMensageiroAzul(mensageiroAzul, tempo, numeroMensageirosAzuis)
        nmensagens += 1

    if mensageiroAzul == True and aceitouHorario == True:
            sinalizadorVermmelho = True


print("O horário de início das mensagens foi 00:00:00 \n")
print(f'O término das trocas de mensagens se deu às:', mostrarHorario(tempo),  f'na mensagem {nmensagens} \n')
print(f'Foram usados {10 - numeroMensageirosAzuis} mensageiros azuis e {5 - numeroMensageirosVermelhos} mensageiros vermelhos\n')

if vitoria == False:
    print("O exército saiu derrotado")
else:
    print("O exército saiu vitorioso")