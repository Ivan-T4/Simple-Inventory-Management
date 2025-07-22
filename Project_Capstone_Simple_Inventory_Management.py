
##Inventory awal ada 5 produk

inventory = {
    "CHAB2503ZIS": {
        "Nama": "CHAIN",
        "Client": "ABCDEF",
        "Tanggal": "25032025",
        "Grade": "B",
        "Stock" : 30,
        "Dimensi": {
             "Lebar": 25,
             "Panjang": 34,
             "Tinggi": 70
        }
    },
    "CHXY2503OXH": {
        "Nama": "CHAIN",
        "Client": "XYZDEF",
        "Tanggal": "25032025",
        "Grade": "A",
        "Stock" : 40,
        "Dimensi": {
             "Lebar": 40,
             "Panjang": 49,
             "Tinggi": 85
        }
    },
    "CH122503DMW": {
        "Nama": "CHAIN",
        "Client": "123DEF",
        "Tanggal": "25032025",
        "Grade": "A",
        "Stock" : 50,
        "Dimensi": {
             "Lebar": 55,
             "Panjang": 64,
             "Tinggi": 100
        }
    },
    "SPAB2503UDT": {
        "Nama": "SPROCKET",
        "Client": "ABCDEF",
        "Tanggal": "25032025",
        "Grade": "B",
        "Stock": 20,
        "Dimensi": {
            "Lebar": 20,
            "Panjang": 29,
            "Tinggi": 45
        }
    },
    "PLXY2603KTD": {
        "Nama": "PLATE",
        "Client": "XYZDEF",
        "Tanggal": "26032025",
        "Grade": "B",
        "Stock": 10,
        "Dimensi": {
            "Lebar": 10,
            "Panjang": 19,
            "Tinggi": 55
        }
    }
        
}

takeout = {}

search_options = {
    1: "Unique_ID",
    2: "Nama",
    3: "Client",
    4: "Tanggal",
    5: "Grade"
}
edit_options = {
    1: "Nama",
    2: "Client",
    3: "Tanggal",
    4: "Grade"
}

def show_product_details_by_id(product_id):
    #product_id = input("Masukkan Unique_ID produk yang ingin dilihat: ").upper()

    if product_id in inventory:
        detail = inventory[product_id]
        nama = detail.get("Nama", "N/A")
        client = detail.get("Client", "N/A")
        tanggal = detail.get("Tanggal", "N/A")
        grade = detail.get("Grade", "N/A")
        stock = detail.get("Stock", "N/A")

        dim = detail.get("Dimensi", {})
        lebar = dim.get("Lebar", "N/A")
        panjang = dim.get("Panjang", "N/A")
        tinggi = dim.get("Tinggi", "N/A")

        print(f"""
Detail Produk:
Unique_ID = {product_id}
Nama Produk = {nama}
Client = {client}
Tanggal masuk = {tanggal}
Grade Produk = {grade} dengan lebar {lebar} cm, panjang {panjang} cm, dan tinggi {tinggi} cm
Jumlah Produk = {stock}
""")
    else:
        print("Produk dengan Unique_ID tersebut tidak ditemukan.")



def print_product(id, details): #belum di check
    print(f"{id:<15} | {details.get('Nama', 'N/A'):<15} | {details.get('Client', 'N/A'):<15} | {details.get('Tanggal', 'N/A'):<15} | {details.get('Grade', 'N/A'):<15} | {details.get('Stock', 'N/A'):<15}")

def search_inventory2():
    print("""
Mencari Produk berdasarkan:
1. Unique_ID
2. Nama Produk
3. Client
4. Tanggal
5. Grade(Ukuran)
6. Exit
    """)
    searchdata = int(input(f'Masukkan pilihan anda: '))

    if searchdata == 6:
        print("Kembali ke menu utama")
        return
    
    #other than 1-6
    field = search_options.get(searchdata)
    if not field:
        print("pilihan tidak ada")
        return #Not good using continue because nothing can be redo because it was search engine
    
    #if it was 1-5
    key = input(f'Masukkan {field} dari produk tersebut:').strip().upper()

    found = False  ###Ini penting biar print yang dibawahnya ke looping di for loops
    print(f"{'ID':<15} | {'Nama':<15} | {'Client':<15} | {'Tanggal':<15} | {'Grade':<15} | {'Stock':<15}")

    #forloops searching
    for id, details in inventory.items():

        #if unique_id yang dipilih
        if searchdata == 1:
            if key.upper() == id.upper():
                print_product(id, details)
                found = True
        
        else:
            if details.get(field, '') == key.upper():
                print_product(id, details) 
                found = True

    if not found: #dan perlu diginiin
        print("Tidak ada nama barang yang sesuai")
        return search_notfound()
    
    return True #if found something

