### Aantekeningen 
    Commando's uit voorbeeld:

Commando report:
python super.py report inventory --now
python super.py report inventory --yesterday
python super.py report inventory --now
python super.py report revenue --yesterday
python super.py report revenue --today
python super.py report revenue --date 2019-12
python super.py report profit --today

# Inventory is uitvoer van de inventory.csv
# Revenue is uitvoer van de inventory.csv

Commando sell:
python super.py sell --product-name orange --price 2
python super.py sell --product-name orange --price 2
>> ERROR: Product not in stock. 

Commando buy:
python super.py buy --product-name orange --price 0.8 --expiration-date 2020-01-01

Commando tijd:
python super.py --advance-time 2

Aanpak in stappen:
 1. Eerst CLI maken waarin je de voorraad kunt zien
 2. Artikel toevoegen in een line als class 
 3. Daarna werken aan het verkopen van de artikelen
 4. Daarna met de tijd gaan werken om die toe te voegen aan de commando's