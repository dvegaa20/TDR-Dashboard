import plotly.graph_objects as go
import pandas as pd
from dash import dcc, html
import plotly.express as px


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


def cost_distribution(data):
    """
    Generates a pie chart of the cost distribution by job code.

    Args:
    data: The data to generate the chart from. Must contain the columns "TotalAmount" and "JobCode".

    Returns:
    A Dash HTML component containing the chart.
    """

    data = data.copy()
    data["JobCode"] = data["JobCode"].str[9:]

    fig_cost_distribution = px.pie(
        data,
        values="TotalAmount",
        names="JobCode",
        color="JobCode",
        title="Distribución de Gastos por Motivo de Reparación",
    )

    fig_cost_distribution.update_traces(
        textposition="inside",
        textinfo="percent+label",
        insidetextorientation="radial",
        hoverinfo="label+percent+value",
        hovertemplate="<b>%{label}</b><br>Porcentaje: %{percent}<br>Total: $%{value}<extra></extra>",
    )

    fig_cost_distribution = standard_layout(fig_cost_distribution)
    fig_cost_distribution.update_layout(
        uniformtext_mode="hide",
    )

    return html.Div(
        style=standard_style(height="90vh"),
        children=[
            dcc.Graph(
                id="cost-distribution-graph",
                figure=fig_cost_distribution,
                config={"displayModeBar": False},
                style={"height": "100%", "width": "100%"},
            )
        ],
    )


def calculate_maintenance_costs(data):
    """
    Generates a bar chart of maintenance costs and job quantities by year.

    Args:
    data: A DataFrame containing maintenance data. Must include the columns "OpenedDate", "JobCode", "OrderID", and "TotalAmount".

    Returns:
    A Dash HTML component containing the chart.
    """

    data["Year"] = pd.to_datetime(data["OpenedDate"]).dt.year

    pm_jobs = data[data["JobCode"].str.contains("preventivo", case=False, na=False)]
    correctivo_jobs = data[
        data["JobCode"].str.contains("CORRECTIVO", case=False, na=False)
    ]
    auxilio_jobs = data[
        data["JobCode"].str.contains("AUXILIO CARRETERO", case=False, na=False)
    ]

    stats = (
        data.groupby("Year")
        .apply(
            lambda group: {
                "PM_Quantity": pm_jobs[pm_jobs["Year"] == group.name][
                    "OrderID"
                ].nunique(),
                "Correctivo_Quantity": correctivo_jobs[
                    correctivo_jobs["Year"] == group.name
                ]["OrderID"].nunique(),
                "Auxilio_Quantity": auxilio_jobs[auxilio_jobs["Year"] == group.name][
                    "OrderID"
                ].nunique(),
                "PM_Cost": pm_jobs[pm_jobs["Year"] == group.name]["TotalAmount"]
                .sum()
                .round(2),
                "Correctivo_Cost": correctivo_jobs[
                    correctivo_jobs["Year"] == group.name
                ]["TotalAmount"].sum(),
                "Auxilio_Cost": auxilio_jobs[auxilio_jobs["Year"] == group.name][
                    "TotalAmount"
                ].sum(),
            }
        )
        .to_list()
    )

    stats_data = pd.DataFrame(stats, index=data["Year"].unique()).reset_index(
        names="Year"
    )

    return stats_data, html.Div(
        style=standard_style(height="90vh"),
        children=[
            dcc.Graph(
                id="maintenance-costs-graph",
                figure=stats_data,
                **standard_graph(),
            )
        ],
    )


def maintenance_comparison_chart(data):
    stats_data, _ = calculate_maintenance_costs(data)

    df = pd.DataFrame(
        {
            "Year": stats_data["Year"],
            "PM_Cost": stats_data["PM_Cost"],
            "Correctivo_Cost": stats_data["Correctivo_Cost"],
            "Auxilio_Cost": stats_data["Auxilio_Cost"],
        }
    )

    df_melted = df.melt(
        id_vars=["Year"],
        value_vars=["PM_Cost", "Correctivo_Cost", "Auxilio_Cost"],
        var_name="Tipo de Mantenimiento",
        value_name="Costo Total ($)",
    )

    fig_cost_comparison = px.bar(
        df_melted,
        x="Year",
        y="Costo Total ($)",
        color="Tipo de Mantenimiento",
        barmode="group",
        title="Comparación de Costos de Mantenimiento (PM, Correctivo, Auxilio Carretero)",
        labels={
            "Year": "Año",
            "Costo Total ($)": "Costo Total ($)",
            "Tipo de Mantenimiento": "Tipo de Mantenimiento",
        },
    )

    fig_cost_comparison = standard_layout(fig_cost_comparison)

    fig_cost_comparison.update_layout(
        legend_title="Tipo de Mantenimiento", xaxis=dict(tickmode="linear")
    )

    return html.Div(
        style=standard_style(height="90vh"),
        children=[
            dcc.Graph(
                id="maintenance-comparison-chart",
                figure=fig_cost_comparison,
                **standard_graph(),
            )
        ],
    )
