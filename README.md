# EC2-Autoscaling-and-SQS

### 1. Creazione della coda SQS

Attraverso la AWS Management Console, è stato inizializzato il processo creando una coda SQS.

### 2. Configurazione della Launch Template

Successivamente, è stata configurata una Launch Template contenente le specifiche necessarie per le istanze EC2, inclusa  user data.

### 3. Creazione dell'Auto Scaling Group

Utilizzando la AWS Management Console, è stato creato un Auto Scaling Group, associato al Launch Template precedentemente configurato, per garantire la gestione dinamica delle istanze EC2.

### 4. Configurazione dell'Auto Scaling Policy

L'Auto Scaling Group è stato configurato con una policy di Auto Scaling che definisce le regole per la crescita dinamica del numero di istanze in base al carico di lavoro.

### 5. Creazione dell'Allarme CloudWatch e SNS Topic

È stato creato un allarme CloudWatch basato su metriche specifiche. Inoltre, è stato creato un SNS topic e configurato nell'allarme CloudWatch. Questo allarme è stato utilizzato per l'aggiunta di nuove istanze EC2 quando c'è un messaggio visibile nella coda SQS.

### 6. Configurazione Coda SQS

Infine, è stato configurato un processo all'interno delle istanze EC2  nel user data per leggere e processare i messaggi, eliminandoli in modo sicuro.

## Risultati dei Test

I test sono stati condotti per verificare l'efficacia del sistema nelle seguenti fasi:

- **Crescita dinamica:** Il sistema è stato in grado di aggiungere nuove istanze automaticamente in risposta al aumento della coda SQS

- **Decrescita dinamica:** Le istanze non necessarie sono state terminate automaticamente quando il carico di lavoro è diminuito.

- **Gestione dei Messaggi:** Il processo di consumo della coda SQS ha funzionato correttamente nel leggere e processare i messaggi, garantendo l'eliminazione sicura dopo l'elaborazione.

## Conclusioni

La configurazione del sistema tramite la AWS Management Console ha dimostrato di essere efficace nel gestire dinamicamente le risorse in base al carico di lavoro.
