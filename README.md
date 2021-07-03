# p1hat
Rasbperry Pi P1 Monitor (ztatz.nl) IO HAT

![pcb](./doc/img/thumbnail_pcb.jpg)

## Behuizing
Er is ook een behuizing!

![render](./doc/img/thumbnail_enclosure.jpg)


## Aansluitingen

![aansluitingen](./doc/img/pcb-text.png)

## Inputs

Er zijn 6 gebufferde ingangen geschikt voor open-collector apparaten.
Zoals S0 pulsen van energiemeters of NPN type inductieve sensoren voor watermeters.

![inputs](./doc/img/input.png)

Het buffer is een 74LVC07A met schmitt trigger ingangen en open drain uitgangen. 
Hiervoor is het dus nodig om de pull-ups in de BCM te activeren. 
Een ander buffer kan ook, velen passen op deze SOIC footprint.

Het filternetwerk 1k/1nF dempt eventuele ingekoppelde storingen en de sterke pull-up van 1 kOhm voorkomt spontane detecties. *(van nabij schakelende relais, motoren of andere storingen)*  

> Als er schakelaars worden aangesloten dient dit netwerk wellicht te worden vertraagd, probeer 100k en 10nf. Of [debounce](https://en.wikipedia.org/wiki/Switch#Contact_bounce) in software.

## Outputs

Twee smart high side fets kunnen bijna elke 12/45V last schakelen.
 - Ze zijn geschikt voor high-side switching. 
 - Ze zijn geschikt voor inductieve lasten zonder vrijloop diode. (relais)
 - Ze zijn thermisch kortsluitbeveiligd.
 
Vrijwel niet kapot te krijgen.

## RS-485

Op de print zit een RS-485 tranceiver. Om bijvoorbeeld te praten met RS-485 energiemeters.
De middelste pin van de RS-485 header is GND, dit is meestal niet nodig.

> Hoe dit op de raspberry werkt moet ik nog uitzoeken.  

## GPIO Header

| Board          | GPIO | Mode       |
|----------------|------|------------|
| IN1            | 17   | Pull-up    |
| IN2            | 27   | Pull-up    |
| IN3            | 22   | Pull-up    |
| IN4            | 23   | Pull-up    |
| IN5            | 24   | Pull-up    |
| IN6            | 25   | Pull-up    |
| OUT1           | 26   | Push-Pull  |
| OUT2           | 16   | Push-Pull  |
| RS485 TX       | 14   | Alt0       |
| RS485 RX       | 15   | Alt0       |
| RS485 TXENABLE | 18   | Push-Pull  |

## BOM

Lijst met onderdelen:

- PCB, zie .txt file in de map PCB voor onderdelen.
    - De onderdelen zijn te krijgen via Conrad, Reichelt of zelfs AliExpress of sinuss.nl (dat is farnell/avnet voor particulieren).
- Raspberry Pi 4 met SD kaart en P1 Monitor
- Behuizing 3D-geprint van PETG.
- Schroeven
    - 4x M2.5x16 Verzonken Torx (TX8) WS 9475TX
    - 4x M2.5x12 Verzonken Torx (TX8) WS 9475TX
        - Zie [rvspaleis.nl](https://www.rvspaleis.nl/bouten/torx/ws-9475/ws-9475-[-]-a2-[-]-m2,5)

> De 1 kOhm pull-ups parallel aan de LED heb ik op mijn print niet geplaatst. Mogelijk zijn deze bij andere typen, of geen, LED's wel nodig.

## Software

De gebruikte software is (gratis) Autodesk Fusion 360 voor niet-commercieel gebruik. 
De `*.f3z` bestanden zijn archieven hiervan.

## Suggesties of problemen?
Zet deze in de [Issues](https://github.com/Jeroen6/p1hat/issues) en vragen in [Discussions](https://github.com/Jeroen6/p1hat/discussions).
