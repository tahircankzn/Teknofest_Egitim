######################  PYTHON TEKRAR ######################
######################     NOTLARI    ######################
# @author: Tahir Can Kozan

#%%
###############################################################################
# VERİ TİPLERİ

tamSayi = 5  # int
ondalikliSayi = 5.0 # float
metin = "Poyraz" # str
liste = [1,2,"Poyraz",5.0]

boolean1 = True
boolean2 = False

dictionary = {
    "Ad" : "Tahir Can",
    "Soyad" : "Kozan",
    "Yaş" : "23",
    "Bölüm" : "Mekatronik Mühendisliği",
    "Sınıf" : "3"       
                } 

yaş = dictionary["Yaş"]

print(yaş)


tupleVeri = (1,2,3,3,4) # içerik değiştirilemez

liste = [1,2,5,6,8]

setVeri = {1,2,2,3,4,4,4,4,4} # {1, 2, 3, 4} , aynı terimler bir defa gösterilir


complex = 1j 
		

print(type(tamSayi)) 

#%%
###############################################################################
# String

text1 = "Poyraz"
text2 = "Ve"
text3 = "Karayel"

print(text1 , text2, text3) # Poyraz Ve Karayel
print(text1 + text2 + text3) # PoyrazVeKarayel

print("{}{}{}".format(text1 , text2, text3 )) # PoyrazVeKarayel
print("{} {} {}".format(text1 , text2, text3 )) # Poyraz Ve Karayel

print("{0}{1}{2}".format(text1 , text2, text3 )) # PoyrazVeKarayel
print("{2}{1}{0}".format(text1 , text2, text3 )) # 

print(f"{text1}{text2}{text3}") # PoyrazVeKarayel
print(f"{text1} {text2} {text3}") # Poyraz Ve Karayel

string1 = " tahir can kozan "

# t a h i r   c a n   k  o  z  a  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
#            ...         -4 -3 -2 -1
                                  
print(string1[0:3:1]) # tah  , 0. dan 2. index e kadar

print(string1[:3]) # tah   ,0. dan 2. index e kadar

print(string1[2:]) # hir can kozan   ,2. index den sonuna kadar kadar

print(string1[0:3:2]) # th   ,0. dan 2. index e kadar 2 şer adımlarla ilerler

print(string1[-1]) # n    , son karakter

print(string1[-2:-5:-1]) # -2 -3 -4 değerler yazılır

print(string1[-2:]) # boş çıkar çünkü -2 den başlayınca otomatik
                      # soldan sağ gider ama -5 -2nin solunda


# [-3:] dersek
#  t  a  h  i   r      yön belirmedikce soldan sağa gider
# -5 -4 -3 -2  -1
#        |------->   sona geldik bitti , yön belirmedikce soldan sağa gider
#                    bu yüzden boş çıktı verir

# [-3:-4:-1] dersek
#  t  a  h  i   r   
# -5 -4 -3 -2  -1      h çıktısı verir 
#     <--|       



print(string1.upper()) # TAHIR CAN KOZAN
print(string1.lower()) # tahir can kozan

print(string1.strip()) # baştaki ve sondaki boşlukları siler varsa

print(string1.replace("h", "H")) # h karakterini çıkardı H karakterini koydu
                                 # değiştirdi

print(string1.split("a")) # ['t', 'hir c', 'n koz', 'n']   , a harfleri çıkarılır ve ayrılır

items1 = string1.split("a")   # ['t', 'hir c', 'n koz', 'n']
print(items1[1])  # "hir c"       0       1        2     3

text1 = "Tahir"
text2 = "Can"
text3 = "Kozan"

print(len(string1.split("a"))) 


#%%
###############################################################################
# Liste

liste = ["tahir","can","kozan"]
liste2 = [22,23,24]

liste.extend(liste2)
print(liste)    # ['tahir', 'can', 'kozan', 22, 23, 24]

liste = ["tahir","can","kozan"]
liste.remove("can") # "can" nı siler ["tahir","kozan"]

liste = ["tahir","can","kozan"]
liste.pop(1) # 1. indeksi siler
liste.pop() # sondakini siler ["tahir","kozan"]

liste = ["tahir","can","kozan"]
del liste[0] # 0. indeksi siler
del liste # kompile siler

