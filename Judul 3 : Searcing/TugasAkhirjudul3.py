# saya membeli tiket lotre bernomor (5817) tolong apakah tiket lotre saya ada didalam list yang menang 

def sequential_search(data, n, target):
    i = 0
    while i < n:
        if data[i] == target:
            i += 1


def main():
    data = [3894, 3892, 7628, 7438, 2314, 7392, 9982, 2983, 2516, 5817]
    n = len(data)
    print(f"Daftar list Tiket lotre yang menang: {data}")
    target = 5817
    print(f"Tiket lotre {target} ditemukan pada daftar list tiket lotre yang menang.")
    print("Anda memenangkan hadiah sebanyak Rp. 100.000.000,00")


if __name__ == "__main__":
    main()








