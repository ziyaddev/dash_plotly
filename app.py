# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

""" Todo List :
- Load CSV button
- semi-colons separator (change parameter "sep" in pd.to_datetime() )
- 
"""

from datetime import date, datetime

import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# import dash_html_components as html
# import dash_core_components as dcc
from dash import dcc, html

app = dash.Dash(__name__)

df = pd.read_csv('data_25_nov_virgule.csv')

#fig = px.scatter(df, x="gdp per capita", y="life expectancy",

unixtime = df.unixtime

date_dfirst = pd.to_datetime(unixtime, dayfirst=True, yearfirst=False, unit="s")

print(date_dfirst)

fig = go.Figure()

fig.add_trace(go.Scatter(x=date_dfirst, y=df.condensing_temp, name='Condensing Temp',
                         line=dict(color='firebrick', width=1)))
fig.add_trace(go.Scatter(x=date_dfirst, y=df.liquid_temp, name = 'Liquid Temp',
                         line=dict(color='orange', width=1)))
fig.add_trace(go.Scatter(x=date_dfirst, y=df.subcooling, name='Subcooling',
                         line=dict(color='orange', width=1)))

fig.add_trace(go.Scatter(x=date_dfirst, y=df.evaporating_temp, name='Evaporating Temp',
                         line = dict(color='royalblue', width=1)))
fig.add_trace(go.Scatter(x=date_dfirst, y=df.suction_temp, name='Suction Temp',
                         line = dict(color='firebrick', width=1)))
fig.add_trace(go.Scatter(x=date_dfirst, y=df.superheat, name='Superheat',
                         line=dict(color='darkorchid', width=1)))

# Edit the layout
fig.update_layout(title='Daikin Chiller Trend',
                   xaxis_title='Time',
                   yaxis_title='Temperature (degrees C)')

# fig = px.line(df, x="unixtime", y="evaporating_temp")#,
#                  #size="population", color="continent", hover_name="country",
#                  #log_x=True #size_max=60)

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1h", step="hour", stepmode="backward"),
            dict(count=2, label="2h", step="hour", stepmode="backward"),
            dict(count=6, label="6h", step="hour", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

fig.show()

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
   app.run_server(debug=True)
