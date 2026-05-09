 # Käyttöohje

## Käynnistys ja aseunnus:
1. kloonaa repositorio
2. mene src kansioon
3. aja install.sh (yleensä "sh install.sh")
4. aja run.sh

Vaihtoehtoisesti:
1. kloonaa repositorio
2. aja "poetry install" src kansiossa
3. käynnistä virtuaaliympäristö "eval $(poetry env activate)"
4. käynnistä komennolla "poetry run invoke start"

## Testaus
Testit:
```bash
 poetry run invoke test
```
Kattavuusraportti:
```bash
 poetry run invoke coverage-report
```
Linttaus:
```bash
 poetry run invoke lint
```
 ## pelaus
 Pelin ideana on kasvattaa taitojasi ja päihittää yhä vahvempia vihollisia.
 
<img width="839" height="674" alt="image" src="https://github.com/user-attachments/assets/2f3aa002-aa26-4fc0-9364-78e0011b2d3a" />

1. Swag eli pelin pääresurssi. tätä saa automaattisesti ja sen saannin määrää voi päivittää.
2. Swag per sekunti. Peli päivittyy kymmenesti sekunnissa.
3. Swägään liittyvät päivitykset. Nimi, hinta, swagin lisäsaannin määärä (per 1/10 sekunnissa).
4. Tämä on se nappi, jolla päivitykset ostetaan (päivityksen voi valita kohdan 3 valikosta).
5. Taisteluun liittyvät taidot. Käyttää AP (apgrade pointseja)
6. Näillä napeilla päivitetään (ja epäpäivitetään) taitoja.
8. Tässä näkyy AP ja kuinka paljon sen ostaminen maksaa.
7. Tästä ostetaan AP.
9. Taisteluun liittyvien taitojen yhdistetty voima.
10. Vihollinen, kohdan 9 voiman tulisi olla yli vihollisen voiman voittaaksesi.
11. Tallentaa ja lataa pelin tiedostosta.

 ## Konfiguraatio
 Peliä voi muuttaa jos jostakin syystä haluaa.
 `data` kansiossa saattaa olla `saveload.txt` niminen tiedosto, jos sitä ei ole pelin tallentaminen luo sen.
 <img width="1190" height="299" alt="image" src="https://github.com/user-attachments/assets/9f917732-e81e-4e3c-860a-7f54055622dc" />
  Pahoittelut hyvästä fontista.
 1. Tällä rivillä ovat päivitykset, päivitykset ovat määritelty hakasulkeiden sisälle ja jaettu pilkulla ja välilyönnillä. Ensimmäinen asia hakasulkeiden sisällä on päivtyksen nimi, toinen hinta ja kolmas kuinka paljon lisää swägiä se entaa per 1/10 sekunti.
 2. Swag
 3. Swag per 1/10 sekunti
 4. Taidot, näitä täytyy olla vähintään 6 tai peli hajoaa, lisäksi jos niitä on yli 6 osa ei tee mitään :) Hakasulkeissa taidon nimi ja taso.
 5. AP
 6. AP:n ostamisen hinta
 7. Vihollisen nimi. Nimen perässä tulisi olla luku jota kasvattaa.
 8. Vihollisen voima
 9. Vihollisen iteraatio, eli kuinka mones vihollinen tämä on.

Konfiguraation voi ladata painamalla load-nappia.
