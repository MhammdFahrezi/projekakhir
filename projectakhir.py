from prettytable import PrettyTable
import csv
import pwinput
#=========================================saldo dan list data========================================
# Inisialisasi saldo E-money dan uang cash
saldo_emoney = 10000
uang_cash = 200000
# Definisi pajak
pembayaran_pajak = [
    {"no": 1, "nama_pajak": "Pajak_PPh", "yang_terkena_pajak": "upah, gaji, tunjangan", "penghasilan_pertahun": 5000, "potongan_persen": "5%"},
    {"no": 2, "nama_pajak": "Pajak_PPn", "yang_terkena_pajak": "pengusaha, perusahaan", "penghasilan_pertahun": 2000, "potongan_persen": "5%"},
]
#======================================staf pajak======================================================
def menu_staf_pajak(pembayaran_pajak):
    try:
        while True:
            print("\nMenu staf pajak:")
            print("1. Lihat list pajak")
            print("2. Tambah pajak")
            print("3. Perbarui pajak")
            print("4. Hapus pajak")
            print("5. Keluar")
            print("===================================")
            menu = input("Pilih menu (1/2/3/4/5): ")
            print("===================================")

            try:
                menu = int(menu)  # Mengonversi input pengguna menjadi bilangan bulat
            except ValueError:
                raise ValueError("Input harus berupa nomor.")

            if menu == 1:
                # Menampilkan daftar pajak
                tampilkan_list_pajak(pembayaran_pajak)
            elif menu == 2:
                # Menambahkan pajak baru
                tambah_pajak(pembayaran_pajak)
            elif menu == 3:
                # Perbarui pajak
                perbarui_pajak(pembayaran_pajak)
            elif menu == 4:
                # Hapus pajak
                hapus_pajak(pembayaran_pajak)
            elif menu == 5:
                break
            else:
                print("Pilihan tidak valid.")
    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
# Fungsi untuk menampilkan daftar pajak
def tampilkan_list_pajak(pajak_data):
    if not pajak_data:
        print("Tidak ada data pajak yang tersedia.")
    else:
        table = PrettyTable()
        table.field_names = ["No.", "Nama Pajak", "Yang Terkena Pajak", "Penghasilan Pertahun", "Potongan Persen"]
        for pajak in pajak_data:
            table.add_row([pajak["no"], pajak["nama_pajak"], pajak["yang_terkena_pajak"],
                        f"Rp {pajak['penghasilan_pertahun']}", pajak["potongan_persen"]])
        print(table)
print("===================================")
# Fungsi untuk menambah pajak baru
def tambah_pajak(pajak_data):
    try:
        nama_pajak = input("Masukkan nama pajak: ")
        yang_terkena_pajak = input("Masukkan yang terkena pajak: ")
        penghasilan_pertahun = int(input("Masukkan penghasilan pertahun: "))
        potongan_persen = input("Masukkan potongan persen: ")
    #memasukan pajak baru
        pajak_baru = {
            "no": len(pajak_data) + 1,
            "nama_pajak": nama_pajak,
            "yang_terkena_pajak": yang_terkena_pajak,
            "penghasilan_pertahun": penghasilan_pertahun,
            "potongan_persen": potongan_persen
        }
        # memasukan ke data csv
        pajak_data.append(pajak_baru)
        simpan_data_ke_csv(pajak_data)  # Simpan data ke CSV
        print(f"{nama_pajak} telah ditambahkan ke pembayaran pajak.")
    except Exception as e:
        print("Terjadi kesalahan ketika menambahkan pajak.")
print("===================================")
# Fungsi untuk menyimpan data ke file CSV
def simpan_data_ke_csv(pajak_data):
    try:
        with open("pajak.csv", mode="w", newline="") as file:
            fieldnames = pajak_data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(pajak_data)
    except Exception as e:
        print("Data gagal disimpan.")

# Fungsi untuk perbarui pajak
def perbarui_pajak(pajak_data):
    try:
        tampilkan_list_pajak(pajak_data)
        no_pajak = input("Pilih nomor pajak yang akan diperbarui: ")
        pajak_pilihan = next((p for p in pajak_data if str(p["no"]) == no_pajak), None)

        if pajak_pilihan:
            # Input perubahan data pajak
            nama_pajak = input("Masukkan nama pajak baru (kosongkan jika tidak ada perubahan): ")
            if nama_pajak:
                pajak_pilihan["nama_pajak"] = nama_pajak
            yang_terkena_pajak = input("Masukkan yang terkena pajak baru (kosongkan jika tidak ada perubahan): ")
            if yang_terkena_pajak:
                pajak_pilihan["yang_terkena_pajak"] = yang_terkena_pajak

            penghasilan_pertahun = input("Masukkan penghasilan pertahun baru (kosongkan jika tidak ada perubahan): ")
            if penghasilan_pertahun and float(penghasilan_pertahun):
                pajak_pilihan["penghasilan_pertahun"] = float(penghasilan_pertahun)

            potongan_persen = input("Masukkan potongan persen baru (kosongkan jika tidak ada perubahan): ")
            if potongan_persen:
                pajak_pilihan["potongan_persen"] = potongan_persen

            simpan_data_ke_csv(pajak_data)  # Simpan data ke CSV
            print("Data pajak telah diperbarui.")
        else:
            print("Nomor pajak tidak valid.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")




