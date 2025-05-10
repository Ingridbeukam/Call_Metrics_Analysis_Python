import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("call_metrics_nettoyé.csv", sep=",")
print(df)

# Bar chart : Appels traités par agent
call_par_agent =df.groupby("agent_id")["calls_handled"].sum().sort_values(ascending=True)
plt.bar(call_par_agent.index, call_par_agent, color ="green")
plt.xlabel("Agent ID",fontsize=12,  fontweight='bold')
plt.ylabel("Nombre d'appel ",fontsize=12, fontweight='bold')
plt.title("Appels traités par agent",fontsize=18, color='darkblue', fontweight='bold', loc='center')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()