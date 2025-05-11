# Testausdokumentti

Ohjelmaa on testattu automatisoiduin testein sekä joitakin osia testattu manuaalisesti (etenkin menu)

## Yksikkötestit

"Level" luokka testataan kokonaan, sillä tämä on yksinkertaisin luokista ja käytetään täysin karttaa luodessa

"Enemy" luokka testataan lähes kokonaan, ainoastaan satunnaista luontia (ja toisiinsa törmäämistä) ei testata, vaan tämän sijalle annetaan vaihtoehtoiset arvot

"Player" on vaikeiten ja huonoiten testattu, suurin osa tämän ja "Enemy" luokan testeistä tehdään pygamen sisällä

"scores" luokka testataan vain hiukan yli puoliksi, sillä testausrata on luotu huonosti, lisäksi uuden db tiedoston luontia ei testata; testit käyttävät erillistä tietokantaa

"game.py" ja "menu.py" tiedostoja ei testata sllä näillä ei ole omia funktioita vaan käyttävät muiden luokkien

![Testikattavuusraportti](https://github.com/tassu60kg/ot-harjoitustyo/blob/main/kuvat/kattavuus.png "raportti")
