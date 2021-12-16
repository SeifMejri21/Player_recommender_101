# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:33:22 2021

@author: Administrator
"""

# CONSTANTS

gk_stats = ['Save%','PSxG+/-','Cmp%','Launch%','AvgLen','Launch%.1','AvgLen.1','Stp%','#OPA','#OPA/90','AvgDist']
df_stats = ['Cmp%','PrgDist/Cmp','Cmp%.1','Cmp%.2','Cmp%.3','xG/90','xA/90','KP/90','Final_Third/90','TklW%','Press90','Tkl90','Int90','DribbfSucc','Dribb90','ProgCar90','ProgRec90']
mf_stats = ['SoT%','G/Sh','Dist','xG/90','npxG/Sh','G-xG','Cmp%','PrgDist/Cmp','Cmp%.1','Cmp%.2','Cmp%.3','xA/90','KP/90','Final_Third/90','TklW%','Press90','Tkl90','Int90','DribbfSucc','Dribb90','ProgCar90','ProgRec90']
fw_stats = ['SoT%','G/Sh','Dist','xG/90','npxG/Sh','G-xG','Cmp%','PrgDist/Cmp','Cmp%.1','Cmp%.2','Cmp%.3','xA/90','KP/90','Final_Third/90','Press90','DribbfSucc','Dribb90','ProgCar90','ProgRec90']



import pandas as pd



data = pd.read_excel("C:/Users/Administrator/Desktop/Systeme de recommendation/data/players.xlsx")


def players_recommender():
    return 1

