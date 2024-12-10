import random
# Membuat grid kosong
grid = [
   [0, 0, 0, 0],
   [0, 0, 0, 0],
   [0, 0, 0, 0],
   [0, 0, 0, 0]
]

# Posisi angka 2 pertama
row = random.randint(0, 3)
column = random.randint(0, 3)
grid[row][column] = 2

# Posisi angka kedua
while True:
    row = random.randint(0, 3)
    column = random.randint(0, 3)
    if grid[row][column] == 0:
        grid[row][column] = random.choice([2, 4])
        break

# Implementasi kontrol
while True:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=' ')
        print()
    arah = input("Perintah (w/a/s/d): ")

    grid_sebelum = [row[:] for row in grid]  # Salin grid sebelum pergerakan

    if arah == 'w':
        # Geser ke atas
        for i in range(4):  # Iterasi kolom
            for j in range(1, 4):  # Iterasi baris
                for k in range(0, j):
                    if grid[j-k-1][i] == 0 or grid[j-k-1][i] == grid[j-k][i]:
                        grid[j-k-1][i] += grid[j-k][i]
                        grid[j-k][i] = 0

    elif arah == 'a':
        # Geser ke kiri
        for i in range(4):  # Iterasi baris
            for j in range(1, 4):  # Iterasi kolom
                for k in range(j):
                    if grid[i][j-k] == 0 or grid[i][j-k] == grid[i][j-k-1]:
                        grid[i][j-k] += grid[i][j-k-1]
                        grid[i][j-k-1] = 0

    elif arah == 's':
        # Geser ke bawah
        for i in range(4):  # Iterasi kolom
            for j in range(2, -1, -1):  # Iterasi baris mundur
                for k in range(j, 3):
                    if grid[k+1][i] == 0 or grid[k+1][i] == grid[k][i]:
                        grid[k+1][i] += grid[k][i]
                        grid[k][i] = 0

    elif arah == 'd':
        # Geser ke kanan
        for i in range(4):  # Iterasi baris
            for j in range(2, -1, -1):  # Iterasi kolom mundur
                for k in range(j, 3):
                    if grid[i][k+1] == 0 or grid[i][k+1] == grid[i][k]:
                        grid[i][k+1] += grid[i][k]
                        grid[i][k] = 0

    else:
        print("Perintah tidak valid.")
        continue

    # Tambahkan angka baru hanya jika grid berubah
    if grid != grid_sebelum:  # Periksa apakah grid berubah
        while True:
            row = random.randint(0, 3)
            column = random.randint(0, 3)
            if grid[row][column] == 0:  # Cari posisi kosong
                grid[row][column] = 2  # Tambahkan angka 2
                break
