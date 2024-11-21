from dash import dcc, html
import plotly.express as px


def cost_distribution(data):
    data = data.copy()
    # Elimina los primeros 9 caracteres (Codigo)
    data["JobCode"] = data["JobCode"].str[9:]

    # Genera el gráfico de pastel
    fig_cost_distribution = px.pie(
        data,
        values="TotalAmount",
        names="JobCode",
        color="JobCode",
    )

    # Configuración de las trazas
    fig_cost_distribution.update_traces(
        textposition="inside",
        textinfo="percent+label",
        insidetextorientation="radial",
        hoverinfo="label+percent+value",  # Muestra porcentaje y valor absoluto

        # Plantilla personalizada para el hover
        hovertemplate="<b>%{label}</b><br>Porcentaje: %{percent}<br>Total: $%{value}<extra></extra>",
    )

    # Configuración de diseño
    fig_cost_distribution.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title="Distribución de Gastos por Motivo de Reparación",
        title_x=0.5,
        uniformtext_minsize=12,
        uniformtext_mode="hide",
    )

    # Devuelve el Div con el gráfico
    return html.Div(
        [
            dcc.Graph(
                id="cost-distribution-graph",
                figure=fig_cost_distribution,

                config={"displayModeBar": False},

                style={"height": "100%", "width": "100%"},
            )
        ],
        style={"height": "89vh", "width": "97vw"},  # Ajuste del tamaño del Div
    )
