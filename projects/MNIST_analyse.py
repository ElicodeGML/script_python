"""
Script d'analyse MNIST - Débruitage d'images avec KNN
Nettoie des images MNIST bruitées en utilisant un classifieur KNN multi-sorties.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


# ============================================================================
# 1. CHARGEMENT DES DONNÉES
# ============================================================================
def load_data():
    """Charge les données MNIST depuis les fichiers CSV."""
    mnists_train = pd.read_csv("text/mnist_donnee/mnist_train_vrai.csv").to_numpy()
    mnists_test = pd.read_csv("text/mnist_donnee/mnist_test_vrai.csv").to_numpy()
    
    # Décommentez si le label est dans la première colonne :
    # X_train = mnists_train[:, 1:]
    # X_test = mnists_test[:, 1:]
    
    X_train = mnists_train
    X_test = mnists_test
    
    return X_train, X_test


# ============================================================================
# 2. GÉNÉRATION DU BRUIT
# ============================================================================
def generate_noise(X_train, X_test):
    """Génère du bruit aléatoire pour les données."""
    noise_train = np.random.randint(0, 100, (len(X_train), 784))
    noise_test = np.random.randint(0, 100, (len(X_test), 784))
    return noise_train, noise_test


# ============================================================================
# 3. ENTRAÎNEMENT DU MODÈLE
# ============================================================================
def train_model(X_train_mod, y_train):
    """Entraîne le modèle KNN multi-sorties."""
    knn_clf = KNeighborsClassifier()
    knn_clf.fit(X_train_mod, y_train)
    return knn_clf


# ============================================================================
# 4. AFFICHAGE D'UNE IMAGE NETTOYÉE
# ============================================================================
def display_cleaned_image(model, X_test_mod, index=0):
    """Prédit et affiche une image nettoyée."""
    # Prédiction sur l'image bruitée
    clean_digit = model.predict([X_test_mod[index]])
    
    # Redimensionner en 28x28 pour l'affichage
    clean_digit_image = clean_digit[0].reshape(28, 28)
    
    # Affichage
    plt.imshow(clean_digit_image, cmap="binary")
    plt.axis("off")
    plt.title(f"Image nettoyée (index {index})")
    plt.show()


# ============================================================================
# 5. EXÉCUTION PRINCIPALE
# ============================================================================
if __name__ == "__main__":
    # Charger les données
    X_train, X_test = load_data()
    
    # Générer le bruit
    noise_train, noise_test = generate_noise(X_train, X_test)
    
    # Créer les données bruitées
    X_train_mod = X_train + noise_train
    X_test_mod = X_test + noise_test
    
    # Cibles : images propres d'origine
    y_train = X_train
    
    # Entraîner le modèle
    knn_clf = train_model(X_train_mod, y_train)
    
    # Afficher une image nettoyée
    display_cleaned_image(knn_clf, X_test_mod, index=0)
