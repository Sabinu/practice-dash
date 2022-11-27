from dash import Dash, page_registry, page_container, html, dcc

app = Dash(__name__, use_pages=True)

app.layout = html.Div(
    [
        html.H1("Multi-page app with Dash Pages"),
        html.Div(
            [
                html.Div(
                    dcc.Link(
                        f"{page['name']} - {page['path']}",
                        href=page["relative_path"],
                    )
                )
                for page in page_registry.values()
            ]
        ),
        page_container,
    ],
    style={"fontFamily": "monospace"},
)

if __name__ == "__main__":
    app.run(debug=True)
