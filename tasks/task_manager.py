import numpy as np

# Tehlikeli kimyasalların isimlerini döndür.
# Input: DataFrame
# Output: Series (Chemical isimleri)
def get_hazardous_chemicals(df):
    return df[df["IsHazardous"]]["Chemical"]


# Tüm "Amount" değerlerini grama çevir. (1 liter = 1000 gram, 1 kg = 1000 gram)
# Input: DataFrame
# Output: Yeni DataFrame, "Amount" sütunu gram cinsinden.
def convert_amounts_to_grams(df):
    multipliers = {
        "kg": 1000,
        "liter": 1000,
        "g": 1
    }
    
    df['Amount'] = df['Amount'] * df['Unit'].str.lower().map(multipliers)
    return df


# Miktarı en fazla olan n kimyasalı döndür (gram cinsinden sıralı).
# Input: DataFrame, n=2
# Output: En fazla miktarda 2 kimyasal.
def get_top_n_chemicals(df, n):
    return df.sort_values(by="Amount", ascending=False).iloc[:n]


# Kullanılan birimlerin listesini döndür ("liter", "kg" vb.)
# Input: DataFrame
# Output: Series ya da list
def get_unique_units(df):
    return df["Unit"]


# İsim içerisinde keyword geçen kimyasalları filtrele.
# Input: keyword="Acetone"
# Output: "Acetone" içeren satırları içeren DataFrame
def filter_chemicals_by_name(df, keyword):
    return df[df["Chemical"].str.contains(keyword)]


# Toplam madde miktarını gram cinsinden hesapla.
# Output: float
def get_total_amount(df):
    return df["Amount"].sum()


# NumPy kullanarak miktarların standart sapmasını hesapla.
# Output: float
def calculate_standard_deviation(df):
    return np.std(df["Amount"])


# Miktarları min-max normalize et.
# (formül: (x - min) / (max - min))
# Output: Series (normalize edilmiş değerler)
def normalize_amounts(df):
   min_df = df["Amount"].min()
   max_df = df["Amount"].max()

   return (df["Amount"] - min_df) / (max_df - min_df)


# Tehlikeli olup miktarı 1000 gramdan fazla olanları "HighRisk" olarak işaretle.
# Output: Yeni DataFrame, HighRisk adında yeni sütun içerir.
def flag_high_risk(df):
    df["HighRisk"] = df["IsHazardous"] & (df["Amount"] > 1000)
    return df