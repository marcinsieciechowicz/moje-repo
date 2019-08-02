a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for number in a:
    if number >= 5:
        print(number)

b = int(input('podaj mi liczbe, a podam Ci liczby z listy ktore sa od niej wieksze '))
numerlist = []
for numer in a:
    if numer > b:
        numerlist.append(numer)
print(numerlist)
