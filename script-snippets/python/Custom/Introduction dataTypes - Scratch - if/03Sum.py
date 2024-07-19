raspuns1 = input("Primul Numar: ")
raspuns2 = input("Al Doilea Numar: ")

raspuns1 = int(raspuns1)
raspuns2 = int(raspuns2)

print("Scrie 1 pentru adunare")
print("Scrie 2 pentru scadere")
print("Scrie 3 pentru impartire")
print("Scrie 4 pentru inmultire")
print()

raspunsOperatie = int(input())

if raspunsOperatie == 1:
    print(raspuns1 + raspuns2)

if raspunsOperatie == 2:
    print(raspuns1 - raspuns2)

if raspunsOperatie == 3:
    print(raspuns1 / raspuns2)

if raspunsOperatie == 4:
    print(raspuns1 * raspuns2)
