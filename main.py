import psycopg2
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go


conn = psycopg2.connect(
    dbname="prueba",
    user="brahian",
    password="pass",
    host="db",
    # host="localhost",
    # port="5431"
)


##Unificacion, depuracion, tranformacion y manipulacion de datos a visualizar
consulta = """
with a as (
    SELECT * FROM historico_aba_macroactivos 
    LEFT JOIN catalogo_activos ON historico_aba_macroactivos.cod_activo = catalogo_activos.cod_activo
    LEFT JOIN catalogo_banca ON historico_aba_macroactivos.cod_banca = catalogo_banca.cod_banca
    LEFT JOIN cat_perfil_riesgo ON historico_aba_macroactivos.cod_perfil_riesgo = cat_perfil_riesgo.cod_perfil_riesgo
),

b as (
SELECT *,
CASE WHEN ingestion_month='' THEN month ELSE ingestion_month END as ingestion_month_clean
FROM a
),

c as (
SELECT CAST(ingestion_year AS INTEGER) AS year,
CAST(ingestion_month_clean AS INTEGER) AS month,
CAST(ingestion_day AS INTEGER) AS day,
id_sistema_cliente,macroactivo,
CAST(NULLIF(aba, '') AS NUMERIC) AS aba,
activo,banca,perfil_riesgo
FROM b
)


select TO_DATE(CONCAT(day, '/', month, '/', year), 'DD/MM/YYYY') AS fecha,
CONCAT(year, '-',month) As year_month, id_sistema_cliente,
macroactivo, aba, activo,banca,perfil_riesgo from c
where day <= 31
"""
df = pd.read_sql_query(consulta, conn)
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m/%d')
df['Mes'] = df['fecha'].dt.to_period('M')


# Inicializa la aplicación Dash
app = dash.Dash(__name__)
unique_months = sorted(df['Mes'].unique())
marks = {i: str(month) for i, month in enumerate(unique_months)}
# Define el layout de la aplicación
app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'padding': '10px', 'font-family': 'Arial, sans-serif'}, children=[
    html.H1("Dirección Estructuracion Mercado de capitales", style={'color': '#2c3e50', 'textAlign': 'center'}),
    html.H2(f"Última fecha de actualización: "+str(df['fecha'].max())[0:10], style={'color': '#2c3e50'}),
    html.Label('Portafolio de inversión por clientes:', style={'color': '#2c3e50', 'font-size': '30px'}),
    html.Br(),
    html.Br(),
    html.Label('Selecciona la identificacíon del cliente:', style={'color': '#2c3e50'}),
    dcc.Dropdown(
        id='dropdown1',
        options=[{'label': categoria, 'value': categoria} for categoria in df["id_sistema_cliente"].unique()],
        value=df["id_sistema_cliente"].unique()[1],  # Valor inicial
        style={'backgroundColor': 'white', 'color': '#2c3e50'}
    ),
    html.Br(),
    
    html.Div([
        dcc.Graph(id='pie-chart-11', style={'display': 'inline-block', 'width': '45%'}),
        dcc.Graph(id='pie-chart-21', style={'display': 'inline-block', 'width': '45%'})
    ], style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),



###-------------------------------------------------------------------------------------------------------------------------##
    html.Label('Portafolio de inversión por banca:', style={'color': '#2c3e50', 'font-size': '30px'}),
    html.Br(),
    html.Br(),
    html.Label('Selecciona el tipo de banca:', style={'color': '#2c3e50'}),
    dcc.Dropdown(
        id='dropdown2',
        options=[{'label': 'Personal', 'value': 'Personal'},
                                    {'label': 'Privada', 'value': 'Privada'},
                                    {'label': 'Preferencial', 'value': 'Preferencial'},
                               
                                    {'label': 'Pymes', 'value': 'Pymes'},
                                    {'label': 'Empresas', 'value': 'Empresas'}],
        value=df["banca"].unique()[0],  # Valor inicial
        style={'backgroundColor': 'white', 'color': '#2c3e50'}
    ),
    html.Br(),
    
    html.Div([
        dcc.Graph(id='pie-chart-12', style={'display': 'inline-block', 'width': '45%'}),
        dcc.Graph(id='pie-chart-22', style={'display': 'inline-block', 'width': '45%'})
    ], style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),


###-------------------------------------------------------------------------------------------------------------------------##
    html.Label('Portafolio de inversión por Riesgos:', style={'color': '#2c3e50', 'font-size': '30px'}),
    html.Br(),
    html.Br(),
    html.Label('Selecciona el tipo de riesgo:', style={'color': '#2c3e50'}),
    dcc.Dropdown(
        id='dropdown3',
        options=[{'label': 'Sin definir', 'value': 'SIN DEFINIR'},
                                    {'label': 'Moderado', 'value': 'MODERADO'},
                                    {'label': 'Conservador', 'value': 'CONSERVADOR'},
                                    {'label': 'Agresivo', 'value': 'AGRESIVO'}
                                    ],
        value=df["perfil_riesgo"].unique()[1],  # Valor inicial
        style={'backgroundColor': 'white', 'color': '#2c3e50'}
    ),
    html.Br(),
    
    html.Div([
        dcc.Graph(id='pie-chart-13', style={'display': 'inline-block', 'width': '45%'}),
        dcc.Graph(id='pie-chart-23', style={'display': 'inline-block', 'width': '45%'})
    ], style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

###-------------------------------------------------------------------------------------------------------------------------##
    html.Label('ABA promedio del total del portafolio:', style={'color': '#2c3e50', 'font-size': '30px'}),
    html.Br(),
    html.Br(),
    dcc.Graph(id='time-series-graph'),
    dcc.RangeSlider(
        id='month-range-slider',
        min=0,
        max=len(unique_months) - 1,
        value=[0, len(unique_months) - 1],
        marks=marks,
        step=1
    )
]
)