def search_notfound():
    percabangan = input(f'apakah anda mau ditampilkan semua inventory?(y/n) ').lower()
    if percabangan == 'y':
        show_all_inventory()
        return True
    else:
        carilagi = input(f'apakah anda mau mencari lagi?(y/n) ').lower()
        if carilagi == 'y':
            search_inventory2()
            return True
        else:
            return False #Gaveup
        
def show_all_inventory():
    print(f"{'ID':<15} | {'Nama':<15} | {'Client':<15} | {'Tanggal':<15} | {'Grade':<15} | {'Stock':<15}")
    for id, details in inventory.items():
        print(f"{id:<15} | {details['Nama']:<15} | {details['Client']:<15} | {details['Tanggal']:<15} | {details['Grade']:<15} | {details['Stock']:<15}")        

def takeoutcart():
    print(f"{'ID':<15} | {'Nama':<15} | {'Client':<15} | {'Tanggal':<15} | {'Grade':<15} | {'Stock':<15}")
    for id, details in takeout.items():
        print(f"{id:<15} | {details['Nama']:<15} | {details['Client']:<15} | {details['Tanggal']:<15} | {details['Grade']:<15} | {details['Stock']:<15}")        

def inventory_display(): #Menu 1
    print("""
Inventory Display:
1. Mencari spesifik barang
2. Melihat semua barang
        """)
    showdata = int(input(f'Masukkan pilihan anda: '))
    if showdata == 1:
        search_inventory2()
    else:
        #if they choose to show all inventory
        show_all_inventory()
        

def main_menu():
    print("""
Main Menu:
1.Menampilkan Daftar Inventory
2.Memasukan Produk 
3.Mengedit Data Produk
4.Menghapus Data Produk
5.Mengeluarkan Produk
6.Exit  
                """)
    print("\n")


def inventory_in(): #Menu 2

    while True:
        menuadd = int(input(f"""
Menu:
1. Add Product
2. Exit
masukkan angka untuk melanjutkan: """))
        if menuadd == 1:

            print("Isi detail produk yang ingin dimasukkkan: ")

            Nama = input("Masukan Nama Produk: ").upper() #Nama Produk
            Client = input("Masukkan Nama Client untuk Produk ini: ").upper() #Nama Client
            Tanggal = (input("Masukkkan Tanggal masuk Produk ke Gudang (cth: 25032025): ")) 
            Lebar = int(input("Masukkan lebar Produk(cm):"))
            Panjang = int(input("Masukkan panjang Produk(cm):"))
            Tinggi = int(input("Masukkan tinggi Produk(cm):"))
            volume = Lebar*Panjang*Tinggi
            if volume >= 60000:
                Grade = 'A' #Grade Produk
            elif 10000 <= volume <60000:
                Grade = 'B'
            elif volume < 10000:
                Grade = 'C'

            Stock = int(input("Masukkan jumlah yang ingin dimasukkan: "))
            ID = Nama[:2]+Client[:2]+str(Tanggal)[:4]+chr(65 + (Lebar % 26))+chr(65 + (Panjang % 26))+chr(65 + (Tinggi % 26)) #Unique_ID
    
            #checking details product
            benartidak = input(f"""
Detail Produk:
Unique_ID = {ID}
Nama Produk = {Nama}
Client = {Client}
Tanggal masuk = {Tanggal}
Grade Produk = {Grade} dengan lebar {Lebar} cm, panjang {Panjang} cm, dan tinggi {Tinggi} cm
Jumlah Produk = {Stock}
Apakah detail produk sudah betul?(y/t):""").lower()
    
            if benartidak == 't':
                return False #redo ##need check

            else:
                if ID in inventory: #if the ID already exists
                    details = inventory[ID]
                    dim = details.get("Dimensi", {})
                 
                    if  details["Client"] == Client and details["Tanggal"] == Tanggal and details["Nama"] == Nama and details["Grade"] == Grade and dim.get("Lebar") == Lebar and dim.get("Panjang") == Panjang and dim.get("Tinggi") == Tinggi:
                        inventory[ID]["Stock"] += Stock  # Add more of the same detail product
                        print(f"Stok {Nama} ditambahkan sebanyak {Stock}.")
                        return True
                    else:
                         print("Proses pemasukan produk gagal. Unique ID ini sudah ada, tapi detail berbeda. mohon masukkan produk 1 hari setelahnya.")
                         return False
                
                else:
                    #if the ID is new
                    inventory[ID] = {"Nama": Nama, "Client": Client, "Tanggal": Tanggal, "Grade": Grade, "Stock": Stock, "Dimensi": {"Lebar": Lebar, "Panjang": Panjang, "Tinggi": Tinggi}}
                    print(f"Produk {Nama} berhasil ditambahkan.")
                    return True
        
        elif menuadd == 2:
            print("Kembali ke menu sebelumnya.")
            return False

        else:
            print("pilihan tidak valid.")
            return False


