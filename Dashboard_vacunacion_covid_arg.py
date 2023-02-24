import dash 
import dash_core_components as dcc
import dash_html_components as html 
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

data = pd.read_csv('covid19_argentina.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1('Vacunas contra el covid-19 en Argentina'),
        html.Img(src='assets/vacuna.png'),
    ], className = 'banner'),

    html.Div([
        html.Div([
            html.P('Seleccione una opción'),
            dcc.RadioItems(
                id = 'radio_boton', 
                options = [
                    {'label': 'Primera dosis', 'value':'primera_dosis_cantidad'},
                    {'label': 'Segunda dosis', 'value':'segunda_dosis_cantidad'},
                    {'label': 'Dosis unica', 'value': 'dosis_unica_cantidad'}
                ], value = 'primera_dosis_cantidad'
            )
        ], className = 'radio_boton')
    ]),

    html.Div([
        html.Div([
            html.H1('Distribución porcentual por jurisdicción de vacunados'),
            dcc.Graph(
                id = 'Grafico_pastel', 
                figure={}
                )
        ], className = 'grafico_pastel'),
        html.Div([
            html.H1('Distribución por jurisdicción de vacunados'),
            dcc.Graph(
                id = 'Grafico_barras',
                figure = {}
                )
        ], className = 'grafico_barras'),
    ])
], className = 'div_principal')

@app.callback(
    Output('Grafico_barras', component_property='figure'),
    [Input('radio_boton', component_property='value')]
)
def actualizar_grafico_barras(value):
    if value == 'primera_dosis_cantidad':
        fig = px.bar(
            data_frame= data,
            x = 'jurisdiccion_nombre',
            y = 'primera_dosis_cantidad'
        )
    elif value == 'segunda_dosis_cantidad':
        fig = px.bar(
            data_frame= data,
            x = 'jurisdiccion_nombre',
            y = 'segunda_dosis_cantidad'
        )
    else:
        fig = px.bar(
            data_frame= data,
            x = 'jurisdiccion_nombre',
            y = 'dosis_unica_cantidad'
        )

    return fig

@app.callback(
    Output('Grafico_pastel', component_property='figure'),
    [Input('radio_boton', component_property='value')]
)
def actualizar_grafico_pastel(value):
    if value == 'primera_dosis_cantidad':
        fig_pastel = px.pie(
            data_frame= data,
            names= 'jurisdiccion_nombre',
            values='primera_dosis_cantidad'
        )
    elif value == 'segunda_dosis_cantidad':
        fig_pastel = px.pie(
            data_frame= data,
            names='jurisdiccion_nombre',
            values='segunda_dosis_cantidad'
        )
    else: 
        fig_pastel = px.pie(
        data_frame= data,
        names='jurisdiccion_nombre',
        values='dosis_unica_cantidad'
        )
    return fig_pastel


if __name__ == ('__main__'):
    app.run_server(debug = True)