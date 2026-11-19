import os, codecs
veri_yolu = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Library-Data", "string_data.txt")

with codecs.open(veri_yolu, 'r', 'utf-8') as f:
    metin = f.read().strip()

with codecs.open(veri_yolu, 'w', 'utf-8') as f:
    f.write(metin.lower())