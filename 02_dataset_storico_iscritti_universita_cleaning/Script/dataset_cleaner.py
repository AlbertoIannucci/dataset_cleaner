from modello_base import ModelloBase
import pandas as pd

class DatasetCleaner(ModelloBase):

    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path, sep= ";")
        self.dataframe_sistemato = self.sistemazione()

    # Metodo di sistemazione del dataframe
    def sistemazione(self):
        # Copia del dataframe
        df_sistemato = self.dataframe.copy()
        # Drop variabili nulle
        df_sistemato = df_sistemato.dropna(axis= 1, how= "all")
        # Divisione dataframe
        colonne_da_sistemare = df_sistemato.drop(["AnnoA", "AteneoNOME", "AteneoCOD", "SESSO", "Isc"], axis=1)
        #Passo 6. Imposto la riga 72 come intestazione
        nuova_header = colonne_da_sistemare.iloc[71]  # La riga 72 ha indice 71
        df_colonne_sistemate = colonne_da_sistemare.iloc[72:].copy()  # Usa la parte successiva del dataframe
        df_colonne_sistemate.columns = nuova_header  # Imposta le intestazioni corrette
        df_colonne_sistemate.reset_index(drop=True)
        # Seleziono le colonne da mantenere
        colonne_da_mantenere = ["AnnoA", "AteneoNOME", "AteneoCOD", "SESSO", "Isc"]
        df_selezionato = df_sistemato[colonne_da_mantenere]
        # Concateno i due dataframe
        df_sistemato = pd.concat([df_selezionato, df_colonne_sistemate], axis=1)
        # Drop variabili ridondanti
        df_sistemato = df_sistemato[["AnnoA", "AteneoNOME", "AteneoCOD", "SESSO", "Isc"]]
        # Drop valori nan
        df_sistemato = df_sistemato.dropna()
        # Rimappatura variabili
        df_sistemato = df_sistemato.rename(columns={
            "AnnoA":"anno_accademico",
            "AteneoNOME":"nome_ateneo",
            "AteneoCOD":"codice_ateneo",
            "SESSO":"sesso",
            "Isc":"numero_iscritti"
        })

        # Conversione valornumero_iscritti
        df_sistemato["numero_iscritti"] = df_sistemato["numero_iscritti"].astype(int)
        # Rimozione .0 da codice_ateneo
        df_sistemato["codice_ateneo"] = df_sistemato["codice_ateneo"].astype(float).astype(int).astype(str)


        return df_sistemato

    def confronto_valori_univoci(self):
        df_sistemato = self.dataframe_sistemato.dropna()  # Rimuovo righe con NaN, se necessario
        # Conversioni valori di ogni colonna
        # ...
        # Ottieni i valori univoci per ogni colonna
        univoci = {col: df_sistemato[col].dropna().unique() for col in df_sistemato.columns}

        # Confronto solo i valori univoci di ciascuna coppia di colonne
        for col1 in df_sistemato.columns:
            for col2 in df_sistemato.columns:
                if col1 != col2:  # Evita di confrontare la colonna con se stessa
                    if set(univoci[col1]) == set(univoci[col2]):
                        print(f"Le colonne '{col1}' e '{col2}' hanno gli stessi valori univoci.")


modello = DatasetCleaner("../Dataset/dataset.csv")
# Passo 1. Analisi generali del dataset
#modello.analisi_generali(modello.dataframe)
# Informazioni separate da ';'
# Passo 2. Apertura personalizzata del dataset
# Passo 3. Aanalisi generali del dataset
#modello.analisi_generali(modello.dataframe)
# Risultati:
# Osservazioni: 4242; Variabili: 11 (Variabili nulle); Tipi: object, int64 e float64; Valori nan: presenti
# Passo 4. Drop variabi nulle
# Passo 5. Analisi generali e dei valori univoci del nuovo dataset
#modello.analisi_generali(modello.dataframe_sistemato)
#modello.analisi_valori_univoci(modello.dataframe_sistemato)
# Attraverso l'analisi dei valori univoci è emerso che dalla Unnamed: 6 alla Unnamed: 10 le intestazioni
# sono slittate di un record
# Passo 6. Strategia risoluzione:
# Passo 6.1. Divido i dataframe in due nuovi dataframe
# Passo 6.2. Analisi generali del dataframe da sistemare
#modello.analisi_generali(modello.dataframe_da_sistemare)
# Passo 6.3. Ricerca delle intestazioni
#print(modello.dataframe_da_sistemare.head(100).to_string())
# Intestazioni: riga 72
# Passo 6.4. Imposto la riga 72 come intestazione
# Passo 6.5. Selezione le colonne che voglio mantenere
# Passo 6.6. Concateno i due sotto dataframe
# Passo 7. Analisi generali del dataframe sistemato
#modello.analisi_generali(modello.dataframe_sistemato)
# Passo 8. Analisi dei valori univoci
#modello.analisi_valori_univoci(modello.dataframe_sistemato)
# Dubbio che le colonne siano ripetute con intestazioni diverse
# Passo 9. Valuto se le colonne hanno gli stessi valori univoci
#modello.confronto_valori_univoci()
# Dopo la conversione dei valori, le colonne risultano essere ridondati
# Passo 10. Drop colonne ridondanti
modello.analisi_generali(modello.dataframe_sistemato)
# Passo 11. Drop valori nan
# Passo 12. Rimappatura intestazioni
# Passo 13. Conversione valori iscritti da object a int
# Passo 14. Rimozione ".0" da codice_ateneo
# Passo 15. Creazione nuovo csv
modello.dataframe_sistemato.to_csv("../Dataset/dataset_nuovo.csv", index=False)

