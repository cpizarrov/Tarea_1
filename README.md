## Clasificador de Propinas para Viajes en Taxi en NYC (2020)

Inspirado en la charla ["Keeping up with Machine Learning in Production"](https://github.com/shreyashankar/debugging-ml-talk) de [Shreya Shankar](https://twitter.com/sh_reya)

Este proyecto muestra la construcción de un modelo de machine learning de juguete, usando datos de viajes de los taxis amarillos de Nueva York para el año 2020, [proporcionados por la NYC Taxi and Limousine Commission (TLC)](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

La idea es encontrar aquellos viajes donde la propina dejada por el pasajero fue alta, es decir, mayor al 20% del costo del viaje.

Para ello ajustaremos un modelo de classificación binaria RandomForest usando los datos de los viajes de enero de 2020. Probaremos el modelo resultante sobre los datos de los viajes de febrero de 2020. Compararemos el desempeño del modelo en ambos casos usando la métrica de [f1-score](https://en.wikipedia.org/wiki/F-score).

**Este proyecto está construido para ser ejecutado en [Google Colab](https://colab.research.google.com/), al que podemos acceder de manera gratuita solo teniendo un usuario de Google (Gmail) y un navegador web. No es necesario instalar nada en el computador local.**

===========

## ¿Cómo ejecutarlo? 

A continuación te detallamos las instrucciones para ejecutar el modelo. 

### 1. Clona el repositorio utilizando git clone: 
```
!git clone https://github.com/cpizarrov/Tarea_1.git
```

### 2. Asegúrate de establecer tu directorio de trabajo en 'content/Tarea_1': 
```
%cd /content/Tarea_1
```

### 3. Instala los requerimientos: 

```
!pip install -r /content/Tarea_1/requirements.txt
```

### 4. Importa las funciones: 

```
from src import (
    load_taxi_data,
    load_taxi_data_full,
    preprocess,
    train_model,
    predict,
    load_model,
    evaluate,
    evaluate_months,
    features,
    target_col,
    plot_casos,
    plot_f1score
)
```
Cada una te servirá para realizar alguna tarea específica. En este caso: 

- **load_taxi_data**: Realiza la carga cruda de datos que serán utilizados para el entrenamiento del modelo. En este caso corresponde a datos de enero del 2020. 
- **load_taxi_data_full**: Realiza la carga cruda de datos en un período más extenso. Por ahora se encuentra limitado desde Enero hasta Abril de 2020. Esto servirá para testear y evaluar el rendimiento del modelo a lo largo del año. 
- **features**: Contiene un listado de variables que formarán parte del entrenamiento del modelo. 
- **target_col**: Define la variable objetivo. 
- **preprocess**: Realiza la limpieza de los datos crudos. El dataframe resultante contiene sólo la variable objetivo y las características de entrada para el entrenamiento del modelo. 
- **train_model**: Entrena y guarda el modelo. 
- **load_model**: Carga el modelo entrenado. 
- **predict**: Realiza las predicciones en base al modelo entrenado. 
- **evaluate:** Retorna la métrica F1-Score que utilizaremos para evaluar el modelo. 
- **evaluate_months**: Retorna la métrica F1-Score. En esta ocasión, se realiza la evaluación automática para varios meses definidos por el usuario. De esta forma, podemos monitorear el desempeño del modelo a lo largo de algún año. 
- **plot_casos**: Permite generar un gráfico de barras para monitorear la cantidad de casos a nivel mensual. 
- **plot_f1score**: Permite generar una gráfico de líneas para monitorear el F1-Score a nivel mensual. 


### 4. Carga y procesa los datos de entrenamiento (Enero 2020): 

```
df = load_taxi_data()
df = preprocess(df, target_col)
```

### 5. Entrena el modelo. 

```
model = train_model(df[features], df[target_col])
```

Si no deseas entrenarlo, recuerda que ya existe uno en el directorio */models*

```
model = load_model("models/random_forest.joblib")
```

### 6. Evalúa su desempeño 

```
probs = predict(model, df[features])
print("F1 Score:", evaluate(probs, df[target_col]))
```

### 7. ¿Quieres ir más allá en su evaluación? Revisemos más meses: 

Primero que todo, cargamos y procesamos los datos desde enero hasta abril: 

```
df_full = preprocess(load_taxi_data_full("2020"), target_col)
```

Evalúa el modelo con este nuevo dataframe. Puedes elegir meses específicos con 'start_month' y 'end_month': 

```
results = evaluate_months(model, df=df_full, year="2020", start_month=1, end_month=4)
```

### 8. Grafica tus resultados! 

Utiliza las funciones *plot_f1score* y *plot_casos* para visualizar tus resultados mes a mes. Puedes establer un nuevo directorio para guardar éstos resultados si así lo deseas:

```
plot_f1score(results, save_dir="reports/figures")
```

```
plot_casos(results, save_dir="reports/figures")
```

### Con esto hemos finalizado! 


