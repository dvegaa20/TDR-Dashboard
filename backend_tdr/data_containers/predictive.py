from dash import dcc, html
import plotly.express as px
import pandas as pd


def standard_layout(fig):
    fig.update_layout(
        margin=dict(l=100, r=30, t=50, b=50),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(size=12),
    )
    return fig


def standard_style(height="2000px", overflowY="scroll"):
    return {
        "overflowY": overflowY,
        "height": height,
        "border": "1px solid #ccc",
        "padding": "10px",
    }


def standard_graph():
    return {
        "config": {"displayModeBar": False},
        "style": {"height": "100%", "width": "97vw"},
        "loading_state": {"is_loading": False},
    }
