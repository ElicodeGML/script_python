import statistics
import math
from collections import Counter

class Statistiques:
    """Classe pour calculer diverses mesures statistiques sur une liste de nombres."""

    def mean(self, data_list):
        """Retourne la moyenne d'une liste de nombres."""
        if not data_list: raise ValueError("List cannot be empty.")
        return sum(data_list) / len(data_list)

    def median(self, data_list):
        """Retourne la médiane."""
        if not data_list: raise ValueError("List cannot be empty.")
        sorted_list = sorted(data_list)
        n = len(sorted_list)
        if n % 2 == 0:
            # Si le nombre d'éléments est pair
            mid1 = sorted_list[n // 2 - 1]
            mid2 = sorted_list[n // 2]
            return (mid1 + mid2) / 2
        else:
            # Si le nombre d'éléments est impair
            return sorted_list[n // 2]

    def mode(self, data_list):
        """Retourne le(s) mode(s). Peut retourner une liste si plusieurs modes."""
        if not data_list: raise ValueError("List cannot be empty.")
        counts = Counter(data_list)
        max_count = max(counts.values())
        modes = [key for key, value in counts.items() if value == max_count]
        return modes

    def std_deviation(self, data_list, sample=True):
        """Retourne l'écart-type. 'sample=True' pour l'écart-type d'échantillon, 'False' pour la population."""
        if len(data_list) < 2 and sample: raise ValueError("Need at least two data points for sample standard deviation.")
        if not data_list: raise ValueError("List cannot be empty.")
        return statistics.stdev(data_list) if sample else statistics.pstdev(data_list)

    def variance(self, data_list, sample=True):
        """Retourne la variance. 'sample=True' pour la variance d'échantillon, 'False' pour la population."""
        if len(data_list) < 2 and sample: raise ValueError("Need at least two data points for sample variance.")
        if not data_list: raise ValueError("List cannot be empty.")
        return statistics.variance(data_list) if sample else statistics.pvariance(data_list)

    def data_range(self, data_list):
        """Retourne l'étendue (max - min) d'une liste de nombres."""
        if not data_list: raise ValueError("List cannot be empty.")
        return max(data_list) - min(data_list)

# Démonstration de la classe Statistiques
stats = Statistiques()
data = []

XX = [1, 1, 1, 1, 1, 5, 9, 9, 9, 9, 9]
YY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
RR = []
X = 0
yy = 0
Yy = 0

for i in range(5):
    RR.append(5*11/100)
RR.append(1*11/100)
for i in range(5):
    RR.append(5*11/100)
        
import matplotlib.pyplot as plt

plt.scatter(XX, RR, c="green", label="point")
plt.plot(XX, RR, color="blue", linestyle='-', label="trait")

print(stats.mode(RR), stats.std_deviation(RR))