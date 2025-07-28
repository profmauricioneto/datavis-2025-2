from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
colors = {
   'background': '#444',
   'text': '#FFF'
}
df = pd.DataFrame({
   "Products": ["MaxSteel", "Barbie", "MaxSteel", "Barbie", "Dinossaur", "Dinossaur"],
   "Amount": [4, 1, 3, 2, 4, 5],
   "City": ["FOR", "FOR", "GRU", "GRU", "GRU", "FOR"]
})
fig = px.bar(df, x="Products", y="Amount", color="City", barmode="group")
fig.update_layout(
   plot_bgcolor=colors['background'],
   paper_bgcolor=colors['background'],
   font_color=colors['text']
)
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
   html.H1(
       children='My First Example Dash App',
       style={
           'textAlign': 'center',
           'color': colors['text']
       }
   ),
   html.Div(children='Products by Cities.', style={
       'textAlign': 'center',
       'color': colors['text']
   }),
   dcc.Graph(
       id='example-graph',
       figure=fig
   )
])

if __name__ == "__main__":
   app.run(debug=True)