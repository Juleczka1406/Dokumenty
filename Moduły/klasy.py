class Czlowiek():
    def __init__(self, imie):
        print("Wywolal się init")
        self.imie = imie
    gatunek = "human"

#Teraz tworze instancje klasy
marcin = Czlowiek()
print(marcin.gatunek)

krzysztof = Czlowiek()
print(krzysztof.gatunek)
