from dash import html
from components.carousel import create_carousel
from components.table import create_table
import pandas as pd


def spendings_page():
    """
    Create the spendings page layout.
    """
    # Sample data for the table
    data = pd.DataFrame({
        "Costo": [100, 200, 300],
        "Categoría": ["A", "B", "C"],
        "Fecha": ["2024-01-01", "2024-01-02", "2024-01-03"]
    })

    # Carousel images
    carousel_images = [
        {"src": "/assets/image1.jpg", "alt": "Cost Analysis 1"},
        {"src": "/assets/image2.jpg", "alt": "Cost Analysis 2"},
        {"src": "/assets/image3.jpg", "alt": "Cost Analysis 3"},
    ]

    return html.Div(
        [
            create_carousel(carousel_images),
            html.Div(
                create_table(data),
                className="page-content",  # Matches unified styling
            ),
        ],
        className="main-content",  # Ensures consistent layout width
    )
