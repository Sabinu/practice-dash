from dash import Dash, page_registry, page_container, html, dcc

app = Dash(
    __name__,
    use_pages=True,
    pages_folder="pages",
    external_scripts=["https://cdn.tailwindcss.com"],
)

app.layout = html.Div(
    [
        html.H1(
            "Multi-page app with Dash Pages",
            className="uppercase font-bold text-lg underline",
        ),
        html.Div(
            [
                html.Div(
                    dcc.Link(
                        f"{page['name']} - {page['path']}",
                        href=page["relative_path"],
                        className="hover:underline italic",
                    )
                )
                for page in page_registry.values()
            ]
        ),
        html.Hr(className="mt-4"),
        html.Div(
            [
                page_container,
            ],
            className="pt-4",
        ),
    ],
    className="font-mono",
)

if __name__ == "__main__":
    app.run(debug=True)
