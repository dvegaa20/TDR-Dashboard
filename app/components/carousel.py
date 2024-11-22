import dash_bootstrap_components as dbc
from dash import html

def create_carousel(images):
    """
    Create a reusable carousel component.
    
    :param images: List of dictionaries with 'src' and 'alt' keys for images.
    :return: A dbc.Carousel component.
    """
    return dbc.Carousel(
        items=[{"key": idx, "src": img["src"], "alt": img["alt"]} for idx, img in enumerate(images)],
        controls=True,
        indicators=True,
        interval=3000,
        ride="carousel",
        style={"margin-bottom": "20px"},  # Add spacing below the carousel
    )
