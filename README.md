# ohjelmistotuotanto harjoitustyö

Minimalistinen idle-peli. Pelissä voi kasvattaa eri numeroita useilla eri tavoilla.

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
 
 - [changelog](https://github.com/tassu60kg/ot-harjoitustyo/blob/main/misc/dokumentaatio/changelog.md)
 - [vaatimusmäärittely](https://github.com/tassu60kg/ot-harjoitustyo/blob/main/misc/dokumentaatio/vaativuusmaarittely.md)
 - [tuntikirjanpito](https://github.com/tassu60kg/ot-harjoitustyo/blob/main/misc/dokumentaatio/tuntikirjanpito.md)
 - [arkkitehtuuri](https://github.com/tassu60kg/ot-harjoitustyo/blob/main/misc/dokumentaatio/arkkitehtuuri.md)
 - [testausdokumentti](https://github.com/tassu60kg/ot-harjoitustyo/blob/main/misc/dokumentaatio/testaus.md)
 - [käyttöohje](https://github.com/tassu60kg/ot-harjoitustyo/blob/main/misc/dokumentaatio/kaytto-ohje.md)
 - [viikko 5 release](https://github.com/tassu60kg/ot-harjoitustyo/releases/tag/viikko5)

