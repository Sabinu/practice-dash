from dash import register_page, html

register_page(__name__)

layout = html.Div(
    [
        html.H1("page: Archive", className="text-lg font-bold"),
        html.Div("This is our Archive page content."),
    ]
)
