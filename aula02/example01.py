import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px

# Carregar dados
df = px.data.iris()

# Iniciar o app
app = dash.Dash(__name__)

# Layout do app
app.layout = html.Div([
    html.H1("Dashboard Interativo da Iris Dataset", style={'textAlign': 'center'}),

    html.Div([
        # Controles
        html.Div([
            html.Label("Selecione o eixo X:"),
            dcc.Dropdown(
                id='x-axis',
                options=[{'label': col, 'value': col} for col in df.columns[:4]],
                value='sepal_length'
            ),

            html.Label("Selecione o eixo Y:", style={'marginTop': '20px'}),
            dcc.Dropdown(
                id='y-axis',
                options=[{'label': col, 'value': col} for col in df.columns[:4]],
                value='sepal_width'
            ),

            html.Label("Intervalo de Largura da Pétala:", style={'marginTop': '20px'}),
            dcc.RangeSlider(
                id='petal-width-slider',
                min=df['petal_width'].min(),
                max=df['petal_width'].max(),
                step=0.1,
                marks={0: '0', 2.5: '2.5'},
                value=[df['petal_width'].min(), df['petal_width'].max()]
            ),

            html.Label("Filtrar Espécies:", style={'marginTop': '20px'}),
            dcc.Checklist(
                id='species-filter',
                options=[{'label': sp, 'value': sp} for sp in df['species'].unique()],
                value=df['species'].unique(),
                labelStyle={'display': 'block'}
            )
        ], style={'width': '20%', 'padding': '20px', 'display': 'inline-block'}),

        # Gráfico
        html.Div([
            dcc.Graph(id='scatter-plot'),
            html.Div(id='summary-stats', style={'marginTop': '20px'})
        ], style={'width': '75%', 'display': 'inline-block', 'verticalAlign': 'top'})
    ])
])


# Callback para atualizar o gráfico e estatísticas
@callback(
    [Output('scatter-plot', 'figure'),
     Output('summary-stats', 'children')],
    [Input('x-axis', 'value'),
     Input('y-axis', 'value'),
     Input('petal-width-slider', 'value'),
     Input('species-filter', 'value')]
)
def update_graph(x_col, y_col, petal_range, selected_species):
    # Filtragem dos dados
    filtered_df = df[
        (df['petal_width'] >= petal_range[0]) &
        (df['petal_width'] <= petal_range[1]) &
        (df['species'].isin(selected_species))
        ]

    # Criar gráfico
    fig = px.scatter(
        filtered_df,
        x=x_col,
        y=y_col,
        color='species',
        title=f"{x_col} vs {y_col}",
        height=600
    )

    # Calcular estatísticas
    stats = filtered_df.groupby('species').agg({
        x_col: ['mean', 'std'],
        y_col: ['mean', 'std']
    }).reset_index()

    stats_table = html.Div([
        html.H4("Estatísticas por Espécie:"),
        html.Table([
                       html.Tr([html.Th("Espécie"), html.Th(f"Média {x_col}"), html.Th(f"Desvio {x_col}"),
                                html.Th(f"Média {y_col}"), html.Th(f"Desvio {y_col}")])
                   ] + [
                       html.Tr([
                           html.Td(sp),
                           html.Td(round(row[x_col]['mean'], 2)),
                           html.Td(round(row[x_col]['std'], 2)),
                           html.Td(round(row[y_col]['mean'], 2)),
                           html.Td(round(row[y_col]['std'], 2))
                       ]) for sp, row in stats.iterrows()
                   ])
    ])

    return fig, stats_table


if __name__ == '__main__':
    app.run_server(debug=True)