import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import requests
import datetime

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='interval-component',
        interval=60 * 1000,
        n_intervals=0
    )
])

# Função para obter o preço atual do Bitcoin (BTC) em USD
def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['bitcoin']['usd']
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter o preço do Bitcoin: {e}")
        return None

historical_data = []

# Callback para atualizar o gráfico
@app.callback(
    Output('live-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    price = fetch_bitcoin_price()
    if price is None:
        return go.Figure()

    timestamp = datetime.datetime.now()

    historical_data.append({'timestamp': timestamp, 'price': price})

    if len(historical_data) > 30:
        historical_data.pop(0)

    timestamps = [entry['timestamp'] for entry in historical_data]
    prices = [entry['price'] for entry in historical_data]

    # Cria o gráfico de linha
    fig = go.Figure(data=[go.Scatter(
        x=timestamps,
        y=prices,
        mode='lines+markers',
        name='Preço do Bitcoin (USD)'
    )])
    fig.update_layout(
        title='Preço do Bitcoin em Tempo Real',
        xaxis_title='Tempo',
        yaxis_title='Preço (USD)',
        template='plotly_dark'
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)