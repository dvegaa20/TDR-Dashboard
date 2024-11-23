from dash import html
from components.carousel import create_carousel
from components.table import create_table
import pandas as pd

from data import tdr_data


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

    # only show jobcode and unit number

    data = tdr_data.copy()
    data_filtered = data[["JobCode", "UnitNumber"]]

    return html.Div(
        [
            html.Div(
                create_table(data_filtered),
                className="page-content",  # Matches unified styling
            ),
        ],
        className="main-content",  # Ensures consistent layout width
    )
