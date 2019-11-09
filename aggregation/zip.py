slowa = ['jablko', 'czeresnia', 'maslo', 'jajko']
liczby = [3,10,1,6]

print(list(zip(slowa,liczby)))
print(list(zip(slowa)))
print(list(zip(slowa,liczby,slowa)))

lista_liczb = [1.12, 121.12, 12.0]
print(list(zip(slowa,lista_liczb)))

from itertools import zip_longest
print(list(zip_longest(slowa,lista_liczb, fillvalue=max(lista_liczb))))