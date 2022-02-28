# imports
import dash
from dash import html


# setup
app = dash.Dash(__name__, title='Dash Deployment')


# Layout
app.layout = html.Div([
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
    app.run_server(debug=True)
