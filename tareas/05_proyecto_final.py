#1. Instalar los paquetes
#pip install dataframe_image #Exporta los dataframes en png
#pip install altair #Grafica

#2. Cargar los paquetes
import os
import pandas as pd #No ejecutado porque se descargó automaticamente "Imported but unused"
import numpy as np #No ejecutado porque se descargó automaticamente "Imported but unused"
import dataframe_image as dfi #Exporta los dataframes en png
#import altair as alt
import seaborn as sns

import matplotlib.pyplot as plt

#from pylab import * #Descargado para un ejercicio de internet

#3. Importar y limpiar
#os.getcwd() #Obtener directorio actual
os.chdir('/Users/davidsegovia/Documents/Economics/Training/Codeando México/Datos abiertos y hacking cívico') #Cambiar de directorio

#PREGUNTA 9: Número de empresas según los medios de pago que aceptan por los productos (bienes o servicios)
df_enaproce9 = pd.read_excel(r"tam_ENAPROCE18.xlsx", sheet_name="9", skiprows=4, header=1) #Importar hoja 1 del archivo omitiendo las 4 primeras filas y nombrando las columnas como la primera fila

df_enaproce9 = df_enaproce9.dropna(axis=0, how='all') #Elimina las filas donde todos sus elementos son missing value
df_enaproce9 = df_enaproce9.dropna(axis=1, how='all') #Elimina las columnas donde todos sus elementos son missing value
df_enaproce9 = df_enaproce9.dropna() #Elimina las filas donde al menos uno de sus elementos es missing value
df_enaproce9

# limpieza del nombre de las columnas, remover espacios, carácteres especiales y pasar a minúsculas
df_enaproce9.columns #Conocer el nombre de las columnas
df_enaproce9.dtypes #Conocer la clase de cada columna 

df_enaproce9.columns = df_enaproce9.columns.str.strip()
df_enaproce9.columns = df_enaproce9.columns.str.replace(' ', '_')

df_enaproce9['Total_2'] = df_enaproce9.iloc[:, 2:].sum(1) #Crea una columna que suma los valores de las otras

list_df_enaproce9 = df_enaproce9.iloc[:, 2:7] 

for i in list_df_enaproce9:      
            df_enaproce9[str(i)+'_%'] = (df_enaproce9[i] / df_enaproce9['Total_2']) *100 #Ejecutado pero incorrecto

df_enaproce9 = df_enaproce9.sort_index(ascending=False) #invierte el orden de las filas

df_enaproce9a = df_enaproce9.filter(regex='Tamaño_de_Empresa|%') #Borra las columnas que no contengan el texto "tamaño_de_empresa" o "%"
df_enaproce9a.columns = ['Tamaño','Efectivo','Tarjetas o cheques','Transferencia','Vales','Otros']           

##PREGUNTA 9
eje_y9 = ['Efectivo','Tarjetas o cheques','Transferencia','Vales','Otros']
#Barras
df_enaproce9at = df_enaproce9a[eje_y9].T
df_enaproce9at.columns = ['Micro','PyMES','Total']
df_enaproce9at= df_enaproce9at.sort_values('Total',ascending=False)
df_enaproce9atp2b = df_enaproce9at.plot.barh(colormap='Dark2').grid(axis='x') #title="Title",CUATRO Barras horizontales #ELEGIDO

#PREGUNTA 14: Número de empresas según los problemas que las empresas indicaron como los tres más importantes que enfrentan para su crecimiento
df_enaproce14 = pd.read_excel(r"tam_ENAPROCE18.xlsx", sheet_name="14", skiprows=5, header=1) #Importar hoja 1 del archivo omitiendo las 4 primeras filas y nombrando las columnas como la primera fila

df_enaproce14 = df_enaproce14.dropna(axis=0, how='all') #Elimina las filas donde todos sus elementos son missing value
df_enaproce14 = df_enaproce14.dropna(axis=1, how='all') #Elimina las columnas donde todos sus elementos son missing value
df_enaproce14 = df_enaproce14.dropna() #Elimina las filas donde al menos uno de sus elementos es missing value

