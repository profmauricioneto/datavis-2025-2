from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')

fig = px.scatter(df, x="gdp per capita",
                 y="life expectancy",
                 size="population",
                 color="continent",
                 hover_name="country",
                 log_x=True,
                 size_max=60)

app = Dash(__name__)

app.layout = html.Div(style={"textAlign": "center"},children=[
        html.H1('My Dashboard'),
        dcc.Graph(
            figure = fig
        )
    ])

if __name__ == '__main__':
    app.run(debug=True)
