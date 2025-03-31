```mermaid
 sequeceDiagram
  Main->>HKLLaitehallinto: lisaa_lataaja(rautatietori)
  Main->>HKLLaitehallinto: lisaa_lukija(ratikka6)
  Main->>HKLLaitehallinto: lisaa_lukija(bussi244) 
  Main->>rautatietori
  Main->>ratikka6
  Main->>bussi244
  Main->>Lukijalaite
  Main->>Lataajalaite
  Kalle->>Kioski: osta_matkakortti("Kalle")
  Kioski-->>Kalle
  Kalle->>rautatietori: lataa_arvoa(kallen_kortti, 3)
  Kalle->>ratikka6: osta_lippu(kallen_kortti, 0)
  Kalle->>bussi244: osta_lippu(kallen_kortti, 2)


```
