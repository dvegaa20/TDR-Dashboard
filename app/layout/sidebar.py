from dash import html


def create_sidebar():
    return html.Div(
        [
            # Sidebar header with logo
            html.Div(
                [
                    html.Img(src="/assets/logo.png",
                             alt="Logo", className="logo"),
                    html.Span("TDR MOVIMIENTO"),
                ],
                className="sidebar-header",
            ),
            # Sidebar menu
            html.Ul(
                [
                    html.Li(
                        html.A(
                            [
                                html.I(className="fas fa-home"),  # Add icon
                                html.Span("Dashboard"),
                            ],
                            href="#",
                            className="menu-item",
                        ),
                    ),
                    html.Li(
                        html.A(
                            [
                                # Add icon
                                html.I(className="fas fa-chart-bar"),
                                html.Span("Estadísticas"),
                            ],
                            href="#",
                            className="menu-item",
                        ),
                    ),
                    html.Li(
                        html.A(
                            [
                                html.I(className="fas fa-truck"),  # Add icon
                                html.Span("Camiones"),
                            ],
                            href="#",
                            className="menu-item",
                        ),
                    ),
                    html.Li(
                        html.A(
                            [
                                html.I(className="fas fa-wrench"),  # Add icon
                                html.Span("Mantenimientos"),
                            ],
                            href="#",
                            className="menu-item",
                        ),
                    ),
                    html.Li(
                        html.A(
                            [
                                # Add icon
                                html.I(className="fas fa-dollar-sign"),
                                html.Span("Gastos"),
                            ],
                            href="#",
                            className="menu-item",
                        ),
                    ),
                ],
                className="sidebar-menu",
            ),
        ],
        className="sidebar",
    )
