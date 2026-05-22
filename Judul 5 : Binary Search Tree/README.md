Program ini dimulai dengan mengimpor modul os untuk kebutuhan manipulasi terminal, lalu mendefinisikan kelas produknode. Kelas ini berfungsi sebagai building block atau cetak biru untuk setiap item produk. Metode __init__ di dalamnya menginisialisasi atribut utama seperti sku, nama_produk, harga, dan stok, serta menyiapkan pointer left dan right yang menjadi dasar pembentukan struktur data Binary Search Tree (BST). 

Selanjutnya, kelas sistem didefinisikan untuk mengelola keseluruhan alur operasi inventaris. Metode __init__ pada kelas ini bertugas menyiapkan self.root dengan nilai awal None. Hal ini menandakan bahwa saat objek sistem baru dibuat, struktur pohon biner masih dalam keadaan kosong dan belum memiliki data produk.

Untuk memasukkan produk ke dalam sistem, metode tambah_produk berperan sebagai pintu masuk utama. Fungsi ini melakukan pemeriksaan kondisi: jika root masih kosong, maka produk tersebut akan otomatis menjadi node akar (root). Namun, jika sudah ada data di dalamnya, sistem akan meneruskan proses penambahan data ke metode pembantu yang bersifat rekursif.

Metode _add_recursive merupakan inti dari logika penyisipan data pada struktur BST agar data tetap terurut. Fungsi ini membandingkan sku baru dengan sku pada node yang sedang dikunjungi; jika sku baru lebih kecil, ia bergerak ke cabang kiri, dan jika lebih besar, ke cabang kanan. Jika ditemukan sku yang identik, sistem akan mencetak pesan kesalahan karena nomor SKU harus unik.

Saat pelanggan melakukan pembelian, metode purchase_product dipanggil untuk memulai proses pencarian barang berdasarkan sku. Fungsi ini bertindak sebagai pembungkus (wrapper) yang memicu proses pencarian rekursif mulai dari node root, sehingga antarmuka pengguna dapat berinteraksi dengan sistem dengan cara yang sederhana dan intuitif.

Logika transaksi yang sebenarnya ditangani oleh metode _purchase_recursive. Fungsi ini menelusuri pohon secara rekursif untuk menemukan node dengan sku yang sesuai; jika ditemukan dan stok masih tersedia (lebih dari nol), sistem akan mengurangi stok sebesar satu dan memberikan status "sukses", namun jika stok habis, sistem akan memberikan notifikasi "stok habis".

Untuk kebutuhan pelaporan, metode print_catalog digunakan untuk menampilkan daftar lengkap produk. Sebelum menampilkan data, metode ini menggunakan modul os untuk membersihkan layar konsol (clear screen) agar tampilan bersih, kemudian mencetak header tabel dan memanggil fungsi rekursif untuk menampilkan seluruh isi inventaris kepada pengguna.

Metode _print_inorder menjalankan algoritma penelusuran in-order (kiri-akar-kanan). Pendekatan ini sangat efektif untuk menampilkan daftar produk dalam urutan sku terkecil ke terbesar secara otomatis. Di sini, sistem juga menambahkan logika kondisional untuk menampilkan status "HABIS" bagi produk yang memiliki stok nol, sehingga laporan lebih informatif.

Setelah struktur kelas selesai, baris kode selanjutnya melakukan inisialisasi objek inventory dan pengisian data. Produk-produk rokok dengan berbagai rincian harga dan stok dimasukkan ke dalam sistem melalui pemanggilan berulang metode tambah_produk, sehingga pohon biner terbentuk dengan rapi sesuai dengan struktur hierarki yang ditentukan oleh nilai sku.

Bagian utama program dijalankan dalam loop while True agar sistem tetap berjalan secara interaktif. Di awal setiap iterasi, inventory.print_catalog() dipanggil untuk memastikan pengguna selalu melihat katalog terbaru beserta data stok yang sudah terbarui setelah adanya transaksi yang dilakukan sebelumnya.

Terakhir, blok try-except menangani input pengguna saat melakukan pembelian untuk mencegah crash pada program. Jika pengguna memasukkan SKU, sistem akan memproses transaksi dan menampilkan hasil berupa struk atau pesan error. Program akan berhenti jika pengguna menekan angka '0', dan fungsi input() di akhir digunakan agar pengguna memiliki waktu untuk melihat hasil transaksi sebelum layar dibersihkan kembali.

link youtube : https://youtu.be/ZUSk9ESk8cA
