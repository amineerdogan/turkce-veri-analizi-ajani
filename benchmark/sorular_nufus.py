import json
from gold_nufus import nufus_yukle

df = nufus_yukle()

sorular = [
    {"id": "nufus_001",
     "soru": "2025 yılında nüfusu en yüksek olan il hangisidir?",
     "altin_cevap": df.loc[df["toplam_2025"].idxmax(), "il"],
     "tur": "metin", "zorluk": "kolay", "hedef_tuzak": "T03"},
    {"id": "nufus_002",
     "soru": "2025 yılında illerin ortalama nüfusu kaçtır?",
     "altin_cevap": round(float(df["toplam_2025"].mean()), 2),
     "tur": "sayi", "zorluk": "kolay", "hedef_tuzak": "T03"},
    {"id": "nufus_003",
     "soru": "2024'ten 2025'e nüfusu azalan kaç il vardır?",
     "altin_cevap": int((df["toplam_2025"] < df["toplam_2024"]).sum()),
     "tur": "sayi", "zorluk": "orta", "hedef_tuzak": "T03"},
    {"id": "nufus_004",
     "soru": "2025 yılında belde ve köylerde yaşayan nüfusu en yüksek olan il hangisidir?",
     "altin_cevap": df.loc[df["belde_koy_2025"].idxmax(), "il"],
     "tur": "metin", "zorluk": "orta", "hedef_tuzak": "T05"},
    {"id": "nufus_005",
     "soru": "2025 yılında Türkiye genelinde belde ve köylerde yaşayan toplam nüfus kaçtır?",
     "altin_cevap": int(df["belde_koy_2025"].sum()),
     "tur": "sayi", "zorluk": "orta", "hedef_tuzak": "T05,T06"},
    {"id": "nufus_006",
     "soru": "2024-2025 döneminde yıllık nüfus artış hızı en yüksek olan il hangisidir ve bu hız binde kaçtır?",
     "altin_cevap": {"il": df.loc[df["hiz_2024_2025"].idxmax(), "il"],
                     "deger": round(float(df["hiz_2024_2025"].max()), 2)},
     "tur": "sozluk", "zorluk": "orta", "hedef_tuzak": "T07"},
]

with open("benchmark/sorular_nufus.json", "w", encoding="utf-8") as f:
    json.dump(sorular, f, ensure_ascii=False, indent=2)

for s in sorular:
    print(s["id"], "|", s["soru"], "->", s["altin_cevap"])
