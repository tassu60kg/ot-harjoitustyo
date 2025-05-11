# Arkkitehtuuri

## rakenne

Ohjelma vastaa seuraavaa rakennetta

![rakenne](https://github.com/tassu60kg/ot-harjoitustyo/blob/main/kuvat/kaavio.png "rakenne")
(player ja enemy välillä ei pitäisi olla viivaa)

scores vastaa tietokantojen käsittelystä, level kartan luonnista, player pelaajan toiminnasta, enemy vastustajien toiminnasta, menu game:n käynnistämisestä ja game pääsilmukan pyörittämisestä

main kutsuu muiden moduulien funktioita pelaajan syötteiden ja sisäisen kellon mukaisesti, myös esim päivittää näytön. lisäksi main luokassa luetaan name.txt tallennettu nimi, joka ladataan tietokantaan.

kuten rakenteesta huomaa, muut moduulit (paitsi player ja level) eivät ole suorassa vuorovaikutuksessa keskenään vaan saavat tiedot toisistaan main:in kautta (esim move_player seinien sijainnit).

## spritejen jako

![spritet](https://github.com/tassu60kg/ot-harjoitustyo/blob/main/kuvat/sprite.png "sprite")

Vihollis-spritet esiintyvät vain omassa ryhmässään enemy moduulissaan, missä muut spritet lisätään level moduulin sprites-spriteryhmään (unohdin lisätä). Näitä ryhmiä käytetään tarkistamaan: pelaajan ja seinien väliset törmäykset (player moduulissa), pelaajan ja vihollisten väliset törmäykset (player moduulissa), vihollisten ja muiden vihollisten väliset törmäykset (viholliset moduulissa) sekä pelaajan laserin ja vihollisten törmäyksiä(?).

(tähän siisti kuva avaamaan edellistä)


## tietokannan toiminta

scores moduuli on vastussa tietokantojen toiminnasta, tätä käytetään vain parhaiden pisteiden tallentamiseen. Tietokanta alustetaan tätä kutsuttaessa.
