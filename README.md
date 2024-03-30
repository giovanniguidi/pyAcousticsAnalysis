### Algoritmi di analisi acustiche per Python

Questo tool fornisce alcuni algoritmi a supporto dell'analisi di misure fonometriche ambientali e edili.
Al momento l'import dei dati è possibile solo sui fonometri Larson & Davis, tramite il software G4 
(https://www.larsondavis.com/Products/software/g4-ld-utility-software). Scaricare i dati in formato 
excel tramite G4 per poterli importare nel tool.

E' possibile utilizzare gli algoritmi di analisi tramite jupyter notebook, che fornisce l'interattività necesssaria a
effettuare alcune operazioni (es. mascheramenti, tagli), vedi la cartella "notebooks". 
In "report_examples" sono presenti alcuni report di esempio.

### Installazione
Il tool è testato su python 3.12.2.
Creare un virtual env traimte conda o venv, poi installare i requirements:
```
pip install -r requirements.txt 
```

### Funzionalità

Alcune funzionalità previste sono ancora in fase di dev o test:

- [x] mascheramenti
- [x] plot vari (SPL, time history, spettro minimi)
- [x] calcoli percentili
- [x] calcoli Leq mascherato e non mascherato
- [x] ricerca componenti tonali e impulsive
- [x] creazione di report in pdf (tramite pdflatex)
- [ ] calcolo T60
- [ ] creazione report requisiti acustici passivi
- [ ] sonogrammi
 

### Referenze

\[1\] [LEGGE 26 ottobre 1995, n. 447 "Legge quadro sull'inquinamento acustico"](https://www.gazzettaufficiale.it/eli/id/1995/10/30/095G0477/sg)


\[2\] [DPCM 14-11-1997 "Determinazione dei valori limite delle sorgenti sonore"](https://www.gazzettaufficiale.it/eli/id/1997/12/01/097A9602/sg)

\[3\] [DM 16 marzo 1998 "Tecniche di rilevamento e di misurazione dell'inquinamento acustico"](https://www.gazzettaufficiale.it/eli/id/1998/04/01/098A2679/sg)
