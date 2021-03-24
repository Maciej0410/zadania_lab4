lista = [0+x for x in range(1, 31, 1)]
lista2 = [str(x*2) for x in lista]
plikliczby = open("liczby.txt", "w")

plikliczby.writelines(lista2)





