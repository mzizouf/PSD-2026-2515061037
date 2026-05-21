### Sebuah toko memiliki ratusan produk yang masing-masing diidentifikasi dengan nomor SKU (Stock Keeping Unit) yang unik.
# Toko ini membutuhkan sistem yang dapat:
# Mencari data produk secara instan ketika pelanggan melakukan order.
# Menampilkan semua daftar produk secara berurutan berdasarkan nomor SKU.###

class produknode:
    def __init__(self, sku, nama_produk, harga, stok):
        self.sku = sku
        self.nama_produk = nama_produk
        self.harga = harga
        self.stok = stok
        self.left = None
        self.right = None

class sistem:
    def __init__(self):
        self.root = None

    def tambah_produk(self, sku, nama_produk, harga, stok):
        if self.root is None:
            self.root = produknode(sku, nama_produk, harga, stok)
        else:
            self._add_recursive(self.root, sku, nama_produk, harga, stok)

    def _add_recursive( self, current, sku, Nama_produk, harga, stok):
        if sku < current.sku:
            if current.left is None:
                current.left = produknode(sku, Nama_produk, harga, stok)
            else:
                self._add_recursive(current.left, sku, Nama_produk, harga, stok)
        elif sku > current.sku:
            if current.right is None:
                current.right = produknode(sku, Nama_produk, harga, stok)
            else:
                self._add_recursive(current.right, sku, Nama_produk, harga, stok)
        else:
            print(f" SKU {sku} sudah ada di sistem. Gagal menambahkan.")

    def purchase_product(self, sku):
        return self._purchase_recursive(self.root, sku)

    def _purchase_recursive(self, current, sku):
        if current is None:
            return None
        
        if current.sku == sku:
            if current.stok > 0:
                current.stok -= 1  
                return current, "Sukses"
            else:
                return current, "stok habis"
                
        if sku < current.sku:
            return self._purchase_recursive(current.left, sku)
        return self._purchase_recursive(current.right, sku)

    def find_produk(self, sku):
        return self._find_recursive(self.root, sku)

    def _find_recursive(self, current, sku):
        if current is None or current.sku == sku:
            return current
        if sku < current.sku:
            return self._find_recursive(current.left, sku)
        return self._find_recursive(current.right, sku)

    def print_catalog(self):
        print("\n=== KATALOG PRODUK (TERURUT BERDASARKAN SKU) ===")
        self._print_inorder(self.root)

    def _print_inorder(self, current):
        if current:
            self._print_inorder(current.left)
            status_stok = f"{current.stok}" if current.stok > 0 else "HABIS"
            print(f"SKU: {current.sku} | {current.nama_produk:<15} | Rp {current.harga:,} | {current.stok}")
            self._print_inorder(current.right)

inventory = sistem()

inventory.tambah_produk(205, "Gudang Garam Filter 12", 25500, 18)
inventory.tambah_produk(215, "Djarum Super 12", 26000, 25)
inventory.tambah_produk(202, "Marlboro Red 20", 46000, 19)
inventory.tambah_produk(208, "Surya 16", 34000, 22)
inventory.tambah_produk(212, "Magnum Filter 12", 22000, 10)
inventory.tambah_produk(218, "Juara Teh Manis 12", 16500, 27)
inventory.tambah_produk(201, "Camel Option Purple 16", 32000, 13)
inventory.tambah_produk(204, "Esse Change Applemint 20", 41000, 10)
inventory.tambah_produk(207, "LA Bold 20", 36500, 9)
inventory.tambah_produk(211, "Dji Sam Soe 234 12 (Kretek)", 21000, 11)
inventory.tambah_produk(214, "Dunhill Mild 20" , 42500, 21)
inventory.tambah_produk(217, "Wismilak Diplomat 16", 35000, 16)
inventory.tambah_produk(220, "Garam Merah 12", 18000, 17)
inventory.tambah_produk(203, "Clas Mild 16", 31000, 5)
inventory.tambah_produk(206, "Marlboro Ice Burst 20", 47500, 7)
inventory.tambah_produk(209, "Djarum Black 16", 33000, 2)
inventory.tambah_produk(213, "Surya Pro Mild 16", 31500, 17)
inventory.tambah_produk(216, "Sampoerna Hijau 12", 17500, 22)
inventory.tambah_produk(219, "Neo Mild 16", 24000, 28)
inventory.tambah_produk(210, "Sampoerna A Mild 16", 38500, 30)

inventory.print_catalog()
while True:
    inventory.print_catalog()
    print("\n--- MENU KASIR / PENCARIAN PRODUK ---")
    print("Ketik '0' untuk keluar dari program.")
    
    try:
        target_sku = int(input("Masukkan nomor SKU yang dibeli: "))
        
        if target_sku == 0:
            print("Program selesai. Terima kasih!")
            break
            
        print(f"\n Memproses SKU {target_sku}...")
        result = inventory.purchase_product(target_sku)

        if result:
            product, status = result
            if status == "sukses":
                print(f" Transaksi Berhasil!")
                print(f"   Nama Merk   : {product.name}")
                print(f"   Harga       : Rp {product.price:,}")
                print(f"   Sisa Stok   : {product.stock} pcs")
            elif status == "stok habis":
                print(f" Gagal Belanja: Stok untuk '{product.name}' sudah HABIS!")
        else:
            print(f" Produk dengan SKU {target_sku} tidak terdaftar.")

    except ValueError:
        print(" Error: Harap masukkan angka bulat untuk nomor SKU.")
        
    input("\nTekan Enter untuk melanjutkan...")
