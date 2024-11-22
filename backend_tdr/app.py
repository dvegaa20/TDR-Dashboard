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


app = dash.Dash(__name__)
server = app.server
CORS(server)

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    """
    Function to render the page based on the url pathname.
    It calls the corresponding function from the data_containers module
    to generate the page content.
    """

    # Stats
    if pathname == "/failure_frequency":
        return failure_frequency(tdr_data)
    elif pathname == "/avg_repair_frecuency":
        return average_repair_frecuency(tdr_data)
    elif pathname == "/monthly_repair_distribution":
        return monthly_failure_distribution(tdr_data)
    elif pathname == "/mtbf":
        return mtbf(tdr_data)

    # Tractos
    elif pathname == "/tractos_failure_distribution":
        return unit_failure_distribution(tdr_data)
    elif pathname == "/tractos_cost_distribution":
        return cost_per_unit(tdr_data)
    elif pathname == "/tractos_age":
        return vehicle_age(tdr_data)

    # Mantenimientos

    # Gastos
    elif pathname == "/cost_distribution":
        return cost_distribution(tdr_data)
    elif pathname == "/calculate_maintenance_costs":
        return maintenance_comparison_chart(tdr_data)

    # Análisis Predictivo

    # 404
    else:
        return "Error al cargar la gráfica (404)"


if __name__ == "__main__":
    app.run_server(debug=False)
