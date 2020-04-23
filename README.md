# Dashboardentwicklung mit Dash von Plotly

Das Repository enthält alle Dateien zu dem zugehörigen Artikel im Entwicklermagazin.

`original_data` beinhaltet die unbereinigten Daten von https://github.com/CSSEGISandData/COVID-19/ und https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html
Alle daten sind heruntergeladen, um einen einheitlichen Stand zu haben.

`notebooks` beinhaltet die Juypter Notebooks mit denen die Datenbereinigung entwickelt wurde.

`data` beinhaltet die bereinnigten Daten zur Verwendung im Dashboard

`dashboard` Die Dash-Applikation für die Darstellung des Dashboards.

`scripts` Ein Skript, das die Daten bereinigt und speichert. Im wesentlichen eine zusammenfassung der Notebooks.

Die benötigten Module für Python sind in `requirements.txt` zu finden.

## Verwendung
Installation der Module mit Anaconda:

```bash 
$ conda env create -f environment.yml
```

Anschließend kann das Dashboard gestartet werden.

```bash
$ cd dashboard
$ python app.py
```

### Daten bereinigen
Das Skript `clean_and_save.py` bereinigt alle vorliegenden Daten im Verzeichnis `original_data`. Ausführen mit:

```bash
$ cd scripts
$ python clean_and_save.py
```

Fragen? Einfach als Issue hier stellen oder gerne per Twitter an [@casarock](https://twitter.com/casarock)
