import pandas as pd
import os

class DataLoader:
    def __init__(self, file_path='datasets/diabetes_data.csv'):
        self.file_path = os.path.join(os.path.dirname(__file__), file_path)

    def load_data(self):
        return pd.read_csv(self.file_path)
