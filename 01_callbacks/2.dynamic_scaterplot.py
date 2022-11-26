from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/"
    "datasets/master/gapminderDataFiveYear.csv"
)

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(id="graph-with-slider"),
        dcc.Slider(
            df["year"].min(),
            df["year"].max(),
            step=None,
            value=df["year"].min(),
            marks={str(year): str(year) for year in df["year"].unique()},
            id="year-slider",
        ),
    ]
)


@app.callback(
    Output("graph-with-slider", "figure"),
    Input("year-slider", "value"),
)
def update_figure(selected_year: int) -> go.Figure:
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(
        filtered_df,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=55,
    )

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == "__main__":
    app.run(debug=True)
