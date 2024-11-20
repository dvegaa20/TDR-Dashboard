from dash import dcc, html
import plotly.express as px
import pandas as pd


def vehicle_age(data):
    current_year = pd.to_datetime("today").year
    data["VehicleAge"] = current_year - data["UnitYear"]

    vehicle_age_counts = data.groupby("VehicleAge")["UnitNumber"].nunique().sort_index()

    fig_vehicle_age = px.bar(
        vehicle_age_counts, x=vehicle_age_counts.index, y=vehicle_age_counts.values
    )

    fig_vehicle_age.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Conteo por Antiguedad de Tractos",
        yaxis_title=None,
    )
    return html.Div(
        [
            dcc.Graph(
                id="iris-graph",
                figure=fig_vehicle_age,
                config={"displayModeBar": False},
                style={"height": "89vh", "width": "97vw"},
            )
        ]
    )


def example():
    print("hola mundo")
