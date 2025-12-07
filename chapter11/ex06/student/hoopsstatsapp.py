"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(df):
    """
    Cleans the basketball stats DataFrame by splitting FG, 3PT, FT columns
    into makes and attempts columns.
    """
    # Listele dönüştürülecek sütunlar ve yeni başlıklar
    cols = [("FG", "FGM", "FGA"), ("3PT", "3PM", "3PA"), ("FT", "FTM", "FTA")]

    for col, make_col, att_col in cols:
        if col in df.columns:
            # Sütunu ayır: "makes/attempts"
            makes = df[col].apply(lambda x: int(str(x).split('/')[0]))
            attempts = df[col].apply(lambda x: int(str(x).split('/')[1]))
            # Orijinal sütunu konumunda sil
            idx = df.columns.get_loc(col)
            df.drop(columns=[col], inplace=True)
            # Yeni sütunları ekle aynı pozisyonda
            df.insert(idx, make_col, makes)
            df.insert(idx + 1, att_col, attempts)

    return df

def main():
    """Creates the data frame and view and starts the app."""
    # CSV dosyasını oku
    frame = pd.read_csv("cleanbrogdonstats.csv")
    # Veriyi temizle
    frame = cleanStats(frame)
    # GUI’yi başlat
    HoopStatsView(frame).mainloop()

if __name__ == "__main__":
    main()
