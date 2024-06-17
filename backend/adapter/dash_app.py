from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

def init_dash(server):
    dash_app = Dash(__name__, server=server, url_base_pathname='/dash/')

    df = pd.read_csv('data/datasets/diabetes_data.csv')
    gender_counts = df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']

    fig_age = px.histogram(df, x='Age', nbins=30, title='Distribución de Edad')
    fig_gender = px.bar(gender_counts, x='Gender', y='Count', labels={'Gender': 'Gender', 'Count': 'Count'}, title='Distribución de Género')
    fig_bmi_hba1c = px.scatter(df, x='BMI', y='HbA1c', color='Diagnosis', title='BMI vs HbA1c')
    fig_cholesterol = px.box(df, x='Diagnosis', y='CholesterolTotal', color='Diagnosis', title='Niveles de Colesterol Total por Diagnóstico')

    dash_app.layout = html.Div([    
        dcc.Dropdown(
            id='graph-type',
            options=[
                {'label': 'Distribución de Edad', 'value': 'age'},
                {'label': 'Distribución de Género', 'value': 'gender'},
                {'label': 'BMI vs HbA1c', 'value': 'bmi_hba1c'},
                {'label': 'Colesterol por Diagnóstico', 'value': 'cholesterol'},
            ],
            value='age'
        ),
        dcc.Graph(id='main-graph')
    ])

    @dash_app.callback(
        Output('main-graph', 'figure'),
        [Input('graph-type', 'value')]
    )
    def update_graph(graph_type):
        if graph_type == 'age':
            return fig_age
        elif graph_type == 'gender':
            return fig_gender
        elif graph_type == 'bmi_hba1c':
            return fig_bmi_hba1c
        elif graph_type == 'cholesterol':
            return fig_cholesterol

    return dash_app
