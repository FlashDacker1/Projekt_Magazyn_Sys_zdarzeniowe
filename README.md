# Projekt Magazyn 
## 1. Problem projektu
Celem projektu jest opracowanie sterownika zarządzającego robotami mobilnymi w magazynie, a nie wyłącznie symulacji ich działania. System ma umożliwić sterowanie ruchem robotów, które autonomicznie odbierają paczki z punktów odbioru, reagując na zdarzenia takie jak przyjazd ciężarówki z ładunkiem czy konieczność przekazania paczki do odpowiedniej rampy.  
Sterownik będzie odpowiadał za:  
1. Rozdzielanie zadań do robotów.
2. Zarządzanie ruchem w czasie rzeczywistym (np. rezerwacja odcinków).
3. Obsługę zdarzeń takich jak konflikty na skrzyżowaniach lub nagłe zatrzymania.  

Efektem projektu będzie moduł sterujący, możliwy do wykorzystania w rzeczywistym środowisku, wraz z symulacją jako narzędziem testowym.

## 2. Plan pracy i harmonogram
Projekt składa się z etapów:  

  * Etap 1: Projektowanie algorytmu nawigacji i omijania przeszkód (Tydzień 1–2).  
  * Etap 2: Implementacja modułu symulacji ruchu robotów (Tydzień 3–4).  
  * Etap 3: Testowanie systemu (Tydzień 5–6).  
  * Etap 4: Tworzenie dokumentacji (Tydzień 7–8).  
  * Etap 5: Publikacja wyników (Tydzień 9–10).  
  
Kamienie milowe:  

  * Ukończenie projektowania systemu (Tydzień 5).  
  * Testowanie zakończone z sukcesem (Tydzień 10).  
  * Publikacja wyników (Tydzień 12).  
  
Diagram Gantta uwzględni podział zadań i dostępność zasobów.

## 3. Doręczenie
Raporty będą składane na zakończenie kluczowych etapów (projektowanie, implementacja, testowanie). Zawartość:
    * Kod w formie archiwum.
    * Dokumentacja techniczna.
Raporty będą przechowywane w systemie kontrolowanego dostępu.

## 4. Środowisko pracy  
  * Narzędzia: Visual Studio Code, Python.  
  
  * Biblioteki:  
  ◦ pygame (symulacja graficzna ruchu robotów).  
  ◦ numpy (modelowanie zdarzeniowe i obliczenia).  
  ◦ simpy (symulacja zdarzeń).  
  ◦ matplotlib (wizualizacja danych).  
  ◦ Inne dedykowane narzędzia do zarządzania ruchem robotów.  
  
  * Plan magazynu:
  ◦ Podzielony na sektory o stałych wymiarach.  
  ◦ Punkty odbioru, rampy, ścieżki komunikacyjne.  
  ◦ Ścieżki są jednokierunkowe z punktami krytycznymi na skrzyżowaniach.

## 5. Model zarządzania i ruchu robotów  
1. Sterowanie:
* Zadania napływają losowo z ciężarówek (różna liczba paczek i sektory).
* Roboty realizują zadania zgodnie z priorytetem.
2. Rezerwacja odcinków:
  * 1 robot na jednym odcinku drogi.
  * Po dojechaniu do skrzyżowania robot czeka na decyzję systemu nadrzędnego.
  * Jeśli pozwolenie jest przyznane, robot rezerwuje bieżący i następny odcinek.
3. Symulacja zdarzeń:
* Generowane zdarzenia np.:
◦ Przyjazd ciężarówki.
◦ Rejestracja nowego zadania.
◦ Przejazd robota do kolejnego sektora.
* System śledzi aktualny stan robotów i całego magazynu.

## 6. Zarządzanie projektem  
* Koordynator: Stanisław Wojtowicz – zarządza pracą zespołu i komunikacją.
* Podział zadań:  
◦ Stanisław Wojtowicz – moduł nawigacji.  
◦ Michał Raciborski – algorytm omijania przeszkód.  
◦ Jan Szykasiuk – testowanie i walidacja systemu.  
◦ Daniel Zakharov – dokumentacja projektu.

* Regularne spotkania online.  
* Dokumentacja i kod przechowywane w systemie wersjonowania (GitHub).

## 7. Stany systemu i zdarzenia  
Stany systemu:  
1. Towar przyjęty na magazyn:  
◦ Ciężarówka zgłasza przyjazd i zleca rozładunek.
2. Towar w trakcie rozładunku:  
◦ Paczki są przypisywane do konkretnych sektorów.
3. Towar rozłożony w magazynie:  
◦ Gotowość do odbioru przez roboty.
4. Robot na zadaniu:  
◦ Robot realizuje odbiór paczki i transport do rampy.
5. Robot na odcinku:  
◦ Przemieszcza się między sektorami.
6. Robot na skrzyżowaniu (punkt krytyczny):  
◦ Oczekuje na decyzję systemu nadrzędnego.
7. Robot w punkcie docelowym:  
◦ Dostarczył paczkę na rampę, zgłasza gotowość do nowego zadania.
8. Czekanie na zadanie:  
◦ Robot nieaktywny, oczekuje na nowe zadanie.

Zdarzenia w systemie:  
1. Przyjazd ciężarówki:  
◦ Generuje nowe zadania i przypisuje je do systemu.
2. Rezerwacja odcinka przez robota:  
◦ Robot zgłasza chęć przejazdu przez odcinek.
3. Wejście robota w punkt krytyczny:  
◦ Robot zgłasza obecność na skrzyżowaniu.
4. Zwolnienie odcinka:  
◦ Robot kończy przejazd i zwalnia trasę dla innych.
5. Dostarczenie paczki:  
◦ Zdarzenie oznaczające zakończenie zadania.
6. Konieczność omijania przeszkody:  
◦ Robot zgłasza obecność przeszkody i czeka na decyzję systemu.
7. Nowe zadanie dla robota:  
◦ System nadrzędny przydziela zadanie z listy zadań.
8. Błąd lub awaria:  
◦ Zgłoszenie błędu robota i wstrzymanie działań na trasie.

Sterownik będzie sterował stanami i obsługiwał powyższe zdarzenia, zapewniając optymalny przepływ zadań oraz bezpieczeństwo w ruchu robotów w magazynie.  

## 8. Dodatkowe wyzwania i przemyślenia
* Modelowanie i optymalizacja napływu zadań.
* Planowanie ruchu w oparciu o symulację zdarzeń.
* Zintegrowanie mechanizmu priorytetów dla robotów w systemie nadrzędnym.
