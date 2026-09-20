import time


def topla(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc += sayi
    return sonuc


def cikar(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc -= sayi
    return sonuc


def carp(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc *= sayi
    return sonuc


def bol(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        if sayi != 0:
            sonuc /= sayi
        else:
            print("Sıfıra bölme hatası!")
            return None
    return sonuc


def MODal(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        if sayi != 0:
            sonuc %= sayi
        else:
            print("Sıfıra mod alma hatası!")
            return None
    return sonuc


def USal(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc **= sayi
    return sonuc


def TAMBol(sayilar):
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        if sayi != 0:
            sonuc //= sayi
        else:
            print("Sıfıra bölme hatası!")
            return None
    return sonuc

def karekok(sayi):
    return sayi ** 0.5


Devam = True

while Devam:

    while True:
        islemler = input("Islem turunu seciniz = (+, -, *, /, **, //, %, karekok) " )
        if islemler in ("+", "-", "*", "/", "**", "//", "%", "karekok"):
            break
        else:
            print("Gecersiz islem turu, tekrar deneyiniz.")
            
    if islemler == "karekok":
            sayimiktar = 1
    else:
        while True:
            try:
                sayimiktar = int(input("Kac sayi gireceksiniz? "))
                if sayimiktar > 0:
                    break
                else:
                    print("Lütfen pozitif bir sayı giriniz.")
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz.")
    sayilar = []

    for i in range(sayimiktar):
        sayi = int(input(f"{i+1}. sayıyı giriniz: "))
        sayilar.append(sayi)

    if islemler == "+":
        print("Cevap =", topla(sayilar))

    elif islemler == "-":
        print("Cevap =", cikar(sayilar))

    elif islemler == "*":
        print("Cevap =", carp(sayilar))

    elif islemler == "/":
        print("Cevap =", bol(sayilar))

    elif islemler == "%":
        print("Cevap =", MODal(sayilar))

    elif islemler == "**":
        print("Cevap =", USal(sayilar))

    elif islemler == "//":
        print("Cevap =", TAMBol(sayilar))
        
    elif islemler == "karekok":
            print("Cevap = ", karekok(sayilar[0]))
            time.sleep(0.5)

    else:
        print("Geçersiz işlem seçtiniz!")

    time.sleep(1.5)

    durum = input("Devam etmek için 'e', çıkmak için 'q' giriniz: ").lower()

    if durum == "q":
        Devam = False

print("Program sonlandırıldı.")
