from dash import Dash, html

app = Dash(__name__)
server = app.server # expondo o servidor Flask para o Gunicorn

app.layout = [
    html.H1("Hello World From Dash!"),
    html.P("Your test was successful.")
]

if __name__ == '__main__':
    app.run(debug=True)