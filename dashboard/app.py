# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import dashboard_figures as mf

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df_ww = pd.read_csv('../data/worldwide_timeseries.csv')
df_total = pd.read_csv('../data/Total_cases_worldwide.csv')
df_germany = pd.read_csv('../data/cases_germany_states.csv')

fig_geo_ww = mf.get_wordlwide_cases(df_total)
fig_germany_bar = mf.get_german_barchart(df_germany)
fig_germany_pie = mf.get_german_piechart(df_germany)

fig_line = mf.get_lineplot('Germany', df_ww)

ww_facts = mf.get_worldwide_facts(df_total)

fact_string = '''Weltweit gibt es insgesamt {} Infektionen. 
    Davon sind bereits {} Menschen vertorben und {} gelten als geheilt. 
    Somit sind offiziell {} Menschen aktiv an einer Coronainfektion erkrankt.'''

fact_string = fact_string.format(ww_facts['total'], 
                                 ww_facts['deaths'], 
                                 ww_facts['recovered'], 
                                 ww_facts['active'])

countries = mf.get_country_names(df_ww)

# Build List for Dropdown/Combobox
dd_options = []
for key in countries:
    dd_options.append({
        'label': key,
        'value': key
    })

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# App Layout
app.layout = html.Div(children=[
    html.H1(children='COVID-19: Dashboard', style={'textAlign': 'center'}),
    html.H2(children='Weltweite Verteilung', style={'textAlign': 'center'}),
    # World and Facts
    html.Div(children=[

        html.Div(children=[
            
            dcc.Graph(figure=fig_geo_ww),

        ], style={'display': 'flex', 
                  'flexDirection': 'column',
                  'width': '66%'}),

        html.Div(children=[
            
            html.H3(children='Fakten'),
            html.P(children=fact_string)

        ], style={'display': 'flex', 
                  'flexDirection': 'column',
                  'width': '33%'})

    ], style={'display': 'flex',
              'flexDirection': 'row', 
              'flexwrap': 'wrap',
              'width': '100%'}),

    # Combobox and Checkbox
    html.Div(children=[
        html.Div(children=[
            # Combobox
            dcc.Dropdown(
                id='country-dropdown',
                options=dd_options,
                value=['Germany'],
                multi=True
            ),
            
        ], style={'display': 'flex', 
                  'flexDirection': 'column',
                  'width': '66%'}),

        html.Div(children=[
            # Radio-Buttons
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display':'inline-block'}
            ),

        ], style={'display': 'flex', 
                  'flexDirection': 'column',
                  'width': '33%'})
    ], style={'display': 'flex',
              'flexDirection': 'row', 
              'flexwrap': 'wrap',
              'width': '100%'}),
    
    # Lineplot and Fakts
    html.Div(children=[
        html.Div(children=[

            #Line plot: Infections
            dcc.Graph(figure=fig_line, id='infections_line'),

        ], style={'display': 'flex', 
                  'flexDirection': 'column',
                  'width': '100%'}),

    ], style={'display': 'flex',
              'flexDirection': 'row', 
              'flexwrap': 'wrap',
              'width': '100%'}),

    # Germany
    html.H2(children='Zahlen aus Deutschland', style={'textAlign': 'center'}),
    html.Div(children=[
        html.Div(children=[
            
            # Barchart Germany
            dcc.Graph(figure=fig_germany_bar),

        ], style={'display': 'flex', 
                  'flexDirection': 'column',
                  'width': '50%'}),

        html.Div(children=[
            
            # Pie Chart Germany
            dcc.Graph(figure=fig_germany_pie),

        ], style={'display': 'flex', 
                  'flexDirection': 'column',
                  'width': '50%'})
    ], style={'display': 'flex',
              'flexDirection': 'row', 
              'flexwrap': 'wrap',
              'width': '100%'})
]) 

# Interaktiv Line Chart
@app.callback(
    Output('infections_line', 'figure'),
    [Input('country-dropdown', 'value'), Input('yaxis-type', 'value')])
def update_graph(countries, axis_type):
    countries = countries if len(countries) > 0 else ['Germany']
    data_value = []
    for country in countries:
        data_value.append(dict(
            x= df_ww['Date'], 
            y= df_ww[country], 
            type= 'lines', 
            name= str(country)
        ))
    
    title = ', '.join(countries)
    title = 'Infektionen: ' + title
    return {
        'data': data_value,
        'layout': dict( 
            yaxis={
                'type': 'linear' if axis_type == 'Linear' else 'log'
            },
            hovermode='closest',
            title = title
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)