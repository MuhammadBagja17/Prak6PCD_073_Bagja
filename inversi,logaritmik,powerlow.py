import numpy as np
import cv2
import matplotlib.pyplot as plt
# masukan import libarary yang dibutuhkan

# Masukan gambar yang akan diproses
img = cv2.imread("image/marvel2.jpeg")

# Mendapatkan dimensi gambar
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]

# Buat array kosong untuk menyimpan gambar yang diinversi
img_inversi = np.zeros(img.shape, dtype=np.uint8)

# Tentukan fungsi untuk menginversi nilai grayscale dari setiap piksel
def inversi_grayscale(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Mendapatkan nilai RGB dari piksel saat ini
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            # Konversi nilai RGB menjadi grayscale
            gray = (int(red) + int(green) + int(blue)) / 3
            # Inversi nilai grayscale
            gray = nilai - gray
            # Tetapkan nilai piksel pada array gambar yang diinversi
            img_inversi[y][x] = (gray, gray, gray)

# Tentukan fungsi untuk menginversi nilai grayscale dari setiap piksel
def inversi_rgb(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Mendapatkan nilai RGB dari piksel saat ini
            red = img[y][x][0]
            red = nilai - red
            green = img[y][x][1]
            # Inversi nilai green channel
            green = nilai - green
            blue = img[y][x][2]
            # Inversi nilai blue channel
            blue = nilai - blue
            # Tetapkan nilai piksel pada array gambar yang diinversi
            img_inversi[y][x] = (red, green, blue)
#  Memanggil fungsi untuk menginversi nilai grayscale dari semua piksel pada gambar
inversi_grayscale(255)
# Menampilkan gambar inversi dengan grayscale
plt.imshow(img_inversi)
plt.title("Inversi Grayscale")
plt.show()
#  Memanggil fungsi untuk menginversi nilai RGB dari semua piksel pada gambar
inversi_rgb(255)
# Menampilkan gambar inversi dengan RGB
plt.imshow(img_inversi)
plt.title("Inversi RGB")
plt.show()

# Buat array kosong untuk menyimpan gambar hasil transformasi logaritmik
img_log = np.zeros(img.shape, dtype=np.uint8)

# Tentukan fungsi untuk melakukan transformasi logaritmik pada setiap piksel gambar
def log(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Dapatkan nilai RGB dari piksel saat ini
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]

            # Konversi nilai RGB menjadi grayscale
            gray = (int(red) + int(green) + int(blue)) / 3

            # Lakukan transformasi logaritmik pada nilai grayscale
            gray = int(c * np.log(gray + 1))

            # Pastikan nilai grayscale tidak melebihi 255 atau kurang dari 0
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0

            # Tetapkan nilai piksel pada array gambar hasil transformasi logaritmik
            img_log[y][x] = (gray, gray, gray)

# Panggil fungsi untuk melakukan transformasi logaritmik pada gambar dengan parameter c=30
log(30)

# Tampilkan gambar hasil transformasi logaritmik
plt.imshow(img_log)
plt.title("Log")
plt.show()

# Buat array kosong untuk menyimpan gambar hasil transformasi logaritmik dan inversi
img_inlog = np.zeros(img.shape, dtype=np.uint8)

# Tentukan fungsi untuk melakukan transformasi logaritmik dan inversi pada setiap piksel gambar
def inlog(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Dapatkan nilai RGB dari piksel saat ini
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]

            # Konversi nilai RGB menjadi grayscale
            gray = (int(red) + int(green) + int(blue)) / 3

            # Lakukan inversi pada nilai grayscale
            gray = 255 - gray

            # Lakukan transformasi logaritmik pada nilai grayscale yang sudah di-inversi
            gray = int(c * np.log(gray + 1))

            # Pastikan nilai grayscale tidak melebihi 255 atau kurang dari 0
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0

            # Tetapkan nilai piksel pada array gambar hasil transformasi logaritmik dan inversi
            img_inlog[y][x] = (gray, gray, gray)

# Panggil fungsi untuk melakukan transformasi logaritmik dan inversi pada gambar dengan parameter c=30
inlog(30)

# Tampilkan gambar hasil transformasi logaritmik dan inversi
plt.imshow(img_inlog)
plt.title("Inversi & Log")
plt.show()

# membuat sebuah array numpy kosong dengan ukuran yang sama dengan gambar asli
img_nthpower = np.zeros(img.shape, dtype=np.uint8)

# mendefinisikan sebuah fungsi untuk melakukan transformasi pangkat n pada gambar input
def nthpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            # menghitung nilai keabuan dengan mengambil rata-rata dari nilai RGB
            gray = (int(red) + int(green) + int(blue)) / 3
            # melakukan transformasi pangkat n pada nilai keabuan
            gray = int(thc * pow(gray, thy))
            # memastikan nilai keabuan hasil transformasi berada dalam range 0-255
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            # menetapkan nilai keabuan baru untuk setiap saluran RGB pada gambar hasil
            img_nthpower[y][x] = (gray, gray, gray)

# menerapkan transformasi pangkat n pada gambar input
nthpower(50, 100)
# menampilkan gambar hasil dengan menggunakan Matplotlib
plt.imshow(img_nthpower)
plt.title("Nth Power")
plt.show()

# Menginisialisasi array kosong img_nthrootpower dengan tipe data uint8 dan ukuran yang sama dengan img
img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)
# Membuat fungsi nthrootpower yang menerima parameter c dan y untuk menghitung pixel gambar dengan rumus c * gray ** (1/y)
def nthrootpower(c, y):
    thc = c / 100
    thy = y / 100
    # Melakukan iterasi untuk setiap piksel pada gambar
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Mengambil nilai intensitas RGB dan menghitung rata-rata gray
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
        
            # Menghitung nilai gray berdasarkan rumus nthrootpower
            gray = int(thc * pow(gray, 1./thy))
        
            # Memastikan nilai gray dalam range 0-255
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            
            # Menyimpan nilai gray ke dalam array img_nthrootpower
            img_nthrootpower[y][x] = (gray, gray, gray)

# Memanggil fungsi nthrootpower dengan parameter 50 dan 100
nthrootpower(50, 100)
# menampilkan gambar hasil dengan menggunakan Matplotlib
plt.imshow(img_nthrootpower)
plt.title("Nth Root Power")
plt.show()