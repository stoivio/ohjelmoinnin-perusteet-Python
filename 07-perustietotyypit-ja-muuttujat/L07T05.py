# Esittele muuttuja, johon tallennetaan pankkitilin saldo euroina (alku saldo on 2000 €).
# Tulosta pankkitilin saldo konsoliin.
# Kysy konsolissa kuinka monta euroa lisätään saldoon.
# Kysy konsolissa kuinka monta senttiä lisätään saldoon. Tulosta saldo konsoliin näiden muutosten jälkeen.

saldo = 2000
print("Bank account balance:", saldo, "€")
euro = int(input("How many euros will be added to the balance?"))
snt = int(input("How many cents will be added to the balance?"))

snt_as_euros = snt / 100
saldo = saldo + euro + snt_as_euros

print("Bank account balance:", saldo, "€")
