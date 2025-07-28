from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
   "Products": ["MaxSteel", "Barbie", "MaxSteel", "Barbie", "Dinossaur", "Dinossaur"],
   "Amount": [4, 1, 3, 2, 4, 5],
   "City": ["FOR", "FOR", "GRU", "GRU", "GRU", "FOR"]
})

fig = px.bar(df, x="Products", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
   html.H1(children="My First Example Dash App"),
   html.Div(children="Products by Cities"),
   dcc.Graph(
       id="products-graph",
       figure=fig
   )
])

if __name__ == "__main__":
   app.run(debug=True)