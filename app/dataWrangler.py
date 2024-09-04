import re

import dataAdquisition as da
import string

#Importa el dataset Adquirido
dataset = da.df
# Suponiendo que tienes un DataFrame llamado 'df'
dataset = dataset.iloc[1:]




## ----------------------------------------------------------------------------------------------------------------------------------------

column_names = {
        'NOMBRE ORGANISMO': 'NOMBRE_ORGANISMO',
        'NOMBRE DEL PROYECTO': 'NOMBRE_DEL_PROYECTO',
        'NOMBRE DE LA ACTIVIDAD': 'NOMBRE_ACTIVIDAD',
        'NOMBRE DE FONDO': 'NOMBRE_DE_FONDO',
        'NOMBRE POSPRE': 'NOMBRE_POSPRE',
        'TIPO DE GASTO': 'TIPO_DE_GASTO',
        ' PPTO INICIAL': 'PTO_INICIAL',
        ' PPTO. MODIFICADO': 'PPTO_MODIFICADO',
        ' TOTAL ACUMULADO CDP': 'TOTAL_ACUMULADO_CDP',
        ' TOTAL ACUMULADO RPC': 'TOTAL_ACUMULADO_RPC',
        ' TOTAL ACUMUL OBLIGAC': 'TOTAL_ACUMUL_OBLIGAC',
        ' SALDOS CDP': 'SALDOS_CDP',
        ' PPTO. DISPONIBLE': 'PPTO_DISPONIBLE'
        # ... and so on for all columns you want to rename
    }

## ----------------------------------------------------------------------------------------------------------------------------------------
#PARTICULAR DATA ASSETS

#### Headers de los datos financieros (NOMBRES)
financialColumns = ['PTO_INICIAL', 
                    'PPTO_MODIFICADO', 
                    'TOTAL_ACUMULADO_CDP', 
                    'TOTAL_ACUMULADO_RPC', 
                    'TOTAL_ACUMUL_OBLIGAC', 
                    'SALDOS_CDP', 
                    'PPTO_DISPONIBLE',
                    ' CONTRACREDITOS',
                    ' CREDITOS',
                    'REDUCCIONES',
                    'ADICIONES',
                    'APLAZAMIENTO',
                    ' PAGOS',
                    ' EJECUCION']


financialColumnsToShow =[
                    'Presupuesto inicial', 
                    'Presupuesto Modificado', 
                    'Ejecución Acumulada del CDP', 
                    'Ejecución Acumulada del RPC', 
                    'Acumulado total de obligaciones', 
                    'Saldos CDP', 
                    'Presupuesto disponible',
                    'Contracréditos',
                    'Créditos',
                    'Reducciones'
                    'Adiciones',
                    'Aplazamiento',
                    'Pagos',
                    'Ejecución']

## ----------------------------------------------------------------------------------------------------------------------------------------

def renombrar_columnas(dataset, column_names):
  """Renombra las columnas de un DataFrame según un diccionario.

  Args:
    dataset: El DataFrame de Pandas.
    new_column_names: Un diccionario donde las claves son los nombres actuales 
                      y los valores los nuevos nombres.

  Returns:
    Un nuevo DataFrame con las columnas renombradas.
  """
  # Renombra las columnas utilizando el método rename()
  dataset = dataset.rename(columns=column_names)
  #print(dataset.columns)

  return dataset

## ----------------------------------------------------------------------------------------------------------------------------------------

def correctNumericData(number):
  number = number.replace(".", "")
  number = number.replace(",", "")
  number = number[:-2]
  return number

## ----------------------------------------------------------------------------------------------------------------------------------------

def transformarDataset(data):  # Add data argument
    for fColumn in data.columns:
        if fColumn in financialColumns:
            data[fColumn] = data[fColumn].apply(correctNumericData)
    return data

## ----------------------------------------------------------------------------------------------------------------------------------------

def convertCategoricalToNumeric(data):
  numericVigencia = []
  for vigencia in dataset['VIGENCIA']:
    if vigencia == 'Actual':
      numericVigencia.append(1)
    elif vigencia == 'Recursos de Balance':
      numericVigencia.append(2)
    elif vigencia == 'Reserva':
      numericVigencia.append(3)
    else:
      numericVigencia.append(0)
      
  return numericVigencia

## ----------------------------------------------------------------------------------------------------------------------------------------

### EJECUCIÓN DE FUNCIONES

## ----------------------------------------------------------------------------------------------------------------------------------------
dataset = renombrar_columnas(dataset, column_names)
dataset = transformarDataset(dataset)
dataset['numericalVigencia'] = convertCategoricalToNumeric(dataset)

## ----------------------------------------------------------------------------------------------------------------------------------------
#print(dataset.columns)
#print(dataset.info())

#print(convertCategoricalToNumeric(dataset))



#print(dataset)