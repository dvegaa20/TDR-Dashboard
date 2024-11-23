from dash import html


def create_carousel(graphs):
    """
    Create a carousel containing only graphs.
    """
    carousel_items = []
    for idx, graph in enumerate(graphs):
        # Add each graph as a carousel item
        carousel_items.append(
            html.Div(
                graph["content"],
                className="carousel-item" + (" active" if idx == 0 else "")
            )
        )

    return html.Div(
        [
            html.Div(
                className="carousel-inner",
                children=carousel_items,
            ),
            # Navigation controls
            html.A(
                "❮", className="carousel-control-prev", href="#graphCarousel", role="button",
                style={"color": "black"}, **{"data-slide": "prev"}
            ),
            html.A(
                "❯", className="carousel-control-next", href="#graphCarousel", role="button",
                style={"color": "black"}, **{"data-slide": "next"}
            ),
        ],
        className="carousel slide",
        id="graphCarousel",
        **{"data-ride": "carousel"}
    )
