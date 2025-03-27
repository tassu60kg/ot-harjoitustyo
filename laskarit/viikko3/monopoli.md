## Monopoli, alustava luokkakaavio

```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Ruutu "1" -- "1" Aloitusruutu
    Ruutu "1" -- "1" Vankila
    Asemat "4" -- "1" Ruutu
    Laitokset "2" -- "1" Ruutu
    Sattuma "3" -- "1" Ruutu
    Yhteismaa "3" -- "1" Ruutu
    Normaali katu (joihin liittyy nimi) "22" -- "1" Ruutu
    Yhteismaa -- Toiminto
    Sattuma -- Toiminto
    Toiminto ">1" -- Pelaaja	
    Ruutu -- Toiminto
    Talo "0..4" -- "1" Katu
    Hotelli "0..1" -- "1" Katu
```
