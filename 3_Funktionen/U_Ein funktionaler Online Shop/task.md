# Ein funktionaler Online-Shop
Die Mathemagierin will ihren Online-Shop auf Funktionen umrüsten. Es wartet also wieder einiges an Arbeit auf dich.

## a.) Schreibe eine Funktion, die den Gesamtpreis der Produkte im Warenkorb berechnet.
Vervollständige die Funktion list_sum(), der als Parameter eine Liste mit den Preisen übergeben wird. Die Funktion soll dann die Summe der Zahlen aus der Liste ausgeben.

### Korrekte Ausgabe ist `63.95`

---

## b.) Schreibe eine Funktion, die für einen Artikel eine Preis-Tabelle erstellt.
Nun wünscht sich die Mathmagierin eine Funktion, der sie einen Artikelnamen und den Verkaufspreis übergeben kann. Daraus soll die Funktion eine Liste erstellen, in der die Preise von einem, zwei, drei,... bis zehn Einheiten des Artikels stehen. Genauer soll jedes Element in der Liste so aussehen: "Anzahl x Artikel: Preis".
Du wunderst dich nur kurz über die Ansprüche der Mathemagierin.


### Korrekte Ausgabe ist `['1 x Wunderkeks: 0.79', '2 x Wunderkeks: 1.58', '3 x Wunderkeks: 2.37', '4 x Wunderkeks: 3.16', '5 x Wunderkeks: 3.95', '6 x Wunderkeks: 4.74', '7 x Wunderkeks: 5.53', '8 x Wunderkeks: 6.32', '9 x Wunderkeks: 7.11', '10 x Wunderkeks: 7.9']`

---
## c.) Schreibe eine Funktion, die die Listen mit den Artikeln auffüllt.
Von nun an soll auch eine Funktion die Waren in die virtuellen Regale einräumen, d.h. an die erste noch leere Position in der Liste shelf packen. Als Parameter soll der Funktion shelve() der einzusortierende Artikel übergeben werden. Die Funktion aktualisiert dann die Liste shelf, und der neue Artikel wurde in das erste leere Regalfach eingeräumt.


### Korrekte Ausgabe ist `['Zaubersäge', "Rubik's Cube", 'Wunderkekse', 'Trickkarten', 'leer']`
