luku = int(input("Anna numero väliltä 1-10: "))

if luku in range(1, 10):
    for i in range(1, luku + 1):
        print("Luvun", i, "neliö on:", i**2)
else:
    print("Luku ei ollut väliltä 1-10")
