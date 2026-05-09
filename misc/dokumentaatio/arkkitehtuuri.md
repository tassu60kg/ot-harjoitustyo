 # Arkkitehtuuri
 
 ## Luokkakaavio
```mermaid
classDiagram
    UI -- character
    UI -- fighting
    UI -- resources
    UI -- upgrades    
    resources -- upgrades
    character -- resources
    saveload -- character
    saveload -- fighting
    saveload -- resources
    saveload -- upgrades
```
`UI` on yllättäen käyttöliittymästä vastaaa luokka. Käyttöliittymä sisältää yhden näkymän.

`resources`-luokka luo olion jota käytetään `character`- ja `upgrades`-luokan asioiden ostamisessa. Lisäksi tämä luokka vastaa resurssien (itsensä) passiivisesta tuotosta `increase()` metodin kautta.
