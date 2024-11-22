from dash import html, dcc


def create_card(title, graph_id):
    return html.Div(
        [
            html.Div(title, className="card-header"),
            dcc.Graph(id=graph_id, className="card-content"),
        ],
        className="card",
    )
