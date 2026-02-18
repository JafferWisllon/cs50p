lista = {}
while True:
    try:
        item = input().strip().lower()
        if item in lista:
            lista[item] += 1
        else:
            lista[item] = 1
    except EOFError:
        for item in sorted(lista):
            print(f"{lista[item]} {item}")
        break