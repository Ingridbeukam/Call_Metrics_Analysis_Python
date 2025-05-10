import pandas as pd
df=pd.read_csv("call_metrics_nettoyé.csv", sep=",")
print(df)
print()
#Total de productivité par agent
print("Tableau présentant la productivité par agent")
Mesure =df.groupby('agent_id').agg({
    'std_pass': 'sum',
    'calls_handled': 'sum',
    'AvgHandleTime_min': 'mean'
}).sort_values('std_pass', ascending=False)
print(Mesure)
print()
#heure de travail estimées par agents
print("Tableau présentant le total d'heure de travail par agents exprimé en minutes")
print()
df['travail_estimees'] = (df['calls_handled'] * df['AvgHandleTime_min']) / 60
print(df[['agent_id', 'calls_handled', 'AvgHandleTime_min', 'travail_estimees']].head(15))
print()
# Volume moyenne des appels par jours
Volume_appel = df.groupby('date')['calls_handled'].sum().mean()
print("Le volume moyen des appels est de:", Volume_appel)

