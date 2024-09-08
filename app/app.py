# Import packages
from dash import Dash, html, dash_table, dcc, Input, Output, callback
import pandas as pd
import dataWrangler as dW
import plotly.express as px
import components


# Incorporate data
df = dW.dataset
dropdownList = df['NOMBRE_ORGANISMO'].unique()
radioItemList = dW.financialColumnsToShow
financial = dW.financialColumns
dfToDisplay = dW.datasetToBeDisplayed


# Initialize the app
app = Dash('Data Santiago de Cali')

## -----------------------------------------------------------------------------------------------------------------

# App layout
app.layout = [
    
    html.Div(className='row', children='INFORMACIÓN DISPONIBLE PROYECTO DE LA ALCALDÍA PMO v1.0',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),

    components.line,
    
    html.H3("DATOS FINANCIEROS DE PROYECTO"),
    html.H4("Filtro por organismo / entidad"),
    
      ## Dropdown
    dcc.Dropdown(
        id='dropdownValues',
        options=[{'label': org, 'value': org} for org in dropdownList],
        value=dropdownList[0]),  # Set initial value
    
## ----------------------------------------------------------------------------------------------------------------- 
    components.line,
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in dfToDisplay.columns],
        page_size=15,
        style_cell={'maxWidth': '250px', 'textOverflow': 'ellipsis'},  # Set max width and ellipsis
        style_header={'backgroundColor': 'lightblue'}),  # Optional: Style header  
    
    
    ## Mostrar Valores Filtrados
    
    #### ESCRIBIR AQUÍ
    
          
    dcc.Graph(figure=px.histogram(df, x='NOMBRE_ORGANISMO', y='PPTO_MODIFICADO',
                                color='NOMBRE_ORGANISMO',height=1180, width=1300)),
    
    dcc.Graph(figure=px.bar(df, y='TOTAL_ACUMULADO_CDP', x='NOMBRE_ORGANISMO', 
                                title='CDP ACUMULADO TOTAL POR ORGANISMO',
                                color='NOMBRE_ORGANISMO',height=1180, width=1300)),
    
    dcc.Graph(figure=px.pie(df, values='numericalVigencia', names='VIGENCIA',
                                title='Distribución de Categorías',
                                color='VIGENCIA',height=980, width=800)),
  
    
   components.line,
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        page_size=15,
        style_cell={'maxWidth': '250px', 'textOverflow': 'ellipsis'},  # Set max width and ellipsis
        style_header={'backgroundColor': 'lightblue'}),  # Optional: Style header  

    
    #dcc.Graph(figure=px.histogram(df, x='NOMBRE_ORGANISMO', y='PPTO_MODIFICADO',color='NOMBRE_ORGANISMO',height=800, width=1600))
]


# Run the app
if __name__ == '__main__':
    app.run(debug=True)