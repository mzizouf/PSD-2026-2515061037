def menu():
    print("\n")
    print("1. Tampilkan List Lagu")
    print("2. Masukan Lagu Kedalam List ")
    print("3. Keluar")

def main():
    playlist = []

    while True:
        menu()
        pilihan = input("pilih menu : ")

        if pilihan == "1":
            print("\nDaftar Lagu ")
            if not playlist:
                print("Playlist kosong")
            else:
                for urutan, lagu in enumerate(playlist, 1):
                    print(f"{urutan}.{lagu} ")

        elif pilihan == "2":
            judul = input("masukan judul lagu: ")
            playlist.append(judul)
            print(f"Berhasil menamahkan '{judul}' ke dalam list.")

        elif pilihan == "3":
            print("Keluar program. terimakasih")
            break

        else:
            print("pilihan tidak valid")

if __name__ == "__main__":
    main()