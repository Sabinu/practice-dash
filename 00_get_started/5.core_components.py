from dash import Dash, html, dcc

app = Dash(__name__)


app.layout = html.Div(
    [
        html.Div(
            [
                html.Label("Dropdown"),
                dcc.Dropdown(
                    value="MTL",
                    options=[
                        {"label": "New York City", "value": "NYC"},
                        {"label": "Montréal", "value": "MTL"},
                        {"label": "San Francisco", "value": "SF"},
                    ],
                ),
            ],
            style={"marginBottom": "1rem"},
        ),
        html.Div(
            [
                html.Label("Multi-Select Dropdown"),
                dcc.Dropdown(
                    value=["MTL", "SF"],
                    multi=True,
                    options=[
                        {"label": "New York City", "value": "NYC"},
                        {"label": "Montréal", "value": "MTL"},
                        {"label": "San Francisco", "value": "SF"},
                    ],
                ),
            ],
            style={"marginBottom": "1rem"},
        ),
        html.Div(
            [
                html.Label("Radio Items"),
                dcc.RadioItems(
                    value="MTL",
                    options=[
                        {"label": "New York City", "value": "NYC"},
                        {"label": "Montréal", "value": "MTL"},
                        {"label": "San Francisco", "value": "SF"},
                    ],
                ),
            ],
            style={"marginBottom": "1rem"},
        ),
        html.Div(
            [
                html.Label("Checkboxes"),
                dcc.Checklist(
                    value=["MTL", "SF"],
                    options=[
                        {"label": "New York City", "value": "NYC"},
                        {"label": "Montréal", "value": "MTL"},
                        {"label": "San Francisco", "value": "SF"},
                    ],
                ),
            ],
            style={"marginBottom": "1rem"},
        ),
        html.Div(
            [
                html.Label("Text Input"),
                html.Br(),
                dcc.Input(value="MTL", type="text"),
            ],
            style={"marginBottom": "1rem"},
        ),
        html.Div(
            [
                html.Label("Slider"),
                dcc.Slider(
                    value=5,
                    min=0,
                    max=9,
                    marks={
                        i: "Label {}".format(i) if i == 1 else str(i)
                        for i in range(1, 6)
                    },
                ),
            ],
            style={"marginBottom": "1rem"},
        ),
    ],
    style={"columnCount": 1, "fontFamily": "monospace"},
)

if __name__ == "__main__":
    app.run(debug=True)
