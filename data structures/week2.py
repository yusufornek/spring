# -*- coding: utf-8 -*-

name = "elma"
if "e" in name:
    print("There is a e")
else:
    print("There is no e")
s1 = int(input("Enter the first number ="))
s2 = int(input("Enter the second number ="))
if s1 % s2 == 0:
    print("ok!")
else:
    print("hop!")

#########################################################
u1 = float(input("Give the first number please : "))
u2 = float(input("Give the Second number please : "))
u3 = float(input("Give the Third number please : "))


def ucgenmi(u1, u2, u3):
    if u1+u2 >= u3 and u2+u3 >= u1 and u3+u1 >= u2:
        return True
    else:
        return False


if ucgenmi(u1, u2, u3):
    print("Ücgen")
else:
    print("Degil")
#########################################################
a = int(input("First number please : "))
b = int(input("Second number please :"))
c = int(input("Third number please :"))

print("Checking your quadric equation ....................................................................................")


def checking(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        return ("Real and different")
    elif discriminant == 0:
        return ("Real and equal")
    else:
        return ("Complex and different")


print(checking(a, b, c))

########################################################
pilotNumber = int(input("Lütfen pilot numaranızı giriniz : "))
if pilotNumber == 152:
    if pilotNumber == 152:
        pilotName = "Yusuf Örnek"
        greetings = "Merhaba {}, Türk Hava Kuvvetleri uçuş bilgisayarına hoş geldiniz."
        print(greetings.format(pilotName))
    else:
        print("Seni tanımıyorum ama sorun yok!")
    pilotPrivateKey = "A4F5D59ff247Z3wR1"
    len(pilotPrivateKey)
    pilotPrivateKey.upper()
    pilotPrivateKey.find("F5", 0, len(pilotPrivateKey))
    pilotPrivateKey.rfind("ff", 0, len(pilotPrivateKey))
    pilotPrivateKey = pilotPrivateKey.replace("ff", "zz")
    feet = 1252
    knot = 400
    attitude = 7
    print("Güncel hızınız :", knot, "knot")
    print("Güncel yüksekliğiniz :", feet, "feet")
    print("Güncel durum cayronuz: ", attitude)

    print("""Dikkat:
          Şuan da Türk Hava Kuvvetleri Sahasında ilerlemektesiniz.
          200 mil Kuzey sonrası Uluslararası hava sahasını ifade eder.""")

else:
    print("\"Yetkisiz giriş!""")
    print("Bilgilerinizi hatırlamıyor musunuz? İşte uçuş kontrol bilgisayarına tanımlı görev bilgileriniz: ")
    ucusKodu = "Akinci1923"
    print("Uçuş Kodunuzun İlk harfi: ", ucusKodu[0])
    print("Uçuş Kodunuzun İkinci harfi: ", ucusKodu[1])
    print("Uçuş Kodunuzun Üçüncü harfi: ", ucusKodu[2])
    print("Uçuş Kodunuz : ", ucusKodu[0:])
    print("Ucus kodunuzun metin kısmı: ", ucusKodu[0:6])
    print("Ucus kodunuzun şifrelenmiş bir kısmı: ", ucusKodu[0::2])
