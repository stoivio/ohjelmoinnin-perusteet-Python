# Tee funktio lotto(), joka arpoo lottorivin seitsemän (7) numeroa väliltä 1-40 ja palauttaa sen merkkijonona, luvut eroteltuna pilkuilla.

import random


def lotto():
    list = []
    lottorivi = ""
    i = 0
    while i < 7:
        # or use random.randrange(1,41) = is number between 1-40
        lottorivi += str(random.randint(1, 40)) + ", "
        # list.append(str(random.randint(1, 40)))
        i += 1

    # lottorivi = ", ".join(list)
    return lottorivi


print(lotto())
