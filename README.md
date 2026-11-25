# Actividad 1: carga y resumen de datos con Hugging Face

Repositorio: https://github.com/juancardona09/Actvidad_1

Este trabajo carga un dataset de Hugging Face, lo convierte en un DataFrame de
pandas, aplica una transformacion minima y genera un resumen en un archivo `.txt`.

## Archivos

- `hf_data_loader.py`: clase `HFDataLoader`, carga el dataset desde Hugging Face.
- `dataset_summarizer.py`: clase `DatasetSummarizer`, genera el resumen en `.txt`.
- `actividad.ipynb`: notebook con el flujo completo.
- `resumen_dataset.txt`: resumen generado a partir de los datos transformados.

## Como ejecutarlo

1. Instalar las dependencias:

   ```
   pip install -r requirements.txt
   ```

2. Abrir `actividad.ipynb` y ejecutar todas las celdas (Run All).

3. Al final se genera `resumen_dataset.txt` con el resumen de los datos transformados.
