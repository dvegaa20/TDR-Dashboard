from dash import html
from components.sidebar import create_sidebar
from components.header import create_header
from components.card import create_card
from graphs.spendings import cost_distribution
from data import tdr_data


def dashboard():
    return html.Div(
        [
            # Sidebar
            create_sidebar(),

            # Main Content
            html.Div(
                [


                    # Grid Layout
                    html.Div(
                        [
                            create_card(
                                "Estadísticas de Mantenimiento", "maintenance-stats"),
                            create_card("Estado de Refacciones",
                                        "refacciones-status"),
                        ],
                        className="grid-row",
                    ),
                    html.Div(
                        [
                            create_card(
                                "Actividades de Mantenimiento (Semanales/Mensuales)",
                                "Content for maintenance activities",
                            ),
                            create_card(
                                "Resumen de Gastos",
                                cost_distribution(tdr_data),
                            ),
                        ],
                        className="grid-row",
                    ),
                ],
                className="main-content",
            ),
        ],
        className="app-container",
    )
