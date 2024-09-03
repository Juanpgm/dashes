# Import packages
from dash import Dash, html, dash_table, dcc, Input, Output, callback
import pandas as pd
import dataWrangler as dW
import plotly.express as px
import components



# Incorporate data
df = dW.dataset


# Initialize the app
app = Dash()

## -----------------------------------------------------------------------------------------------------------------

# App layout
app.layout = [
    components.titleComponent('INFORMACIÓN DISPONIBLE PROYECTO DE LA ALCALDÍA PMO v1.0'),
    components.line,
    components.dropDownComponent(dW.dataset['NOMBRE_ORGANISMO'].unique()),
    components.line,
    components.radioItemComponent(dW.financialColumnsToShow),
    components.line,
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        page_size=15,
        style_cell={'maxWidth': '250px', 'textOverflow': 'ellipsis'},  # Set max width and ellipsis
        style_header={'backgroundColor': 'lightblue'}),  # Optional: Style header
         
    
        dcc.Graph(figure=components.histogramComponent(df['NOMBRE_ORGANISMO'], df[' PAGOS']))
]


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