# limpieza del nombre de las columnas, remover espacios, carácteres especiales y pasar a minúsculas
df_enaproce14.columns #Conocer el nombre de las columnas
df_enaproce14.dtypes #Conocer la clase de cada columna 

df_enaproce14.columns = df_enaproce14.columns.str.strip()
df_enaproce14.columns = df_enaproce14.columns.str.replace(' ', '_')

list_df_enaproce14a = df_enaproce14.iloc[:, 2:6] 

for i in list_df_enaproce14a:      
            df_enaproce14[str(i)+'_%'] = (df_enaproce14[i] / df_enaproce14['Total']) *100 #Ejecutado pero incorrecto

list_df_enaproce14b = df_enaproce14.iloc[:, 7:11] 

for i in list_df_enaproce14b:      
            df_enaproce14[str(i)+'_%'] = (df_enaproce14[i] / df_enaproce14['Total_.1']) *100 #Ejecutado pero incorrecto
            
df_enaproce14 = df_enaproce14.sort_index(ascending=False) #invierte el orden de las filas

df_enaproce14.rename(columns={'Unnamed:_0':'Tamaño_de_Empresa'}, inplace=True)

df_enaproce14a = df_enaproce14.filter(regex='Tamaño_de_Empresa|%') #Borra las columnas que no contengan el texto "tamaño_de_empresa" o "%"
df_enaproce14a.columns = ['Tamaño','Sin instrucción 2016(`16)', 'Básica `16','Media `16', 'Superior `16','Sin instrucción 2017(`17)', 'Básica `17','Media `17', 'Superior `17'] 
df_enaproce14a = df_enaproce14a[['Tamaño','Sin instrucción 2016(`16)','Sin instrucción 2017(`17)', 'Básica `16', 'Básica `17','Media `16','Media `17','Superior `16','Superior `17']] 

list_df_enaproce14c = df_enaproce14a.iloc[:, 1:] 

for i in list_df_enaproce14c:      
            df_enaproce14a[i] = df_enaproce14a[i].astype(float).round(1) 

dfi.export(df_enaproce14a,"df_enaproce14a.png")

#PREGUNTA 16: Número de empresas según la principal carencia del personal que contratan
df_enaproce16 = pd.read_excel(r"tam_ENAPROCE18.xlsx", sheet_name="16", skiprows=4, header=1) #Importar hoja 1 del archivo omitiendo las 4 primeras filas y nombrando las columnas como la primera fila

df_enaproce16 = df_enaproce16.dropna(axis=0, how='all') #Elimina las filas donde todos sus elementos son missing value
df_enaproce16 = df_enaproce16.dropna(axis=1, how='all') #Elimina las columnas donde todos sus elementos son missing value
df_enaproce16 = df_enaproce16.dropna() #Elimina las filas donde al menos uno de sus elementos es missing value

# limpieza del nombre de las columnas, remover espacios, carácteres especiales y pasar a minúsculas
df_enaproce16.columns #Conocer el nombre de las columnas
df_enaproce16.dtypes #Conocer la clase de cada columna 

df_enaproce16.columns = df_enaproce16.columns.str.strip()
df_enaproce16.columns = df_enaproce16.columns.str.replace(' ', '_')

df_enaproce16['Total_2'] = df_enaproce16.iloc[:, 2:].sum(1) #Crea una columna que suma los valores de las otras

list_df_enaproce16 = df_enaproce16.iloc[:, 2:10] 

for i in list_df_enaproce16:      
            df_enaproce16[str(i)+'_%'] = (df_enaproce16[i] / df_enaproce16['Total_2']) *100 #Ejecutado pero incorrecto

df_enaproce16 = df_enaproce16.sort_index(ascending=False) #invierte el orden de las filas

df_enaproce16a = df_enaproce16.filter(regex='Tamaño_de_Empresa|%') #Borra las columnas que no contengan el texto "tamaño_de_empresa" o "%"
df_enaproce16a.columns = ['Tamaño','Disciplina', 'Habilidades analíticas','Iniciativa', 'Solución de problemas','Calidad educativa','No disponibilidad de la carrera','Sin carencia', 'Otra']