# Fungsi untuk menghapus pajak
def hapus_pajak(pajak_data):
    try:
        tampilkan_list_pajak(pajak_data)
        no_pajak = input("Pilih nomor pajak yang akan dihapus: ")
        pajak_pilihan = next((p for p in pajak_data if str(p["no"]) == no_pajak), None)

        if pajak_pilihan:
            pajak_data.remove(pajak_pilihan)
            simpan_data_ke_csv(pajak_data)  # Simpan data ke CSV
            print("Data pajak telah dihapus.")
        else:
            print("Nomor pajak tidak valid.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
#==========================================menu pembayar======================================================
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def menu_pembayar(pembayaran_pajak):
    while True:
        try:
            print("\nMenu pembayar pajak:")
            print("1. Lihat list pajak")
            print("2. Pembayaran pajak")
            print("3. Keluar")
            print("===================================")
            menu_pembayaran_pajak = input("Pilih menu (1/2/3): ")

            if menu_pembayaran_pajak == "1":                                                                                                                        
                # Menampilkan daftar pajak
                tampilkan_list_pajak(pembayaran_pajak)
            elif menu_pembayaran_pajak == "2":
                # Melakukan pembayaran pajak
                struk = pembayaran_pajak_menu(pembayaran_pajak)
                if struk:
                    print("======= Struk Pembayaran =======")
                    print("Nama Pajak:", struk["nama_pajak"])
                    print("Penghasilan Pertahun:", f"Rp {struk['penghasilan']:.2f}")
                    print("Potongan Persen:", struk["potongan_persen"])
                    print("Jumlah Pajak:", f"Rp {struk['pajak']:.2f}")
                    print("Metode Pembayaran:", struk["metode_pembayaran"])
                    if struk["metode_pembayaran"] == "E-money":
                        print("Saldo E-money:", f"Rp {struk['saldo_emoney']:.2f}")
                    elif struk["metode_pembayaran"] == "Cash":
                        print("Uang Cash Anda saat ini:", f"Rp {struk['uang_cash']:.2f}")
                    print("===================================")
            elif menu_pembayaran_pajak == "3":
                break
            else:
                print("Pilihan tidak valid.")
        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")

def pembayaran_pajak_menu(pajak_data):
    try:
        tampilkan_list_pajak(pajak_data)
        no_pajak = input("Pilih nomor pajak yang akan dibayarkan: ")
        pajak_pilihan = next((p for p in pajak_data if str(p["no"]) == no_pajak), None)

        if pajak_pilihan:
            while True:
                penghasilan = input(f"Masukkan penghasilan pertahun (minimal {pajak_pilihan['penghasilan_pertahun']}): ")
                if is_integer(penghasilan):
                    penghasilan = int(penghasilan)
                    break
                else:
                    print("Penghasilan harus berupa angka.")

            if penghasilan < pajak_pilihan['penghasilan_pertahun']:
                print("Penghasilan tidak mencukupi untuk membayar pajak ini.")
            else:
                potongan_persen = int(pajak_pilihan["potongan_persen"][:-1]) / 100
                pajak = penghasilan * potongan_persen
                print(f"Anda harus membayar pajak {pajak_pilihan['nama_pajak']} sebesar Rp {pajak:.2f}")

                while True:
                    print("1. Bayar dengan E-money")
                    print("2. Bayar dengan metode lain")
                    metode_pembayaran = input("Pilih metode pembayaran (1/2): ")

                    if metode_pembayaran == "1":
                        global saldo_emoney
                        if saldo_emoney >= pajak:
                            saldo_emoney -= pajak
                            struk = {
                                "nama_pajak": pajak_pilihan["nama_pajak"],
                                "penghasilan": penghasilan,
                                "potongan_persen": pajak_pilihan["potongan_persen"],
                                "pajak": pajak,
                                "metode_pembayaran": "E-money",
                                "saldo_emoney": saldo_emoney,
                            }
                            print(f"Pajak {pajak_pilihan['nama_pajak']} sebesar Rp {pajak:.2f} telah dibayar menggunakan E-money.")
                            print(f"Saldo E-money Anda saat ini: Rp {saldo_emoney:.2f}")
                            return struk
                        else:
                            print("Saldo E-money tidak mencukupi.")
                        break
                    elif metode_pembayaran == "2":
                        global uang_cash
                        while True:
                            uang_cash = input(f"Masukkan uang cash Anda saat ini (minimal {pajak} Rp): ")
                            if is_integer(uang_cash):
                                uang_cash = int(uang_cash)
                                break
                            else:
                                print("Uang cash harus berupa angka.")
                        
                        if uang_cash >= pajak:
                            uang_cash -= pajak
                            struk = {
                                "nama_pajak": pajak_pilihan["nama_pajak"],
                                "penghasilan": penghasilan,
                                "potongan_persen": pajak_pilihan["potongan_persen"],
                                "pajak": pajak, 
                                "metode_pembayaran": "Cash",
                                "uang_cash": uang_cash,
                            }
                            print(f"Pajak {pajak_pilihan['nama_pajak']} sebesar Rp {pajak:.2f} telah dibayar menggunakan cash.")
                            print(f"Uang cash Anda saat ini: Rp {uang_cash:.2f}")
                            return struk
                    else:
                        print("Pilihan metode pembayaran tidak valid.")
        else:
            print("Nomor pajak  tidak valid.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
#====================================== menu untuk regis dan login=============================================
# Fungsi untuk membaca akun staf dari file CSV
def akun_staf():
    try:
        with open("akun_staf.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            akun_staf = {rows[0]: rows[1] for rows in reader}
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan file 'akun_staf.csv' ada.")
        akun_staf = {}
    return akun_staf
# Fungsi untuk memasukkan akun staf ke file CSV
def masukan_akun_staf(akun_staf):
    try:
        with open("akun_staf.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            for nama_staf, sandi_staf in akun_staf.items():
                writer.writerow([nama_staf, sandi_staf])
    except Exception as e:
        print(f"Error: {e}")
# Fungsi untuk membaca akun pelanggan dari file CSV
def akun_pembayar():
    try:
        with open("akun_pembayar.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            akun_pembayar = {rows[0]: rows[1] for rows in reader}
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan file 'akun_pembayar.csv' ada.")
        akun_pembayar = {}
    return akun_pembayar
# Fungsi untuk memasukkan akun pembayar ke file CSV
def masukan_akun_pembayar(akun_pembayar):
    try:
        with open("akun_pembayar.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            for nama_pembayar, sandi_pembayar in akun_pembayar.items():
                writer.writerow([nama_pembayar, sandi_pembayar])
    except Exception as e:
        print(f"Error: {e}")
# Fungsi untuk login staf
def login_staf(akun_staf):
    try:
        nama_staf = input("Masukkan nama staf: ")
        sandi_staf = pwinput.pwinput("Masukkan sandi staf: ")
        if nama_staf in akun_staf and akun_staf[nama_staf] == sandi_staf:
            return nama_staf
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
# Fungsi untuk mendaftarkan akun staf
def register_staf(akun_staf):
    try:
        nama_staf = input("Masukkan nama staf: ")
        sandi_staf = pwinput.pwinput("Masukkan sandi staf: ")
        akun_staf [nama_staf] = sandi_staf
        masukan_akun_staf(akun_staf)  # Simpan perubahan ke file CSV
        print("============Akun staf berhasil terdaftar============")
    except Exception as e:
        print(f"Error: {e}")
# Fungsi untuk login pelanggan
def login_pembayar(akun_pembayar):
    try:
        nama_pembayar = input("Masukkan nama pembayar: ")
        sandi_pembayar = pwinput.pwinput("Masukkan sandi pembayar: ")
        if nama_pembayar in akun_pembayar and akun_pembayar[nama_pembayar] == sandi_pembayar:
            return nama_pembayar
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
# Fungsi untuk mendaftarkan akun pelanggan
def register_pembayar(akun_pembayar):
    try:
        nama_pembayar = input("Masukkan nama pembayar: ")
        sandi_pembayar = pwinput.pwinput("Masukkan sandi pembayar: ")
        akun_pembayar[nama_pembayar] = sandi_pembayar
        masukan_akun_pembayar(akun_pembayar)  # Simpan perubahan ke file CSV
        print("============Akun pembayar berhasil terdaftar============")
    except Exception as e:
        print(f"Error: {e}")
#=========================================menu untuk meilih masuk sebagi staf atau pembayar================================

staf = akun_staf()
pelanggan = akun_pembayar()
pilihan = ""

while pilihan != "5":
    print("1. Daftar akun staf")
    print("2. Login sebagai staf")
    print("3. Daftar akun pelanggan")
    print("4. Login sebagai pelanggan")
    print("5. Keluar")
    
    try:
        pilihan = input("Pilih tindakan (1/2/3/4/5): ")
        if pilihan == "1":
            try:
                register_staf(staf)
                masukan_akun_staf(staf)  # Simpan perubahan ke file CSV
            except FileNotFoundError:
                print("Error: File tidak ditemukan.")
        elif pilihan == "2":
            if staf:
                login_staf(staf)
                print("Anda telah login sebagai staf.")
                print("Selamat datang")
                menu_staf_pajak(pembayaran_pajak)  # Masukkan daftar pajak sebagai argumen
        elif pilihan == "3":
            try:
                register_pembayar(pelanggan)
                masukan_akun_pembayar(pelanggan)  # Simpan perubahan ke file CSV
            except FileNotFoundError:
                print("Error: File tidak ditemukan.")
        elif pilihan == "4":
            if pelanggan:
                login_pembayar(pelanggan)
                print("Anda telah login sebagai pelanggan.")
                print("Selamat datang")
                menu_pembayar(pembayaran_pajak)  # Masukkan daftar pajak sebagai argumen
        elif pilihan == "5":
            print("Keluar")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    except KeyboardInterrupt:
        print("Input tidak valid. Silakan coba lagi.")