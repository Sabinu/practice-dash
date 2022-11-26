from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H3("Change the value in the text box to see callbacks in action!"),
        html.Div(
            [
                "Input: ",
                dcc.Input(id="my-input", value="initial value", type="text"),
            ]
        ),
        html.Br(),
        html.Div(id="my-output"),
    ],
    style={"font-family": "monospace"},
)


@app.callback(
    Output(component_id="my-output", component_property="children"),
    Input(component_id="my-input", component_property="value"),
)
def update_output_div(input_value: str) -> str:
    return f"Output: {input_value}"


if __name__ == "__main__":
    app.run(debug=True)
