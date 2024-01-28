### Aantekeningen 
    Commando's uit voorbeeld: X

Commando report: X
python super.py report inventory --now X
python super.py report inventory --yesterday X
python super.py report inventory --now X
python super.py report revenue --yesterday X
python super.py report revenue --today X
python super.py report revenue --date 2019-12 X
python super.py report profit --today X

# Inventory is uitvoer van de inventory.csv X
# Revenue is uitvoer van de inventory.csv X

Commando sell: X
python super.py sell --product-name orange --price 2 X X 
python super.py sell --product-name orange --price 2 X
>> ERROR: Product not in stock. X 

Commando buy:
python super.py buy --product-name orange --price 0.8 --expiration-date 2020-01-01 X

Commando tijd:
python super.py --advance-time 2 X

Aanpak in stappen:
 1. Eerst CLI maken waarin je de voorraad kunt zien X
 2. Artikel toevoegen in een line als class  X
 3. Daarna werken aan het verkopen van de artikelen X
 4. Daarna met de tijd gaan werken om die toe te voegen aan de commando's X

-  Default tijd is huidige tijd 
 Tijd is bij opstarten default kan vooruit, terug maar ook naar huidige tijd worden gezet. X

- Report in terminal en naar csv bestanden X
 
- Gebruik maken van rich-argparse X

- Als modules niet herkent worden: controleer welke interpreter je gebruikt: cntrl+shift+p X