k = (1,2,3,4,5,6,7,8,9,10)

#Sposób 1
# nowa_lista = []
# for x in k:
#     if x % 2 ==0:
#         nowa_lista.append(x)
#
# print(nowa_lista)

#Sposób 2

# def jest_parzysty(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

#Sposób 2.1
# def jest_parzysty(x):
#    return x % 2 == 0
#
# print(tuple(filter(jest_parzysty, k)))

# def jest_parzysty2(x):
#     return (x % 2 == 0) and (x != 6)

# print(tuple(filter(jest_parzysty2, k)))

#Sposób 3

# print(tuple(filter(lambda x: (x % 2 == 0) and (x != 6), k)))
# print(tuple(filter(lambda x: not ((x % 2 == 0) and (x != 6)), k)))