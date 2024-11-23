import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from data_containers.stats import (
    failure_frequency,
    average_repair_frecuency,
    monthly_failure_distribution,
    get_stats_data,
)
from data_containers.tractos import (
    unit_failure_distribution,
    cost_per_unit,
    vehicle_performance,
    vehicle_age,
    get_tractos_data,
)

from data_containers.maintenance import (
    frecuencia_actividades_mantenimiento,
    actividades_por_parte,
    duracion_promedio_por_tipo,
    get_maintenance_data,
)
from data_containers.spendings import (
    cost_distribution,
    maintenance_comparison_chart,
    get_spendings_data,
)

# from data_containers.predictive import predictive_layout
from data import tdr_data
from flask_cors import CORS


app = dash.Dash(__name__)
server = app.server
CORS(server)

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        dcc.Loading(
            id="loading",
            type="cube",  # 'circle' | 'dot' | 'default' | 'cube'
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

# Routes
route_map = {
    # Dashboard
    "/dash_monthly_repair_distribution": lambda data: monthly_failure_distribution(
        data, simplified=True
    ),
    "/dash_tractos_failure_distribution": lambda data: unit_failure_distribution(
        data, simplified=True
    ),
    "/dash_part_number": lambda data: actividades_por_parte(data, simplified=True),
    "/dash_cost_distribution": lambda data: maintenance_comparison_chart(
        data, simplified=True
    ),
    # Stats
    "/failure_frequency": failure_frequency,
    "/avg_repair_frecuency": average_repair_frecuency,
    "/monthly_repair_distribution": monthly_failure_distribution,
    # Tractos
    "/tractos_failure_distribution": unit_failure_distribution,
    "/tractos_cost_distribution": cost_per_unit,
    "/tractos_performance": vehicle_performance,  # Falta revisar
    "/tractos_age": vehicle_age,
    # Mantenimientos
    "/part_number": actividades_por_parte,
    "/maintenance_activities": frecuencia_actividades_mantenimiento,
    "/time_to_complete": duracion_promedio_por_tipo,
    # Gastos
    "/maintenance_costs": maintenance_comparison_chart,
    "/cost_distribution": cost_distribution,
    # Análisis Predictivo
    ## Faltan lo que pienses pa esa
}


# API Endpoints
@app.server.route("/api/data/stats", methods=["GET"])
def api_stats_data():
    return get_stats_data(tdr_data)


@app.server.route("/api/data/tractos", methods=["GET"])
def api_tractos_data():
    return get_tractos_data(tdr_data)


@app.server.route("/api/data/spendings", methods=["GET"])
def api_spendings_data():
    return get_spendings_data(tdr_data)


@app.server.route("/api/data/maintenance", methods=["GET"])
def api_maintenance_data():
    return get_maintenance_data(tdr_data)


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
