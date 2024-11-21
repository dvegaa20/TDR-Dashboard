import pandas as pd
from dash import dcc, html
import plotly.express as px


def cost_distribution(data):
    fig_cost_distribution = px.pie(data, values="TotalAmount", names="RepairReason")

    fig_cost_distribution.update_traces(
        textposition="inside",
        textinfo="percent+label",
        insidetextorientation="radial",
    )

    fig_cost_distribution.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        uniformtext_minsize=12,
        uniformtext_mode="hide",
    )
    return html.Div(
        [
            dcc.Graph(
                id="cost-distribution-graph",
                figure=fig_cost_distribution,
                config={"displayModeBar": False},
                style={"height": "89vh", "width": "97vw"},
            )
        ]
    )
