# 1.) Ein automatisierter Trick

## a.)
Eine Mathemagierin bittet dich darum einen ihrer Tricks durch ein kleines Programm zu automatisieren. Der Trick beginnt wie folgt:

1. Denke dir eine Zahl aus (Variable `number`)
2. Multipliziere sie mit 2
3. Addiere 10 zum Ergebnis
4. Teile das Ergebnis durch 2

Führe diese Rechnung  für die Variable _number_ durch und gebe das Ergebnis aus.

### Korrekte Ausgabe ist `11.0`

---
---

## b.)
Als sie das sieht, rümpft die Mathemagierin die Nase: Das Ergebnis wird nämlich noch als Kommazahl angezeigt.
Wandle das Ergebnis in eine Ganzzahl um, bevor du es ausgibst.


### Korrekte Ausgabe ist `11`
---
---

## c.)
Die Mathemagierin weißt noch darauf hin, dass es bei Zaubertricks auch auf die Präsentation ankommt. Gebe nun einen Antwortsatz der Form
"Du hast 6 ausgewählt, das magische Ergebnis ist 11!"
aus, wobei für die Zahl 6 die Variable number und für die Zahl 11 das Ergebnis (Variable result) eingesetzt werden soll.
Hinweis: In Python darf ein print - Befehl wie folgt über mehrere Zeilen gehen. Das könnte praktisch sein, gerade wenn du viele Strings hintereinander hängen möchtest:

```python
print("Hallo" +
      "Welt")
```

### Korrekte Ausgabe ist `Du hast 6 ausgewählt, das magische Ergebnis ist 11!`
