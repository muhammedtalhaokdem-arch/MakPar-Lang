import datetime
import os

kutuphane_klasoru = os.path.dirname(os.path.abspath(__file__))
ana_klasor = os.path.dirname(kutuphane_klasoru)
veri_klasoru = os.path.join(ana_klasor, "Library-Data")

if not os.path.exists(veri_klasoru):
    os.makedirs(veri_klasoru)

sonuc_yolu = os.path.join(veri_klasoru, "date_year.txt")

try:
    yil = datetime.datetime.now().strftime("%Y")
    with open(sonuc_yolu, "w", encoding="utf-8") as f:
        f.write(yil)
except Exception as e:
    with open(sonuc_yolu, "w", encoding="utf-8") as f:
        f.write("HATA")
