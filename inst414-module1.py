import pandas as pd
import matplotlib.pyplot as plt

# Reads in data set
df = pd.read_csv("StressLevelDataset.csv")

social_columns = [
    'social_support',
    'peer_pressure',
    'extracurricular_activities',
    'bullying',
    'academic_performance'
]

df_selected = df[social_columns]
df_clean = df_selected.dropna()
correlations = df_clean.corr()['academic_performance']
correlations = correlations.drop('academic_performance') 
plt.figure()
plt.bar(correlations.index, correlations.values)

plt.xlabel("Factors")
plt.ylabel("Correlation with Academic Performance")
plt.title("Impact of Social Factors on Academic Performance")

plt.xticks(rotation=45)
plt.show()

psychological_columns = ['anxiety_level', 'depression', 'academic_performance']
df_selected = df[psychological_columns].dropna()
correlations = df_selected.corr()['academic_performance']
correlations = correlations.drop('academic_performance')
plt.figure()
plt.bar(correlations.index, correlations.values)

plt.xlabel("Mental Health Factors")
plt.ylabel("Correlation with Academic Performance")
plt.title("Anxiety & Depression vs Academic Performance")

plt.show()