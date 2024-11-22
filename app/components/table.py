from dash import dash_table

def create_table(data):
    """
    Create a reusable table component.

    :param data: A pandas DataFrame.
    :return: A DataTable component.
    """
    return dash_table.DataTable(
        data=data.to_dict("records"),
        columns=[{"name": col, "id": col} for col in data.columns],
        style_table={"overflowX": "auto", "margin-top": "20px"},
        style_header={"backgroundColor": "#f8f9fa", "fontWeight": "bold"},
        style_cell={"textAlign": "left", "padding": "10px"},
    )
