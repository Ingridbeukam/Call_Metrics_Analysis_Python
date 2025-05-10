#importer les données
import pandas as pd
df=pd.read_csv("call_metrics_dataset.csv", sep=";")
print(df.head())
print()
print(df.tail())
print()
#exploration des données
print(df.describe())
print()
print(df.corr)
print()
print(df.columns)
print()
print(df.info())
print()
print(df)


print("""

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

""")