import os
import json
masaüstü = os.path.join(os.path.expanduser("~"), "Desktop")
proje_klasörü = os.path.join(masaüstü, "python projeler")
os.makedirs(proje_klasörü, exist_ok=True)
görevler_dosya_yolu = os.path.join(proje_klasörü, "görevler.json")
if not os.path.exists(görevler_dosya_yolu):
    with open("görevler.json", "w", encoding="utf-8") as dosya:
        json.dump([], dosya, ensure_ascii=False, indent=4)
def görev_ekle():
    görev = input("Yeni görev girin: ")
    yeni_görev = {
        "görev": görev,
        "tamamlandı": False
    }
    try:
        with open(görevler_dosya_yolu, "r", encoding="utf-8") as dosya:
            görevler = json.load(dosya)
        görevler.append(yeni_görev)
        with open(görevler_dosya_yolu, "w", encoding="utf-8") as dosya:
            json.dump(görevler, dosya, ensure_ascii=False, indent=4)
        print("Görev başarıyla eklendi.")
    except Exception as hata:
        print(f"Bir hata oluştu: {hata}")
def görevleri_listele():
    try:
        with open(görevler_dosya_yolu, "r", encoding="utf-8") as dosya:
            görevler = json.load(dosya)
        if not görevler:
            print("Henüz bir görev eklenmedi.")
        else:
            print("---Görevler Listesi---")
            for i, görev in enumerate(görevler, start=1):
                durum = "✅" if görev["tamamlandı"] else "❌"
                print(f"{i}. {görev['görev']} - {durum}")
    except Exception as hata:
        print(f"Beklenmeyen bi hata oluştu: {hata}")
def görev_tamamla():
    try:
        görev_seçilen = int(input("Tamamlamak istediğiniz görevi seçiniz: "))
        with open(görevler_dosya_yolu, "r", encoding="utf-8") as dosya:
            görevler = json.load(dosya)
        if not görevler:
            print("Tamamlayabileceğin görev bulunmuyor.")
        else:
            for i, görev in enumerate(görevler, start=1):
                if görev_seçilen == i:
                    görevler[görev_seçilen - 1]["tamamlandı"]=True
                    print("Görev Tamamlandı!")
            with open(görevler_dosya_yolu, "w", encoding="utf-8") as dosya:
                json.dump(görevler, dosya, ensure_ascii=False, indent=4)
    except Exception as hata:
        print(f"Beklenmeyen bi hata oluştu: {hata}")
def görev_silme():
    try:
        görev_seçilen = int(input("Silmek istediğiniz görevi seçiniz: "))
        with open(görevler_dosya_yolu, "r", encoding="utf-8") as dosya:
            görevler = json.load(dosya)
        for i, görev in enumerate(görevler, start=1):
            if görev_seçilen == i :
                del görevler[görev_seçilen-1]
        with open(görevler_dosya_yolu, "w", encoding="utf-8") as dosya:
            json.dump(görevler, dosya, ensure_ascii=False, indent= 4)
    except Exception as hata:
        print(f"Beklenmeyen bir hata oluştu: {hata}")
def menü_göster():
    print("---Görev Çizelgesi---")
    print("1.Görev Ekle")
    print("2.Görevleri Listele")
    print("3.Görev Tamamla")
    print("4.Görev Silme")
    print("5.Çıkış yap")
def çalıştır():
    while True:
        menü_göster()
        seçilen = input("Seçiminizi Yapınız(1,2,3,4,5): ")
        if seçilen == "1":
            görev_ekle()
        elif seçilen == "2":
            görevleri_listele()
        elif seçilen == "3":
            görev_tamamla()
        elif seçilen == "4":
            görev_silme()
        else:
            print("Çıkış yapılıyor...")
            break
çalıştır()
