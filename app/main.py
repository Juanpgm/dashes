@callback(
    Output('grafico', 'figure'),
    Input('dropdownValues', 'value'),
    )



def update_graph(option_selected, y_columns=financial):
    filtered_df = df[df.NOMBRE_ORGANISMO==option_selected] 
    fig = px.histogram(filtered_df,
                    x = 'NOMBRE_ORGANISMO', y = y_columns,
                       barmode='group', 
                       color='NOMBRE_ORGANISMO',
                       height=800, width=160, 
                       histfunc='avg')
    
    fig.update_layout(title='Histograma Comparativo || Variables asociadas',
                      transition_duration = 500)
    
    return fig