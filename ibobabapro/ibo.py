a=int(input("gir"))
b=int(input("gir"))
c=int(input("gir"))
print(a+b)
print((a+b)/2)
print((a+b+c)/3)
vize=int(input("vizeyi gir"))
final=int(input("final"))
print((vize+final)/2)


ort=int(input("ortalamayı gir"))
if(ort<50):
    print("kaldı")
else:
    print( "gecti")
if(a%2==0):
    print("cift")
else:
    print("tek")
if(a<0):
    print("negatif")
elif(a>0):
        print("positif")
else:
    print("0")
boy=float(input("boyunu gir"))
kilo=int(input("kilonu gir"))
print(kilo/(boy*boy))

yaş=int(input("yaşını gir"))
if(yaş<18):
     print("ehliyet alamassın")
else:
     print("al")
for sayilar in range(100):
    print(sayilar)
    
for sayi in range(100):
    if(sayi%2==0):
          print(sayi)
    elif(sayi%3==0 & sayi%5==0):
          print("3e ve 5e tam bölunuyor")  
    else:
          print(sayi)
     

sa=int(input("sayi gir"))
for s in range(sa):
     print(sa)

kenar1=int(input("kenarı gir"))
kenar2=int(input("kenarı gir"))

print(kenar1*kenar2)
print(2*(kenar1+kenar2))

metin=str(input("kelime gir"))
for harfler in metin:
    print(harfler)

say1=int(input("sayi gir"))
say2=int(input("sayi gir"))
tplm=0
for a in range(say1,say2):
     tplm+=a
print(tplm)

tercih = input("Sinema mı  tiyatro mu  ")

ogrenci = input("Öğrenci misin")


if tercih == "sinema":
    fiyat = 15
elif tercih == "tiyatro":
    fiyat = 10


if ogrenci == "evet":
    indirimli_fiyat = fiyat * 0.5
    print(indirimli_fiyat)
elif ogrenci == "hayır":
    print(fiyat)

for asa in range (2,a):
     if(a%asa==0):
          print("asal değil")
          break
     else: 
        print("asal")
        break

#22
çiftsayilar = 0
teksayilar = 0
sayi = int(input("Sayıyı girin : "))
for i in range(sayi):
    if (i%2==0):
        çiftsayilar+=i

    elif(i%2==1):
        teksayilar+=i
print("çift sayıların toplamı = " , çiftsayilar)
print("tek sayıların toplamı = " , teksayilar)

# --- MAAŞA ZAM ÖRNEĞİ ---
maas = float(input(" Maaşınızı girin  : "))
zam = float(input(" Zam oranını girin (%)  : "))
yenimaas = maas + (maas * zam/100)
print("yeni maaşınız = ",yenimaas)


# --- FONKSİYON ÖRNEK ---
def fonksiyon():
    kisak = int(input(" Kısa kenarı giriniz : "))
    uzuk = int(input(" Uzun kenarı giriniz : "))    
    print(kisak*uzuk)

fonksiyon()
# --- KARAKTER BULMA ---





def dairealan():
    r = int(input(" Yarıçapı giriniz : "))
    alan = 3*r**2
    print(alan)
dairealan()

# --- SAYI TAHMİN OYUNU ---
hak = 3
c = random.randint(1,100)
print(c)
while hak > 0:
    t = int(input("Tahmin girin : "))
    if(t == c):
        print("Tebrikler Kazandınız ")
        break
    elif(t < c):
        print("Daha büyük bir sayı girin")
        hak-=1
    elif(t > c):
        print("Daha küçük bir sayı girin")
        hak-=1

if(hak == 0):
    print("Kaybettiniz")

#27#
from datetime import datetime


tarih_str = input("Tarihi gir ")



tarih = datetime.strptime(tarih_str, "%d-%m-%Y")
    
gun_numarasi = tarih.timetuple().tm_yday
print(f"{tarih_str} tarihi yılın {gun_numarasi}. günü.")


#28#

sayilar = [10, 15, 23, 30, 41, 50, 5, 22, 100, 33]

beşin_katlari = [sayi for sayi in sayilar if sayi % 5 == 0]

print("5'in katı olan sayılar:", beşin_katlari)

#29#
def karakter_var_mi(metin, karakter):

    if karakter in metin:
        return True 
    else:
        return False 
metin = "Merhaba, dünya!" 
karakter = "d"  
if karakter_var_mi(metin, karakter):
    print(f"'{karakter}' karakteri metin içinde bulunmaktadır.")
else:
    print(f"'{karakter}' karakteri metin içinde bulunmamaktadır.")

#30#
def cift_mi(sayi):
    
    return sayi % 2 == 0


sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

toplam = 0
sayi_adedi = 0


for sayi in range(sayi1,sayi2):
    if cift_mi(sayi):
        toplam += sayi
        sayi_adedi += 1



ortalama = toplam / sayi_adedi
print(ortalama)

#31#
def dikdortgen_alani(genislik, yukseklik):
    
    return genislik * yukseklik


genislik = int(input("genişliğini "))
yukseklik = int(input(" yüksekliğini "))


alan = dikdortgen_alani(genislik, yukseklik)

#32#

gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]

indeks = int(input("0-4 arası sayı gir"))

#33#


sayilar = list(range(10, 21))

sayilar2 = [21, 22, 23, 24, 25]

birlesik_liste = sayilar + sayilar2


bolunenler = [sayi for sayi in birlesik_liste if sayi % 4 == 0]


print("4'e tam bölünen sayılar:", bolunenler)


#34#


    # --- KULLANICININ GİRDİĞİ SAYILARI TOPLAMA ---
sayi = str(input("sayı giriniz : "))
toplam = 0
for i in sayi:
    toplam += int(i) 
print(toplam)

#35#

toplam = 0


while True:
    sayi = float(input(" sayı gir "))
    
    if sayi == 0:
        break  
    
    toplam += sayi 


print(toplam)



        




