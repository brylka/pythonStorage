
# Aplikacja Flask

Ta aplikacja została stworzona na zajęciach w Zespole Szkół Rzemiosł Artystycznych w Jeleniej Górze na kierunku Technik Informatyk na zajęciach Programowanie Aplikacji. Projekt obejmuje podstawowe funkcjonalności aplikacji webowej, takie jak zarządzanie danymi przez ORM, routing oraz szablony HTML dla interfejsu użytkownika.

## Funkcjonalności

- Zarządzanie danymi za pomocą Flask-SQLAlchemy (modele danych dla produktów, kategorii i marek)
- Wyświetlanie danych w przeglądarce (szablony HTML)
- Generowanie przykładowych danych do testowania aplikacji

## Instalacja

Aby zainstalować wymagane zależności, sklonuj repozytorium i uruchom:

```
pip install -r requirements.txt
```

Następnie, aby skonfigurować bazę danych, wykonaj następujące polecenia:

```
flask db init
flask db migrate
flask db upgrade
```

## Uruchamianie aplikacji

Aplikację można uruchomić za pomocą polecenia:

```
python app.py
```

## Struktura katalogów

- `app/` - główne pliki aplikacji (modele, trasy, inicjalizacja)
- `app/templates` - szablony HTML
- `scripts/` - skrypty pomocnicze, np. do generowania danych
- `app.py` - plik uruchomieniowy aplikacji
- `config.py` - konfiguracja aplikacji

## Prawa autorskie

Projekt został stworzony jako część ćwiczeń na zajęciach z Programowania aplikacji w klasie 4IR przez Bartosza Bryniarskiego. Możesz dowolnie korzystać z kodu.