def inventory_out(): #Menu 5
    while True:
        menutakeout = int(input(f"""
Menu:
1. Takeout Product
2. Exit
masukkan angka untuk melanjutkan: """))
        if menutakeout == 1:

            found = search_inventory2() #kalo ketemu return True dan dia bisa edit

            if not found: #if search_inventory2 return False ini dari search_notfound() usernya gaveup
                print("Tidak ada produk yang ditemukan untuk diedit.")
                return False

            takeoutbyID = input(f""" Masukkan Unique_ID yang diinginkan untuk di edit: """).upper()
            if takeoutbyID.upper() in inventory:
                show_product_details_by_id(takeoutbyID)
                benartidak = input("Apakah detail produk sudah betul? (y/t): ").lower()
                if benartidak == 't':
                    print("Proses pengeluaran dibatalkan.")
                    return False
                 
                while True:
                    jumlahtakout = int(input(f'Berapa Jumlah yang ingin diambil: '))
                    if jumlahtakout > inventory[takeoutbyID]["Stock"]:
                        print(f"Stok tidak cukup, stock produk dengan Unique_ID {takeoutbyID} tersisa: {inventory[takeoutbyID]["Stock"]}")
                        return False
                    else:
                        break
                
                #checkout in takeoutcart
                if takeoutbyID in takeout:
                    takeout[takeoutbyID]["Stock"] += jumlahtakout  # Add more of the same product
                    ##ini perlu di print
                    print(f'Barang yang diambil:')
                    print(f"{'ID':<15} | {'Nama':<15} | {'Client':<15} | {'Tanggal':<15} | {'Grade':<15} | {'Stock':<15}")
                    for id, details in takeout.items():
                        print_product(id, details)
                else:
                    takeout[takeoutbyID] = {"Nama" : inventory[takeoutbyID]["Nama"], "Client" : inventory[takeoutbyID]["Client"], "Tanggal" : inventory[takeoutbyID]["Tanggal"], "Grade" : inventory[takeoutbyID]["Grade"], "Stock": jumlahtakout}
                    print(f'Barang yang diambil:')
                    print(f"{'ID':<15} | {'Nama':<15} | {'Client':<15} | {'Tanggal':<15} | {'Grade':<15} | {'Stock':<15}")
                    for id, details in takeout.items():
                        print_product(id, details)
            
                
                inventory[takeoutbyID]["Stock"] -= jumlahtakout
                if inventory[takeoutbyID]["Stock"] < 1:
                    inventory.pop(takeoutbyID)
                    return True
            
            else:
                print("Product tidak ditemukan di inventory.")
                return False

    
        elif menutakeout == 2:
            print("Kembali kemenu sebelumnya.")
            return False

        else:
            print("pilihan tidak valid.")
            return False

