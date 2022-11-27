from dash import register_page, html, dcc, callback, Input, Output

register_page(__name__)

layout = html.Div(
    [
        html.H1("page: Analytics", className="text-lg font-bold"),
        html.Div(
            [
                "Select a city: ",
                dcc.RadioItems(
                    ["New York City", "Montreal", "San Francisco"],
                    "Montreal",
                    id="analytics-input",
                ),
            ]
        ),
        html.Br(),
        html.Div(id="analytics-output"),
    ]
)


@callback(
    Output("analytics-output", "children"),
    Input("analytics-input", "value"),
)
def update_city_selected(input_value):
    return f"You selected: {input_value}"
