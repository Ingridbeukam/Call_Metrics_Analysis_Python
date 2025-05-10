import pandas as pd
df=pd.read_csv("../call_metrics_nettoyé.csv", sep=",")
print(df)


# tableau résumé par jour
print("Résumé des actvités par jours")
daily_perf = df.groupby(df['date']).agg({
    'AvgHandleTime': 'mean',
    'std_pass': 'mean',
    'calls_handled': 'sum'
}).reset_index()

print(daily_perf)
print()

# Détecter les jours de mauvaise performance
# Critères de mauvaise performance
print("Identification des jours de travail pas rentable")
bad_days = daily_perf[
    (daily_perf['AvgHandleTime'] > 1200) |
    (daily_perf['std_pass'] < 0.5) |
    (daily_perf['calls_handled'] < daily_perf['calls_handled'].quantile(0.25))
]
print(bad_days)

#Visualiser les jours critiques

import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.plot(daily_perf['date'], daily_perf['AvgHandleTime'], label='AvgHandleTime', color='blue')
plt.scatter(bad_days['date'], bad_days['AvgHandleTime'], color='red', label='Jours critiques')
plt.title('Temps moyen de traitement avec mise en évidence des jours critiques',fontsize=18, fontweight="bold", color="darkblue")
plt.xlabel('Date',fontsize=12, fontweight="bold")
plt.ylabel('AvgHandleTime (sec)',fontsize=12, fontweight="bold")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
