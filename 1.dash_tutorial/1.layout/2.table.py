from dash import Dash, html
import pandas as pd

df = pd.read_csv(
    "https://gist.githubusercontent.com/chriddyp/"
    "c78bf172206ce24f77d6363a2d754b59/raw/"
    "c353e8ef842413cae56ae3920b8fd78468aa4cb2/"
    "usa-agricultural-exports-2011.csv"
)


def generate_table(df: pd.DataFrame, max_rows: int = 10) -> html.Table:
    return html.Table(
        [
            html.Thead(
                html.Tr([html.Th(col) for col in df.columns]),
            ),
            html.Tbody(
                [
                    html.Tr([html.Td(df.iloc[i][col]) for col in df.columns])
                    for i in range(min(len(df), max_rows))
                ]
            ),
        ]
    )


app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("US Agriculture Exports (2011)"),
        generate_table(df),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
