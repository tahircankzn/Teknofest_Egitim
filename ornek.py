students = {  
    
    "Tahir" : {"vize" : 50 , 
               "final" : 30,
               "ortalama": 10},

    "Alperen" : {"vize" : 20 , 
               "final" : 10,
               "ortalama": 80},
    }


print(students.keys())

girdi = input("Bilgi almak istediğiniz öğrencinin adını giriniz > ")

sınav_bilgisi = int(input("Vize notu için > 1 \n final için > 2 \n ortalama için > 3 "))

if sınav_bilgisi == 1:
    print(students[girdi]["vize"])

elif sınav_bilgisi == 2:
    print(students[girdi]["final"])

elif sınav_bilgisi == 3:
    print(students[girdi]["ortalama"])
    