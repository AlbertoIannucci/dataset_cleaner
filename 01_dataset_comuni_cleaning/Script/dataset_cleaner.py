from modello_base import ModelloBase
import pandas as pd

class DatasetCleaner(ModelloBase):

    def __init__(self, dataset_path):
        self.dataframe = pd.read_csv(dataset_path, sep=";")
        self.dataframe_sistemato = self.sistemazione()

    # Metodo di sistemazione del dataframe
    def sistemazione(self):
        # Copia del dataframe
        df_sistemato = self.dataframe.copy()
        # Drop variabile denominazione_altra
        df_sistemato = df_sistemato.drop(["denominazione_altra"], axis=1)
        # Drop variabile ridondante
        df_sistemato = df_sistemato.drop(["denominazione_ita_altra"], axis=1)
        # Conversione tipo di dato lat, lon e superficie_kmq
        colonne_da_convertire = ["lat", "lon", "superficie_kmq"]
        for col in colonne_da_convertire:
            if col in df_sistemato.columns:
                df_sistemato[col] = df_sistemato[col].str.strip().str.replace(",", ".").astype(float)
        # Drop valori nan
        df_sistemato = df_sistemato.dropna()
        # Rinonimo variabili lat e lon
        df_sistemato.rename(columns={"lat":"latitudine", "lon":"longitudine"}, inplace=True)
        # Sostituzione separatore ';' con ','
        df_sistemato = df_sistemato.replace(";", ",")

        return df_sistemato


modello = DatasetCleaner("../Dataset/dataset.csv")
# Passo 1. Analisi generali del dataset
# Il separatore dei dati del csv non è ',' (come di default) ma ';'
# Passo 2. Implemento l'apertura corretta del csv specificando il separatore ';'
# Passo 3. Analisi generali del dataset
#modello.analisi_generali(modello.dataframe)
# Risultati:
# Osservazioni: 7896; Variabili: 11; Tipi: object e int64; Valori nan: presenti
# Variabile: denominazione_altra, presenta più del 50% di valori nan
# Passo 4. Drop variabile denominazione_altra
# Passo 5. Analisi dei valori univoci del dataset
#modello.analisi_generali(modello.dataframe_sistemato)
#modello.analisi_valori_univoci(modello.dataframe_sistemato)
# Risultati:
# Variabile denominazione_ita_altra ridondante
# Variabili: lat, lon e superficie_kmq tipo object da convertire in tipo float
# Passo 6. Drop variabile ridondante
# Passo 7. Conversione tipi delle variabili lat, lon e superficie_kmq
# Passo 8. Pochi valori nan eseguo il drop
# Passo 9. Rinonimo le colonne lat e lon
# Passo 10. Sostituisco il separatore ";" con ","
# Passo 11. Creo un nuovo csv sistemato
modello.dataframe_sistemato.to_csv("../Dataset/dataset_nuovo.csv", index=False)
