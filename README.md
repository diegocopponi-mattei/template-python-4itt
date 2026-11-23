# Template Python 3 — Guida all'uso con GitHub Codespaces

Benvenuto nel repository template ufficiale per le esercitazioni di Informatica! Questo ambiente di sviluppo è progettato per offrirti una postazione di lavoro completa e standardizzata direttamente nel browser web tramite **GitHub Codespaces**.

Non occorre installare alcun interprete o software sul tuo computer locale: il sistema si avvia in un contenitore cloud preconfigurato con **Python 3.12**, l'estensione ufficiale **Python** per Visual Studio Code e la personalizzazione visiva dell'istituto.

---

## 1. Struttura del Progetto

Il repository presenta una struttura essenziale per lo sviluppo di script e programmi Python in ambiente scolastico. Quando apri il progetto per la prima volta, l'albero dei file si presenta nel modo seguente:

```text
template-python-4itt/
├── .devcontainer/
│   └── devcontainer.json    # Configurazione della macchina virtuale cloud (Python 3.12)
├── .vscode/
│   └── settings.json        # Impostazioni dell'editor minimale e colori dell'istituto
├── main.py                  # Codice sorgente Python da modificare ed estendere
└── .gitignore               # Regole per escludere cache e file temporanei dal controllo versione
```

### Significato dei file e delle cartelle principali

- **File `main.py`:** Contiene il punto di partenza (*entry point*) dell'applicazione Python da completare durante l'esercizio.
- **Cartella `.devcontainer/`:** Contiene la configurazione dell'ambiente Linux cloud e delle estensioni preinstallate su Codespaces.
- **Cartella `.vscode/`:** Custodisce le impostazioni dell'editor, inclusa la disattivazione dei suggerimenti automatici (IntelliSense e IA) e la configurazione dei colori istituzionali.
- **File `.gitignore`:** Impedisce il caricamento su GitHub di cartelle generate automaticamente da Python durante l'esecuzione (come `__pycache__/`).

---

## 2. Passo 1: Creare il proprio Repository personale dal Template

Per iniziare un nuovo esercizio o compito in classe, non devi lavorare direttamente su questo repository di partenza, ma devi crearne una tua copia personale.

> **Avviso Importante:** Non utilizzare il pulsante **Fork**. Il comando Fork crea un collegamento pubblico visibile a tutta la classe. Utilizza esclusivamente la procedura descritta di seguito.

### Procedura passo-passo

1. Assicurati di aver effettuato l'accesso a GitHub con il tuo account personale.
2. Nella pagina principale di questo repository template, individua in alto a destra il pulsante verde **Use this template** e seleziona la voce **Create a new repository**.
3. Nella schermata di configurazione del nuovo repository:
   - **Owner:** Verifica che sia selezionato il tuo nome utente personale.
   - **Repository name:** Inserisci il nome dell'esercitazione seguendo la convenzione indicata dal docente (ad esempio `es01-calcolatrice` oppure `es02-gestione-registro`).
   - **Visibility:** Seleziona **Private** (obbligatorio, affinché il codice non sia visibile agli altri studenti).
   - **Include all branches:** Lascia la casella deselezionata.
4. Fai clic sul pulsante verde **Create repository** in fondo alla pagina.

Dopo pochi secondi, GitHub creerà la tua copia riservata del progetto con l'intera struttura pronta all'uso.

---

## 3. Passo 2: Avviare l'Ambiente di Sviluppo (Codespaces)

Una volta creato il tuo repository privato, puoi avviare il computer virtuale nel cloud su cui eseguirai il codice.

1. All'interno del tuo nuovo repository privato, fai clic sul pulsante verde **<> Code** in alto a destra.
2. Seleziona la scheda **Codespaces** (accanto alla scheda *Local*).
3. Fai clic sul pulsante **Create codespace on main**.

Si aprirà una nuova scheda nel browser web con l'interfaccia di Visual Studio Code.

> **Nota sul primo avvio:** La prima volta che avvii un Codespace su un nuovo repository, il sistema impiega circa 30–60 secondi per scaricare l'immagine Linux, preparare Python 3.12 e configurare l'ambiente. Gli avvii successivi saranno molto più rapidi.

Al termine del caricamento, noterai che la barra superiore e inferiore dell'editor assumono la colorazione blu ufficiale dell'istituto.

---

## 4. Passo 3: Scrittura ed Esecuzione del Codice

### Il file di partenza (`main.py`)

Nella cartella principale troverai il file `main.py`, già strutturato con le buone pratiche di programmazione apprese a lezione:

- Presenta la **docstring di modulo** iniziale con la descrizione del programma e i segnaposto per **Autore** e **Data** (da compilare sempre).
- Include la funzione di utilità `stampa_intestazione(titolo: str) -> None` con **type hinting** e **docstring** per l'output incorniciato a terminale.
- Definisce la funzione `main() -> None` e il blocco standard di avvio `if __name__ == "__main__":`.

### Regole per il salvataggio e l'esecuzione

Per mantenere un ambiente di apprendimento pulito e favorire la lettura autonoma del codice e dei messaggi di errore:

1. **Autocompletamento e IA disattivati:** I suggerimenti automatici durante la digitazione sono disabilitati. Scrivi il codice con attenzione controllando sintassi e indentazione.
2. **Salvataggio del file:** Prima di eseguire lo script, salva sempre le modifiche premendo **Ctrl + S** (o **Cmd + S** su macOS). Un pallino bianco accanto al nome del file `main.py` indica che ci sono modifiche non ancora salvate.
3. **Esecuzione del programma:** Per avviare lo script, fai clic sull'icona **Play** (▷) situata in alto a destra nell'editor, oppure apri il **Terminal** in basso e digita:
   ```bash
   python main.py
   ```
