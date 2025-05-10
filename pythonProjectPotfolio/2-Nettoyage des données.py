import pandas as pd
df=pd.read_csv("call_metrics_dataset.csv", sep=";")
print(df.head(15))

# 1-renommer les noms de colonnes
df.rename(columns={'avg_aht':'AvgHandleTime'},inplace=True)
df.to_csv('call_metrics_dataset.csv', index=False)
print(df.columns)

"""
Nom de colonne	Description
AGENT_ID:	Identifiant unique de l’agent qui a traité les appels. 
Utile pour l’analyse individuelle ou comparative.
DATE:	Date de la journée d’analyse. Format : YYYY-MM-DD. Permet les analyses temporelles.
PRODUCT_ID:	Identifiant du produit ou service concerné par l’appel. 
Permet d’identifier les produits avec le plus de support.
LANG_ID:	Identifiant de la langue utilisée (ex. : 1 = anglais, 2 = espagnol, etc.).
Sert à analyser la performance par langue.
CALLS_HANDLED:	Nombre total d’appels pris en charge par l’agent ce jour-là. 
Indicateur de charge de travail.
AVGHANDLETIME:	Temps moyen de traitement par appel (en secondes ou minutes). 
KPI central pour mesurer l'efficacité.
STD_PASS:	Score de qualité ou conformité des appels passés, souvent basé sur une 
norme interne (e.g. script respecté, procédure suivie). 
Peut être une note sur 100 ou un score de validation automatique.
"""
print(df)
# Conversion du format time en minutes et hh:mm:ss
import datetime
# 3. Ajouter une colonne en minutes

df["AvgHandleTime_min"] = df["AvgHandleTime"] / 60
df.to_csv('call_metrics_dataset.csv', index=False)
print(df)

#Ajouter une colonne en hh:mm:ss
def minutes_to_hms(minutes):
    if pd.notnull(minutes):  # Vérifier si la valeur n'est pas NaN
        seconds = int(minutes * 60)  # Convertir les minutes en secondes
        return str(datetime.timedelta(seconds=seconds))
    else:
        return None  # Retourner None si la valeur est NaN

# 2. Appliquer la fonction à la colonne 'AvgHandleTime_min'
df["AvgHandleTime_hms"] = df["AvgHandleTime_min"].apply(minutes_to_hms)

# Sauvegarder le DataFrame nettoyé
df.to_csv('call_metrics_dataset.csv', index=False)

# Afficher le résultat pour vérification
print(df)


# Exporter le DataFrame nettoyé en fichier CSV
df.to_csv('call_metrics_nettoyé.csv', index=False)
# index=False pour ne pas inclure l'index dans le fichier CSV

