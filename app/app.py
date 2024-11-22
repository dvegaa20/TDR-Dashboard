from dash import Dash
from layout.main import create_layout

# Initialize Dash app
app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Mantenimiento TDR"

# Set layout
app.layout = create_layout()

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
