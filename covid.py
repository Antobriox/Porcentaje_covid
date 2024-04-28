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

print("Porcentaje de registros con COVID:", porcentaje_covid)
print("Porcentaje de registros sin COVID:", porcentaje_no_covid)

# Porcentaje de las personas fallecidas y no fallecidas por tener COVID
fallecidos_covid = len(df[(df['clasificacion_final'] == 'CONFIRMADO') & (df["condicion_final"] == 'MUERTO')])
no_fallecidos_covid = covid_registros - fallecidos_covid

porcentaje_fallecidos_covid = (fallecidos_covid / covid_registros) * 100
porcentaje_no_fallecidos_covid = (no_fallecidos_covid / covid_registros) * 100

print("Porcentaje de personas fallecidas por COVID:", porcentaje_fallecidos_covid)
print("Porcentaje de personas no fallecidas por COVID:", porcentaje_no_fallecidos_covid)

# Porcentaje de hombres y mujeres con COVID
hombres_covid = len(df[(df['clasificacion_final'] == 'CONFIRMADO') & (df["sexo_paciente"] == 'HOMBRE')])
mujeres_covid = covid_registros - hombres_covid

porcentaje_hombres_covid = (hombres_covid / covid_registros) * 100
porcentaje_mujeres_covid = (mujeres_covid / covid_registros) * 100

print("Porcentaje de hombres con COVID:", porcentaje_hombres_covid)
print("Porcentaje de mujeres con COVID:", porcentaje_mujeres_covid)

# Porcentajes de personas que tienen COVID por provincia
covid_por_provincia = df[df['clasificacion_final'] == 'CONFIRMADO']["provincia"].value_counts() / covid_registros * 100

print("Porcentajes de personas con COVID por provincia:")
print(covid_por_provincia)

# Sacar por rango de edades los porcentajes de personas con COVID
bins = [0, 18, 30, 45, 60, 75, 150]
labels = ['0-18', '19-30', '31-45', '46-60', '61-75', '75+']
df['rango_edad'] = pd.cut(df["edad_paciente"], bins=bins, labels=labels, right=False)

covid_por_rango_edad = df[df['clasificacion_final'] == 'CONFIRMADO']['rango_edad'].value_counts() / covid_registros * 100

print("Porcentajes de personas con COVID por rango de edad:")
print(covid_por_rango_edad)

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

plt.tight_layout()
plt.show()
