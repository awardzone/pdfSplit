## Descrizione
Legge un file <b><i>pdf</i></b> passato come parametro in ingresso e lo suddivide in file più piccoli. 
L'utente dovrà passare come parametri il file pdf da leggere e il numero di pagine in cui suddividere il file. 
I files che verranno genrati avranno  una progressione numerica e saranno salvati nella cartella <b><i>out/</i></b>

## Prerequisiti

Prima di eseguire lo script, assicurati di aver installato la libreria necessaria tramite terminale:

>  ``pip install pypdf ``

## Come utilizzarlo

Puoi lanciare lo script direttamente dal terminale passando il file di origine e il numero di pagine in cui suddividere il file.

Ad esempio, se hai un file chiamato documento.pdf (magari di 11 pagine) e vuoi dividerlo in blocchi da 5 pagine, scriverai:

>  ``python split_pdf.py documento.pdf 5 ``
