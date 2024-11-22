import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from data_containers.stats import (
    failure_frequency,
    average_repair_frecuency,
    monthly_failure_distribution,
    mtbf,
)
from data_containers.tractos import (
    unit_failure_distribution,
    cost_per_unit,
    vehicle_age,
)

# from data_containers.maintenance import maintenance_distribution
from data_containers.spendings import cost_distribution, maintenance_comparison_chart

# from data_containers.predictive import predictive_layout
from data import tdr_data
from flask_cors import CORS
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML


app = dash.Dash(__name__)
server = app.server
CORS(server)

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        dcc.Loading(
            id="loading",
            type="dot",  # Puedes cambiar el tipo de loader: "default", "circle", "dot"
            children=html.Div(id="page-content"),
            style={
                "position": "fixed",
                "top": "50%",
                "left": "50%",
                "transform": "translate(-50%, -50%)",
            },
        ),
    ]
)

route_map = {
    # Stats
    "/failure_frequency": failure_frequency,
    "/avg_repair_frecuency": average_repair_frecuency,
    "/monthly_repair_distribution": monthly_failure_distribution,
    "/mtbf": mtbf,
    # Tractos
    "/tractos_failure_distribution": unit_failure_distribution,
    "/tractos_cost_distribution": cost_per_unit,
    "/tractos_age": vehicle_age,
    # Mantenimientos
    # Gastos
    "/cost_distribution": cost_distribution,
    "/calculate_maintenance_costs": maintenance_comparison_chart,
    # Análisis Predictivo
}


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    """
    Function to render the page based on the url pathname.
    It calls the corresponding function from the data_containers module
    to generate the page content.
    """
    if pathname in route_map:
        return route_map[pathname](tdr_data)
    else:
        return "Error al cargar la gráfica (404)"


if __name__ == "__main__":
    app.run_server(debug=False)
