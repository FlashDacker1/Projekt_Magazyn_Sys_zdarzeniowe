import simpy
from magazyn import Magazyn

def main():
    # Inicjalizacja środowiska
    env = simpy.Environment()

    # Tworzenie magazynu z 3 robotami
    magazyn = Magazyn(env, liczba_robotow=3)

    # Uruchomienie generatora zadań
    env.process(magazyn.generuj_zadania())

    # Symulacja przez 30 jednostek czasu
    print("Rozpoczynam symulację...")
    env.run(until=30)
    print("Symulacja zakończona.")

if __name__ == "__main__":
    main()
