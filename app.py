# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


app = dash.Dash(__name__)

df = pd.read_csv('data_25_nov_virgule.csv')

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

#fig = px.scatter(df, x="gdp per capita", y="life expectancy",

unixtime = df.unixtime

fig = go.Figure()

fig.add_trace(go.Scatter(x=unixtime, y=df.condensing_temp, name='Condensing Temp',
                         line=dict(color='firebrick', width=1)))
fig.add_trace(go.Scatter(x=unixtime, y=df.liquid_temp, name = 'Liquid Temp',
                         line=dict(color='orange', width=1)))
fig.add_trace(go.Scatter(x=unixtime, y=df.subcooling, name='Subcooling',
                         line=dict(color='orange', width=1) # dash options include 'dash', 'dot', and 'dashdot'
))
fig.add_trace(go.Scatter(x=unixtime, y=df.evaporating_temp, name='Evaporating Temp',
                         line = dict(color='royalblue', width=1)))
fig.add_trace(go.Scatter(x=unixtime, y=df.suction_temp, name='Suction Temp',
                         line = dict(color='firebrick', width=1)))
fig.add_trace(go.Scatter(x=unixtime, y=df.superheat, name='Superheat',
                         line=dict(color='royalblue', width=1)))

# Edit the layout
fig.update_layout(title='Daikin Chiller capture',
                   xaxis_title='Time',
                   yaxis_title='Temperature (degrees C)')

# fig = px.line(df, x="unixtime", y="evaporating_temp")#,
#                  #size="population", color="continent", hover_name="country",
#                  #log_x=True #size_max=60)

fig.update_xaxes(rangeslider_visible=True)
fig.show()

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
