from dash import dcc, html
from flask import jsonify
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


def unit_failure_distribution(data, simplified=False):
    """
    Generates a bar chart of the distribution of failures per vehicle unit.

    Args:
    data: The data to generate the chart from. Must contain the columns "UnitNumber" and "JobCode".
    simplified (bool): If True, the chart will omit axis labels for use in a dashboard.

    Returns:
    A Dash HTML component containing the chart.
    """

    failures_per_vehicle = (
        data.groupby("UnitNumber")["JobCode"]
        .count()
        .reset_index()
        .rename(columns={"JobCode": "CantidadFallas"})
    )

    fig_failures_per_vehicle = px.bar(
        failures_per_vehicle,
        x="UnitNumber",
        y="CantidadFallas",
        title="Distribución de Fallas por Tracto",
        text="CantidadFallas",
    )

    fig_failures_per_vehicle = standard_layout(fig_failures_per_vehicle)

    if simplified:
        fig_failures_per_vehicle.update_layout(
            xaxis_title=None,
            yaxis_title=None,
            margin=dict(t=30, l=0, r=40, b=0),
        )

    fig_failures_per_vehicle.update_traces(
        hovertemplate="Tracto (Unidad) = %{x}<br>Cantidad de Fallas = %{y}",
        marker=dict(
            color="indianred", opacity=0.8, line=dict(color="black", width=1.5)
        ),
        textfont=dict(size=10),
    )

    fig_failures_per_vehicle.update_layout(
        xaxis=dict(
            type="category",
            tickangle=45,
        )
    )

    return html.Div(
        style=standard_style(height="88vh"),
        children=[
            dcc.Graph(
                id="distribucion-fallas-vehiculo",
                figure=fig_failures_per_vehicle,
                **standard_graph(),
            )
        ],
    )


def cost_per_unit(data):
    """
    Generates a bar chart of the total cost per vehicle.

    Args:
    data: The data to generate the chart from. Must contain the columns "UnitNumber" and "TotalAmount".

    Returns:
    A Dash HTML component containing the chart.
    """
    cost_per_unit = (
        data.groupby("UnitNumber")["TotalAmount"]
        .sum()
        .reset_index()
        .rename(columns={"TotalAmount": "CostoTotal"})
        .round(2)
    )

    fig_cost_per_unit = px.bar(
        cost_per_unit,
        x="UnitNumber",
        y="CostoTotal",
        title="Costo Total por Tracto",
        text="CostoTotal",
    )

    fig_cost_per_unit = standard_layout(fig_cost_per_unit)

    fig_cost_per_unit.update_traces(
        hovertemplate="Tracto (Unidad) = %{x}<br>Costo de Reparaciones = $%{y}",
        marker=dict(
            color="darkgreen", opacity=0.8, line=dict(color="black", width=1.5)
        ),
        textfont=dict(size=10),
    )

    fig_cost_per_unit.update_layout(
        xaxis=dict(
            type="category",
            tickangle=45,
        )
    )

    return html.Div(
        style=standard_style(height="88vh"),
        children=[
            dcc.Graph(
                id="costo-total-vehiculo",
                figure=fig_cost_per_unit,
                **standard_graph(),
            )
        ],
    )


def vehicle_performance(data):
    """
    Generates a line chart showing the monthly mileage performance for each truck.

    Args:
    data: The data to generate the chart from. Must contain the columns "OpenedDate", "UnitNumber", and "Kilometers".

    Returns:
    A Dash HTML component containing the chart.
    """
    data["OpenedDate"] = pd.to_datetime(data["OpenedDate"])

    data["Mes"] = data["OpenedDate"].dt.to_period("M").astype(str)

    kilometraje_mensual = (
        data.groupby(["UnitNumber", "Mes"])["Kilometers"]
        .sum()
        .reset_index()
        .sort_values("Mes")
    )

    kilometraje_mensual["Kilometers"] = kilometraje_mensual["Kilometers"] / 1000

    fig_kilometraje = px.line(
        kilometraje_mensual,
        x="Mes",
        y="Kilometers",
        color="UnitNumber",
        title="Rendimiento de los Tractos por Kilometraje Mensual",
        labels={
            "Kilometers": "Kilómetros Recorridos",
            "UnitNumber": "Tracto",
        },
        line_group="UnitNumber",
    )

    fig_kilometraje = standard_layout(fig_kilometraje)

    fig_kilometraje.update_traces(
        line=dict(width=2),
        hovertemplate="Mes = %{x}<br>Kilómetros Recorridos = %{y:,} km",
        marker=dict(opacity=0.8),
    )
    fig_kilometraje.update_layout(
        xaxis=dict(type="category", title=None),
        yaxis=dict(tickformat=","),
        legend=dict(title="Tracto", orientation="h", y=-0.2),
    )

    return html.Div(
        style=standard_style(height="88vh"),
        children=[
            dcc.Graph(
                id="rendimiento-por-kilometraje",
                figure=fig_kilometraje,
                **standard_graph(),
            )
        ],
    )


def vehicle_age(data):
    """
    Generates a bar chart of the distribution of tractor units by age.

    Args:
    data: The data to generate the chart from. Must contain the columns "UnitNumber" and "UnitYear".

    Returns:
    A Dash HTML component containing the chart.
    """

    current_year = pd.to_datetime("today").year
    data["VehicleAge"] = current_year - data["UnitYear"]

    vehicle_age_counts = (
        data.groupby("VehicleAge")["UnitNumber"]
        .nunique()
        .reset_index()
        .rename(columns={"UnitNumber": "CantidadTractos"})
    )

    fig_vehicle_age = px.bar(
        vehicle_age_counts,
        x="VehicleAge",
        y="CantidadTractos",
        title="Distribución de Tractos por Antigüedad",
        text="CantidadTractos",
    )

    fig_vehicle_age = standard_layout(fig_vehicle_age)

    fig_vehicle_age.update_traces(
        hovertemplate="Años de Antigüedad = %{x}<br>Cantidad de Tractos = %{y}",
        marker=dict(
            color="royalblue", opacity=0.8, line=dict(color="black", width=1.5)
        ),
        textfont=dict(size=10),
    )
    return html.Div(
        style=standard_style(height="88vh"),
        children=[
            dcc.Graph(
                id="distribucion-fallas-mes",
                figure=fig_vehicle_age,
                **standard_graph(),
            )
        ],
    )


def get_tractos_data(data):
    columns = [
        "UnitNumber",
        "JobCode",
        "TotalAmount",
        "Kilometers",
    ]
    filtered_data = data[columns]

    return jsonify(filtered_data.to_dict(orient="records"))
