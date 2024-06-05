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

## Funkcjonalności na frontend:
> Rejestracja

> Logowanie

> Strona główna
- Przeglądanie podopiecznych
- Sortowanie podopiecznych po dacie urodenia, imieniu, nazwisku, dacie przyjęcia
- Wyszukiwanie sierot biologicznych
- Dodawanie podopiecznych
> Widok podopiecznych
- Edycja dziecka
- Dodawanie dokumentów związanych z dany dzieckiem i ewentualnie przypisanie osoby powiązanej także związanej z teym dokumentem
- Przeglądanie dokumentów związanych z dany dzieckiem
- Usuwanie dokumentów związanych z dany dzieckiem
- Edycja dokumentów związanych z dany dzieckiem
- Dodawanie osób powiązanych do dziecka
- Edycja osób powiązanych z dzieckiem
- Usuwanie osób powiązanych z dzieckiem
- Dodawanie notatek do dziecka
- Edycja notatek 
- Usuwanie notatek
- Dodawanie szkół, do których uczęszcza(ło) dziecko
- Usuwanie szkól, do których uczęszcza(ło) dziecko
- Edycja informacji o szkołach, do których uczęszcza(ło) dziecko

## Funkcjonalności przewidziane przez backend:
> Rejestracja

> Logowanie

> Strona główna - spis podopiecznych
- Przeglądanie podopiecznych
- Sortowanie podopiecznych po dacie urodenia
- Wyszukiwanie podopiecznych po imieniu i nazwisku
- Wyszukiwanie sierot biologicznych
- Dodawanie podopiecznych
> Widok podopiecznego
- Edycja dziecka
- Dodawanie dokumentów związanych z dany dzieckiem i ewentualnie przypisanie osoby powiązanej także związanej z tym dokumentem
- Przeglądanie dokumentów związanych z dany dzieckiem
- Dodawanie osób powiązanych do dziecka
- Przeglądanie osób powiązanych z danym dzieckiem
- Edycja osób powiązanych z dzieckiem
- Usuwanie osób powiązanych z dzieckiem
- Dodawanie notatek do dziecka
- przeglądanie notatek
- Edycja notatek dziecka
- Usuwanie notatek
- Dodawanie szkół, do których uczęszcza(ło) dziecko
- Przeglądanie szkól, do których uczęszcza(ło) dziecko
- Usuwanie szkól, do których uczęszcza(ło) dziecko
- Edycja informacji o szkołach, do których uczęszcza(ło) dziecko
> Spis osób powiązanych
- Przeglądanie osób powiązanych
- Dodawanie osoby powiązanej
> Widok osóby powiązanej
- Edycja osoby powiązanej
- Dodawanie dokumentów związanych z daną osobą powiązaną i ewentualnie przypisanie dziecka także związanego z tym dokumentem
- Przeglądanie dokumentów związanych z osobą powiązanej
- Dodawanie dziecka do osoby powiązanej
- Usuwanie dziecka od osóby powiązanej
- Przeglądanie dokumentów powiązanych z dzieckiem
>Spis dokumentów
- Pzeglądanie dokumentów
- Dodawanie dokumentów
> Widok dokumentu
- Przeglądanie dokumentu
- Usuwanie dokumentu
- Edycja dokumentu
- Dodawanie nowego dokumentu
>Spis szkół
- Przeglądanie szkół
- Dodawanie szkoły
>Widok szkoły
- Przeglądanie informacji o szkole
- Edycja szkoły
- Usuwanie szkoły


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
![SS1](https://github.com/KaVerSv/PZ-fundacjaROZ-manager/blob/main/screenshot1.png)
![SS6](https://github.com/KaVerSv/PZ-fundacjaROZ-manager/blob/main/screenshot6.png)
![SS4](https://github.com/KaVerSv/PZ-fundacjaROZ-manager/blob/main/screenshot4.png)
![SS2](https://github.com/KaVerSv/PZ-fundacjaROZ-manager/blob/main/screenshot2.png)
![SS3](https://github.com/KaVerSv/PZ-fundacjaROZ-manager/blob/main/screenshot3.png)
![SS5](https://github.com/KaVerSv/PZ-fundacjaROZ-manager/blob/main/screenshot5.png)
![SS6](https://github.com/KaVerSv/PZ-fundacjaROZ-manager/blob/main/screenshot6.png)
![SS7](https://github.com/KaVerSv/PZ-fundacjaROZ-manager/blob/main/screenshot7.png)

## Zakładany wygląd strony:

https://www.figma.com/design/sVHy4P28XsD8guK0B8IINp/FundacjaROZ?node-id=0-1
