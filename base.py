# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 21:40:27 2021

@author: Administrator
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors


gk_stats = ['Player','Save%','PSxG+/-','Cmp%','Launch%','AvgLen','Launch%.1','AvgLen.1','Stp%','#OPA','#OPA/90','AvgDist']
df_stats = ['Player','Cmp%','PrgDistCmp','Cmp%.1','Cmp%.2','Cmp%.3','xA90','KP90','Fin.Third90','TklW%','Press90','Tkl90','Int90','Dribb90','ProgCar90']
mf_stats = ['Player','Dist','xG90','npxG/Sh','Cmp%','PrgDistCmp','Cmp%.1','Cmp%.2','Cmp%.3','xA90','KP90','Fin.Third90','TklW%','Press90','Tkl90','Int90','DribbfSucc','Dribb90','ProgCar90','ProgRec90']
fw_stats = ['Player','SoT%','G.Sh','Dist','xG90','npxG/Sh','G-xG','Cmp%','xA90','KP90','Press90','DribbfSucc','Dribb90','ProgCar90','ProgRec90']



def position_finder(player):
    gk =  list(pd.read_excel("C:/Users/Administrator/Desktop/Systeme de recommendation/data/gk_names.xlsx")['Player'])
    pl_names = list(pd.read_excel("C:/Users/Administrator/Desktop/Systeme de recommendation/data/pl_names.xlsx")['Player'])
    pl_positions = list(pd.read_excel("C:/Users/Administrator/Desktop/Systeme de recommendation/data/pl_names.xlsx")['Pos'])
    if player in gk : 
        return 'GK'
    elif player in pl_names :
        return pl_positions[pl_names.index(player)]
    else:
        print("Error: Wrong name or does not exist")



###########################################################################################################################
# Data Filtering

def data_filter(data, position):
    if position == "GK":
        data_2 = data[gk_stats]
    elif position == "DF":
        data = data[data['Pos']==position]
        data_2 = data[df_stats]  
    elif position == "MF":
        data = data[data['Pos']==position]
        data_2 = data[mf_stats]    
    elif position == "FW":
        data = data[data['Pos']==position]
        data_2 = data[fw_stats]
    data_2 = data_2.dropna()
    data_2.reindex()
    return data_2


def recommender(np_array):
    norm = np.linalg.norm(np_array)
    np_array = np_array/norm    
    nbrs = NearestNeighbors(n_neighbors=len(np_array), algorithm='ball_tree').fit(np_array)
    distances, indices = nbrs.kneighbors(np_array)
    return distances, indices 

def GK_recommender(player):
    gk_data = pd.read_excel("C:/Users/Administrator/Desktop/Systeme de recommendation/data/goalkeepers.xlsx")
    gk_data = data_filter(gk_data,'GK')
    players = list(gk_data['Player']) 
    gk_data = gk_data.drop('Player', axis= 'columns')
    
    np_array=np.array(gk_data)
    distances, indices = recommender(np_array)
    print("----- Similar to ",player," -----")
    sim_players =[]
    sim_scores =[]    
    for i in range(1,11):
        sim_players.append(players[indices[players.index(player)][i]])
        sim_scores.append(round(((max(distances[players.index(player)]))-distances[players.index(player)][i])/max(distances[players.index(player)]),4)*100)
        similar_player = " Similar player "+str(i)+":  "+players[indices[players.index(player)][i]]
        similarity_score = "   with score: "+str(round(((max(distances[players.index(player)]))-distances[players.index(player)][i])/max(distances[players.index(player)]),4)*100)+"%"
        print(similar_player + similarity_score)    
    return  {'Player': sim_players ,  'Similarity Score':sim_scores}

def PLAYER_recommender(player):
    player_data=pd.read_excel("C:/Users/Administrator/Desktop/Systeme de recommendation/data/players.xlsx")
    all_palyers = list(player_data['Player'])
    if not player in all_palyers:
        return {'Player': ['NONNNNNN'] ,  'Similarity Score':['NONNNNNN']}
    else:
        if position_finder(player) == 'DF':
            player_data_2 = data_filter(player_data, 'DF')
            print(player)
        elif position_finder(player) == 'MF':
            print(player)
            player_data_2 = data_filter(player_data, 'MF')
        elif position_finder(player) == 'FW':
            player_data_2 = data_filter(player_data, 'FW')
            print(player)
        else: print("SHIT")
        players = list(player_data_2['Player']) 
        player_data_2 = player_data_2.drop('Player', axis= 'columns')
        np_array=np.array(player_data_2)
        distances, indices = recommender(np_array)
        print("----- Similar to ",player," -----")
        sim_players =[]
        sim_scores =[] 
        for i in range(1,11):
            sim_players.append(players[indices[players.index(player)][i]])
            sim_scores.append(round(((max(distances[players.index(player)]))-distances[players.index(player)][i])/max(distances[players.index(player)]),4)*100)
            similar_player = " Similar player "+str(i)+":  "+players[indices[players.index(player)][i]]
            similarity_score = "   with score: "+str(round(((max(distances[players.index(player)]))-distances[players.index(player)][i])/max(distances[players.index(player)]),4)*100)+"%"
            print(similar_player + similarity_score)    
        return {'Player': sim_players ,  'Similarity Score':sim_scores}

def Recommender(player):
    if position_finder(player) == 'GK':
        return GK_recommender(player)
    elif position_finder(player) in ['DF','MF','FW']:
        return PLAYER_recommender(player)
        


dicti = Recommender("Virgil van Dijk")

###########################################################################################################################
###########################################################################################################################
###########################################################################################################################









