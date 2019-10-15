L = [1, 2, 4, 8, 16, 32, 64]
X = 5
for i in L:
    if 2 ** X == i:
        print('Liczba 2 do potęgi 5 znajduje się w liście L pod indeksem', L.index(i))
        break
else:
    print('Nie odnaleziono szukanej liczby w liście L')
