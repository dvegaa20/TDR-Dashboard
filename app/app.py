from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from components.sidebar import create_sidebar
from components.header import create_header
from pages.spendings import spendings_page
from layout.main import dashboard

# Initialize the app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)

# Define the app layout
app.layout = html.Div(
    [
        dcc.Location(id="url"),  
        html.Div(
            [
                create_sidebar(),  # Sidebar
                html.Div(
                    [
                        create_header(),  # Header
                        html.Div(id="page-content"),  # Page content
                    ],
                    className="main-content",
                ),
            ],
            className="app-container",
        ),
    ]
)


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/spendings":
        return spendings_page()
    else:  # Default to home
        return dashboard()

if __name__ == "__main__":
    app.run_server(debug=True)
