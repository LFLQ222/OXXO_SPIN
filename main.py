import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "main_s.css"])


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "width": "100%",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "auto",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/", active="exact")),
        dbc.NavItem(dbc.NavLink("Datos", href="/data", active="exact")),
        dbc.NavItem(dbc.NavLink("AI supervizado", href="/ai-s", active="exact")),
        dbc.NavItem(dbc.NavLink("AI no supervizado", href="/ai-n", active="exact")),
        dbc.NavItem(dbc.NavLink("Propuesta", href="/final", active="exact")),
        dbc.NavItem(dbc.NavLink("Nosotros", href="/nosotros", active="exact")),
    ],
    brand="OXXO SPIN",
    brand_href="/",
    color="#0E1D31",
    dark=True,
    class_name='secondary-color'
)

####MAIN PAGE#####

home_page = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(html.Img(src='/assets/oxxo_spin.jpg', className='oxxo-logo')),
                dbc.Col(html.H1('Análisis de Datos para Churn', className="Home-txt"), width=8),
            ],
            className="flex-container"
        ),
        html.Hr(),
        html.H2('Background', className='title2-home'),
        html.P('Mollit ea sint dolore cupidatat laborum aute nulla nostrud sunt dolore quis aliquip. Mollit dolor esse do anim. Do est ea irure dolor qui in velit tempor minim in aute nisi excepteur.Ex pariatur officia magna est aliqua non aute ullamco.', 
               className='parag-main1'),
        html.Hr(),
        html.H2('Hypothesis',className='title2-home'),
        html.P('Mollit ea sint dolore cupidatat laborum aute nulla nostrud sunt dolore quis aliquip. Mollit dolor esse do anim. Do est ea irure dolor qui in velit tempor minim in aute nisi excepteur.Ex pariatur officia magna est aliqua non aute ullamco.', 
               className='parag-main1')
    ]
)


    




##################


content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    navbar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    #####PAGINA DE INICIO
    if pathname == "/":
        return [home_page            
                
                ]
    #####PAGINA EXPLICANDO QUE FART CON LOS DATOS
    elif pathname == "/data":
       return [
                html.H1('Pagina de info de datos'),
                
                ]
    #####CODIGO DE AI USANDO MODELO SUPERVIZADO
    elif pathname == "/ai-s":
       return [
                html.H1('Pagina de ai supervizado'),
                
                ]
    #####CODIGO DE AI USANDO MODELO NO SUPERVIZADO
    elif pathname == "/ai-n":
        return [
                html.H1('Pagina de ai no supervizado'),
                
                ]
    
    #####PROPUESTA FINAL
    elif pathname == "/final":
       return [
                html.H1('Pagina final'),
                
                ]
    
    #####CODIGO DE US DE QUIEN LO HIZO
    elif pathname == "/nosotros":
        return [
                html.H1('Pagina de nosotros'),
                
                ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__=='__main__':
    app.run_server(debug=True, port=3000)