from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objs as go

app = Dash()

df = pd.read_csv(
    "https://gist.githubusercontent.com/chriddyp/"
    + "5d1ea79569ed194d432e56108a04d188/raw/"
    + "a9f9e8076b837d541398e999dcbac2b2826a81f8/"
    + "gdp-life-exp-2007.csv"
)


app.layout = html.Div(
    [
        dcc.Graph(
            id="life-exp-vs-gdp",
            style={"height": "800px"},
            figure={
                "data": [
                    go.Scatter(
                        x=df[df["continent"] == i]["gdp per capita"],
                        y=df[df["continent"] == i]["life expectancy"],
                        text=df[df["continent"] == i]["country"],
                        mode="markers",
                        opacity=0.7,
                        marker={"size": 15, "line": {"width": 0.5, "color": "white"}},
                        name=i,
                    )
                    for i in df.continent.unique()
                ],
                "layout": go.Layout(
                    xaxis={"type": "log", "title": "GDP Per Capita"},
                    yaxis={"title": "Life Expectancy"},
                    margin={"l": 40, "b": 40, "t": 10, "r": 10},
                    legend={"x": 0, "y": 1},
                    hovermode="closest",
                ),
            },
        )
    ]
)

if __name__ == "__main__":
    app.run()