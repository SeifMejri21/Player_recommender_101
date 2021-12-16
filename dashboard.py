# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:09:12 2021

@author: Administrator
"""

# Dashboard
from PIL import Image
import dash
import os
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot

import numpy as np
from base import Recommender

pl_names = list(pd.read_excel("C:/Users/Administrator/Desktop/Systeme de recommendation/data/pl_names.xlsx")['Player'])
def image_importer(name):
    path = "C:/Users/Administrator/Desktop/Systeme de recommendation/photo 2/"
    if  os.path.exists(path):
        img = np.array(Image.open(path+name+".jpg"))
    else:
        img = np.array(Image.open(path+"noone.png"))
    fig = px.imshow(img, color_continuous_scale='gray')
    fig.update_layout(coloraxis_showscale=False)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    return fig


def data_table(player):
    a = Recommender(player)
    b = list(a.keys())
    c =  list(a.values())
    fig = go.Figure(data=[go.Table(header=dict(values=b),cells=dict(values=c))])
    return fig





app = dash.Dash(__name__)
app.layout = html.Div([ 
    html.H1('Player recommender', style={ 'font-size': '50px' , 'color':'#46BE52' , 
                               'font-family' : 'Verdana', 'text-align': 'center','backgroundColor':'#1A2127'}),

    html.Div([
        html.Label(['Player name'],   
           style={'font-weight': 'bold', 'font-size': '17px' , 'color':'#1A2127' , 'font-family' : 'Verdana', 'text-align': 'center','backgroundColor':'#46BE52'}),
        dcc.Dropdown(id='players_list',
            options= [{'label':x, 'value':x} for x in pl_names] ,
            value='Lionel Messi',
            multi=False,
            clearable=False,
            style={'width': '50%' , 'align': 'center' }),]),
    
      html.Div([dcc.Graph(id='player_image',
                                   style={ 'align': 'left' , 'height': '400px'}),
                  html.H3(id='player_name_out', children=[], style={'font-weight': 'bold', 'font-size': '17px' ,
                                    'color':'#1A2127' , 'font-family' : 'Verdana', 'text-align': 'left'}),    
    dbc.Col([
    html.Div([dcc.Graph(id='data_table',
                style={ 'align': 'left' })      ])
        ], width=2)
  ])  ])

@app.callback(
    Output('player_image', component_property='figure'),
    Output('player_name_out', component_property='children'),
    Output('data_table', component_property='figure'),
    Input('players_list', component_property='value')
)
def update_graph(player):
    return image_importer(player), "Chosen player:  "+player ,data_table(player)


if __name__ == '__main__':
    app.run_server(debug=False)










