# Sales Analytics Data Warehouse

## Ziel

Entwicklung einer Analytics-Lösung zur Analyse von Umsatz-, Gewinn- und Vertriebskennzahlen.

## Technologien

- PostgreSQL
- SQL
- Python
- Pandas
- Power BI
- Git
- GitHub

# Architekturentscheidung: Star Schema

## Warum ein Star Schema?

Für dieses Projekt wurde das Data Warehouse als **Star Schema** modelliert. Das Star Schema ist eines der am häufigsten eingesetzten Datenmodelle im Bereich Business Intelligence und Data Analytics, da es speziell für analytische Abfragen optimiert ist.

Im Mittelpunkt steht eine **Faktentabelle**, welche die messbaren Geschäftsvorfälle (Facts) enthält. Diese wird von mehreren **Dimensionstabellen** umgeben, die die Fakten aus unterschiedlichen Blickwinkeln beschreiben, beispielsweise Kunde, Produkt, Mitarbeiter oder Datum.

## Vorteile des Star Schemas

Die Entscheidung für ein Star Schema wurde aus folgenden Gründen getroffen:

* **Einfache Verständlichkeit:** Das Datenmodell ist übersichtlich aufgebaut und kann sowohl von Entwicklern als auch von Fachbereichen leicht nachvollzogen werden.
* **Hohe Performance:** Analytische Abfragen benötigen in der Regel nur wenige JOIN-Operationen und lassen sich effizient ausführen.
* **Optimiert für BI-Tools:** Werkzeuge wie Power BI, Tableau oder Amazon QuickSight arbeiten besonders effizient mit Sternschemas.
* **Flexible Analysen:** Kennzahlen können nach unterschiedlichen Dimensionen ausgewertet werden, beispielsweise nach Zeitraum, Produkt, Kunde oder Vertriebsmitarbeiter.
* **Erweiterbarkeit:** Neue Dimensionen oder Kennzahlen können später ergänzt werden, ohne das bestehende Modell grundlegend zu verändern.

## Geschäftsprozess

Das Data Warehouse bildet den Geschäftsprozess **Sales** ab. Jede Zeile der Faktentabelle repräsentiert eine einzelne Verkaufsposition und enthält die zugehörigen Kennzahlen wie Umsatz, Menge, Rabatt und Gewinn.

## Geplantes Datenmodell

Das Star Schema besteht aus einer zentralen Faktentabelle und mehreren Dimensionstabellen.

**Faktentabelle**

* FactSales

**Dimensionstabellen**

* DimCustomer
* DimProduct
* DimEmployee
* DimDate

Die Region wird in diesem Projekt als Attribut des Kunden modelliert und daher nicht als eigenständige Dimension geführt. Dadurch bleibt das Datenmodell kompakt und entspricht einer typischen Modellierung für analytische Fragestellungen.

## Ziel des Data Warehouses

Das Data Warehouse dient als zentrale Grundlage für alle weiteren Analysen. Es ermöglicht unter anderem die Beantwortung folgender Fragestellungen:

* Wie entwickeln sich Umsatz und Gewinn über die Zeit?
* Welche Kunden und Branchen sind besonders profitabel?
* Welche Produkte erzielen die höchsten Margen?
* Wie unterscheiden sich Vertriebsmitarbeiter hinsichtlich ihrer Performance?
* Welche Trends lassen sich im Zeitverlauf erkennen?

Auf Basis dieses Datenmodells werden im weiteren Projektverlauf SQL-Abfragen, Python-Analysen sowie ein interaktives Power-BI-Dashboard entwickelt.
