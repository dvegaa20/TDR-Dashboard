from dash import html


def create_sidebar():
    return html.Div(
        [
            # Main Content

            html.Link(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",
            ),
            # Sidebar header with logo
            html.Div(
                [
                    html.Img(src="/assets/tdr_logo.png",
                             alt="Logo", className="logo"),
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
                            href="/",
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
                            href="/spendings",
                            className="menu-item",
                        ),
                    ),
                ],
                className="sidebar-menu",
            ),
        ],
        className="sidebar",
    )
