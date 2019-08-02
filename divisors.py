a = int(input("Podaj swoja liczbe "))

listRange = list(range(1, a+1))

lista = []

for element in listRange:
    if a % element == 0:
        lista.append(element)
print(lista)
