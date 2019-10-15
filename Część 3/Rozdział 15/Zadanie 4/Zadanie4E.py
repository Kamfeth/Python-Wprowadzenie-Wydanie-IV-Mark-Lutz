L = list(map(lambda i: 2 ** i, range(7)))
print(L)
X = 5
if 2 ** X in L:
    print('Liczba 2 do potęgi 5 znajduje się w liście L pod indeksem', L.index(2 ** X))
else:
    print('Nie odnaleziono szukanej liczby w liście L')
