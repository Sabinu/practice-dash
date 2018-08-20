# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()


app.layout = html.Div(
    [ html.Label('Dropdown')
    , dcc.Dropdown( value='MTL'
                  , options=[ {'label': 'New York City', 'value': 'NYC'}
                            , {'label': u'Montréal',     'value': 'MTL'}
                            , {'label': 'San Francisco', 'value': 'SF'}
                            ]
                  )
    , html.Br(), html.Br()

    , html.Label('Multi-Select Dropdown')
    , dcc.Dropdown( value=['MTL', 'SF']
                  , multi=True
                  , options=[ {'label': 'New York City', 'value': 'NYC'}
                            , {'label': u'Montréal',     'value': 'MTL'}
                            , {'label': 'San Francisco', 'value': 'SF'}
                            ]
                  )
    , html.Br(), html.Br()

    , html.Label('Radio Items')
    , dcc.RadioItems( value='MTL'
                    , options=[ {'label': 'New York City', 'value': 'NYC'}
                              , {'label': u'Montréal',     'value': 'MTL'}
                              , {'label': 'San Francisco', 'value': 'SF'}
                              ]
                    )
    , html.Br(), html.Br()

    , html.Label('Checkboxes')
    , dcc.Checklist( values=['MTL', 'SF']
                   , options=[ {'label': 'New York City', 'value': 'NYC'}
                             , {'label': u'Montréal',     'value': 'MTL'}
                             , {'label': 'San Francisco', 'value': 'SF'}
                             ]
                   )
    , html.Br(), html.Br()

    , html.Label('Text Input')
    , html.Br()
    , dcc.Input(value='MTL', type='text')
    , html.Br(), html.Br()
    , html.Br(), html.Br()

    , html.Label('Slider')
    , dcc.Slider( value=5
                , min=0
                , max=9
                , marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)}
                )
    ]

    # , style={'columnCount': 2}
    )

if __name__ == '__main__':
    app.run_server(debug=True)