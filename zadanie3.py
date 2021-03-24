with open("tekst.txt", "w") as pliktext:
    for i in range(5) :
        pliktext.write("Python jest super\n")
with open("tekst.txt", "r") as pliktext:
    for x in pliktext:
        print(x, end="")