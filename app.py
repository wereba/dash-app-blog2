import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from azure.storage.blob import ContainerClient, BlobClient
import io

container_name = "gsr"
blob_name = "Twatter.csv"
account_url = "https://sam123.blob.core.windows.net"

container_client = ContainerClient(account_url=account_url, container_name=container_name)
blob_client = BlobClient(account_url=account_url, container_name=container_name, blob_name=blob_name)

blob_data = blob_client.download_blob().readall().decode('utf-8')
df = pd.read_csv(io.StringIO(blob_data))
app = dash.Dash()


app.layout = html.Div([
    dcc.Graph(
        id='graph',
        figure= px.Scatter(df, x='Date', y='Open'))
])

if __name__ == '__main__':
    app.run_server(debug=True)
