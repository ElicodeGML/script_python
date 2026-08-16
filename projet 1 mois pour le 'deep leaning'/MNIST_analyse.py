import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# 1. Chargement des données (On suppose que le CSV contient uniquement les 784 pixels)
mnists_train = pd.read_csv("text/mnist_donnee/mnist_train_vrai.csv").to_numpy()
mnists_test = pd.read_csv("text/mnist_donnee/mnist_test_vrai.csv").to_numpy()

# Si vos fichiers CSV contiennent le label (le chiffre) dans la première colonne,
# décommentez les lignes suivantes pour ne garder que les pixels :
# X_train = mnists_train[:, 1:]
# X_test = mnists_test[:, 1:]
X_train = mnists_train
X_test = mnists_test

# 2. Génération du bruit (Génère une matrice de la même taille que vos données)
noise_train = np.random.randint(0, 100, (len(X_train), 784))
noise_test = np.random.randint(0, 100, (len(X_test), 784))

# 3. Les entrées (X) sont les images BRUITÉES
X_train_mod = X_train + noise_train
X_test_mod = X_test + noise_test

# 4. Les cibles (y) sont les images PROPRES d'origine
y_train_mod = X_train
y_test_mod = X_test

# 5. Entraînement du modèle Multi-sorties
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train_mod, y_train_mod)

# 6. Test et affichage d'un chiffre nettoyé
# On prend par exemple le premier élément du jeu de test (index 0)
some_index = 0
clean_digit = knn_clf.predict([X_test_mod[some_index]])

# Redimensionner en 28x28 pour l'affichage matplotlib
clean_digit_image = clean_digit.reshape(28, 28)

plt.imshow(clean_digit_image, cmap="binary")
plt.axis("off")
plt.show()
