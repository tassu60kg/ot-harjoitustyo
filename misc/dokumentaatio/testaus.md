# Testausdokumentti
 Ohjelmaa on testattu yksikkö- ja integraatiotestein unittestia käyttäen. Lisäksi järjestelmätestausta on tehty manuaalisesti.

## yksikkö- ja integraatiotestaus
  Sovelluslogiikasta vastaavia luokkia `character`, `fighting`, `resources` ja `upgrades`, sekä tiedon tallentamisesta vastaavaa `saveload`-luokkaa testataan näiden testataan näiden omilla [testiluokilla](https://github.com/tassu60kg/ot-harjoitustyo/tree/main/src/tests). Testit sisältävät sekä yksikkö-, että integraatiotestejä. `savelaod` luokalle on lisäksi omat `testsave.txt` ja `testload.txt` testaustiedostot, mistä haetaan tai tallennetaan tietoa normaalin tallennustiedoston sijasta.

## Testikattavuus
  Lähes kaikki oleellinen testataan, ulkopuolelle jää mm. tiedoston puuttumisen testaus sekä luokkien luomisen yhteydessä saatavat oletusarvot. Käyttöliittymää ei testata.
  <img width="888" height="432" alt="image" src="https://github.com/user-attachments/assets/e33ef2bb-2ddb-4997-8dd8-a44dffa3e7c1" />

## Järjestelmätestaus
 Suoritettu manuaalisesti.

### Asennus ja konfigurointi
 Ohjelmaa on testattu vain käyttöohjeen määrittelemällä tavalla Linux-ympäristössä.

### Toiminnallisuus
 Vaativuusmäärittelyn ja käyttöohjeen toiminnallisuudet on käyty käyty läpi.
 
## Jääneet laatuongelmat
  Jos käyttäjä muuttaa tallennustiedostoa väärin, ohjelma voi heittää virheilmoituksia tai hajota jollakin tavalla. Tässä tapauksessa syy on kuitenkin käyttäjän.
