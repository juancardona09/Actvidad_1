from datasets import load_dataset


class HFDataLoader:
    """Carga un dataset de Hugging Face y lo devuelve como DataFrame."""

    def __init__(self, dataset_id, split="train"):
        # Nombre del dataset en Hugging Face, por ejemplo "scikit-learn/iris"
        self.dataset_id = dataset_id
        # Parte del dataset que se va a cargar
        self.split = split

    def load(self):
        # Descarga el dataset desde Hugging Face
        dataset = load_dataset(self.dataset_id, split=self.split)
        # Convierte el dataset a un DataFrame de pandas
        df = dataset.to_pandas()
        return df
