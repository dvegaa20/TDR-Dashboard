import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from data_containers.layouts import iris_layout
from data_containers.tractos import vehicle_age
from data import tdr_data


app = dash.Dash(__name__)
server = app.server

# Layout de la app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callbacks para actualizar el contenido según la URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/iris':
        return iris_layout(tdr_data)
    elif pathname == '/tractos_age':
        return vehicle_age(tdr_data)
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=False)