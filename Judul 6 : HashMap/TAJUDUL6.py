### di sebuah gedung ada beberapa ruangan dengan kode unik tolong tampilkan 
# kode unik dan nama ruangan dan 
# jika ada maka akan mengeluarkan output (ruangan ditemukan) dan 
# jika tidak ditemukan (ruangan tidak di temukan)

class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=12):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nIsi Hash Table (Open Addressing, Linear Probing):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"({self.table[i].key},{self.table[i].value})")


def main():
    hashmap = HashMapOpenAddressing()
    hashmap.insert(9, "H17")
    hashmap.insert(0, "H18")
    hashmap.insert(1, "H19")
    hashmap.insert(2, "H20")
    hashmap.insert(10, "H5")
    hashmap.insert(3, "Seminar")
    hashmap.insert(11, "Kompre")
    hashmap.insert(8, "Kaprodi")
    hashmap.insert(7, "Kajur")
    hashmap.insert(6,"Sekjur")
    hashmap.insert(5,"Dosen")
    hashmap.insert(4,"Admin")
    hashmap.display()

    x = int(input("masukkan ruangan yang anda cari : "))
    hashmap.search(x)
    if 0 > x or x < 3:
        print("ruangan ditemukan, ruangan berada di lantai 1")
    elif 3 > x or x < 8:
        print("ruangan ditemukan, ruangan berada di lantai 2")
    elif 9 > x or x < 12:
        print("ruangan ditemukan , ruangan berada di lantai 3")
    else:
        print("ruangan tidak ditemukan")
if __name__ == "__main__":
    main()