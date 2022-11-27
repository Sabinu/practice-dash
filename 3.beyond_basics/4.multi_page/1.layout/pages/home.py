from dash import register_page, html

register_page(__name__, path="/")

layout = html.Div(
    [
        html.H1("page: HOME", className="text-lg font-bold"),
        html.Div("This is our Home page content."),
    ]
)
