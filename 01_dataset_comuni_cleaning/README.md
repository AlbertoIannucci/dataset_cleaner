# DatasetCleaner 📊🧹

Uno script Python per ripulire automaticamente dataset in formato CSV, utile per analisi statistiche, reportistica o machine learning.

## ⚙️ Funzionalità

- Rimozione di colonne completamente vuote
- Eliminazione automatica di variabili con meno di 2 valori univoci
- Caricamento dati e salvataggio del nuovo dataset ripulito
- Rimappatura dei nomi di alcune colonne
- Conversione dei tipi di alcune colonne
- Sostituzione separatore nel dataset
- Estendibile tramite una superclasse astratta con metodi di analisi

## 🧱 Architettura

La classe `DatasetCleaner` eredita da `ModelloBase`, una superclasse astratta che contiene metodi generici per analizzare dataset pandas (es. distribuzioni, valori univoci, tipologie).
