# Prozessanalyse Auftragsabwicklung (A3 / PDCA)

Analyse von rund 16.000 Bestellungen mit SQL, Python und Excel, aufgebaut als A3-Report im PDCA-Zyklus.

**Ergebnis:** Hauptursache für 23 % verspätete Bestellungen sind zu knapp zugesagte Liefertermine, nicht Versender oder Mitarbeiter. Ziel: Termintreue von 77 % auf 90 % steigern.

## 1. Problem
Rund 23 % aller Bestellungen kommen zu spät. Die Termintreue liegt damit bei nur 77 %.

## 2. Ist-Zustand
- Definition: Eine Bestellung gilt als verspätet, wenn sie nach dem zugesagten Liefertermin versendet wird.
- 16.261 Bestellungen wurden versendet, 21 noch offene Bestellungen sind ausgeschlossen.
- Die durchschnittliche Durchlaufzeit von der Bestellung bis zum Versand liegt bei 7,8 Tagen, bei einer Streuung von 0 bis über 30 Tagen.
- Die Verspätungsquote je Versanddienstleister liegt zwischen 22,9 % und 23,3 %.
- Der Umsatz ist breit verteilt: 80 % des Umsatzes entfallen auf 73 von 93 Kunden, der größte Kunde hat einen Anteil von nur 1,4 %.

![Verspätungsquote je Versanddienstleister](output/verspaetung_versender.png)
![Kumulierter Umsatzanteil je Kunde](output/pareto_umsatz.png)

## 3. Ursachenanalyse (Ishikawa)
- **Mensch:** ausgeschlossen, die Bearbeitung ist bei allen Mitarbeitern nahezu gleich schnell (7,6 bis 8,0 Tage Durchlaufzeit).
- **Dienstleister:** ausgeschlossen, die drei Versender liegen nahezu gleichauf (22,9 bis 23,3 %).
- **Kunde:** Kein Großkunde dominiert (größter Umsatzanteil 1,4 %), einzelne Kunden scheiden als Treiber aus. Offen bleibt, ob die kurzen Zusagen auf Kundenwünsche zurückgehen. Das wäre im nächsten Schritt mit dem Vertrieb zu klären.
- **Methode (Hauptursache):** Verspätete Aufträge hatten im Schnitt nur 6,7 Tage zugesagte Lieferzeit, pünktliche dagegen 22,8 Tage. Bei einer durchschnittlichen Durchlaufzeit von 7,8 Tagen ist eine Zusage unter 7 Tagen unrealistisch.

## 4. Maßnahmen (Do)
- Liefertermine nur noch mit realistischem Vorlauf zusagen, mindestens 10 Tage.
- Aufträge mit kürzerer Zusage als Eilaufträge kennzeichnen und gesondert einplanen.

## 5. Wirkungsmessung (Check-Plan)
Da keine Daten nach Umsetzung der Maßnahmen vorliegen, ist dies ein Messplan:
- Kennzahl: Termintreue, Ausgangswert 77 %.
- Ziel: 90 %. Aufträge mit mindestens 10 Tagen zugesagter Lieferzeit erreichen im Datensatz bereits 92 %.
- Wöchentliche Messung mit den bestehenden SQL-Abfragen, getrennt nach zugesagter Lieferzeit.

## 6. Standardisierung (Act)
- Mindestvorlauf von 10 Tagen als Standard in der Auftragsannahme festschreiben.
- Termintreue als feste Wochenkennzahl verfolgen, Abweichungen mit der 5-Why-Methode klären.

## Daten und Methode
- Daten: Northwind-Beispieldatenbank (synthetische Übungsdaten, SQLite), Quelle: github.com/jpwhite3/northwind-SQLite3. Die Datenbank ist nicht im Repository enthalten.
- 8 SQL-Abfragen im Ordner `sql/`, ausgeführt mit `analyse.py` (Python: sqlite3, csv, matplotlib).
- Ergebnisse als CSV-Dateien und Diagramme im Ordner `output/`, Pivot-Auswertung nach Land und Versender in Excel.
- Kunden werden über die Kundennummer gruppiert, da ein Firmenname in den Daten doppelt vorkommt.

## Ausführen
1. `northwind.db` von der oben genannten Quelle herunterladen und in den Ordner `data/` legen.
2. `python analyse.py` ausführen. CSV-Dateien und Diagramme landen in `output/`.
