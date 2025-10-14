from click import style
from dash import Dash, html, dcc, page_registry, page_container
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1("Meu Dashboard de Múltiplas Páginas!", style={"textAlign": "center"}),
    html.Div([
        dcc.Link(page['name'], href=page['path'], style={"margin": "10px"})
        for page in page_registry.values() #percorrendos as páginas
    ], style={"textAlign": "center"}),
    html.Hr(),
    page_container # conteúdo onde será renderizado as páginas.
])