4. **Input da Terminale:** Quando il programma richiede di inserire dati da tastiera tramite la funzione `input()`, fai clic nel riquadro del **Terminal** in basso e digita la risposta seguita da **Invio**.

---

## 5. Passo 4: Salvataggio delle Modifiche (Git) e Consegna

A fine lezione o al completamento dell'esercizio, devi salvare il tuo lavoro sul repository remoto di GitHub e consegnarlo al docente.

### 1. Eseguire Commit e Sync dei sorgenti

1. Fai clic sull'icona **Source Control** nella barra laterale sinistra di VS Code (l'icona raffigurante un ramo Git con un numerino).
2. Nel campo di testo in alto (*Message*), scrivi un breve messaggio che descriva il lavoro svolto (ad esempio `"Completato esercizio 01"`).
3. Fai clic sul pulsante blu **Commit**.
4. Fai clic sul pulsante **Sync Changes** (oppure *Publish Branch*) per inviare le modifiche su GitHub.

### 2. Aggiungere il docente come Collaboratore

Poiché il tuo repository è impostato su **Private**, il docente non potrà vedere il tuo codice se non gli fornisci l'accesso.

1. Apri la pagina del tuo repository su GitHub nel browser.
2. Vai nella scheda **Settings** nella barra del repository.
3. Nel menu laterale sinistro, seleziona **Collaborators** (sotto la voce *Access*).
4. Fai clic su **Add people**.
5. Inserisci il nome utente GitHub del docente e conferma l'invio dell'invito.

### 3. Consegna su Google Classroom

1. Copia l'indirizzo URL della pagina principale del tuo repository.
2. Apri la scheda del compito su **Google Classroom**.
3. Fai clic su **Aggiungi o crea** -> **Link**.
4. Incolla l'URL del tuo repository e fai clic su **Contrassegna come inviato** o **Consegna**.

---

## 6. Passo 5: Gestione della Quota Gratuita e Pulizia (Delete vs Stop)

Ogni account GitHub gratuito include mensilmente:
- **60 ore di calcolo** (pari a 120 core-hours su macchine standard a 2 core).
- **15 GB di spazio di archiviazione (Storage)** per salvare gli ambienti di lavoro.

Per evitare di esaurire le risorse gratuite prima della fine del mese, è fondamentale seguire una corretta gestione delle macchine virtuali.

### Configurazione consigliata dei timer sul proprio account GitHub

Fai questa configurazione una sola volta dal tuo profilo GitHub:

1. Fai clic sulla tua foto profilo in alto a destra su GitHub e seleziona **Settings**.
2. Nel menu laterale sinistro, fai clic su **Codespaces** (sotto la voce *Code, planning, and automation*).
3. Imposta le seguenti opzioni:
   - **Default idle timeout:** Imposta a **15** o **30 minutes**. Se lasci il browser aperto o chiudi la scheda senza spegnere la macchina, il consumo delle ore si ferma automaticamente dopo questo intervallo.
   - **Default retention period:** Imposta a **1 day** o **7 days**. I Codespace inattivi verranno eliminati automaticamente dopo il periodo indicato.
4. Fai clic su **Save**.

### Quando fare STOP e quando fare DELETE

| Azione | Quando usarla | Cosa comporta |
| :--- | :--- | :--- |
| **Stop (Sospensione)** | Quando fai una pausa breve durante la giornata e devi riprendere lo stesso esercizio più tardi. | Ferma il consumo delle 60 ore di calcolo, ma mantiene occupata la quota di 15 GB di archiviazione. |
| **Delete (Eliminazione)** | **Sempre a esercizio concluso**, dopo aver completato la procedura di *Commit & Sync*. | Elimina il contenitore temporaneo, liberando al 100% sia le ore di calcolo sia lo spazio su disco. Il codice rimane al sicuro nel repository. |

> **Nota:** Per eliminare un Codespace a lavoro finito, vai alla pagina di gestione dei Codespaces su GitHub (`github.com/codespaces`), fai clic sui tre puntini (`...`) accanto al nome dell'ambiente concluso e seleziona **Delete**.

---

## 7. Domande Frequenti e Risoluzione Problemi

### Il pulsante Play (▷) in alto a destra non compare o non avvia il file
- **Causa:** L'estensione Python sta ancora completando l'inizializzazione iniziale oppure il file attivo non ha estensione `.py`.
- **Soluzione:** Attendi 10–15 secondi e verifica che in basso a destra nella barra blu compaia la scritta `Python 3.12`. In alternativa, puoi sempre avviare lo script dal terminale digitando `python main.py`.

### Errore `FileNotFoundError` quando apro un file di testo o CSV
- **Causa:** Il file dati non si trova nella stessa cartella dello script Python oppure il nome contiene errori di maiuscole/minuscole (su Linux i nomi dei file sono *case-sensitive*).
- **Soluzione:** Controlla nell'Esplora Risorse a sinistra che il file sia nella cartella principale accanto a `main.py` e verifica l'esatta ortografia del nome.

### Errore durante il Push o la sincronizzazione
- **Causa:** Mancata esecuzione del Commit prima del Sync oppure conflitto di sessione.
- **Soluzione:** Assicurati che l'operazione di **Commit** sia stata completata prima di premere **Sync Changes**. In alternativa, dal terminale integrato puoi eseguire `git push origin main`.
