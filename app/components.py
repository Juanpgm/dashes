
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
    title = html.H1(children=text)
    return title

#LineSpacer
line = html.Hr()



#RadioItem

def radioItemComponent(radioItemList):
    return dcc.RadioItems(
        id='controls-and-radio-item',
        options=[{'label': col, 'value': col} for col in radioItemList],
    )


def dropdownComponent(dropdownList):
    return dcc.Dropdown(
        id='dropdownValues',
        options=[{'label': org, 'value': org} for org in dropdownList],
        value=dropdownList[0]  # Set initial value
    )
    

### Revisar los callbacks