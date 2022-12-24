etunimi = input("Anna etunimi: ")
sukunimi = input("Anna sukunimi: ")

# Tulosta etunimen ensimmäistä kirjainta niin monta kertaa kun etunimessä on kirjaimia.
i = 0

while i < len(etunimi):
    print(etunimi[0].upper(), end="")
    i += 1
print(" ", end="")

# Tulosta käyttäjän sukunimi käänteisessä järjestyksessä.
for i in range(len(sukunimi) - 1, -1, -1):
    print(sukunimi[i], end="")

# for char in reversed(sukunimi):
#     print(char, end="")

# or reverse using slicing:
# rev = sukunimi[::-1]
# print(rev, end="")