def edit_inventory(): #Menu 3
    while True:
        menuedit = int(input(f"""
Menu:
1. Edit Product details
2. Exit
masukkan angka untuk melanjutkan: """))
        if menuedit == 1:

            found = search_inventory2() #kalo ketemu return True dan dia bisa edit

            if not found: #if search_inventory2 return False ini dari search_notfound() usernya gaveup
                print("Tidak ada produk yang ditemukan untuk diedit.")
                continue
            
            editbyID = input(f""" Masukkan Unique_ID yang diinginkan untuk di edit: """).upper()
            if editbyID.upper() in inventory:
                show_product_details_by_id(editbyID)

                processedit = int(input(""" 
Apa yang mau diubah:
1. Nama Product
2. Client
3. Tanggal
4. Grade(Ukuran)
Masukkan pilihan:"""))
                field2 = edit_options.get(processedit)
                if not field2:
                    print("pilihan tidak ada")
                    return False ##to backk to edit menu again
                
                
                ###ini perlu ganti IDnya juga karena dimensi berubah
                oldID = inventory[editbyID]


                #if it was 1-4
                if processedit == 4:
                    lebars = int(input("Masukkan lebar Produk(cm):"))
                    panjangs = int(input("Masukkan panjang Produk(cm):"))
                    tinggis = int(input("Masukkan tinggi Produk(cm):"))
                    newvolume = lebars*panjangs*tinggis
                    if newvolume >= 60000:
                        Grades = 'A' #Grade Produk
                    elif 10000 <= newvolume <60000:
                        Grades = 'B'
                    elif newvolume < 10000:
                        Grades = 'C'

                    
                    newID = oldID["Nama"][:2]+oldID["Client"][:2]+oldID["Tanggal"][:4]+chr(65 + (lebars % 26))+chr(65 + (panjangs % 26))+chr(65 + (tinggis % 26)) #Unique_ID
                    
                    newNama = oldID["Nama"] 
                    newClient = oldID["Client"] 
                    newTanggal = oldID["Tanggal"] 
                    newGrade = Grades #keeping the new grade
                    newStock = oldID["Stock"] 
                    newtinggi = tinggis #keeping the new height
                    newpanjang = panjangs #keeping the new length
                    newlebar = lebars #keeping the new width

                    
                else:
                    keyedit = input(f'Masukkan {field2} dari produk tersebut:').strip().upper()
                    if field2 == "Nama":

                        newID = keyedit[:2]+oldID["Client"][:2]+oldID["Tanggal"][:4]+chr(65 + (oldID["Dimensi"]["Lebar"] % 26))+chr(65 + (oldID["Dimensi"]["Panjang"] % 26))+chr(65 + (oldID["Dimensi"]["Tinggi"] % 26)) #Unique_ID

                        newNama = keyedit #keeping the new name
                        newClient = oldID["Client"]  
                        newTanggal = oldID["Tanggal"] 
                        newGrade = oldID["Grade"] 
                        newStock = oldID["Stock"] 
                        newtinggi = oldID["Dimensi"]["Tinggi"] 
                        newpanjang = oldID["Dimensi"]["Panjang"] 
                        newlebar = oldID["Dimensi"]["Lebar"] 
                    
                        
                    elif field2 == "Client":
                        
                        newID = oldID["Nama"][:2]+keyedit[:2]+oldID["Tanggal"][:4]+chr(65 + (oldID["Dimensi"]["Lebar"] % 26))+chr(65 + (oldID["Dimensi"]["Panjang"] % 26))+chr(65 + (oldID["Dimensi"]["Tinggi"] % 26)) #Unique_ID
                         
                        newNama = oldID["Nama"] 
                        newClient = keyedit #keeping the new client 
                        newTanggal = oldID["Tanggal"] 
                        newGrade = oldID["Grade"] 
                        newStock = oldID["Stock"] 
                        newtinggi = oldID["Dimensi"]["Tinggi"] 
                        newpanjang = oldID["Dimensi"]["Panjang"] 
                        newlebar = oldID["Dimensi"]["Lebar"] 
                        
                    else:
                        
                        newID = oldID["Nama"][:2]+oldID["Client"][:2]+keyedit[:4]+chr(65 + (oldID["Dimensi"]["Lebar"] % 26))+chr(65 + (oldID["Dimensi"]["Panjang"] % 26))+chr(65 + (oldID["Dimensi"]["Tinggi"] % 26)) #Unique_ID
                       
                        newNama = oldID["Nama"] 
                        newClient = oldID["Client"]  
                        newTanggal = keyedit #keeping the new date
                        newGrade = oldID["Grade"] 
                        newStock = oldID["Stock"] 
                        newtinggi = oldID["Dimensi"]["Tinggi"] 
                        newpanjang = oldID["Dimensi"]["Panjang"] 
                        newlebar = oldID["Dimensi"]["Lebar"] 

                        
                    
                    #creating temp entry for newID
                    temp_entry = {
                                    "Nama": newNama,
                                    "Client": newClient,
                                    "Tanggal": newTanggal,
                                    "Grade": newGrade,
                                    "Stock": newStock,
                                    "Dimensi": {
                                    "Lebar": newlebar,
                                    "Panjang": newpanjang,
                                    "Tinggi": newtinggi
        }
    }

                # show_product_details_by_id(editbyID) cant use this function because we creating new details so we cant use editbyID
                print(f"""
Detail Produk:
Unique_ID = {newID}
Nama Produk = {newNama}
Client = {newClient}
Tanggal masuk = {newTanggal}
Grade Produk = {newGrade} dengan lebar {newlebar} cm, panjang {newpanjang} cm, dan tinggi {newtinggi} cm
Jumlah Produk = {newStock}
""")
                #checking details product
                benartidak = input("Apakah detail produk sudah betul? (y/t): ").lower()
                if benartidak == 't':
                    print("Silakan ulangi pengeditan.")
                    return False
                else:
                    inventory[newID] = temp_entry
                    del inventory[editbyID]
                    print("Perubahan disimpan.")
                    return True        
            else:
                print("ID tidak ditemukan dalam inventory.")
                return False

        elif menuedit == 2:
            print("Kembali ke menu sebelumnya.")
            return False

        else:
            print("pilihan tidak valid.")
            return False


