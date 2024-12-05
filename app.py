from flask import Flask, render_template
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

df = pd.read_csv("C:/Users/prash/OneDrive/Desktop/DASHBOARD/Electric_Vehicle_Population_Data.csv")

# Flask app
server = Flask(__name__)

# Dash app
app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')

# Dash app layout
app.layout = html.Div(children=[
    html.H1(children='Data Visualization Dashboard'),
    dcc.Graph(
        id='bar-chart',
        figure=px.bar(df, x='County', y='Electric Utility', title='Bar Chart Example')
    ),
    dcc.Graph(
        id='line-chart',
        figure=px.line(df, x='County', y='Make', title='Line Chart Example')
    ),
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(df, x='City', y='Base MSRP', color='Electric Range', title='Scatter Plot Example')
    )
])

# route for the main page
@server.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    server.run(debug=True)
