tempo = 43200
seg  = 0
minu = 0
hora = 0


minu = int((tempo / 60) % 60)
hora = int((tempo / 60) / 60)
seg  = int(tempo % 60)

print(f'{hora} : {minu} : {seg}')