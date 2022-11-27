import dash
from dash import html, dcc

dash.register_page(__name__)


layout = html.Div(
    [
        html.H1("2020 Summary"),
        html.Div("This is our page's content."),
    ]
)
