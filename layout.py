# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 22:29:24 2021

@author: Administrator
"""


import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html


pl_names = list(pd.read_excel("C:/Users/Administrator/Desktop/Systeme de recommendation/data/pl_names.xlsx")['Player'])



my_layout = html.Div([
        
    html.H1('Player recommender', style={ 'font-size': '50px' , 'color':'#46BE52' , 
                               'font-family' : 'Verdana', 'text-align': 'center','backgroundColor':'#1A2127'}),
    

    html.Div([
        html.Label(['Dates'],   
           style={'font-weight': 'bold', 'font-size': '17px' , 'color':'#1A2127' , 'font-family' : 'Verdana', 'text-align': 'center','backgroundColor':'#46BE52'}),
        dcc.Dropdown(id='players_list',
            options= [{'label':x, 'value':x} for x in pl_names] ,
            value=pl_names[0],
            multi=False,
            clearable=False,
            style={"width": "50%"}),]),
    
        html.Div([
            dash_table.DataTable(
    id='table',
    columns=['Player', 'Similarity Score'],
    data=update_graph(),
)
            
            ])

])