from dash import Dash, html, dcc, Input, Output, State

app = Dash(
    __name__,
    external_scripts=["https://cdn.tailwindcss.com"],
)

url_bar_and_content_div = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

layout_index = html.Div(
    [
        dcc.Link('Navigate to "/page-1"', href="/page-1"),
        html.Br(),
        dcc.Link('Navigate to "/page-2"', href="/page-2"),
    ]
)

layout_page_1 = html.Div(
    [
        html.H2("Page 1"),
        dcc.Input(id="input-1-state", type="text", value="Montreal"),
        dcc.Input(id="input-2-state", type="text", value="Canada"),
        html.Button(id="submit-button", n_clicks=0, children="Submit"),
        html.Div(id="output-state"),
        html.Br(),
        dcc.Link('Navigate to "/"', href="/"),
        html.Br(),
        dcc.Link('Navigate to "/page-2"', href="/page-2"),
    ]
)

layout_page_2 = html.Div(
    [
        html.H2("Page 2"),
        dcc.Dropdown(["LA", "NYC", "MTL"], "LA", id="page-2-dropdown"),
        html.Div(id="page-2-display-value"),
        html.Br(),
        dcc.Link('Navigate to "/"', href="/"),
        html.Br(),
        dcc.Link('Navigate to "/page-1"', href="/page-1"),
    ]
)

# index layout
app.layout = url_bar_and_content_div

# "complete" layout
app.validation_layout = html.Div(
    [
        url_bar_and_content_div,
        layout_index,
        layout_page_1,
        layout_page_2,
    ]
)


# Index callbacks
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname == "/page-1":
        return layout_page_1
    elif pathname == "/page-2":
        return layout_page_2
    else:
        return layout_index


# Page 1 callbacks
@app.callback(
    Output("output-state", "children"),
    Input("submit-button", "n_clicks"),
    State("input-1-state", "value"),
    State("input-2-state", "value"),
)
def update_output(n_clicks, input1, input2):
    return f"The Button has been pressed {n_clicks} times. \
            Input 1 is {input1} and Input 2 is {input2}"


# Page 2 callbacks
@app.callback(
    Output("page-2-display-value", "children"),
    Input("page-2-dropdown", "value"),
)
def display_value(value):
    return f"You have selected {value}"


if __name__ == "__main__":
    app.run(debug=True)