##PREGUNTA 16 (anteriorenmente se incluyó Total pero carecia de propósito en tanto tampoco estaba Micro y por lo tanto era la misma información que PYMES)
eje_y16 = ['Disciplina', 'Habilidades analíticas','Iniciativa', 'Solución de problemas','Calidad educativa','No disponibilidad de la carrera','Sin carencia', 'Otra']
#Barras
df_enaproce16a = df_enaproce16a[~df_enaproce16a.index.isin([2])] #Borra el renglón 2 correspondiente a Total
df_enaproce16a.rename(columns={'Tamaño':'PyMES'}, inplace=True) #Se agregó de último minuto
df_enaproce16ap1a = df_enaproce16a.plot.bar('PyMES', stacked=True,colormap='tab20b').legend(loc='center left', bbox_to_anchor=(1, 0.5)).axes.xaxis.set_ticklabels([]) #, title="Title"UNO barra verticas apilada. No se pudo agregar grid (.grid(axis='y')) junto a legend porque era uno u otro #ELEGIDO #Se modificó de último minuto

#PREGUNTA 18: Número de empresas según la principal causa por la que no ofreció capacitación al personal
df_enaproce18 = pd.read_excel(r"tam_ENAPROCE18.xlsx", sheet_name="18", skiprows=5, header=1) #Importar hoja 1 del archivo omitiendo las 4 primeras filas y nombrando las columnas como la primera fila

df_enaproce18 = df_enaproce18.dropna(axis=0, how='all') #Elimina las filas donde todos sus elementos son missing value
df_enaproce18 = df_enaproce18.dropna(axis=1, how='all') #Elimina las columnas donde todos sus elementos son missing value
df_enaproce18 = df_enaproce18.dropna() #Elimina las filas donde al menos uno de sus elementos es missing value

# limpieza del nombre de las columnas, remover espacios, carácteres especiales y pasar a minúsculas
df_enaproce18.columns #Conocer el nombre de las columnas
df_enaproce18.dtypes #Conocer la clase de cada columna 

df_enaproce18.columns = df_enaproce18.columns.str.strip()
df_enaproce18.columns = df_enaproce18.columns.str.replace(' ', '_')

list_df_enaproce18a = df_enaproce18.iloc[:, 2:13] 

for i in list_df_enaproce18a:      
            df_enaproce18[str(i)+'_%'] = (df_enaproce18[i] / df_enaproce18['Total']) *100 #Ejecutado pero incorrecto

list_df_enaproce18b = df_enaproce18.iloc[:, 14:25] 

for i in list_df_enaproce18b:      
            df_enaproce18[str(i)+'_%'] = (df_enaproce18[i] / df_enaproce18['Total.1']) *100 #Ejecutado pero incorrecto
            
df_enaproce18 = df_enaproce18.sort_index(ascending=False) #invierte el orden de las filas

df_enaproce18.rename(columns={'Unnamed:_0':'Tamaño_de_Empresa'}, inplace=True)

df_enaproce18a = df_enaproce18.filter(regex='Tamaño_de_Empresa|%') #Borra las columnas que no contengan el texto "tamaño_de_empresa" o "%"
df_enaproce18a.columns = ['Tamaño','Interrumpe producción(Ip) 2016(`16)','Exigencias salariales(Es) `16','No encontró capacitador(Nec) `16','Costo elevado(Ce) `16','Habilidades adecuadas(Ha) `16','Cambio de trabajo(Cdt) `16','Se capacitó previamente(Scp) `16','Sin apoyo público(Sap) `16','No hay beneficios(Nhb) `16','Personal externo capacitado(Pec) `16', 'Otra(O) `16','Ip 2017(`17)','Es `17','Nec `17','Ce `17','Ha `17','Cdt `17','Scp `17','Sap `17','Nhb `17','Pec `17', 'O `17']
df_enaproce18a = df_enaproce18a[['Tamaño','Interrumpe producción(Ip) 2016(`16)','Ip 2017(`17)','Exigencias salariales(Es) `16','Es `17','No encontró capacitador(Nec) `16','Nec `17','Costo elevado(Ce) `16','Ce `17','Habilidades adecuadas(Ha) `16','Ha `17','Cambio de trabajo(Cdt) `16','Cdt `17','Se capacitó previamente(Scp) `16','Scp `17','Sin apoyo público(Sap) `16','Sap `17','No hay beneficios(Nhb) `16','Nhb `17','Personal externo capacitado(Pec) `16','Pec `17', 'Otra(O) `16','O `17']]

