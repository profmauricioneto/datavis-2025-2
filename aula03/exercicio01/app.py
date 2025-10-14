from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# =======================
# 🔹 Dados de exemplo
# =======================
data = {
    "Região": ["Norte", "Sul", "Leste", "Oeste"] * 25,
    "Vendedor": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"] * 20,
    "Produto": ["Notebook", "Monitor", "Mouse", "Teclado", "Headset"] * 20,
    "Valor da Venda": [x * 100 for x in range(1, 101)],
    "Data": pd.date_range("2024-01-01", periods=100, freq="D")
}
df = pd.DataFrame(data)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    dbc.Row([
        # Sidebar
        dbc.Col([
            html.H2("Filtros", className="text-center mb-3"),
            dbc.Label("Selecione a Região:"),
            dcc.Dropdown(
                id="regiao-dropdown",
                options=[{"label": r, "value": r} for r in df["Região"].unique()],
                value=None,
                placeholder="Escolha uma região"
            ),
            html.Br(),
            dbc.Label("Selecione o Período:"),
            dcc.DatePickerRange(
                id="data-picker",
                start_date=df["Data"].min(),
                end_date=df["Data"].max(),
                display_format="DD/MM/YYYY"
            ),
            html.Br(), html.Br(),
            dbc.Button("Atualizar", id="atualizar-btn", color="primary", className="w-100")
        ], width=3, className="bg-light p-4 rounded-3 shadow-sm"),

        # Conteúdo principal
        dbc.Col([
            html.H2("Dashboard de Vendas", className="text-center mb-4"),

            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardHeader("💰 Total de Vendas"),
                    dbc.CardBody(html.H4(id="total-vendas", className="card-title"))
                ], color="success", inverse=True), width=4),

                dbc.Col(dbc.Card([
                    dbc.CardHeader("📦 Número de Vendas"),
                    dbc.CardBody(html.H4(id="num-vendas", className="card-title"))
                ], color="info", inverse=True), width=4),

                dbc.Col(dbc.Card([
                    dbc.CardHeader("🏆 Melhor Vendedor"),
                    dbc.CardBody(html.H4(id="melhor-vendedor", className="card-title"))
                ], color="warning", inverse=True), width=4)
            ], className="mb-4"),

            dbc.Card([
                dbc.CardHeader("Vendas por Produto"),
                dbc.CardBody([
                    dcc.Graph(id="grafico-vendas")
                ])
            ], className="shadow-sm")
        ], width=9)
    ])
], fluid=True, className="py-4")

@app.callback(
    [Output("grafico-vendas", "figure"),
     Output("total-vendas", "children"),
     Output("num-vendas", "children"),
     Output("melhor-vendedor", "children")],
    Input("atualizar-btn", "n_clicks"),
    State("regiao-dropdown", "value"),
    State("data-picker", "start_date"),
    State("data-picker", "end_date")
)
def atualizar_dashboard(n_clicks, regiao, data_ini, data_fim):
    # Filtragem
    dff = df.copy()
    if regiao:
        dff = dff[dff["Região"] == regiao]
    dff = dff[(dff["Data"] >= data_ini) & (dff["Data"] <= data_fim)]

    # Gráfico
    fig = px.bar(
        dff.groupby("Produto")["Valor da Venda"].sum().reset_index(),
        x="Produto",
        y="Valor da Venda",
        title="Total de Vendas por Produto",
        text_auto=True,
        color="Produto"
    )
    fig.update_layout(template="plotly_white", title_x=0.5)

    # Métricas
    total_vendas = f"R$ {dff['Valor da Venda'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    num_vendas = f"{len(dff):,}".replace(",", ".")
    if not dff.empty:
        melhor = dff.groupby("Vendedor")["Valor da Venda"].sum().idxmax()
    else:
        melhor = "-"

    return fig, total_vendas, num_vendas, melhor

if __name__ == "__main__":
    app.run(debug=True)
