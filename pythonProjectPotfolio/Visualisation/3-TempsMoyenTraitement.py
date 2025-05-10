import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("../call_metrics_nettoyé.csv", sep=",")
print(df)

#Line chart : Évolution du AvgHandleTime dans le temps
# Assure-toi que 'date' est de type datetime
df['date'] = pd.to_datetime(df['date'])



# Regrouper par jour et langue
# Moyenne par jour
daily_handle_time = df.groupby(df['date'].dt.date)['AvgHandleTime'].mean()

plt.figure(figsize=(10, 5))
plt.plot(daily_handle_time.index, daily_handle_time.values, marker='o')
plt.title('Évolution du temps moyen de traitement (AvgHandleTime)',fontsize=18, fontweight="bold", color='darkblue')
plt.xlabel('Date', fontsize=12, fontweight="bold")
plt.ylabel('Temps moyen (sec)', fontsize=12, fontweight="bold")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
print("temps moyen de traitement")
print(daily_handle_time)
plt.show()


