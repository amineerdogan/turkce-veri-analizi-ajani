import pandas as pd

DOSYA = "data/raw/nufus_il.xls"

def nufus_yukle(yol=DOSYA):
    ham = pd.read_excel(yol, header=None)
    df = ham.iloc[5:86, [0, 1, 2, 4, 5, 7, 8, 10, 11]].copy()
    df.columns = ["il", "toplam_2024", "toplam_2025",
                  "merkez_2024", "merkez_2025",
                  "belde_koy_2024", "belde_koy_2025",
                  "hiz_2023_2024", "hiz_2024_2025"]
    df["il"] = df["il"].astype(str).str.strip()
    for c in df.columns[1:]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df.reset_index(drop=True)

if __name__ == "__main__":
    df = nufus_yukle()
    ham = pd.read_excel(DOSYA, header=None)
    print("il sayisi:", len(df))
    print("2025 toplam (illerin toplami):", df["toplam_2025"].sum())
    print("2025 toplam (dosyadaki Toplam satiri):", ham.iloc[4, 2])
    print(df.dtypes)
    print(df[df["belde_koy_2025"].isna()])
