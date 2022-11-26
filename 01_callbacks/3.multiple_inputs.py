from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

from typing import Literal

app = Dash(__name__)

df = pd.read_csv("https://plotly.github.io/datasets/country_indicators.csv")

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            df["Indicator Name"].unique(),
                            "Fertility rate, total (births per woman)",
                            id="xaxis-column",
                        ),
                        dcc.RadioItems(
                            ["linear", "log"], "linear", id="xaxis-type", inline=True
                        ),
                    ],
                    style={"width": "48%", "display": "inline-block"},
                ),
                html.Div(
                    [
                        dcc.Dropdown(
                            df["Indicator Name"].unique(),
                            "Life expectancy at birth, total (years)",
                            id="yaxis-column",
                        ),
                        dcc.RadioItems(
                            ["linear", "log"], "linear", id="yaxis-type", inline=True
                        ),
                    ],
                    style={"width": "48%", "float": "right", "display": "inline-block"},
                ),
            ]
        ),
        dcc.Graph(id="indicator-graphic"),
        dcc.Slider(
            df["Year"].min(),
            df["Year"].max(),
            step=None,
            id="year--slider",
            value=df["Year"].max(),
            marks={str(year): str(year) for year in df["Year"].unique()},
        ),
    ],
    style={"font-family": "monospace"},
)


@app.callback(
    Output("indicator-graphic", "figure"),
    Input("xaxis-column", "value"),
    Input("yaxis-column", "value"),
    Input("xaxis-type", "value"),
    Input("yaxis-type", "value"),
    Input("year--slider", "value"),
)
def update_graph(
    xaxis_column_name: str,
    yaxis_column_name: str,
    xaxis_type: Literal["linear", "log"],
    yaxis_type: Literal["linear", "log"],
    year_value: int,
) -> go.Figure:
    dff = df[df["Year"] == year_value]

    fig = px.scatter(
        x=dff[dff["Indicator Name"] == xaxis_column_name]["Value"],
        y=dff[dff["Indicator Name"] == yaxis_column_name]["Value"],
        hover_name=dff[dff["Indicator Name"] == yaxis_column_name]["Country Name"],
    )

    fig.update_layout(margin={"l": 40, "b": 40, "t": 10, "r": 0}, hovermode="closest")
    fig.update_xaxes(title=xaxis_column_name, type=xaxis_type)
    fig.update_yaxes(title=yaxis_column_name, type=yaxis_type)

    return fig


if __name__ == "__main__":
    app.run(debug=True)
