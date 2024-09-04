# Import packages
from dash import Dash, html, dash_table, dcc, Input, Output, callback
import pandas as pd
import dataWrangler as dW
import plotly.express as px
import components

def update_graph(X):
    fig = px.histogram(df, x=X, y=df['PPTO_MODIFICADO'], histfunc='avg')
    return fig

# Incorporate data
df = dW.dataset
dropdownList = df['NOMBRE_ORGANISMO'].unique()
radioItemList = dW.financialColumnsToShow
financial = dW.financialColumns


# Initialize the app
app = Dash('Data Santiago de Cali')

## -----------------------------------------------------------------------------------------------------------------

# App layout
app.layout = [
    components.titleComponent('INFORMACIÓN DISPONIBLE PROYECTO DE LA ALCALDÍA PMO v1.0'),
    components.line,
    #components.dropdownComponent(dropdownList),
    
    ## Dropdown
    dcc.Dropdown(
        id='dropdownValues',
        options=[{'label': org, 'value': org} for org in financial],
        value=dropdownList[0]),  # Set initial value
    
    dcc.Graph(figure=px.histogram(df, x='NOMBRE_ORGANISMO', y='PPTO_MODIFICADO',
                                  color='NOMBRE_ORGANISMO',height=800, width=1600)),
    
    components.line,
    
    #Graph:
    dcc.Graph(id='grafico'),
    
    components.line,
    #components.radioItemComponent(radioItemList),
    components.line,
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        page_size=15,
        style_cell={'maxWidth': '250px', 'textOverflow': 'ellipsis'},  # Set max width and ellipsis
        style_header={'backgroundColor': 'lightblue'}),  # Optional: Style header  
    
    #dcc.Graph(figure=px.histogram(df, x='NOMBRE_ORGANISMO', y='PPTO_MODIFICADO',color='NOMBRE_ORGANISMO',height=800, width=1600))
]

@callback(
    Output('grafico', 'figure'),
    Input('dropdownValues', 'value'),
    #[Input('controls-and-radio-item', 'value')]
    )



def update_graph(option_selected): 
    filtered_df = df[df.NOMBRE_ORGANISMO==option_selected] 
    fig = px.histogram(filtered_df,
                    x = 'NOMBRE_ORGANISMO', y = 'PPTO_MODIFICADO',
                       barmode='group', 
                       color='NOMBRE_ORGANISMO',
                       height=800, width=160, 
                       histfunc='avg')
    
    fig.update_layout(title='Histograma Comparativo || Variables asociadas',
                      transition_duration = 500)
    
    return fig
    


# Run the app
if __name__ == '__main__':
    app.run(debug=True)