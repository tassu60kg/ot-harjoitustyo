```mermaid
 sequenceDiagram
    create participant Main
    create participant HKLLaitehallinto
    create participant rautatietori
    create participant ratikka6
    create participant bussi244
    create participant Lukijalaite
    create participant Lataajalaite
    create participant Kioski
    create participant Kalle   
    Main ->> HKLLaitehallinto: lisaa_lataaja(rautatietori)
    Main ->> HKLLaitehallinto: lisaa_lukija(ratikka6)
    Main ->> HKLLaitehallinto: lisaa_lukija(bussi244) 
    Main ->> rautatietori:
    Main ->> ratikka6: lisaa_lataaja
    Main ->> bussi244: lisaa_
    Main ->> Lukijalaite
    Main ->> Lataajalaite
    Kalle ->> Kioski: osta_matkakortti("Kalle")
    Kioski -->> Kalle
    Kalle ->> rautatietori: lataa_arvoa(kallen_kortti, 3)
    Kalle ->> ratikka6: osta_lippu(kallen_kortti, 0)
    Kalle ->> bussi244: osta_lippu(kallen_kortti, 2)
```
