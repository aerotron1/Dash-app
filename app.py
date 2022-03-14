# imports
import dash
# dcc and html is the layout and web page components
from dash import dcc, html
# input, output for callbacks
from dash.dependencies import Input, Output

import pandas as pd
# for the graph
import plotly.express as px

# setup initialisation
app = dash.Dash(__name__, title='Dash Deployment')
server = app.server

# Layout
app.layout = html.Div([
    html.H3('Consumer Behaviour Dashboard', style={
        'color': 'blue',
        'padding-top': '60px',
        'text-align': 'center'
    }),
    html.P('Dashboard to follow soon...', style={
        'color': 'blue',
        'text-align': 'center',
        'padding-top': '60px'
    }),
    html.Br(),
    html.Button('Track Purchased', id='track-purchased-btn', style={
        'background-color': 'red'
    }),
    html.Br(),
    dcc.Graph(
        figure={
        #     # 'data': [
        #     # {'x': [], 'y': [], 'type': 'bar', 'name': 'Most Purchased'},
        #     # {'x': [], 'y': [], 'type': 'bar', 'name': 'Least Purchased'},
        #     # ],
            'layout': {
            'title': 'Most & Least purchased products and categories'
        }
        },
        id='purchased'
    ), 
    html.Br(),
    html.Button('Track Performance', id='track-performance-btn', style={
        'background-color': 'red'
    }),
    html.Br(),
    dcc.Graph(
        figure={},
        id='best-performance'
    ), 
    html.Br(),
    html.Button('Track Sales per hour', id='track-sales-btn', style={
        'background-color': 'red'
    }),
    html.Br(),
    dcc.Graph(
        figure={},
        id='sales-per-hour'
    ),
    html.Br(),
    html.Button('Track Profitable branches', id='track-profitable-btn', style={
        'background-color': 'red'
    }),
    html.Br(),
    dcc.Graph(
        figure={},
        id='profitable-branches'
    )
])

# callback
# purchased graph
@app.callback (
    # output to show the graph using the id graph component
    Output(component_id='purchased', component_property='figure'),
    # input when click the button for id= purchased
    Input(component_id='track-purchased-btn', component_property='n_clicks')
)

def track_purchased(button):
    print('clicked purchase')

    if button is not None:
# attach csv file for most and least purchased
        product_df = pd.DataFrame(data=pd.read_csv(''))
        fig = px.bar(product_df, x = ['Most Purchased','Least Purchased'], y='Products')
        return fig 
    return {}   

# performance graph
@app.callback (
    # output to show the graph using the id graph component
    Output(component_id='best-performance', component_property='figure'),
    # input when click the button for id= purchased
    Input(component_id='track-performance-btn', component_property='n_clicks')
)

def track_performance(button):
    print('clicked performance')


# sales per hour graph
@app.callback (
    # output to show the graph using the id graph component
    Output(component_id='sales-per-hour', component_property='figure'),
    # input when click the button for id= purchased
    Input(component_id='track-sales-btn', component_property='n_clicks')
)

def track_sales(button):
    print('clicked sales')

# profitable graph
@app.callback (
    # output to show the graph using the id graph component
    Output(component_id='profitable-branches', component_property='figure'),
    # input when click the button for id= purchased
    Input(component_id='track-profitable-btn', component_property='n_clicks')
)

def track_profitable(button):
    print('clicked profit')

# run
if __name__ == '__main__':
    app.run_server(debug=True)
