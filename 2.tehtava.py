numerot = []

numero = input('Anna ensimmainen numero: ')
while numero !="":
    numerot.append(float(numero))
    numerot.sort(reverse=True)
    numero = input('Anna seuraava numero tai lopeta painamalla enter: ')
    if numero == "":
            break
try:
    for numero in range(5):
        print(f'{numerot[numero]}')
except IndexError:
    pass
