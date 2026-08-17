# ===== IMPORTS =====
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.image as mpimg

# ===== DATA LOADING =====
df = pd.read_csv("text/datata.csv")
image = "images/california.png"

# ===== DIAGRAM FROM BOOK =====
california_img = mpimg.imread(image)
ax = df.plot(kind="scatter", x="longitude", y="latitude", figsize=(10, 7),
             s=df['population']/100, label="Population",
             c="median_house_value", cmap=plt.get_cmap("jet"),
             colorbar=False, alpha=0.4)
plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.5,
           cmap=plt.get_cmap("jet"))
plt.ylabel("Latitude", fontsize=14)
plt.xlabel("Longitude", fontsize=14)

# Add colorbar with formatted labels
prices = df["median_house_value"]
tick_values = np.linspace(prices.min(), prices.max(), 11)
cbar = plt.colorbar(ticks=tick_values/prices.max())
cbar.ax.set_yticklabels(["$%dk" % (round(v/1000)) for v in tick_values], fontsize=14)
cbar.set_label('Median House Value', fontsize=16)

plt.legend(fontsize=16)
plt.show()

# ===== CUSTOM DIAGRAM =====
plt.figure(figsize=(8, 6))
plt.scatter(df['longitude'], df['latitude'], s=df['population']/50, 
            c=df['median_house_value'], alpha=0.25)
plt.ylabel("latitude")
plt.xlabel("longitude")
plt.title("diagrame du nb d'abitant en fonction du lieu et du prix")

# Add colorbar with price formatting
bar = plt.colorbar()
bar.ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:.0f} $"))

# Add legend for population sizes
for pop in [1, 5, 10, 20]:
    plt.scatter([], [], s=pop*1000/50, color='gray', alpha=0.5, label=f"{pop*100} habitants")
plt.legend(title="Population")
# plt.show()

# ===== DATA INSPECTION =====
print(df["ocean_proximity"].head(10))