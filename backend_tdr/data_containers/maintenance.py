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


def standard_style(height="2000px"):
    return {
        "overflowY": "scroll",
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


def actividades_por_parte(data, simplified=False):
    """
    Generates a stacked bar chart showing the count of repairs by PartNumber grouped by month.

    Args:
    data: The data to generate the chart from. Must contain the columns "OpenedDate" and "PartNumber".

    Returns:
    A Dash HTML component containing the chart.
    """

    data["OpenedDate"] = pd.to_datetime(data["OpenedDate"])

    data["Mes"] = data["OpenedDate"].dt.to_period("M").astype(str)

    actividades_mensuales = (
        data.groupby(["Mes", "PartNumber"])
        .size()
        .reset_index(name="CantidadActividades")
    )

    fig_actividades = px.bar(
        actividades_mensuales,
        x="Mes",
        y="CantidadActividades",
        color="PartNumber",
        title="Recuento de Reparaciones por Parte y Mes",
        labels={
            "Mes": "Mes",
            "CantidadActividades": "Cantidad de Actividades",
            "PartNumber": "Número de Parte:",
        },
    )

    fig_actividades = standard_layout(fig_actividades)

    fig_actividades.update_layout(
        xaxis=dict(
            title=None,
            ticklabelstandoff=10,
        )
    )

    if simplified:
        fig_actividades.update_layout(
            xaxis_title=None,
            yaxis_title=None,
            margin=dict(t=30, l=20, r=20, b=0),
            showlegend=False,
        )

    return html.Div(
        style=standard_style(height="89vh"),
        children=[
            dcc.Graph(
                id="actividades-por-partnumber-mes",
                figure=fig_actividades,
                **standard_graph(),
            )
        ],
    )


def frecuencia_actividades_mantenimiento(data):
    """
    Generates a bar chart showing the frequency of maintenance activities by type.

    Args:
    data: The data to generate the chart from. Must contain the columns "JobCode" and "RepairReason".

    Returns:
    A Dash HTML component containing the chart.
    """

    actividades_frecuencia = (
        data.groupby("RepairReason")["JobCode"]
        .count()
        .reset_index()
        .rename(columns={"JobCode": "Frecuencia", "RepairReason": "Actividad"})
        .sort_values("Frecuencia", ascending=False)
    )

    actividades_frecuencia = actividades_frecuencia[
        actividades_frecuencia["Frecuencia"] > 5
    ]

    fig_actividades = px.bar(
        actividades_frecuencia,
        x="Actividad",
        y="Frecuencia",
        title="Frecuencia de Actividades de Mantenimiento",
        labels={
            "Frecuencia": "Número de Actividades",
        },
    )

    fig_actividades = standard_layout(fig_actividades)

    fig_actividades.update_layout(
        xaxis=dict(
            tickangle=45,
            tickfont=dict(size=8),
            title=None,
        ),
    )

    fig_actividades.update_traces(
        marker=dict(color="orange", opacity=0.8, line=dict(color="black", width=1.5))
    )

    return html.Div(
        style=standard_style(height="89vh"),
        children=[
            dcc.Graph(
                id="frecuencia-actividades",
                figure=fig_actividades,
                **standard_graph(),
            )
        ],
    )


def duracion_promedio_por_tipo(data):
    """
    Generates a bar chart showing the average duration of maintenance activities by order type.

    Args:
    data: The data to generate the chart from. Must contain the columns "PartNumber", "OpenedDate", and "ClosedDate".

    Returns:
    A Dash HTML component containing the chart.
    """

    data["OpenedDate"] = pd.to_datetime(data["OpenedDate"])
    data["ClosedDate"] = pd.to_datetime(data["ClosedDate"])

    data["DuracionDias"] = (data["ClosedDate"] - data["OpenedDate"]).dt.days

    duracion_promedio = (
        data.groupby("PartNumber")["DuracionDias"]
        .mean()
        .reset_index()
        .sort_values("DuracionDias", ascending=False)
    )

    duracion_promedio = duracion_promedio[duracion_promedio["DuracionDias"] > 2]

    fig_duracion = px.bar(
        duracion_promedio,
        x="PartNumber",
        y="DuracionDias",
        title="Duración Promedio de Actividades por Tipo de Orden",
        labels={
            "DuracionDias": "Duración Promedio (días)",
        },
    )

    fig_duracion = standard_layout(fig_duracion)

    fig_duracion.update_layout(
        xaxis=dict(
            tickfont=dict(size=8),
            title=None,
        )
    )

    return html.Div(
        style=standard_style(height="89vh"),
        children=[
            dcc.Graph(
                id="duracion-promedio-por-tipo",
                figure=fig_duracion,
                **standard_graph(),
            )
        ],
    )
