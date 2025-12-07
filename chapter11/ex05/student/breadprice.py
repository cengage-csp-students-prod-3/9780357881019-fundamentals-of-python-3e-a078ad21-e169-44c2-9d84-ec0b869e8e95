"""
File: breadprice.py
Displays a line plot of the average price of bread by year.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Verileri elle tablo gibi oluşturuyoruz
    data = {
        "Year": [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
        "Jan":  [1.423, 1.422, 1.365, 1.479, 1.425, 1.351, 1.281, 1.274, 1.351, 1.546, 1.555],
        "Feb":  [1.442, 1.411, 1.388, 1.435, 1.407, 1.358, 1.265, 1.282, 1.375, 1.537, 1.578],
        "Mar":  [1.395, 1.412, 1.359, 1.440, 1.416, 1.329, 1.309, 1.261, 1.374, 1.526, 1.607],
        "Apr":  [1.426, 1.409, 1.388, 1.454, 1.406, 1.328, 1.281, 1.285, 1.406, 1.510, 1.612],
        "May":  [1.412, 1.401, 1.401, 1.463, 1.382, 1.327, 1.293, 1.289, 1.412, 1.511, 1.606],
        "Jun":  [1.403, 1.439, 1.400, 1.467, 1.333, 1.335, 1.279, 1.280, 1.474, 1.510, 1.691],
        "Jul":  [1.427, 1.434, 1.413, 1.447, 1.349, 1.327, 1.293, 1.281, 1.485, 1.491, 1.715],
        "Aug":  [1.407, 1.408, 1.396, 1.420, 1.341, 1.348, 1.302, 1.275, 1.495, 1.467, np.nan],
        "Sep":  [1.401, 1.419, 1.405, 1.432, 1.329, 1.349, 1.288, 1.296, 1.492, 1.580, np.nan],
        "Oct":  [1.422, 1.358, 1.414, 1.418, 1.343, 1.328, 1.277, 1.325, 1.503, 1.526, np.nan],
        "Nov":  [1.418, 1.382, 1.420, 1.409, 1.362, 1.295, 1.274, 1.361, 1.515, 1.547, np.nan],
        "Dec":  [1.436, 1.385, 1.466, 1.428, 1.362, 1.316, 1.290, 1.363, 1.538, 1.532, np.nan]
    }

    # DataFrame oluştur
    df = pd.DataFrame(data)

    # NaN değerleri sütun ortalamasıyla doldur
    df = df.fillna(df.mean(axis=1))

    # Yıllık ortalama fiyatı hesapla
    df['AvgPrice'] = df.iloc[:, 1:13].mean(axis=1)

    # Line plot
    plt.figure(figsize=(8, 4))
    plt.plot(df['Year'], df['AvgPrice'], marker='o', linestyle='-', color='blue')
    plt.title("Average Price of Bread by Year")
    plt.xlabel("Year")
    plt.ylabel("Average Price ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
