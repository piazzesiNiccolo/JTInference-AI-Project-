## Prerequisiti e installazione

Per poter avviare il programma è necessario python 3.6 o superiore.

È stato utilizzato [pgmpy](https://pgmpy.org/) per modellare le distribuzioni di probabilità condizionata

Per scaricare il programma ed installare le dipendenze necessarie aprire il terminale ed eseguire i seguenti comandi:

```bash
$ git clone https://github.com/piazzesiNiccolo/JTInference-AI-Project-.git
$ cd JTInference-AI-Project-/
$ pip3 install -r requirements.txt
```
Al posto di pip può essere utilizzato anche conda:

```bash
$ conda install -c ankurankan pgmpy
```
Per visualizzare le reti e verificare i risultati installare inoltre [Hugin Educational](https://www.hugin.com/index.php/hugin-explorerhugin-educational/).
Le reti utilizzate sono presenti nella cartella samples del path dove è installato hugin, ma sono state incluse per sicurezza anche nella cartella hugin_networks di questo progetto

## Esecuzione
Per eseguire il programma, aprire il terminale nella cartella base del progetto ed eseguire il seguente comando:

```
$ python3 run_examples.py
```



## Riferimenti

L'algoritmo implementato è ripreso da [Introduction to Bayesian Networks ](http://ai.dinfo.unifi.it/teaching/ai19/jtree.7z) di Jensen (password dell'archivio:ai19)



* 
