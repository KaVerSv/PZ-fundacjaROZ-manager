# FundacjaROZ Manager
![Logo Projektu](https://github.com/KaVerSv/PZ-fundacjaROZ-manager/blob/main/logo.png)

FundacjaROZ Manager jest to aplikacja do zarządzania placówką opiekuńczo-wychowawcza typu rodzinnego.


## Instalacja

Aby zainstalować aplikacje należy wykonać następujące kroki:

git clone [<_LINK>](https://github.com/KaVerSv/PZ-fundacjaROZ-manager)

## Uruchomienie

Aby uruchomić aplikacje należy wykonać następujące kroki:

```bash
cd PZ-fundacjaROZ-manager

docker-compose up
```

## Dostęp do dysku googla

Aby mieć dostęp do dysku googla należy plik credentials.json,  możliwy do pobrania po nadaniu upranien do dysku dla aplikacji, wstawić w folder na backendzie: 
```bash
PZ-fundacjaROZ-manager\backend\fundacjaROZ\views_collection
```
a następnie po zalogowaniu w nowej zakładce przejść przez strone autoryzacji do dysku googla i po sukcesie wyłączyć zakładke i odświeżyć stronę główną

## Użytkowanie

Aby korzystać z aplikacji należy wejść na stronę:

http://localhost:8080

## Funkcjonalności na frontendzie:
- Rejestracja
- Logowanie
- Przeglądanie podopiecznych
- Sortowanie podopiecznych po imieniu, nazwisku, dacie urodzenia, dacie przyjęcia
- Dodawanie podopiecznych
- Edycja podopiecznych
- Dodawanie, usuwanie i edycja dokumentów związanych z dany dzieckiem dzieckiem i ewentualnie do osób powiązanych
- Dodawanie, edycja i usuwanie osób powiązanych do dziecka
- Dodawanie, edycja i usuwanie notatek do dziecka
- Dodawanie, edycja i usuwanie szkół do których uczęszczało dziecko

## Funkcjonalności na bakendzie:
- Rejestracja
- Logowanie
- Przeglądanie podopiecznych
- Sortowanie podopiecznych po imieniu, nazwisku, dacie urodzenia, dacie przyjęcia
- Dodawanie podopiecznych
- Edycja podopiecznych
- Dodawanie, usuwanie i edycja dokumentów związanych z dany dzieckiem dzieckiem i ewentualnie do osób powiązanych
- Dodawanie, edycja i usuwanie osób powiązanych do dziecka
- Dodawanie, edycja i usuwanie notatek do dziecka
- Dodawanie, edycja i usuwanie szkół do których uczęszczało dziecko

## Technologie:
- React
- TypeScript
- Django
- Postgres
- Tailwind
- Vite

## Diagram ERD
![Diagram_ERD](https://github.com/KaVerSv/PZ-fundacjaROZ-manager/blob/main/zespolowy.png)

## Autorzy
Zakhar Sytoi, Konrad Tatomir, Maksymilian Toczek, Kacper Węglarz, Piotr Żywczak

## Obecny wygląd strony:
![SS1](https://github.com/zywczak/WdPAI/blob/main/screenshot1.png)
![SS6](https://github.com/zywczak/WdPAI/blob/main/screenshot6.png)
![SS4](https://github.com/zywczak/WdPAI/blob/main/screenshot4.png)
![SS2](https://github.com/zywczak/WdPAI/blob/main/screenshot2.png)
![SS3](https://github.com/zywczak/WdPAI/blob/main/screenshot3.png)
![SS5](https://github.com/zywczak/WdPAI/blob/main/screenshot5.png)

## Zakładany wygląd strony:

https://www.figma.com/design/sVHy4P28XsD8guK0B8IINp/FundacjaROZ?node-id=0-1
