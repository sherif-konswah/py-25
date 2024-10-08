import random as rdm
capital = "Cairo"
bird = "Abu Kerdan"
flower = "sun flower"
song ="Belady blady blady"


def randfuc():
    funahly = [
        "Ahli is biggest club in affrica",
        "Ahly Won 12 Championship league - CAF",
        "Ahly Won 44 Egyption League",
        "Ahly is a great club"
    ]
    
    index = rdm.choice("0123")
    print(funahly[int(index)])


if (__name__ == "__main__"):
    randfuc()
    