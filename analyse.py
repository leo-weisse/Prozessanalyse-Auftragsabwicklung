import sqlite3
import csv
import matplotlib.pyplot as plt

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DB = "data/northwind.db"
def lade_sql(dateiname):
    pfad = "sql/" + dateiname 
    with open(pfad,"r", encoding ="utf-8") as f:
      return f.read()
    


def abfrage(verbindung, dateiname):                                     #Stellt verbindung zu Dateien da 
    sql_text = lade_sql(dateiname)
    ergebnis = verbindung.execute(sql_text)
    zeilen = ergebnis.fetchall()
    spalten = [eintrag[0] for eintrag in ergebnis.description ]
    return spalten, zeilen
    


def speichere_csv(dateiname, spalten, zeilen):
    pfad = "output/" + dateiname                       
    with open(pfad, "w", newline="", encoding="utf-8") as f:   
        schreiber = csv.writer(f, delimiter=";")            #erstellt die csv Dateien
        schreiber.writerow(spalten)                  
        schreiber.writerows(zeilen)                    
def diagramm_versender(zeilen):
    namen = [zeile[0] for zeile in zeilen]
    werte = [zeile[1] for zeile in zeilen]         

    plt.figure(figsize=(7, 4))
    balken = plt.bar(namen, werte)                        
    plt.bar_label(balken, fmt="%.1f %%")
    plt.title("Verspätungsquote je Versanddienstleister")                                   
    plt.ylabel("Verspätete Lieferungen in %")       
    plt.ylim(0,30)    
    plt.savefig("output/verspaetung_versender.png", dpi=150, bbox_inches="tight")
    plt.close()    
def diagramm_pareto(zeilen):
    umsaetze = [zeile[1] for zeile in zeilen]
    gesamt = sum(umsaetze)

    kumuliert = []
    laufend = 0
    for umsatz in umsaetze:
        laufend = laufend + umsatz                    
        kumuliert.append((laufend/gesamt)*100)             

    kunden = range(1, len(umsaetze) + 1)
    kunde_80 = 0
    for nummer, wert in zip(kunden, kumuliert):
        if  wert>= 80:                      
            kunde_80 = nummer
            break
    print("80 % des Umsatzes bei Kunde", kunde_80, "von", len(umsaetze))
    plt.figure(figsize=(7, 4))
    plt.plot(kunden, kumuliert)
    plt.axhline(80, linestyle="--", color="gray")
    plt.axvline(kunde_80, linestyle=":", color="gray")
    plt.title("Kumulierter Umsatzanteil je Kunde")                         
    plt.xlabel("Kunden, nach Umsatz absteigend sortiert")
    plt.ylabel("Kumulierter Umsatzanteil in %")
    plt.ylim(0, 100)
    plt.savefig("output/pareto_umsatz.png", dpi=150, bbox_inches="tight")
    plt.close() 
def main():                                                 #Fehler melden 
    try:
        verbindung = sqlite3.connect(DB)
    except sqlite3.Error as fehler:
        print("Datenbank konnte nicht geöffnet werden:", fehler)
        return

    dateien = ["Verspaetung_pro_Country.sql", "04_mitarbeiter.sql","Verspaetung_pro_Company.sql", "Umsatz_pro_Company.sql", "durchlaufzeit.sql", "05_offen.sql", "export_bestellungen.sql","lieferzusage.sql"]                     
    for dateiname in dateien:                               #Liest die SQL Dateien durch 
        spalten, zeilen = abfrage(verbindung, dateiname)         
        csv_name = dateiname.replace(".sql", ".csv")
        speichere_csv(csv_name, spalten, zeilen)                      
        print(dateiname, len(zeilen), "Zeilen")
    spalten, zeilen = abfrage(verbindung, "Verspaetung_pro_Company.sql")
    diagramm_versender(zeilen)
    spalten, zeilen = abfrage(verbindung, "Umsatz_pro_Company.sql")
    diagramm_pareto(zeilen)
    verbindung.close()
if __name__ == "__main__":
    main()
