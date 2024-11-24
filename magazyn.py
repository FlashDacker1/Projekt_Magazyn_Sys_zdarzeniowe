# Logika zarządzania magazynem
import random
from robot import Robot

class Magazyn:
    def __init__(self, env, liczba_robotow):
        self.env = env
        self.roboty = [Robot(env, f"Robot-{i+1}", self) for i in range(liczba_robotow)]
        self.zadania = []

    def generuj_zadania(self):
        """Generator losowych zadań."""
        while True:
            yield self.env.timeout(random.randint(2, 5))  # Co 2-5 jednostek czasu
            zadanie = f"Zadanie-{len(self.zadania)+1}"
            print(f"{self.env.now}: Dodano {zadanie}")
            self.zadania.append(zadanie)
            self.przypisz_zadanie()

    def przypisz_zadanie(self):
        """Przypisuje zadanie pierwszemu dostępnemu robotowi."""
        for robot in self.roboty:
            if not robot.zajety and self.zadania:
                zadanie = self.zadania.pop(0)
                print(f"{self.env.now}: {robot.nazwa} otrzymuje {zadanie}")
                self.env.process(robot.wykonuj_zadanie(zadanie))
