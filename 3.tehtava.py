numero = int(input('Anna kokonaisluku: '))

arvo = False

if numero > 1:
    for i in range(2,numero):
        if (numero % i)== 0:
            arvo = True
            break
if arvo:
    print('Ei ole alkuluku.')
else:
    print('On alkuluku.')