from dash import dcc, html
import plotly.express as px
import pandas as pd


def vehicle_age(data):
    current_year = pd.to_datetime("today").year
    data["VehicleAge"] = current_year - data["UnitYear"]

    vehicle_age_counts = data.groupby("VehicleAge")["UnitNumber"].nunique().sort_index()

    fig_vehicle_age = px.bar(
        vehicle_age_counts,
        x=vehicle_age_counts.index,
        y=vehicle_age_counts.values,
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


def repair_frecuency(data):
    # Calcular frecuencia de reparaciones por unidad
    component_freq_total = data["UnitNumber"].value_counts()

    # Crear el gráfico con barras horizontales
    fig_repair_frecuency = px.bar(
        x=component_freq_total.values,
        y=component_freq_total.index,
        orientation="h",  # Orientación horizontal
        labels={"x": "Frecuencia de Reparaciones", "y": "Código de la Unidad"},
        title="Frecuencia Total de Reparación de Componentes",
    )

    # Ajustar el diseño del gráfico
    fig_repair_frecuency.update_layout(
        margin=dict(l=50, r=30, t=40, b=40),
        paper_bgcolor="rgba(255,255,255,1)",  # Fondo blanco
        plot_bgcolor="rgba(255,255,255,1)",
        xaxis_title="Frecuencia de Reparaciones",
        yaxis_title="Código de la Unidad",
    )

    # Retornar el gráfico como un componente Dash
    return html.Div(
        [
            dcc.Graph(
                id="repair-frequency-graph",
                figure=fig_repair_frecuency,
                config={"displayModeBar": True},  # Mostrar barra de herramientas
                style={"height": "89vh", "width": "97vw"},
            )
        ]
    )
