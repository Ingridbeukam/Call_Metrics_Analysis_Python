import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("../call_metrics_nettoyé.csv", sep=",")
print(df)

#Scatter plot : AvgHandleTime vs std_pass
# :Corrélation entre le temps de traitement et le score qualité des appels
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='AvgHandleTime', y='std_pass', hue='lang_id', alpha=0.7)
plt.title('AvgHandleTime vs Qualité (std_pass)',fontsize=18, fontweight="bold", color='darkblue' )
plt.xlabel('Temps moyen de traitement (sec)', fontsize=12, fontweight="bold")
plt.ylabel('Score de qualité (std_pass)', fontsize=12, fontweight="bold")
plt.legend(title='Langue')
plt.tight_layout()
plt.show()