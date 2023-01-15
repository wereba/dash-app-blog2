import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd



dash_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app = dash_app.server

dash_app.layout = html.Div([
    dcc.Graph(id='graph-with-slider')
])


if __name__ == '__main__':
    dash_app.run_server(debug=True)
