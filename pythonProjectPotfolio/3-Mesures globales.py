#Lecture de données
import pandas as pd
df=pd.read_csv("call_metrics_nettoyé.csv", sep=",")
print(df.columns)
print(df)
print()
print(df.dtypes)



#Total des appels traités
total_calls_handled = df['calls_handled'].sum()
print(f"Le total des appels traités est de : {total_calls_handled}")
print()
#Calculer le temps moyen de traitement des appels (en minutes) :
avg_handle_time = df['AvgHandleTime_min'].mean()
print(f"Le temps moyen de traitement des appels est de : {avg_handle_time:.2f} minutes")
print()
# Écart-type du temps de traitement : Evaluer la régularité entre les appels
std_temps_traitement = df['AvgHandleTime'].std()
print("l'ecart-type du temps de traitement",std_temps_traitement,"s")
print()
#Score qualité moyen :Mesure la qualité ou conformité globale des appels.
score_qualite = df["std_pass"].mean()
print("le score de qualité moyen est de :", score_qualite)
print()
#Nombre d'agents actifs :Agents qui ont traité au moins un appel.
agent_actifs = df['agent_id'].nunique()
print(agent_actifs, " agents sont actifs")
print()
#Nombre de jours couverts :  Période couverte par le dataset.
Jours_couverts =df['date'].nunique()
print("Le nombre de jours couverts est de:",Jours_couverts)

