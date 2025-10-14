from dash import html, register_page
import dash_bootstrap_components as dbc
register_page(__name__, path='/', name='Home')

layout = html.Div([
    html.H2('Página Inicial'),
    html.H3('Bem-vindo à página inicial da minha Aplicação Multipages!'),
    dbc.Alert("Hello from Bootstrap!", color='success'),
])