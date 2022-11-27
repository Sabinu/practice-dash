from dash import (
    register_page,
    page_registry,
    page_container,
    Dash,
    html,
    dcc,
)

app = Dash(
    __name__,
    use_pages=True,
    external_scripts=["https://cdn.tailwindcss.com"],
)

register_page("home", path="/", layout=html.Div("Home Page"))
register_page("analytics", layout=html.Div("Analytics"))

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    dcc.Link(
                        f"{p['name']} - {p['path']}",
                        href=p["relative_path"],
                    )
                )
                for p in page_registry.values()
            ]
        ),
        page_container,
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
