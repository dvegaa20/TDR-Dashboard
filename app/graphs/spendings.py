from dash import dcc
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


def cost_distribution(data):
    data = data.copy()
    # Remove the first 9 characters from JobCode
    data["JobCode"] = data["JobCode"].str[9:]

    # Generate the pie chart
    fig_cost_distribution = px.pie(
        data,
        values="TotalAmount",
        names="JobCode",
        color="JobCode",
    )

    # Configure trace details
    fig_cost_distribution.update_traces(
        textposition="none",  # Do not show text inside the chart
        hoverinfo="label+percent+value",  # Show details on hover
        hovertemplate="<b>%{label}</b><br>Porcentaje: %{percent}<br>Total: $%{value}<extra></extra>",
    )

    # Layout configuration
    fig_cost_distribution.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title_x=0.5,
        uniformtext_minsize=12,
        uniformtext_mode="hide",
    )

    # Return the dcc.Graph
    return dcc.Graph(
        id="cost-distribution-graph",
        figure=fig_cost_distribution,
        config={"displayModeBar": False},
        style={"height": "100%", "width": "100%"},
    )


def calculate_maintenance_costs(df):
    # Convert 'OpenedDate' to datetime and extract the year
    df['Year'] = pd.to_datetime(
        df['OpenedDate']).dt.year

    # Filter for PM, Correctivo, and Auxilio Carretero based on 'JobCode'
    pm_jobs = df[df['JobCode'].str.contains(
        'preventivo', case=False, na=False)]
    correctivo_jobs = df[df['JobCode'].str.contains(
        'CORRECTIVO', case=False, na=False)]
    auxilio_jobs = df[df['JobCode'].str.contains(
        'AUXILIO CARRETERO', case=False, na=False)]

    # Group by year and calculate stats
    stats = (
        df.groupby('Year')
        .apply(lambda group: {
            'PM_Quantity': pm_jobs[pm_jobs['Year'] == group.name]['OrderID'].nunique(),
            'Correctivo_Quantity': correctivo_jobs[correctivo_jobs['Year'] == group.name]['OrderID'].nunique(),
            'Auxilio_Quantity': auxilio_jobs[auxilio_jobs['Year'] == group.name]['OrderID'].nunique(),
            'PM_Cost': pm_jobs[pm_jobs['Year'] == group.name]['TotalAmount'].sum().round(2),
            'Correctivo_Cost': correctivo_jobs[correctivo_jobs['Year'] == group.name]['TotalAmount'].sum(),
            'Auxilio_Cost': auxilio_jobs[auxilio_jobs['Year'] == group.name]['TotalAmount'].sum()
        })
        .to_list()
    )

    # Convert stats to a DataFrame
    return pd.DataFrame(stats, index=df['Year'].unique()).reset_index(names='Year')


def maintenance_comparison_chart(df):
    # Calculate maintenance stats
    stats_df = calculate_maintenance_costs(df)

    # Create grouped bar chart using Plotly
    fig = go.Figure()

    # Add bars for PM, Correctivo, and Auxilio Carretero costs
    fig.add_trace(
        go.Bar(
            x=stats_df['Year'],
            y=stats_df['PM_Cost'],
            name='PM',
            marker_color='lightblue',
            text=stats_df['PM_Cost'],
            textposition='outside',
            hovertemplate="<b>Año:</b> %{x}<br><b>Costo PM:</b> $%{y:.2f}<br><b>Órdenes:</b> %{text}<extra></extra>"
        )
    )

    fig.add_trace(
        go.Bar(
            x=stats_df['Year'],
            y=stats_df['Correctivo_Cost'],
            name='Correctivo',
            marker_color='lightgreen',
            text=stats_df['Correctivo_Cost'],
            textposition='outside',
            hovertemplate="<b>Año:</b> %{x}<br><b>Costo Correctivo:</b> $%{y:.2f}<br><b>Órdenes:</b> %{text}<extra></extra>"
        )
    )

    fig.add_trace(
        go.Bar(
            x=stats_df['Year'],
            y=stats_df['Auxilio_Cost'],
            name='Auxilio Carretero',
            marker_color='lightcoral',
            text=stats_df['Auxilio_Cost'],
            textposition='outside',
            hovertemplate="<b>Año:</b> %{x}<br><b>Costo Auxilio:</b> $%{y:.2f}<br><b>Órdenes:</b> %{text}<extra></extra>"
        )
    )

    # Configure layout
    fig.update_layout(
        title="Comparación de Costos de Mantenimiento (PM, Correctivo, Auxilio Carretero)",
        xaxis_title="Año",
        yaxis_title="Costo Total ($)",
        barmode="group",
        bargap=0.15,
        bargroupgap=0.1,
        legend_title="Tipo de Mantenimiento",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    # Return the chart wrapped in a Dash Div
    return html.Div(
        style=standard_style(
            height="120vh"
        ),
        children=[
            dcc.Graph(
                id="maintenance-comparison-chart",
                figure=fig,
                config={"displayModeBar": False},
                style={"height": "150vh", "width": "97vw"}
            )
        ]
    )
