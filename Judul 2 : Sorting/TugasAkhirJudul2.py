def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tukar(arr, j, j + 1)

def main():
    try:
        n = int(input("Input Jumlah Mahasiswa: "))
    except ValueError:
        print("Input tidak valid!")
        return
        
    arr = []
    print(f"Masukkan tinggi badan untuk {n} mahasiswa (dalam cm):")
    for i in range(n):
        while True:
            try:
                tinggi = int(input(f"Mahasiswa ke-{i+1}: "))
                arr.append(tinggi)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
                
    print(f"\nDaftar tinggi badan sebelum diurutkan: {arr}")
    bubble_sort(arr, n)
    print("Daftar tinggi badan setelah diurutkan (Terkecil ke Terbesar):", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    main()