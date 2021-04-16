# Aufgabe 2: Zersägte E-Mail-Adressen
Die Mathemagierin ist sehr zufrieden mit deiner Arbeit und bittet dich um Hilfe bei der Betreuung von ihrem Online-Shop. Sie kennt nur die Mailadressen ihrer Kunden und du sollst anhand der Mailadressen ein vereinfachtes Verzeichnis mit ihren Namen anlegen.

## a. ) Ziehe einen Namen aus einer Mailadresse der Form name@service.com
Wenn die Mailadresse Max-Mustermann@gmail.com lautet, sollst du Max-Mustermann ausgeben, wenn die Mailadresse KlaraKlarnamen@uni-berlin.de heisst, sollst du KlaraKlarnamen ausgeben.
Hinweis: Schau dir dazu auf jeden Fall nochmal die .split() - Methode an. Damit kannst du z.B. eine E-Mail-Adresse am @ - Symbol zersägen / zerlegen.

### Korrekte Ausgabe ist `willy.wizard`

---
## b.) Ziehe einen Namen aus einer Mailadresse der Form info@name.com
Manchmal stehen die Namen bei einer Mailadresse auch erst hinter dem @-Zeichen. Gebe auch für solche Fälle die Namen aus; entferne dabei die Endung .com bzw. .de. Du darfst dazu voraussetzen, dass innerhalb des Namens kein Punkt vorkommt. Wenn die Mailadresse also info@Max-Mustermann.com lautet, sollst du Max-Mustermann ausgeben.
Hinweis: Es ist okay, wenn du für die Berechnung mehere .split() - Befehle benötigst, oder ein Ergebnis zwischenspeichern möchtest. Gerne kannst du auch den Code aus der Teilaufgabe a) hier mitverwenden.


### Korrekte Ausgabe ist `helena-hexe`

---
## c.) Berechne: Wie viele Kunden gibt es im Online-Shop?
Aktuell legen alle Kunden (mail1, mail2, mail3) als separate Variable vor. Wir möchten daraus jetzt eine Liste bauen, sodass wir die Möglichkeit hätten, später noch weitere Kunden in diese Liste hinzuzufügen.
Überführe deswegen die Kunden mail1, mail2 und mail3 in die Liste clients, und lasse dir anschließend die Anzahl der Elemente der Liste clients mit Hilfe von Python ausgeben.

### Korrekte Ausgabe ist `['zarah.zauber@zauberberg.de', 'info@trixie-trickser.com', 'uwe_unhold@dunkelnetz.de']`
### Korrekte Ausgabe ist `3`

---
## d.) Eine Mailadresse aus Strings zusammenbauen
Plötzlich fällt der Mathemagierin ein, dass in der Liste clients noch ihr wichtigster Onlineshop-Kunde fehlt. Die Infos zu ihm wurden bei einem misslungenen Trick in zwei Teile zersägt und liegen seitdem in der Liste ["Buehnenzauberer", "magic.com"] herum.
Rekonstruiere mit Hilfe von Python die Mailadresse des Kunden (da fehlt ein @ zwischen "Buehnenzauberer" und "magic.com") und gebe sie aus, damit sich der Onlineshop-Kundendienst nach seinem Wohlbefinden erkundigen kann.

### Korrekte Ausgabe ist `Buehnenzauberer@magic.com`
