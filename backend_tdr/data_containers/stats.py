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


def failure_frequency(data):
    """
    Generates a bar chart of the failure frequency by component.

    Args:
    data: The data to generate the chart from. Must contain the columns "ComponentCode" and "JobCode".

    Returns:
    A Dash HTML component containing the chart.
    """

    fallas_por_componente = (
        data.groupby("ComponentCode")["JobCode"]
        .count()
        .reset_index()
        .sort_values("JobCode", ascending=True)
        .rename(columns={"JobCode": "CantidadFallas"})
    )

    fig_fallas = px.bar(
        fallas_por_componente,
        x="CantidadFallas",
        y="ComponentCode",
        title="Frecuencia de Fallas por Componente",
        labels={
            "ComponentCode": "Componente",
            "CantidadFallas": "Frecuencia de Fallas",
        },
    )

    fig_fallas = standard_layout(fig_fallas)

    fig_fallas.update_traces(
        marker=dict(color="steelblue", opacity=0.8, line=dict(color="black", width=1.5))
    )

    return html.Div(
        style=standard_style(),
        children=[
            dcc.Graph(
                id="fallas-por-componente",
                figure=fig_fallas,
                **standard_graph(),
            )
        ],
    )


def average_repair_frecuency(data):
    """
    Generates a bar chart of the average repair duration by component.

    Args:
    data: The data to generate the chart from. Must contain the columns "ComponentCode", "OpenedDate", and "CompleteDate".

    Returns:
    A Dash HTML component containing the chart.
    """

    data["OpenedDate"] = pd.to_datetime(data["OpenedDate"])
    data["CompleteDate"] = pd.to_datetime(data["CompleteDate"])

    data["RepairDuration"] = (
        data["CompleteDate"] - data["OpenedDate"]
    ).dt.total_seconds() / 3600

    promedio_duracion = (
        data.groupby("ComponentCode")["RepairDuration"]
        .mean()
        .reset_index()
        .sort_values("RepairDuration", ascending=True)
        .rename(columns={"RepairDuration": "PromedioDuracion"})
    )

    fig_tiempos = px.bar(
        promedio_duracion,
        x="PromedioDuracion",
        y="ComponentCode",
        orientation="h",
        title="Promedio de Tiempos de Reparación por Componente",
        labels={"ComponentCode": "Componente", "PromedioDuracion": "Promedio (Horas)"},
    )

    fig_tiempos = standard_layout(fig_tiempos)

    fig_tiempos.update_traces(
        marker=dict(
            color="darkorange", opacity=0.8, line=dict(color="black", width=1.5)
        )
    )

    return html.Div(
        style=standard_style(),
        children=[
            dcc.Graph(
                id="promedio-tiempos-reparacion",
                figure=fig_tiempos,
                **standard_graph(),
            )
        ],
    )


def monthly_failure_distribution(data, simplified=False):
    """
    Generates a bar chart of the distribution of failures by month.

    Args:
    data: The data to generate the chart from. Must contain the columns "JobCode" and "OpenedDate".
    simplified (bool): If True, the chart will omit axis labels for use in a dashboard.

    Returns:
    A Dash HTML component containing the chart.
    """

    data["OpenedDate"] = pd.to_datetime(data["OpenedDate"])
    data["Mes"] = data["OpenedDate"].dt.month

    fallas_por_mes = (
        data.groupby("Mes")["JobCode"]
        .count()
        .reset_index()
        .rename(columns={"JobCode": "DistribucionFallas"})
    )

    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }
    fallas_por_mes["MesNombre"] = fallas_por_mes["Mes"].map(meses)
    fallas_por_mes = fallas_por_mes.sort_values("Mes")

    fig_fallas_mes = px.bar(
        fallas_por_mes,
        x="MesNombre",
        y="DistribucionFallas",
        title="Distribución de Fallas por Mes",
        labels={
            "MesNombre": "Mes",
            "DistribucionFallas": "Cantidad de Fallas",
        },
        text="DistribucionFallas",
    )

    fig_fallas_mes = standard_layout(fig_fallas_mes)

    if simplified:
        fig_fallas_mes.update_layout(
            xaxis_title=None,
            yaxis_title=None,
            margin=dict(t=30, l=0, r=40, b=0),
        )

    fig_fallas_mes.update_traces(
        marker=dict(
            color="royalblue", opacity=0.8, line=dict(color="black", width=1.5)
        ),
        textfont=dict(size=10),
    )

    return html.Div(
        style=standard_style(height="89vh"),
        children=[
            dcc.Graph(
                id="distribucion-fallas-mes",
                figure=fig_fallas_mes,
                **standard_graph(),
            )
        ],
    )


# Aún no sale bien
def mtbf(data):
    # Convertir columnas de fechas a formato datetime
    data["OpenedDate"] = pd.to_datetime(data["OpenedDate"])
    data["ClosedDate"] = pd.to_datetime(data["ClosedDate"])

    # Ordenar los datos por OpenedDate
    data = data.sort_values(by="OpenedDate").reset_index(drop=True)

    # Calcular tiempo operativo entre fallas
    data["TiempoEntreFallas"] = (
        data["OpenedDate"].shift(-1) - data["ClosedDate"]
    ).dt.total_seconds() / (
        60 * 60 * 24
    )  # Convertir a días

    # Asegurar valores positivos
    data["TiempoEntreFallas"] = data["TiempoEntreFallas"].apply(
        lambda x: x if x > 0 else None
    )

    # Agrupar por mes y calcular el MTBF
    data["Mes"] = data["OpenedDate"].dt.to_period("M").dt.to_timestamp()
    mtbf_por_mes = (
        data.groupby("Mes")["TiempoEntreFallas"]
        .mean()
        .reset_index()
        .rename(columns={"TiempoEntreFallas": "MTBF"})
    )

    # Creación de Gráfica
    fig_mtbf = px.line(
        mtbf_por_mes,
        x="Mes",
        y="MTBF",
        title="Tiempo Medio Entre Fallas (MTBF)",
        labels={"Mes": "Mes", "MTBF": "MTBF (días)"},
    )

    # Diseño de Gráfica
    fig_mtbf = standard_layout(fig_mtbf)

    fig_mtbf.update_traces(
        line=dict(color="royalblue", width=2),
        marker=dict(size=8),
    )

    # Contenedor del gráfico
    return html.Div(
        style=standard_style(height="89vh"),
        children=[
            dcc.Graph(
                id="mtbf-graph",
                figure=fig_mtbf,
                **standard_graph(),
            )
        ],
    )