######################################### Callback para actualizar los gráficos###################################
@app.callback(
    [Output('pie-chart-11', 'figure'),
     Output('pie-chart-21', 'figure')],
    [Input('dropdown1', 'value')]
)
def update_pie_charts(selected_category):
    filtered_df = df[df['id_sistema_cliente'] == selected_category]

    fig1 = px.pie(filtered_df.value_counts(["macroactivo"]).reset_index(name="conteo"), names='macroactivo', values="conteo", title='Porcentaje de macroactivos:')
    fig2 = px.pie(filtered_df.value_counts(["activo"]).reset_index(name="conteo"), names='activo', values="conteo", title='Porcentaje de activo:')
    return fig1, fig2




# Callback para actualizar los gráficos
@app.callback(
    [Output('pie-chart-12', 'figure'),
     Output('pie-chart-22', 'figure')],
    [Input('dropdown2', 'value')]
)
def update_pie_charts(selected_category):
    filtered_df = df[df['banca'] == selected_category]
    
    fig1 = px.pie(filtered_df.value_counts(["macroactivo"]).reset_index(name="conteo"), names='macroactivo', values="conteo", title='Porcentaje de macroactivos:')
    fig2 = px.pie(filtered_df.value_counts(["activo"]).reset_index(name="conteo"), names='activo', values="conteo", title='Porcentaje de activo:')
    return fig1, fig2



# Callback para actualizar los gráficos
@app.callback(
    [Output('pie-chart-13', 'figure'),
     Output('pie-chart-23', 'figure')],
    [Input('dropdown3', 'value')]
)
def update_pie_charts(selected_category):
    filtered_df = df[df['perfil_riesgo'] == selected_category]

    fig1 = px.pie(filtered_df.value_counts(["macroactivo"]).reset_index(name="conteo"), names='macroactivo', values="conteo", title='Porcentaje de macroactivos:')
    fig2 = px.pie(filtered_df.value_counts(["activo"]).reset_index(name="conteo"), names='activo', values="conteo", title='Porcentaje de activo:')
    return fig1, fig2


# Callback para las serie de tiempo ADB en función del rango de meses seleccionado
@app.callback(
    Output('time-series-graph', 'figure'),
    [Input('month-range-slider', 'value')]
)
def update_graph(month_range):
    # Convertir los valores del slider a meses
    start_month = unique_months[month_range[0]].start_time
    end_month = unique_months[month_range[1]].end_time
    # Filtrar el DataFrame según el rango de meses seleccionado
    filtered_df = df[(df['fecha'] >= start_month) & (df['fecha'] <= end_month)]
    filtered_df = filtered_df.groupby('fecha').aba.mean().reset_index()
    
    # Crear el gráfico de serie de tiempo
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_df['fecha'], y=filtered_df['aba'], mode='lines'))
    fig.update_layout(title='Linea de tiempo de ABA promedio',
                      xaxis_title='Fecha',
                      yaxis_title='ABA promedio',
                      yaxis=dict(
                        tickformat=',',  # Formato de números con coma como separador de miles
                        tickprefix='',   # Prefijo vacío para no mostrar M
                        ticksuffix=''    # Sufijo vacío para no mostrar M
        )
)
    return fig



# Ejecuta la aplicación
if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8051, use_reloader=False)
