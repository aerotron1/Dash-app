# imports
import dash
from dash import html


# setup
dashboard = dash.Dash(__name__, title='My First Dash Deployment')


# Layout
dashboard.layout = html.Div([
    html.H3('Consumer Behaviour Dashboard', style={
        'color': 'green',
        'padding-top': '60px',
        'text-align': 'center'
    }),
    html.P('Dashboard to follow soon...', style={
        'color': 'blue',
        'text-align': 'center',
        'padding-top': '60px'
    })
])


# run
if __name__ == '__main__':
    dashboard.run_server(debug=True)
