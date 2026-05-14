# saya memiliki tumpukan sebuah buku berisi 10 buku dengan judul yang akan diinputkan oleh user, temukan buku mana yang diambil duluan
class StackArray:
    def __init__(self, max_size=10):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Tumpukan buku sudah berisi 10 buku")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"Buku {x} berhasil disusun dalam tumpukan")

    def pop(self):
        if self.is_empty():
            print("Buku tidak disusun")
            return
        print(f"anda telah mengambil buku {self.st[self.top_idx]} ")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Buku tidak disusun")
            return
        print(f"Buku yang paling atas: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Buku tidak disusun")
            return
        print("susunan buku: ", end="")
        for i in range(self.top_idx, -1, -1):
            print(self.st[i], end=" ")
        print()


def main():
    stack = StackArray()
    pilih = 0
    while pilih != 5:
        print("\n=== STACK (Array) ===")
        print("1. tambahkan buku")
        print("2. ambil buku yang paling atas")
        print("3. buku yang paling atas")
        print("4. Lihat susunan buku")
        print("5. Keluar Program")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                val = str(input("buku yang ingin doitambahkan: "))
                stack.push(val)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            stack.pop()
        elif pilih == 3:
            stack.peek()
        elif pilih == 4:
            stack.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()