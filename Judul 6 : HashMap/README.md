Program ini dimulai dengan mendefinisikan kelas SlotState yang berfungsi sebagai penyimpan status konstanta. Dengan nilai EMPTY, OCCUPIED, dan DELETED, sistem dapat melacak kondisi setiap slot dalam hash table secara akurat, yang merupakan langkah krusial dalam mengelola ruang memori pada struktur data hash map.

Selanjutnya, kelas Entry dibentuk sebagai wadah unit data terkecil. Setiap objek Entry akan menyimpan key (kode ruangan), value (nama ruangan), dan status slot tersebut. Inisialisasi awal pada metode __init__ memastikan bahwa setiap entri dimulai dalam kondisi EMPTY sebelum data dimasukkan oleh pengguna.

Kelas HashMapOpenAddressing kemudian menjadi pusat logika sistem. Metode __init__ menyiapkan table berupa list berukuran 12, yang diisi dengan objek Entry. Struktur ini memberikan batasan kapasitas yang tetap namun efisien untuk menampung data ruangan dengan metode pengalamatan langsung.

Fungsi hash_function bertindak sebagai penentu posisi data. Dengan menggunakan operasi modulo (key % self.SIZE), sistem dapat memetakan setiap kode unik ruangan ke indeks yang spesifik dalam table. Penambahan perhitungan + self.SIZE sebelum modulo memastikan bahwa hasil hash selalu bernilai positif, mencegah kesalahan indeks pada angka negatif.

Metode insert mengimplementasikan logika utama untuk memasukkan data dengan teknik linear probing. Jika terjadi tabrakan (collision) pada indeks tertentu, metode ini akan menelusuri slot berikutnya yang tersedia hingga menemukan tempat kosong atau slot yang ditandai DELETED, sehingga data tetap tersimpan dengan rapi tanpa menimpa entri lain.

Untuk menemukan data, metode search digunakan untuk menelusuri tabel berdasarkan key yang diberikan. Dengan mengulangi pencarian mulai dari posisi hash awal, sistem akan terus bergerak secara linear hingga menemukan key yang dicari atau bertemu dengan slot EMPTY, yang menandakan bahwa data tersebut memang tidak ada dalam sistem.

Program juga dilengkapi dengan metode remove_key untuk manajemen data yang dinamis. Jika suatu ruangan tidak lagi diperlukan, metode ini akan memanggil search untuk menemukan key tersebut, lalu mengubah status slotnya menjadi DELETED. Teknik ini memungkinkan penghapusan data tanpa merusak rantai pencarian linear yang sudah terbentuk.

Metode display berfungsi sebagai alat visualisasi untuk pengembang. Dengan mencetak isi table dari indeks 0 hingga 11, pengguna dapat memantau secara langsung bagaimana status setiap slot (EMPTY, DELETED, atau berisi data). Ini membantu memvalidasi efektivitas distribusi data di dalam hash table.

Bagian main menjadi tempat inisialisasi dan pengujian sistem. Di sini, berbagai data ruangan seperti "Seminar", "Admin", hingga "Dosen" dimasukkan ke dalam objek hashmap menggunakan metode insert. Pengisian ini mensimulasikan kondisi gedung nyata dengan berbagai ruangan yang memiliki kode unik masing-masing.

Logika interaksi pengguna terletak di bagian akhir program, di mana sistem meminta input kode ruangan yang ingin dicari. Program kemudian memproses pencarian melalui hashmap.search(x). Sistem ini dirancang untuk memberikan umpan balik instan kepada pengguna mengenai keberadaan data ruangan yang dicari tersebut.

Terakhir, blok kondisional if-elif-else digunakan untuk menampilkan informasi lokasi lantai ruangan. Meskipun saat ini kodenya mengecek rentang angka, struktur ini memberikan alur yang jelas bagi pengguna untuk mengetahui di mana ruangan tersebut berada. Program ini ditutup dengan perlindungan if __name__ == "__main__": agar fungsi main hanya berjalan jika skrip dijalankan secara langsung.

LINK YOUTUBE : https://youtu.be/bnoCc2NR3e8
