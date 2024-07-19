raspuns1 = input("Primul Numar: ")
raspuns2 = input("Al Doilea Numar: ")

raspuns1 = int(raspuns1)
raspuns2 = int(raspuns2)

print("Scrie 1 pentru a afisa numarul mai mic&")
print("Scrie 2 pentru a afisa numarul mai mare")
print()

raspunsOperatie = int(input())


if(raspunsOperatie == 2):
    if(raspuns1 > raspuns2):
        print(f"Numarul mai mare este: {raspuns1}")
    else:
        print(f"Numarul mai mare este: {raspuns2}")



if(raspunsOperatie == 1):
    if(raspuns1 < raspuns2):
        print(f"Numarul mai mic este: {raspuns1}")
    else:
        print(f"Numarul mai mic este: {raspuns2}")



    
if(raspuns1 == raspuns2):
    print(raspuns1)