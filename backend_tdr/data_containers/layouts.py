import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

def iris_layout(data):
    fig_iris = px.scatter(data, x='Kilometers', y='TotalAmount', title='Iris Dataset')
    fig_iris.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return html.Div([
        dcc.Graph(
            id='iris-graph',
            figure=fig_iris,
            config={"displayModeBar": False},
            style={"height": "89vh", "width": "97vw"}
        )
    ])