list_df_enaproce18c = df_enaproce18a.iloc[:, 1:] 

for i in list_df_enaproce18c:      
            df_enaproce18a[i] = df_enaproce18a[i].astype(float).round(1)

dfi.export(df_enaproce18a,"df_enaproce18a.png")

#PREGUNTA 33: Número de empresas según el número de indicadores clave de desempeño que se monitorearon
df_enaproce33 = pd.read_excel(r"tam_ENAPROCE18.xlsx", sheet_name="33", skiprows=4, header=1) #Importar hoja 1 del archivo omitiendo las 4 primeras filas y nombrando las columnas como la primera fila

df_enaproce33 = df_enaproce33.dropna(axis=0, how='all') #Elimina las filas donde todos sus elementos son missing value
df_enaproce33 = df_enaproce33.dropna(axis=1, how='all') #Elimina las columnas donde todos sus elementos son missing value
df_enaproce33 = df_enaproce33.dropna() #Elimina las filas donde al menos uno de sus elementos es missing value

# limpieza del nombre de las columnas, remover espacios, carácteres especiales y pasar a minúsculas
df_enaproce33.columns #Conocer el nombre de las columnas
df_enaproce33.dtypes #Conocer la clase de cada columna 

df_enaproce33.columns = df_enaproce33.columns.str.strip()
df_enaproce33.columns = df_enaproce33.columns.str.replace(' ', '_')

df_enaproce33['Total_2'] = df_enaproce33.iloc[:, 2:].sum(1) #Crea una columna que suma los valores de las otras

list_df_enaproce33 = df_enaproce33.iloc[:, 2:7] 

for i in list_df_enaproce33:      
            df_enaproce33[str(i)+'_%'] = (df_enaproce33[i] / df_enaproce33['Total_2']) *100 #Ejecutado pero incorrecto

df_enaproce33 = df_enaproce33.sort_index(ascending=False) #invierte el orden de las filas

df_enaproce33a = df_enaproce33.filter(regex='Tamaño_de_Empresa|%') #Borra las columnas que no contengan el texto "tamaño_de_empresa" o "%"
df_enaproce33a.columns = ['Tamaño','1-2', '3-5', '6-9', '10 o más','No se monitorearon']

##PREGUNTA 33
eje_y33 = ['1-2', '3-5', '6-9', '10 o más','No se monitorearon']
#Barras
df_enaproce33atp3a1 = df_enaproce33at.plot.pie(y='Micro',legend=False,autopct='%1.1f%%',labels=None,colormap='Pastel2') #,title="Micro" #ELEGIDO
df_enaproce33atp3a2 = df_enaproce33at.plot.pie(y='PyMES',legend=False,autopct='%1.1f%%',labels=None,colormap='Pastel2') #,title="PyMES" #ELEGIDO
df_enaproce33atp3a3 = df_enaproce33at.plot.pie(y='Total',autopct='%1.1f%%',labels=None,colormap='Pastel2').legend(df_enaproce33at.index,loc='center left', bbox_to_anchor=(1, 0.5)) #,title="Total" #ELEGIDO

#PREGUNTA 50: Número de empresas según la causa principal por la que no solicitaron apoyo de los programas del Gobierno Federal
df_enaproce50 = pd.read_excel(r"tam_ENAPROCE18.xlsx", sheet_name="50", skiprows=4, header=1) #Importar hoja 1 del archivo omitiendo las 4 primeras filas y nombrando las columnas como la primera fila

