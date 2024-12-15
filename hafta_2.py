
# Bir sayının asal olup olmadığının bulunması

"""sayi = int(input("bir sayı giriniz : "))

asalmı = None
for i in range(2,sayi):
    if sayi%i == 0:
        print("asal değil")
        asalmı = False
        break
        
if asalmı != False:
    print("asal")"""
    
# Bir sayının kare kökünün alınması - math.sqrt()


# Kare prizma kütlesinin hesaplanması - gram - cm3


def Kutle(a,yoğunluk):
    hacim = a**3

    return yoğunluk * hacim

a = int(input("bir sayı giriniz : "))
yoğunluk = int(input("yoğunluk : "))


kütle = Kutle(a,yoğunluk)


print(kütle)






