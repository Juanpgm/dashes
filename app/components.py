
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dataWrangler as dW


ALLOWED_TYPES = (
    "text", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)
suppress_callback_exceptions=True


## ----------  FUNCIONES PARA COMPONENTES GENÉRICOS:
#Title
def titleComponent(text):
    title = html.Div(children=text)
    return title

#LineSpacer
line = html.Hr()

#Dropdown

@callback(
    Output('dd-output-container', 'children'),  # Update based on dropdown
    [Input('dropdownValues', 'value')]
)

def dropDownComponent(dropdownList):
    dropdown = dcc.Dropdown(dropdownList, id='dropdownValues', value='Secretaría de Gobierno')
    return dropdown

#RadioItem

@callback(
    Output('controls-radio', 'value'),   # Update with the histogram
    [Input('controls-and-radio-item', 'value')]
)

def radioItemComponent(radioItemList):
    radioItem = dcc.RadioItems(options=radioItemList, id='controls-radio')
    return radioItem

#DataTable

## ----------  COMPONENTES DE GRAFICACIÓN // VISUALIZACIÓN:
def histogramComponent(x,y):
    histogram = px.histogram(x, y, histfunc='avg')
    return histogram 




### Revisar los callbacks