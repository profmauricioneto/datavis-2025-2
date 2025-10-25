from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

colors = {
    "background": "#444",
    "text": "#fff"
}

df = pd.DataFrame({
    "produtos": ["MaxSteel", "Barbie", "MaxSteel", "Barbie", "Dinossaur", "Dinossaur"],
    "quantidade": [4, 1, 3, 2, 4, 5],
    "cidade": ["FOR", "FOR", "GRU", "GRU", "GRU", "FOR"]
})

graph = px.bar(df, x="produtos", y="quantidade", color="cidade", barmode="group")
graph.update_layout(
    plot_bgcolor=colors["background"],
    paper_bgcolor=colors["background"],
    font_color=colors["text"]
)


app = Dash(__name__)

app.layout = [
    html.Div(style={'backgroundColor':'#444', 'color':'#fff'},children=[
        html.H1(style={'color': '#fff', 'textAlign': 'center'}, children='Meu Primeiro Dashboard com Dash'),
        html.Div(style={'color': '#fff', 'textAlign': 'center'}, children='Informações sobre vendas de produtos por cidade'),
        dcc.Graph(
            id='graph-product',
            figure=graph
        )
    ])
]

if __name__ == '__main__':
    app.run(debug=True)