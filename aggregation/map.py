k = [1,2,3,4,5,10,2.3,"string"]

#Sposób 1
# nowa_lista = []
# for x in k:
#     nowa_lista.append(x * 2)
#
# print(nowa_lista)

#Sposób 2
#
# def razy_dwa(elem):
#     return elem *2
#
# print(list(map(razy_dwa,k)))

#Sposób 3

# print(list(map(lambda x: x*2,k)))
# print("".join(list(map(lambda x: x*2,"string"))))

print((list(map(lambda x: x=="s","string"))))

print(list(filter(lambda x: x=="s","string")))
