# Mengimport library numpy dan OpenCV
import numpy as np
import cv2
# Mengimport library matplotlib untuk plotting gambar
import matplotlib.pyplot as plt

# Membaca gambar dengan menggunakan OpenCV
img = cv2.imread("image/DC.jpeg")

# Mendapatkan tinggi, lebar, dan jumlah channel gambar
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]

# Membuat array numpy kosong dengan ukuran dan tipe data yang sama dengan gambar asli
img_grayscale = np.zeros(img.shape, dtype=np.uint8)

# Looping untuk setiap piksel di gambar
for y in range(0, img_height):
    for x in range(0, img_width):
        # Mendapatkan nilai komponen warna merah, hijau, dan biru (RGB) di setiap piksel
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img[y][x][2]
        # Menghitung nilai grayscale di setiap piksel dengan cara rata-rata RGB
        gray = (int(red) + int(green) + int(blue)) / 3
        # Memasukkan nilai grayscale ke setiap komponen warna (RGB) di setiap piksel
        img_grayscale[y][x] = (gray, gray, gray)

# Menampilkan gambar grayscale
plt.imshow(img_grayscale)
plt.title("Grayscale")
plt.show()

# Membuat array numpy kosong dengan ukuran 256 untuk menyimpan histogram grayscale
hg = np.zeros((256))

# Looping untuk setiap nilai grayscale
for x in range(0, 256):
    hg[x] = 0

# Looping untuk setiap piksel di gambar grayscale
for y in range(0, img_height):
    for x in range(0, img_width):
        # Mendapatkan nilai grayscale di setiap piksel
        gray = img_grayscale[y][x][0]
        # Menambahkan nilai 1 ke histogram grayscale pada posisi grayscale yang sesuai
        hg[gray] += 1

# Membuat 100 interval bin untuk histogram grayscale
bins = np.linspace(0, 256, 100)
# Menampilkan histogram grayscale dengan 100 interval bin
plt.hist(hg, bins, color="black", alpha=0.5)
plt.title("Histogram")
plt.show()

# Membuat array numpy kosong untuk histogram R, G, B, dan RGB
hgr = np.zeros((256))
hgg = np.zeros((256))
hgb = np.zeros((256))
hgrgb = np.zeros((768))

# Looping untuk setiap nilai R, G, B, dan RGB
for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768):
    hgrgb[x] = 0

for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768):
    hgrgb[x] = 0

# th = int(256/64)
temp = [0]  # menginisialisasi sebuah list dengan satu elemen 0
for y in range(0, img.shape[0]):  # melakukan iterasi pada baris dari sebuah gambar
    for x in range(0, img.shape[1]):  # melakukan iterasi pada kolom dari sebuah gambar
        # mengekstrak nilai warna RGB dari piksel saat ini
        red = int(img[y][x][0])
        green = int(img[y][x][1])
        blue = int(img[y][x][2])
        
        # memodifikasi nilai hijau dan biru
        green = green + 256
        blue = blue + 512
        
        # memperbarui histogram untuk setiap saluran warna
        hgrgb[red] += 1
        hgrgb[green] += 1
        hgrgb[blue] += 1

# mendefinisikan bins untuk histogram dan memplotnya
binsrgb = np.linspace(0, 768, 100)
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5)
plt.title("Histogram Merah Hijau Biru")
plt.show()

for y in range(0, img_height):  # melakukan iterasi pada setiap baris gambar
    for x in range(0, img_width):  # melakukan iterasi pada setiap kolom gambar
        # mengekstrak nilai warna merah, hijau, dan biru dari piksel saat ini
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img[y][x][2]
        
        # mengupdate histogram untuk setiap saluran warna
        hgr[red] += 1
        hgg[green] += 1
        hgb[blue] += 1

# mendefinisikan bins untuk setiap histogram dan memplotnya
bins = np.linspace(0, 256, 100)
plt.hist(hgr, bins, color="red", alpha=0.5)
plt.title("Histogram Merah")
plt.show()

plt.hist(hgg, bins, color="green", alpha=0.5)
plt.title("Histogram Hijau")
plt.show()

plt.hist(hgb, bins, color="blue", alpha=0.5)
plt.title("Histogram Biru")
plt.show()

# membuat array kosong hgk dan c dengan ukuran 256
hgk = np.zeros((256))
c = np.zeros((256))

# menginisialisasi setiap nilai pada hgk dan c dengan 0
for x in range(0, 256):
    hgk[x] = 0
    c[x] = 0

# melakukan iterasi pada setiap piksel pada gambar grayscale
for y in range(0, img_height):
    for x in range(0, img_width):
        # mengekstrak nilai warna abu-abu dari piksel saat ini
        gray = img_grayscale[y][x][0]
        hgk[gray] += 1
                
# melakukan proses kumulatif pada nilai c untuk setiap piksel
c[0] = hgk[0]
for x in range(1, 256):
     c[x] = c[x-1] + hgk[x]

# mencari nilai hmaxk dari c
hmaxk = c[255]

# melakukan normalisasi pada nilai c dan memplot histogramnya
for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

bins = np.linspace(0, 256, 100)
plt.hist(c, bins, color="black", alpha=0.5)
plt.title("Histogram Kumulatif Grayscale")
plt.show()

# Inisialisasi array untuk menyimpan nilai histogram
hgh = np.zeros((256))
h = np.zeros((256))
c = np.zeros((256))

# Setel semua nilai dalam array menjadi 0
for x in range(0, 256):
    hgh[x] = 0
    h[x] = 0
    c[x] = 0

# Loop melalui setiap piksel dalam gambar dan tambahkan nilai histogram yang sesuai
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hgh[gray] += 1
                
# Hitung histogram kumulatif
h[0] = hgh[0]
for x in range(1, 256):
     h[x] = h[x-1] + hgh[x]

# Normalisasi nilai histogram kumulatif
for x in range(0, 256):
     h[x] = h[x] / img_height / img_width

# Setel array hgh kembali ke 0
for x in range(0, 256):
    hgh[x] = 0
    
# Loop melalui setiap piksel dalam gambar dan hitung nilai grayscale baru menggunakan histogram kumulatif yang dinormalisasi
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        gray = h[gray] * 255
        hgh[int(gray)] += 1

# Hitung histogram kumulatif dari nilai grayscale baru
c[0] = hgh[0]
for x in range(1, 256):
     c[x] = c[x-1] + hgh[x]

# Hitung nilai maksimum pada histogram kumulatif
hmaxk = c[255]

# Skala nilai histogram kumulatif ke rentang [0, 190]
for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

# Plot histogram menggunakan nilai histogram kumulatif yang sudah diteskalasi
plt.hist(c, bins, color="black", alpha=0.5)
plt.title("Histogram Grayscale Hequalisasi")
plt.show()
