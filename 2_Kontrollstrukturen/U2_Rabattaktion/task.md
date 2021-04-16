# 2. Aufgabe: Rabattaktion
Zurück zur Mathemagierin: Sie möchte in ihrem Shop eine Rabattaktion starten, um das Geschäft anzukurbeln. Natürlich hat sie dabei wieder etwas zu programmieren für dich. Du sollst die Berechnung der reduzierten Preise mit einer if-elif-else-Struktur vereinfachen.
Dabei ist zu beachten:
Artikel, die zwischen 0 und 20 (einschließlich) Taler kosten, werden um 20% reduziert; Artikel, die zwischen 20 (nicht einschließlich) und 50 Taler (einschließlich) kosten, werden um 40% reduziert, alle anderen Artikel, also solche die mehr als 50 Taler kosten, werden um 60% reduziert.

## a.) Gebe für die Variable price den neuen, rabattierten Preis aus.

### Korrekte Ausgabe ist `30.0`

---
## b.) Berechne nun für jeden der alten Preise aus der Liste prices die passenden reduzierten Preise und speichere sie in der neuen Liste new_prices, gebe diese Liste schließlich aus.

### Korrekte Ausgabe ist `[1.6, 30.0, 28.0, 18.0]`

---
## c.) Zusatzaufgabe (schwierig!)
Nun überreicht dir die Mathemagierin mit zitternden Händen die Liste chaos, in der neue und alte Preise gemischt sind! Angesichts dieser undurchdachten Arbeit schlägst du dir die Hände vor dem Kopf zusammen, aber es hilft ja nichts: Nur du kannst hier wieder Ordnung schaffen, indem du alles zusammenbringst, was du schon gelernt hast!
Gehe die Elemente in der Liste chaos durch. Bei einem neuen Preis ziehst du bloß den neuen Wert aus dem String und hängst ihn der Liste order an. Bei einem alten Preis hingegen holst du dir den alten Wert, berechnest den neuen Preis und hängst diesen Wert an die Liste order.
Schließlich gibst du die vollständige Liste order aus, in der nur noch neue Preise drinstehen (und nur noch Zahlen!).
Tipp: Mit Hilfe des in - Operators kannst du prüfen, ob old oder new in einem Listenelement vorkommt ("old" in "old price: 123"), und entsprechend entscheiden, ob du die Rabatierung durchführen möchtest oder nicht.


### Korrekte Ausgabe ist `[24.0, 21, 17.4, 30.0, 101]`
