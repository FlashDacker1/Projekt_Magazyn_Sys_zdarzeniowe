# Klasa reprezentująca robota
class Robot:
    def __init__(self, env, nazwa, magazyn):
        self.env = env
        self.nazwa = nazwa
        self.magazyn = magazyn
        self.zajety = False

    def wykonuj_zadanie(self, zadanie):
        """Robot realizuje zadanie."""
        self.zajety = True
        print(f"{self.env.now}: {self.nazwa} rozpoczyna {zadanie}")
        czas_realizacji = 3  # Stały czas realizacji (można rozszerzyć na losowy)
        yield self.env.timeout(czas_realizacji)
        print(f"{self.env.now}: {self.nazwa} zakończył {zadanie}")
        self.zajety = False
        self.magazyn.przypisz_zadanie()
