L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print('Liczba 2 do potęgi 5 znajduje się w liście L pod indeksem', i)
        break
    i += 1
else:
    print('Nie odnaleziono szukanej liczby w liście L')
