import datetime
import os

veri_klasoru = r"C:\MakPar\Library-Data"
if not os.path.exists(veri_klasoru):
    os.makedirs(veri_klasoru) # Klasor yoksa otomatik olustur

dosya = os.path.join(veri_klasoru, "date_full.txt")
if not os.path.exists(dosya):
    open(dosya, "w").close() # Dosya yoksa otomatik olustur
    
with open(dosya, "w", encoding="utf-8") as f:
    f.write(datetime.datetime.now().strftime("%d.%m.%Y"))