df_enaproce50 = df_enaproce50.dropna(axis=0, how='all') #Elimina las filas donde todos sus elementos son missing value
df_enaproce50 = df_enaproce50.dropna(axis=1, how='all') #Elimina las columnas donde todos sus elementos son missing value
df_enaproce50 = df_enaproce50.dropna() #Elimina las filas donde al menos uno de sus elementos es missing value

# limpieza del nombre de las columnas, remover espacios, carácteres especiales y pasar a minúsculas
df_enaproce50.columns #Conocer el nombre de las columnas
df_enaproce50.dtypes #Conocer la clase de cada columna 

df_enaproce50.columns = df_enaproce50.columns.str.strip()
df_enaproce50.columns = df_enaproce50.columns.str.replace(' ', '_')

df_enaproce50['Total_2'] = df_enaproce50.iloc[:, 2:].sum(1) #Crea una columna que suma los valores de las otras

list_df_enaproce50 = df_enaproce50.iloc[:, 2:9] 

for i in list_df_enaproce50:      
            df_enaproce50[str(i)+'_%'] = (df_enaproce50[i] / df_enaproce50['Total_2']) *100 #Ejecutado pero incorrecto

df_enaproce50 = df_enaproce50.sort_index(ascending=False) #invierte el orden de las filas

df_enaproce50a = df_enaproce50.filter(regex='Tamaño_de_Empresa|%') #Borra las columnas que no contengan el texto "tamaño_de_empresa" o "%"
df_enaproce50a.columns = ['Tamaño','Innecesario','Incrédulo','Trámites excesivos','Desinformado','Desinteresado','Inexistentes','Otra']

##PREGUNTA 50
eje_y50 = ['Innecesario','Incrédulo','Trámites excesivos','Desinformado','Desinteresado','Inexistentes','Otra']
#Barras
df_enaproce50ap1b = df_enaproce50a.plot.barh('Tamaño', stacked=True,colormap='tab20c').legend(loc='center left', bbox_to_anchor=(1, 0.5)) #, title="Title"#DOS barra horizontal apilada. No se pudo agregar grid (.grid(axis='y')) junto a legend porque era uno u otro #ELEGIDO #No se pudo borrar la yenda del eje y por lo cual se procedio a cortar en word

#PREGUNTA 81: Número de empresas según los problemas que las empresas indicaron como los tres más importantes que enfrentan para su crecimiento
df_enaproce81 = pd.read_excel(r"tam_ENAPROCE18.xlsx", sheet_name="81", skiprows=4, header=1) #Importar hoja 1 del archivo omitiendo las 4 primeras filas y nombrando las columnas como la primera fila

df_enaproce81 = df_enaproce81.dropna(axis=0, how='all') #Elimina las filas donde todos sus elementos son missing value
df_enaproce81 = df_enaproce81.dropna(axis=1, how='all') #Elimina las columnas donde todos sus elementos son missing value
df_enaproce81 = df_enaproce81.dropna() #Elimina las filas donde al menos uno de sus elementos es missing value

# limpieza del nombre de las columnas, remover espacios, carácteres especiales y pasar a minúsculas
df_enaproce81.columns #Conocer el nombre de las columnas
df_enaproce81.dtypes #Conocer la clase de cada columna 

df_enaproce81.columns = df_enaproce81.columns.str.strip()
df_enaproce81.columns = df_enaproce81.columns.str.replace(' ', '_')

df_enaproce81['Total_2'] = df_enaproce81.iloc[:, 2:].sum(1) #Crea una columna que suma los valores de las otras

list_df_enaproce81 = df_enaproce81.iloc[:, 2:17] 

for i in list_df_enaproce81:      
            df_enaproce81[str(i)+'_%'] = (df_enaproce81[i] / df_enaproce81['Total_2']) *100 #Ejecutado pero incorrecto

df_enaproce81 = df_enaproce81.sort_index(ascending=False) #invierte el orden de las filas

