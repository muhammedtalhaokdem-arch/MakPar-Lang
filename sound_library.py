import winsound
import os

# 1. Klasör yollarını bul
kutuphane_klasoru = os.path.dirname(os.path.abspath(__file__))
ana_klasor = os.path.dirname(kutuphane_klasoru)
veri_klasoru = os.path.join(ana_klasor, "Library-Data")

# Library-Data yoksa oluştur (güvenlik)
if not os.path.exists(veri_klasoru):
    os.makedirs(veri_klasoru)

# 2. Okunacak dosyanın tam yolu
bip_yolu = os.path.join(veri_klasoru, "bip.txt")

try:
    # 3. MakPar'ın bıraktığı bip değerini oku
    with open(bip_yolu, "r", encoding="utf-8") as f:
        deger = int(f.read().strip())
        
    frekans = 1500 # Sesin inceliği (1500 Hz standart uyarı sesidir)

    # 4. Değere göre sesi tetikle
    if deger == 0:
        # 0 ise kısa bir uyarı sesi (500 milisaniye / yarım saniye)
        winsound.Beep(frekans, 500)
    elif deger > 0:
        # 0'dan büyükse, o sayı kadar SANİYE boyunca uzun bip ("biiiiipleme")
        # winsound.Beep milisaniye kabul ettiği için sayıyı 1000 ile çarpıyoruz
        sure_milisaniye = deger * 1000
        winsound.Beep(frekans, sure_milisaniye)
        
except Exception:
    # Dosya yoksa veya içine sayı yerine harf yazılmışsa motoru çökertmemek için sessizce kapan
    pass