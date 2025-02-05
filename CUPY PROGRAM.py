import numpy as cp #UBAH KE NUMPY IF NVIDIA
import time


for clear_screen in range (20):
    print("")
    
    
print ("📢⏳ SYSTEM - TURNING ON  ")
time.sleep(1)
print ("📢✅ SYSTEM - ONLINE ")
time.sleep(1)
print ("📢🛠  STATUS : 🔵🔵🔵")
time.sleep(1)
print ("📢💡 SYSTEM - INFORMATION")
time.sleep(1)

created_by = [
    "=--------------------------------------------------=",
    "|            PROGRAM CUPY N LOOP . PY              |",
    "|--------------------------------------------------|",
    "|   OSCAR VICTORIOUS PUTRA TAMBUNAN ( 51424063 )   |",
    "=--------------------------------------------------=",
    
    
]

for show_member in (created_by):
    print (show_member)

print ("")

time.sleep(1)
print ("📢💡 SYSTEM - INFORMATION SECTION")
time.sleep(1)

information_content_1 = [
    
    "=--------------------------------------------------=",
    "|                  BEFORE WE START                 |",
    "=--------------------------------------------------=",
    "|          PROGRAM SOLO - FOR TEST CUPY/NUMPY      |",
    "=--------------------------------------------------="

]

for show_information in (information_content_1):
    print (show_information)
    
time.sleep(1)

for clear_screen in range(99):
    print ()
time.sleep(1)


