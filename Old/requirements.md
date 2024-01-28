# Eisen van Superpy 

## Algemeen 
1. Command line tool genaamd SuperPy X
2. Inventory (voorraad) van supermarkt X 
3. Core function: keeping track and producing reports. X 


## Deel argparse 
1. Tijd moet met een command als "$ python super.py --advance-time 2" twee dagen naar de toekomst kunnen X
    - Dit om te kijken of bijvoorbeeld over de datum gaat x
2. interactie via command line zie sample_terminal voor hoe dit eruit zou moeten zien. x
3. User friendly CLI met overal een --help sectie x

## Deel CSV

1. Welke producten de supermarkt heeft x
2. Welke voorraad van een product de supermarkt heeft  x
3. De inkoop prijs van het product en de houdbaarheidsdatum  x
4. Verkoopprijs OF als t.h.t datum is verlopen het feit dat het over de datum is x
5. Alle data moet in CSV files staan x
6. Eigen data structuur maar er is een voorbeeld: x
7. bought.csv -> id,product_name,buy_date,buy_price,expiration_date x
8. sold.csv -> id,bought_id,sell_date,sell_price -> id is hier een integer  x
9. Alle data in csv bestanden x
10. Rapporteren over omzet en winst over gespecificeerde tijdsperioden x
11. Exporteren selecties van data naar CSV files. X


## Deel tijd

1. programma moet weten wat de huidige datum het is X
2. tijd mag/moet opgeslagen zijn in een simpel text bestand (of csv) X
3. tijd moet met een command als "$ python super.py --advance-time 2" twee naar toekomst kunnen X
4. De datum kunnen instellen dat het programma ziet als huidige datum X
5. Vastleggen kopen en verkopen producten op datums X
    
## Overige voorwaarden

Wees creatief en minimaal:

1. Goed gestructureerde code X
    -   Duidelijke variabelen, functies etc X
    -   Gebruik van comments wanneer nodig X
    -   Splitsen van de code in duidelijke blokken en/of files X

2. Gebruik van modules:
    -   csv X
    -   argparse X
    -   datetime, met strftime, strptime en timedelta X

5. Txt file met read me guide en aantal voorbeelden 

7. Kies twee van de volgende 4 dingen: 
    - Gebruik van de module rich.  X
    - Het import/exporteren van rapporteren van/naar formats naast CSV.
    - Visualiseren van data met Matplotlib. X
    - Een andere zelf bedachte feature. X

8. Afronding:
    - Voeg een klein rapport van 300 woorden toe dat 3 technische elementen van je programma die noemenswaardig zijn. X
    - Leg uit welk probleem ze oplossen en waarom je zo hebt geimplementeerd X
    - Dit verslag inleveren als report.md  X
    - Je mag markdown gebruiken om de report mooi weer te geven.  X

