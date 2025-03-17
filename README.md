# 🦆 Rozwiązanie Zagadki Kaczuszek 🦆

Ten projekt pomaga rozwiązać zagadkę zaginionej kaczuszki analizując dane liczb rzeczywistych.

## 📊 O projekcie

W ramach programu stażowego **RAS TECH Summer 4.0**, pomagamy znaleźć zaginioną 14. kaczuszkę! Projekt analizuje duży zbiór danych numerycznych, aby znaleźć dwie najczęściej występujące liczby - klucz do rozwiązania zagadki.

## 🛠️ Instalacja i uruchomienie

### Wymagania wstępne

- Python 3.8+
- Dostęp do internetu (do pobrania danych)

### Krok po kroku

1. **Klonowanie repozytorium:**
   ```bash
   git clone <url-repozytorium>
   cd kaczuszki-analysis
   ```

2. **Instalacja zależności przy użyciu uv:**
   ```bash
   # Instalacja narzędzia uv (jeśli jeszcze nie zainstalowano)
   pip install uv

   # Instalacja zależności projektu przy użyciu uv
   uv pip install numpy pandas matplotlib seaborn requests
   ```

3. **Uruchomienie skryptu:**
   ```bash
   python data_analysis.py
   ```

## 🔍 Jak to działa

Skrypt wykonuje następujące kroki:
1. Pobiera archiwum ZIP z podanego URL
2. Rozpakowuje plik tekstowy zawierający liczby rzeczywiste
3. Analizuje dane, zliczając wystąpienia każdej liczby
4. Identyfikuje dwie najczęściej występujące wartości
5. Tworzy wizualizację danych w postaci histogramu
6. Zapisuje wynik w formacie `liczba1,liczba2`

## 📈 Wyniki

Rozwiązanie zagadki (dwie najczęściej występujące liczby):
```
50.0764583,19.9467553
```

