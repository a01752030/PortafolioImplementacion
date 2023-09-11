# README

## Descripción del Modelo de ML Implementado
El script implementa un modelo de Regresión Logística desde cero. Esta técnica es ampliamente utilizada para clasificación binaria. Algunas características clave del modelo son:

- **Función Sigmoidal**: Es el corazón de la regresión logística y convierte cualquier número en un valor entre 0 y 1, lo que es útil para una tarea de clasificación binaria.
  
- **Función de Costo**: Utilizamos una función de costo logarítmico regularizada para evaluar qué tan bien (o mal) el modelo está funcionando.

- **Gradiente Descendiente**: Este algoritmo optimiza los parámetros del modelo minimizando iterativamente la función de costo.

El modelo también implementa regularización para prevenir overfitting, lo que mejora su generalización en datos no vistos.

## Dataset Utilizado
El dataset usado es el **Spaceship Titanic** que se puede encontrar en [Kaggle](https://www.kaggle.com/competitions/spaceship-titanic). Este dataset es una variante ficticia del famoso dataset del Titanic, y es utilizado para predecir si un pasajero sobrevivió o no basado en diversas características.

## Archivos para Revisión
Para evaluar los indicadores de las subcompetencias, se deberán revisar los siguientes archivos:

- `logistic.py`: Este archivo contiene la implementación principal de la regresión logística.
  
- `data.py`: Aquí es donde se gestiona la carga y preprocesamiento de los datos que se utilizan en `logistic.py`.

## Cambios Implementados

### Feedback del Docente
1. **Agregar el README**: Se solicitó la creación de un archivo README para proporcionar una visión general y detalles técnicos del proyecto.

    **Solución**: Se redactó este archivo README para incluir todos los detalles solicitados.

2. **Agregar el Reporte**: Se requirió un reporte que describa los hallazgos y resultados obtenidos a partir del modelo.

    **Solución**: Se generó un reporte (no incluido en este README) que presenta un análisis detallado de los resultados, las métricas de rendimiento y posibles mejoras.

---

Se recomienda que cualquier persona interesada en ejecutar o modificar este código tenga un conocimiento básico de Python, Regresión Logística, y técnicas generales de Machine Learning para obtener el máximo provecho.

Puedes copiar y pegar el contenido de arriba directamente en tu archivo README.md en tu repositorio. ¡Espero que te sea de ayuda!
