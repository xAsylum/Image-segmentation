# Założenie projektu
Celem projektu jest wytrenowanie i porównanie różnych architektur (modeli), sporządzenie interfejsu do wczytywania danych i przekazywania ich do modeli, sporządzenie funkcjonalności przedstawiającej i porównującej otrzymane wyniki, m.in. za pomocą wykresów.

# Proponowane Interfejsy
## Dataset

- Pary <Image, Label>
- ### Podział na zbiór treningowy i walidacyjny:
- Podział domyślny (zaproponowany przez autorów datasetu)
- Własne proporcje
- Walidacja krzyżowa

## IDatasetLoader:
- loadDataset(path: str) -> Dataset

Zastanowić się, czy Dataset ma być naszą klasą, czy czymś oferowanym przez np. pyTorch

## IModel
- Wczytanie danych formatu Dataset
- Definicja forward-pass (szkielet modelu)
- Weryfikacja skuteczności modelu
- Trenowanie modelu
- Zachowanie informacji o jakości treningu
- Funkcja predict do pokazywania na nowych danych

## AnalyzeData = TrainData + TestData
- Wygeneruj wykresy na podstawie danych treningowych i testowych (weryfikacyjnych)
- Konstrukcja na podstawie zapisywalnych danych o treningu


# Wykorzystane technologie
pyTorch