while True:
    print ("📢🔄 SYSTEM - LOOP SECTION",)
    time.sleep(1)
    print ("📢⏳ - WAIT FOR USER ACTION ")
    time.sleep(1)
    limit_loop_informaton_content = [
     
     
     "=---------------------------------------------------------=",
     "|                     !!! REMINDER !!!                    |",
     "=---------------------------------------------------------=",
     "|                                                         |",
     "|   BATAS MAKSIMAL LOOP YANG DI SARANKAN MAX SEBESAR 1000 |",
     "|        Peringatan: Loop mendekati batas maksimal        |",
     "|Pertimbangkan untuk menghentikan atau mengoptimalkan kode|",
     "|                                                         |",
     "=---------------------------------------------------------="
     
    ]
    
    for show_limit_loop in (limit_loop_informaton_content):
        print (show_limit_loop)
     
    
    time.sleep(1)
    
    try:
        for i in range (1) :
            print ("")
            
        n_for_loop = int(input("JUMLAH LOOP YANG DI INGINKAN :"))

        if n_for_loop < 0 :
            print ("📢EROR - VALUE CANT UNDER 0")
            print("📢SYSTEM - RETURN TO MAIN MENU")
            continue


    
        elif n_for_loop == 0 :
            
            print ("📢🔄 SYSTEM - RUNNING...")
            time.sleep (1)
            print ("📢🛑 SYSTEM - MATRIX PROGRAM HAS BEEN SKIPED")
            time.sleep (1)
        
            n_for_random_matrix_1 = 0
    
        elif n_for_loop <= 1000 :
            print ("📢🔄 SYSTEM - RUNNING...")
            time.sleep (1)
            print ("📢⏳ SYSTEM - WAIT TO USER INPUT")
            time.sleep (1)
            limit_loop_informaton_content = [
     
     
            "=---------------------------------------------------------=",
            "|                     !!! REMINDER !!!                    |",
            "=---------------------------------------------------------=",
            "|                                                         |",
            "|                   Peringatan: WARNING                   |",
            "|     SEMAKIN BESAR , USAGE RAM DAN GPU % SEMAKIN BESAR   |",
            "|                                                         |",
            "=---------------------------------------------------------="
            
            ]
            
            for show_limit_loop in (limit_loop_informaton_content):
                print (show_limit_loop)
            
            time.sleep (1)
            print ("📢🔄 PROGRAM - RUNNING...")
            time.sleep(1)
            print ("📢⏳ SYSTEM - WAIT TO USER TO CHOICE")
            time.sleep(1)
                
            n_for_random_matrix_1= int(input("INPUT SIZE RANDOM MATRIX LOAD : "))
            time.sleep (1)
            print ("📢🔄 PROGRAM - RUNNING...")
    
        else :
            
            print ("📢🔄 SYSTEM - RUNNING...")
            time.sleep(1)
            n_for_loop >1000 
            
            print ("📢🔄 SYSTEM - VALUE OVER LOAD")
            time.sleep(1)
            print ("📢❌ EROR - CANT GO OVER 1000")
            time.sleep(1)
            print ("📢⚠️  STATUS : 🟡🟡🟡")
            time.sleep(1)
            print ("📢⏳ SYSTEM - WAIT TO USER TO CHOICE")
            time.sleep(1)
            
            n_user_loop_reminder_info = [
            "=------------------------------------------------=",
            "|--1-- Melanjutkan Program (ADVANCE)             |",
            "|--2-- Tidak               (Exit Program)        |",
            "=------------------------------------------------="
            ]
            for show_n_user_loop_reminder_info in (n_user_loop_reminder_info):
             print (show_n_user_loop_reminder_info)

            user_choice_reminder = input ("MASUKKAN PILIHAN ANDA    :  ")
            if user_choice_reminder == "1" :
                print ("📢🔄 PROGRAM - RUNNING...")
                time.sleep(1)
                print ("📢⏳ SYSTEM - WAIT TO USER TO CHOICE")
                time.sleep(1)
                n_for_random_matrix_1 = int(input("INPUT SIZE RANDOM MATRIX LOAD    :"))

            elif user_choice_reminder == "2":
                
                for i in range (20):
                    print ("")
                print ("📢🔄 PROGRAM - SHUTDOWN")
                time.sleep (1)
                print ("📢🔄 PROGRAM - OFFLINE")
                time.sleep (1)
                print ("📢 🏁 THANKYOU FOR USING OUR SERVICE")
                
                break

            else :
                print ("Value Eror")
                print ("Program Di matikan")
                break

            

            
            
        
    except ValueError:
        
        for i in range (12):
            print ()
        
        for j in range (3):
            for i in range (3):
                time.sleep(0.1)
                print("⚠️ ⚠️ - INPUT HARUS BERUPA ANGKA - ⚠️ ⚠️ ")
            time.sleep(2)
            for i in range (13):
                time.sleep(0.2)
                print ("")
        continue
    

    
    
    
    for i in range (n_for_loop):

        
       
        
        random_matrix = cp.random.rand(1,n_for_random_matrix_1) 
        matriks_3A = cp.random.randint(1, 9999999999999999, (3, 3), dtype=cp.int64)
        matriks_3B = cp.random.randint(1, 9999999999999999, (3, 3), dtype=cp.int64)

        print ("---------------------------------------")
        print("Matriks 3A:")
        print(matriks_3A)

        print ("---------------------------------------")

        print("\nMatriks 3B:")
        print(matriks_3B)
        print ("---------------------------------------")

        # Operasi penjumlahan, pengurangan, dan perkalian matriks
        penambahan = cp.add(matriks_3A,matriks_3B)
        pengurangan = cp.subtract(matriks_3A,matriks_3B)
        perkalian = cp.matmul(matriks_3A, matriks_3B)
        pembagian = cp.divide(matriks_3A,matriks_3B)

        print ("---------------------------------------")
        print("\nHasil Penjumlahan:")
        print(penambahan)

        print ("---------------------------------------")

        print("\nHasil Pengurangan:")
        print(pengurangan)
        print ("---------------------------------------")

       
        print("\nHasil Perkalian:")
        print(perkalian)
        print ("---------------------------------------")

        print("\nHasil Perkalian:")
        print(pembagian)
        print ("---------------------------------------")

        print("\nrandom matrix :")
        print(random_matrix)
        print ("---------------------------------------")
        
    try :
        ini_opsi = [
        "=-------------------------------------=",
        "|-- 0 -- |Exit                        |",
        "|-- 1 -- |Re-Start                    |",
        "|-- 2 -- |Clear                       |",
        "=-------------------------------------=",
        ]
        for jenis_opsi in ini_opsi:
            print(jenis_opsi)

        user_choice = input("MASUKKAN PILIHAN ANDA   :")

        if user_choice == "0" :
            for i in range (15):
                print ("")
            print ("📢🔄 PROGRAM - SHUTDOWN")
            time.sleep (1)
            print ("📢🔄 PROGRAM - OFFLINE")
            time.sleep (1)
            print ("📢 🏁 THANKYOU FOR USING OUR SERVICE")
            
            break

        elif user_choice == "1" :
            print ( "📢 PROGRAM RE-START")
            

        elif user_choice == "2":
            print ("📢🔄 PROGRAM - RUNNING...")
            time.sleep (1)
            print ("📢🔄 PROGRAM - CLEAN SCREEN")
            time.sleep (1)
            print ("📢✅ PROGRAM - STATUS : DONE ")
            time.sleep (2)
            print ("📢⏳ PROGRAM - RETURN TO LOOP SECTION ")
            time.sleep (1)
            
            for i in range (99) :
                print ("")
                

        
        else:
            print ("MASUKKIN PILIHAN YANG BENER !!!!!!!!!!!!!!")
            for i in range (99) :
                print ()
            break
    
    except ValueError:
        print ("AH GA BENER")
        break
            
            
