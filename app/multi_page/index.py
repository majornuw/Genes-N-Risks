import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import consent, main, statistic, load

#app = dash.Dash(__name__, suppress_callback_exceptions=True)
#server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/consent':
        return consent.layout
    elif pathname == '/statistic':
        return statistic.layout
    elif pathname == '/load':
        return load.layout
    else:
        return main.layout

if __name__ == '__main__':
    app.run_server(debug=True)