liste = ["tahir","can","kozan"]
liste.clear() # liste içini siler []

liste = ["tahir","can","kozan"]
liste.append("22") # listenin sonuna ekleme yapar  ["tahir","can","kozan","22"]
print(liste) 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []


liste7 = ["banana","apple" , "cherry", "kiwi", "mango"]
liste5 = [1,5,2]
liste5.sort()
print(liste5)


#%%
###############################################################################
# Dictionary

library = {
    "Ad" : "Tahir Can",
    "Soyad" : "Kozan",
    "Yaş" : 23,
    "Bölüm" : "Mekatronik Mühendisliği",
    "Sınıf" : 3       
                } 

print(library.keys())

print(library.values())


print(library["Ad"])

print(library["Yaş"]) # 23

library["Yaş"] = 25

print(library["Yaş"]) # 25

library.pop("Yaş")

try:
    print(library["Yaş"])
except KeyError:

    pass

library["Yaş"] = 25

print(library["Yaş"])

# %%
###############################################################################
# Veri dönüşmleri

veri1 = "10"
veri2 = "12"

print(type(veri1)) # str
veri3 = int(veri1)
print(type(veri3)) # int

print(veri1 + veri2)

print(int(veri1) + int(veri2))

veri3 = "10.0"
print(int(veri3)) # ilk önce float sonra integer veri tipine çevirmeliyiz
print(int(float(veri3)))


# %%
###############################################################################
# Matematik işlemleri

sayi1 = 34
sayi2 = 2

# Toplama
toplam = sayi1 + sayi2

# Çıkarma
fark = sayi1 - sayi2

# Bölme
bölüm = sayi1 / sayi2

# Bölümün tam kısmı
bölümünTamKısmı = sayi1 // sayi2 

# Kalan
kalan = sayi1 % sayi2

veri = 10 % 2 # 0

veri2 = 3*3

# Üst alma
kare = 3**2

# %%
###############################################################################
# Kullanıcıdan veri alma

sayi1 = float(input("Bir sayı giriniz")) 
sayi2 = float(input("Bir sayı giriniz")) 

print(sayi1 + sayi2)


# %%
###############################################################################
# Karar yapıları

pi = 2

if pi < 3:
    print("sayı 3 den küçük")

elif pi > 3:
    print("sayı 3 den büyük")

else:
    print("sayı 3")

# alan hesaplayan kod kare ve üçgen


# %%
###############################################################################
# Döngüler

# For döngüsü


for sayı in range(1,5,2): 
    print(sayı)


#%%

veri = int(input("Bir sayı giriniz > "))
sonuc = 1
for sayı in range(1,veri+1): # 1 2 3 4 5
    sonuc = sonuc * sayı 

print(sonuc)

#%%

sayı = 1


while True:
    sayı +=1

    if sayı < 5:
        print("5 den küçük")
    elif sayı == 5:
        print("sayı 5")
    elif sayı > 5:
        break

print("döngü bitti")
    


# %%
###############################################################################
# Fonksiyonlar


print("ax**2 + bx + c 2 bilinmeyenli denklemin köklerinin bulunması")

a = float(input("a sayısını giriniz > "))
b = float(input("b sayısını giriniz > "))
c = float(input("c sayısını giriniz > "))

delta = b**2 - 4*a*c
kök1 = (-b + delta**(1/2)) / (2*a)
kök2 = (-b - delta**(1/2)) / (2*a)

print(f"1. Kök : {kök1}\n2. Kök : {kök2}")


# %%

def kök_bul(a,b,c):
    delta = b**2 - 4*a*c
    kök1 = (-b + delta**(1/2)) / (2*a)
    kök2 = (-b - delta**(1/2)) / (2*a)

    return kök1 , kök2



a1 = float(input("a sayısını giriniz > "))
b1 = float(input("b sayısını giriniz > "))
c1 = float(input("c sayısını giriniz > "))

kök1 , kök2 = kök_bul(a1,b1,c1)
print(f"1. Kök : {kök1}\n2. Kök : {kök2}")


# %%

students = {  
    
    "Tahir" : {"vize" : 0 , 
               "final" : 0,
               "ortalama": 0},

    "Alperen" : {"vize" : 0 , 
               "final" : 0,
               "ortalama": 0},
    }


print(students["Tahir"])
    

# %%
