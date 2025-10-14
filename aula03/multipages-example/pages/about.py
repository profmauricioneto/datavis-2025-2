from dash import html, register_page

register_page(__name__, path='/about', name='About')

layout = html.Div([
    html.H2('Sobre o Projeto'),
    html.H3('Este projeto foi desenvolvido em Dash com múltiplas páginas.')
])