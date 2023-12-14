from sklearn import svm
import joblib
import pandas as pd

class SVMModel:
    def __init__(self):
        # Chargez le modèle SVM pré-entraîné
        self.model = joblib.load('app/svm_model.pkl')

    def classify_genre(self, features):
        # Implémentez la logique de classification ici
        prediction = self.model.predict(features)
        return prediction.tolist()
