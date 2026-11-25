class DatasetSummarizer:
    """Recibe un DataFrame y escribe un resumen de su contenido en un .txt."""

    def __init__(self, output_path):
        # Ruta del archivo .txt donde se guarda el resumen
        self.output_path = output_path

    def summarize(self, df):
        # Arma el texto del resumen
        texto = "=== RESUMEN DEL DATASET ===\n\n"
        texto += f"Filas: {df.shape[0]}\n"
        texto += f"Columnas: {df.shape[1]}\n\n"

        texto += "Nombres y tipos de columna:\n"
        texto += str(df.dtypes) + "\n\n"

        texto += "Valores nulos por columna:\n"
        texto += str(df.isna().sum()) + "\n"
        texto += f"Total de valores nulos: {df.isna().sum().sum()}\n\n"

        texto += "Estadisticas basicas:\n"
        texto += str(df.describe()) + "\n"

        # Guarda el resumen en el archivo .txt
        with open(self.output_path, "w", encoding="utf-8") as archivo:
            archivo.write(texto)

        return texto
