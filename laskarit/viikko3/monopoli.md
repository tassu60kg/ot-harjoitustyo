```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Ruutu "1" -- "1" Aloitusruutu
    Aloitusruutu "1" -- "1" Monopolipeli
    Aloitusruutu "1" -- "1" Toiminto
    Ruutu "1" -- "1" Vankila
    Vankila "1" -- "1" Monopolipeli
    Vankila "1" --"1" Toiminto
    Ruutu "1" -- "22" Katu
    Katu "1" -- "0..4" Talo
    Katu "1" -- "0..1" Hotelli
    Katu "1" -- "1" Katu : Nimi
    Katu "1" -- "1" Toiminto
    Ruutu "1" -- "8" Laitokset
    Laitokset "1" -- "1" Toiminto
    Ruutu "1" -- "3" Sattuma
    Ruutu "1" -- "3" Yhteismaa
    Sattuma "1" -- "?" Kortti
    Yhteismaa "1" -- "?" Kortti
    Kortti "?" -- "1" Toiminto
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "1" -- "*" Raha
    
```
