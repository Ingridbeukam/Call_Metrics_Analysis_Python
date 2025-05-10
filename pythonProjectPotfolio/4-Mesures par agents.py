import pandas as pd
df=pd.read_csv("call_metrics_nettoyé.csv", sep=",")
print(df)

#Mesure par agents


Mesure =df.groupby('agent_id').agg({
    'calls_handled': 'sum',
    'AvgHandleTime_min': 'mean',
    'std_pass': 'mean'
}).sort_values('calls_handled', ascending=False)
print("Perfomances des agents")
print(Mesure)
