import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv('https://storage.googleapis.com/kagglesdsdata/datasets%2F4538%2F7213%2FETFs%2Faadr.us.txt?GoogleAccessId=gcp-kaggle-com@kaggle-161607.iam.gserviceaccount.com&Expires=1597903794&Signature=jqpuPoLQmE2FIt6kmO%2BEuVbJ%2B4b2FWKK%2F52P1xPTVAJ3p2EGV8nCtJvgnMnzBtI2kCzAZSXDF%2FvLHz4hA4dv9qtP2ElCA%2Bs98cfXuLwxZ0244%2BuTvAiaocDBpYGT9hF61uWOP8XO5HEh2Fkr9gzJ2Mruw%2BabmyYnseb54hynKZmy86N5wX5DtsMlWkRR9SKnzDX%2BwRXvsnY1nquto0oUqfutIi2pCySfCk25%2BgRUMCQiLSRRluYhJoPJcBI3xVp4HYIlSFbxR2%2FyVKVwCB7nBh6fnJx5zowxFvFTC%2FnYUOM3LZYmpjPzcNsBkK6nL%2FSixJ0v3SC1A8f2sm8P9JtWJA%3D%3D')

fig = px.scatter(df, x='Date', y='Open',color='Open')

app.layout = html.Div(children=[
    html.H4('Test Dash'),
    dcc.Graph(
        id='test_graph', figure = fig
    )
])

if __name__=='__main__':
    app.run_server(debug=True)
