with open("Menu.txt", "r",encoding="utf-8") as f:
    menu = f.read()
    print(menu)

taban = input("Pizza tabanı seçiniz: ")

with open("Menu.txt", "a") as f:
    if taban == "1":
        f.write("\nSeçtiğiniz pizza tabanı: Klasik")
    elif taban == "2":
        f.write("\nSeçtiğiniz pizza tabanı: Margarita")
    elif taban == "3":
        f.write("\nSeçtiğiniz pizza tabanı: TürkPizza")
    elif taban == "4":
        f.write("\nSeçtiğiniz pizza tabanı: Sade Pizza")
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
        exit()

    f.write("\nLütfen bir sos seçiniz:")
    f.write("\n11: Zeytin")
    f.write("\n12: Mantarlar")
    f.write("\n13: Keçi Peyniri")
    f.write("\n14: Et")
    f.write("\n15: Soğan")
    f.write("\n16: Mısır")
    sos = input("Sos seçiniz: ")

    if sos == "11":
        f.write("\nSeçtiğiniz sos: Zeytin")
    elif sos == "12":
        f.write("\nSeçtiğiniz sos: Mantarlar")
    elif sos == "13":
        f.write("\nSeçtiğiniz sos: Keçi Peyniri")
    elif sos == "14":
        f.write("\nSeçtiğiniz sos: Et")
    elif sos == "15":
        f.write("\nSeçtiğiniz sos: Soğan")
    elif sos == "16":
        f.write("\nSeçtiğiniz sos: Mısır")
    else:
        f.write("\nSeçtiğiniz sos: Yok")

    f.write("\n* Teşekkür ederiz!")
    print("Siparişiniz kaydedildi. İyi günler!")
