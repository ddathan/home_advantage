# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('../Data/E0.csv')

home_goals = df['FTHG']
away_goals = df['FTAG']

maxgoals = np.amax([home_goals,away_goals])
scores = np.zeros((maxgoals+1,maxgoals+1))

for i in range(0,len(df)):
    hg = df['FTHG'].iloc[i]
    ag = df['FTAG'].iloc[i]
    scores[hg][ag] = scores[hg][ag]+1 

    

sns.heatmap(data=scores)



