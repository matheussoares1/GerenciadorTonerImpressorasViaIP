from dash import Dash, html
import dash_bootstrap_components as dbc

ips = [
    "192.168.0.102", "192.168.0.148", "192.168.0.53", "192.168.0.139",
    "192.168.0.96", "192.168.0.135", "192.168.0.126", "192.168.0.45",
    "192.168.0.40", "192.168.0.75", "192.168.0.65", "192.168.0.199",
    "192.168.0.60", "192.168.0.41"
]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H2("Mosaico de Impressoras - Xerox", style={"marginBottom": "30px"}),

    dbc.Container([
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H5(f"Impressora {ip}", className="card-title"),
                        dbc.Button("Abrir Interface", href=f"http://{ip}", target="_blank", color="primary")
                    ])
                ], className="mb-4"),
                width=6
            )
            for ip in ips[i:i + 2]
        ])
        for i in range(0, len(ips), 2)
    ])
], style={"padding": "40px"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)

