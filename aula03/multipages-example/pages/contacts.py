from dash import html, register_page

register_page(__name__, path='/contact', name='Contact')

layout = html.Div([
    html.H2('Contato'),
    html.H3('Entre em contato pelo email: mauricio.moreira@unichristus.edu.br')
])