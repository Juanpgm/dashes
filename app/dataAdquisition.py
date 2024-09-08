import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Ruta al archivo JSON de credenciales
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('app\serviceAccountKey.json', scope)

# Autentificación
client = gspread.authorize(creds)

# Abrir el archivo de Google Sheets por su ID
sheet = client.open_by_key('1FMYEXoQ7WZQE4-NepeOt6CxaTkl4Sv6xmMudL4U5Zg8').sheet1

# Leer todos los valores de la hoja
data = sheet.get_all_values()

# Crear un DataFrame de pandas (opcional)

df = pd.DataFrame(data, columns=sheet.row_values(1))

# Mostrar los primeros 5 registros
#print(df.head())