def delete_inventory(): #Menu 4
    while True:
        menudelete = int(input(f"""
Menu:
1. Delete Product details
2. Exit
masukkan angka untuk melanjutkan: """))
        
        if menudelete == 1:

            found = search_inventory2() #kalo ketemu return True dan dia bisa edit

            if not found: #if search_inventory2 return False ini dari search_notfound() usernya gaveup
                print("Tidak ada produk yang ditemukan untuk dihapus.")
                return False

            deletebyID = input(f""" Masukkan Unique_ID yang diinginkan untuk di edit: """).upper()
            if deletebyID.upper() in inventory:
                show_product_details_by_id(deletebyID)
                yakin = input(f'Apakah anda yakin untuk menghapus data produk dari inventory?(y/t)')
                if yakin.lower() == 'y':
                    inventory.pop(deletebyID)
                    print(f' Data {deletebyID} berhasil di hapus')
                    return True
                else:
                    print("Produk tidak jadi dihapus.")
                    return False

            else:
                print("ID tidak ditemukan dalam inventory.")
                return False

        elif menudelete == 2:
            print("Kembali ke menu sebelumnya.")
            return False

        else:
            print("pilihan tidak valid.")
            return False

### MAIN WHILE FUNCTION FOR MENU OPTION
while True:


    #Main menu function
    main_menu()
    menuNo = int(input("Masukkan menu yang diinginkkan: "))
    print("\n")

    if menuNo == 1: #display menu
        inventory_display()
        print("\n")

    elif menuNo == 2: #adding item to the inventory
        while True:
            
            result = inventory_in()
            print("\n")
            
            if result is False:
                break

            #Loop add menu
            tambah_lagi = input("Apakah Anda ingin memasukkan produk ke gudang lagi? (y/t): ").lower()
            if tambah_lagi == 't':
                break
        
    elif menuNo == 3: #edit menu
        while True:

            #display the edit menu + edit function
            result = edit_inventory()
            print("\n")
            if result is False:
                break
           
            
            #Loop edit menu
            edit_lagi = input("Apakah Anda ingin mengubah detail produk lain? (y/t): ").lower()
            if edit_lagi == 't':
                break

    elif menuNo == 4: #delete menu
        while True:

            #display the delete menu + delete function
            result = delete_inventory()
            print("\n")
            
            if result is False:
                break

            #Loop delete menu
            delete_lagi = input("Apakah Anda ingin menghapus detail produk lain? (y/t): ").lower()
            if delete_lagi == 't':
                break

    elif menuNo == 5: #takeout menu  

        while True:

            #display the delete menu + delete function
            result = inventory_out()
            print("\n")
            
            if result is False:
                break

            #Loop delete menu
            takeout_lagi = input("Apakah Anda ingin mengambil produk lain? (y/t): ").lower()
            if takeout_lagi == 't':
                break    

        #clearing the cart
        takeout.clear()

    elif menuNo == 6: #exit program
        break

    else:
        break
