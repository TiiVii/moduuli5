from random import randint

nopat = int(input('Anna noppien maara: '))

summa = 0

for luku in range(1, nopat+1):
    luku = randint(1, 6)
    summa += luku
    print(f'Nopan antama luku: {int(luku)}')

print(f'Noppien summa on: {int(summa)}')