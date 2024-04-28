import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset especificando el separador y omitiendo el encabezado
df = pd.read_csv('MSP_cvd19_casos_20220403.csv', encoding='ISO-8859-1', delimiter=';')

# Porcentaje de registros que tienen y no tienen COVID
total_registros = len(df)
covid_registros = len(df[df['clasificacion_final'] == 'CONFIRMADO'])
no_covid_registros = len(df[df['clasificacion_final'] == 'DESCARTADO'])

porcentaje_covid = (covid_registros / total_registros) * 100
porcentaje_no_covid = (no_covid_registros / total_registros) * 100

# Porcentaje de las personas fallecidas y no fallecidas por tener COVID
fallecidos_covid = len(df[(df['clasificacion_final'] == 'CONFIRMADO') & (df["condicion_final"] == 'MUERTO')])
no_fallecidos_covid = covid_registros - fallecidos_covid

porcentaje_fallecidos_covid = (fallecidos_covid / covid_registros) * 100
porcentaje_no_fallecidos_covid = (no_fallecidos_covid / covid_registros) * 100

# Porcentaje de hombres y mujeres con COVID
hombres_covid = len(df[(df['clasificacion_final'] == 'CONFIRMADO') & (df["sexo_paciente"] == 'HOMBRE')])
mujeres_covid = covid_registros - hombres_covid

porcentaje_hombres_covid = (hombres_covid / covid_registros) * 100
porcentaje_mujeres_covid = (mujeres_covid / covid_registros) * 100

# Porcentajes de personas que tienen COVID por provincia
covid_por_provincia = df[df['clasificacion_final'] == 'CONFIRMADO']["provincia"].value_counts() / covid_registros * 100

# Visualización de los datos
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Gráfico de porcentaje de registros con y sin COVID
axs[0, 0].pie([porcentaje_covid, porcentaje_no_covid], labels=['COVID', 'No COVID'], autopct='%1.1f%%')
axs[0, 0].set_title('Porcentaje de registros con y sin COVID')

# Gráfico de porcentaje de personas fallecidas y no fallecidas por COVID
axs[0, 1].pie([porcentaje_fallecidos_covid, porcentaje_no_fallecidos_covid], labels=['Fallecidos', 'No Fallecidos'], autopct='%1.1f%%')
axs[0, 1].set_title('Porcentaje de personas fallecidas y no fallecidas por COVID')

# Gráfico de porcentaje de hombres y mujeres con COVID
axs[1, 0].pie([porcentaje_hombres_covid, porcentaje_mujeres_covid], labels=['Hombres', 'Mujeres'], autopct='%1.1f%%')
axs[1, 0].set_title('Porcentaje de hombres y mujeres con COVID')

# Gráfico de porcentaje de personas con COVID por provincia
axs[1, 1].bar(covid_por_provincia.index, covid_por_provincia.values)
axs[1, 1].set_title('Porcentaje de personas con COVID por provincia')
axs[1, 1].tick_params(axis='x', rotation=90)  # Rotar las etiquetas del eje x para mejor visualización

plt.tight_layout()
plt.show()
