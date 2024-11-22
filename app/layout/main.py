from dash import html
from layout.sidebar import create_sidebar
from layout.header import create_header
from layout.cards import create_card
from graphs.spendings import cost_distribution
from data import tdr_data


def create_layout():
    return html.Div(
        [
            # Sidebar
            create_sidebar(),
            create_header(),

            # Main Content
            html.Div(
                [
                    html.Link(
                        rel="stylesheet",
                        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",
                    ),
                    # Header


                    # Grid Layout
                    html.Div(
                        [
                            # Row 1
                            create_card(
                                "Estadísticas de Mantenimiento", "maintenance-stats"),
                            create_card("Estado de Refacciones",
                                        "refacciones-status"),
                        ],
                        className="grid-row",
                    ),
                    html.Div(
                        [
                            # Row 2
                            create_card(
                                "Actividades de Mantenimiento (Semanales/Mensuales)",
                                "Content for maintenance activities",
                            ),
                            create_card(
                                "Resumen de Gastos",
                                # Add the graph as the content
                                cost_distribution(tdr_data),
                            ),
                        ],
                        className="grid-row",
                    ),
                    html.Div(
                        [
                            # Row 3
                            create_card("ScatterPlot", "scatter-plot"),
                            create_card("IDK", "idk-content"),
                        ],
                        className="grid-row",
                    ),
                ],
                className="main-content",
            ),
        ],
        className="container",
    )
