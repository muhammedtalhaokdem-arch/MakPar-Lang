import datetime
with open("date.txt", "w", encoding="utf-8") as f:
    f.write(datetime.datetime.now().strftime("%Y"))
