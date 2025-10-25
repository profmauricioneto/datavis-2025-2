from dash import Dash, html

app = Dash(__name__)

app.layout = [
    html.H2('Hello World from Dash'),
    html.Div('Essa é a minha primeira aplicação Dash.')
]

if __name__ == '__main__':
    app.run(debug=True)