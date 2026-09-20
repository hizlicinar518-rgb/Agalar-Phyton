ogrenci = {
    "Isim": "",
    "Yas": 0,
    "Sinif": 0,
}

ogrenci["Isim"] = input("Ogrenci adini giriniz = ")
ogrenci["Yas"] = int(input("Ogrenci Yasini giriniz = "))
ogrenci["Sinif"] = int(input("Ogrencinin kacinci Sinif oldugunu giriniz = "))


def Mat():
    mat = {}

    mat["Birinci Sinav Notu"] = int(input("Birinci Sinav Notu = "))
    mat["Ikinci Sinav Notu"] = int(input("Ikinci Sinav Notu = "))
    mat["Sozlu Notu"] = int(input("Sozlu Notu = "))

    return mat


def Turk():
    turk = {}

    turk["Birinci Sinav Notu"] = int(input("Birinci Sinav Notu = "))
    turk["Ikinci Sinav Notu"] = int(input("Ikinci Sinav Notu = "))
    turk["Sozlu Notu"] = int(input("Sozlu Notu = "))

    return turk


def Fen():
    fen = {}

    fen["Birinci Sinav Notu"] = int(input("Birinci Sinav Notu = "))
    fen["Ikinci Sinav Notu"] = int(input("Ikinci Sinav Notu = "))
    fen["Sozlu Notu"] = int(input("Sozlu Notu = "))

    return fen


def Ing():
    ing = {}

    ing["Birinci Sinav Notu"] = int(input("Birinci Sinav Notu = "))
    ing["Ikinci Sinav Notu"] = int(input("Ikinci Sinav Notu = "))
    ing["Sozlu Notu"] = int(input("Sozlu Notu = "))

    return ing


def ort():
    secim = input(
        "Hangi dersin ortalamasini hesaplamak istiyorsunuz? = (MatO, TurkO, FenO, IngO, OrtO) "
    )

    if secim == "MatO":
        mat = Mat()
        print("Birinci Matematik Sinav Notu", mat["Birinci Sinav Notu"])
        print("Ikinci Matematik Sinav Notu",mat["Ikinci Sinav Notu"])
        print("Matematik Sozlu Notu", mat["Sozlu Notu"])

        Mat_ort = (
            (mat["Birinci Sinav Notu"] * 2)
            + (mat["Ikinci Sinav Notu"] * 2)
            + mat["Sozlu Notu"]
        ) / 5

        print(ogrenci["Isim"], ogrenci["Sinif"], ". Sinif Matematikten", " Ortalama", Mat_ort, "aldi")

    elif secim == "TurkO":
        turk = Turk()
        print("Birinci Turkce Sinav Notu",turk["Birinci Sinav Notu"])
        print("Ikinci Turkce Sinav Notu", turk["Ikinci Sinav Notu"])
        print("Turkce Sozlu Notu", turk["Sozlu Notu"])

        Turk_ort = (
            (turk["Birinci Sinav Notu"] * 2)
            + (turk["Ikinci Sinav Notu"] * 2)
            + turk["Sozlu Notu"]
        ) / 5

        print(ogrenci["Isim"], ogrenci["Sinif"], ". Sinif Turkceden", " Ortalama", Turk_ort, "aldi")

    elif secim == "FenO":
        fen = Fen()
        print("Birinci Fen Sinav Notu", fen["Birinci Sinav Notu"])
        print("Ikinci Fen Sinav Notu", fen["Ikinci Sinav Notu"])
        print("Fen Sozlu Notu", fen["Sozlu Notu"])

        Fen_ort = (
            (fen["Birinci Sinav Notu"] * 2)
            + (fen["Ikinci Sinav Notu"] * 2)
            + fen["Sozlu Notu"]
        ) / 5

        print(ogrenci["Isim"], ogrenci["Sinif"], ". Sinif Fenden", " Ortalama", Fen_ort, "aldi")

    elif secim == "IngO":
        ing = Ing()
        print("Birinci Ingilizce Sinav Notu", ing["Birinci Sinav Notu"])
        print("Ikinci Ingilizce Sinav Notu", ing["Ikinci Sinav Notu"])
        print("Ingilizce Sozlu Notu", ing["Sozlu Notu"])

        Ing_ort = (
            (ing["Birinci Sinav Notu"] * 2)
            + (ing["Ikinci Sinav Notu"] * 2)
            + ing["Sozlu Notu"]
        ) / 5

        print(ogrenci["Isim"],ogrenci["Sinif"],". Sinif Ingilizceden", " Ortalama", Ing_ort, "aldi")

    elif secim == "OrtO":
        mat1 = Mat()
        turk1 = Turk()
        fen1 = Fen()
        ing1 = Ing()

        mat_notu = ((mat1["Birinci Sinav Notu"] * 2) + (mat1["Ikinci Sinav Notu"] * 2) + mat1["Sozlu Notu"]) / 5
        turk_notu = ((turk1["Birinci Sinav Notu"] * 2) + (turk1["Ikinci Sinav Notu"] * 2) + turk1["Sozlu Notu"]) / 5
        fen_notu = ((fen1["Birinci Sinav Notu"] * 2) + (fen1["Ikinci Sinav Notu"] * 2) + fen1["Sozlu Notu"]) / 5
        ing_notu = ((ing1["Birinci Sinav Notu"] * 2) + (ing1["Ikinci Sinav Notu"] * 2) + ing1["Sozlu Notu"]) / 5

        ortalama = (mat_notu + turk_notu + fen_notu + ing_notu) / 4

        print(ogrenci["Isim"], ogrenci["Sinif"], ". Sinif Genel Ortalamasi olarak", ortalama , "aldi")

    else:
        print("Gecersiz secim!")

ort()
