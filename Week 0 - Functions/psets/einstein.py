def main():
    m = int(input("m:"))
    print("E:", calculate_energy(mass))

def calculate_energy(m, c = 300000000):
    return m * ( c ** 2)

main()