df_enaproce81a = df_enaproce81.filter(regex='Tamaño_de_Empresa|%') #Borra las columnas que no contengan el texto "tamaño_de_empresa" o "%"
df_enaproce81a.columns = ['Tamaño','Crédito', 'Materias primas','Calidad de personal', 'Infraestructura', 'Demanda','Trámites gubernamentales','Inseguridad pública', 'Impuestos altos', 'Impuestos complejos','Empresas informales', 'Energia', 'Costos de telecomunicaciones','Búsqueda de personal','Sin problemas', 'Otro']

##PREGUNTA 81
eje_y81 = ['Crédito', 'Materias primas','Calidad de personal', 'Infraestructura', 'Demanda','Trámites gubernamentales','Inseguridad pública', 'Impuestos altos', 'Impuestos complejos','Empresas informales', 'Energia', 'Costos de telecomunicaciones','Búsqueda de personal','Sin problemas', 'Otro']
#Barras
df_enaproce81at = df_enaproce81a[eje_y81].T
df_enaproce81at.columns = ['Micro','PyMES','Total']
df_enaproce81at= df_enaproce81at.sort_values('Total',ascending=False)
df_enaproce81atp2a = df_enaproce81at.plot.bar().grid(axis='y') #title="Title"#TRES Barras verticales #ELEGIDO, aunque quizá cambiar de colores (valorar bien el TRES por las gridlines)

#PREGUNTA 85: Número de empresas según la manera de cómo han llevado la contabilidad
df_enaproce85 = pd.read_excel(r"tam_ENAPROCE18.xlsx", sheet_name="85", skiprows=5, header=1) #Importar hoja 1 del archivo omitiendo las 4 primeras filas y nombrando las columnas como la primera fila

df_enaproce85 = df_enaproce85.dropna(axis=0, how='all') #Elimina las filas donde todos sus elementos son missing value
df_enaproce85 = df_enaproce85.dropna(axis=1, how='all') #Elimina las columnas donde todos sus elementos son missing value
df_enaproce85 = df_enaproce85.dropna() #Elimina las filas donde al menos uno de sus elementos es missing value

# limpieza del nombre de las columnas, remover espacios, carácteres especiales y pasar a minúsculas
df_enaproce85.columns #Conocer el nombre de las columnas
df_enaproce85.dtypes #Conocer la clase de cada columna 

df_enaproce85.columns = df_enaproce85.columns.str.strip()
df_enaproce85.columns = df_enaproce85.columns.str.replace(' ', '_')

df_enaproce85.rename(columns={'Unnamed:_2':'Total'}, inplace=True)

list_df_enaproce85 = df_enaproce85.iloc[:, 2:] 

for i in list_df_enaproce85:      
            df_enaproce85[str(i)+'_%'] = (df_enaproce85[i] / df_enaproce85['Total']) *100 #Ejecutado pero incorrecto
            
df_enaproce85 = df_enaproce85.sort_index(ascending=False) #invierte el orden de las filas

df_enaproce85.rename(columns={'Unnamed:_0':'Tamaño_de_Empresa'}, inplace=True)

df_enaproce85a = df_enaproce85.filter(regex='Tamaño_de_Empresa|%') #Borra las columnas que no contengan el texto "tamaño_de_empresa" o "%"
df_enaproce85a.columns = ['Tamaño','Libreta(L) Inicio(I)','Contador profesional(Cp) I','Portal Mis Cuentas(PMC) I','Programas(P) I','Sin contabilidad(Sc) I', 'No sabe(Ns) I', 'Otro(O) I','L Actual (A)','Cp A','PMC A','P A','Sc A', 'Ns A', 'O A']
df_enaproce85a = df_enaproce85a[['Tamaño','Libreta(L) Inicio(I)','L Actual (A)','Contador profesional(Cp) I','Cp A','Portal Mis Cuentas(PMC) I','PMC A','Programas(P) I','P A','Sin contabilidad(Sc) I','Sc A', 'No sabe(Ns) I', 'Ns A', 'Otro(O) I', 'O A']]

list_df_enaproce85a = df_enaproce85a.iloc[:, 1:] 

for i in list_df_enaproce85a:      
            df_enaproce85a[i] = df_enaproce85a[i].astype(float).round(1) 

dfi.export(df_enaproce85a,"df_enaproce85a.png")