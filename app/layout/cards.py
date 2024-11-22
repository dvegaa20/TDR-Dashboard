from dash import html, dcc


def create_card(title, content=None):
    return html.Div(
        [
            # Card Header
            html.Div(
                title,
                className="card-header",
            ),
            # Card Content
            html.Div(
                content,
                className="card-content",
            ),
        ],
        className="card",
    )
