import numpy as np # import library numpy
import cv2 # import library openCV
import matplotlib.pyplot as plt # import library matplotlib untuk plot gambar

img = cv2.imread("image/marvel.jpg") # membaca gambar dan menyimpannya di variabel img

img_height = img.shape[0] # menyimpan tinggi gambar ke variabel img_height
img_width = img.shape[1] # menyimpan lebar gambar ke variabel img_width
img_channel = img.shape[2] # menyimpan jumlah channel pada gambar ke variabel img_channel
img_type = img.dtype # menyimpan tipe data gambar ke variabel img_type

img_flip_horizontal = np.zeros(img.shape, img_type) # membuat array kosong dengan dimensi yang sama dengan gambar dan tipe data yang sama dengan gambar untuk menyimpan hasil flip horizontal
img_flip_vertical = np.zeros(img.shape, img_type) # membuat array kosong dengan dimensi yang sama dengan gambar dan tipe data yang sama dengan gambar untuk menyimpan hasil flip vertical

for y in range(0, img_height): # melakukan iterasi untuk setiap baris gambar
    for x in range(0, img_width): # melakukan iterasi untuk setiap kolom gambar
        for c in range(0, img_channel): # melakukan iterasi untuk setiap channel gambar
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c] # menyimpan nilai piksel gambar yang di-flip secara horizontal ke array img_flip_horizontal

for y in range(0, img_height): # melakukan iterasi untuk setiap baris gambar
    for x in range(0, img_width): # melakukan iterasi untuk setiap kolom gambar
        for c in range(0, img_channel): # melakukan iterasi untuk setiap channel gambar
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c] # menyimpan nilai piksel gambar yang di-flip secara vertikal ke array img_flip_vertical

plt.imshow(img_flip_horizontal) # menampilkan gambar hasil flip horizontal
plt.title("Flip Horizontal") # memberikan judul pada gambar
plt.show() # menampilkan gambar

plt.imshow(img_flip_vertical) # menampilkan gambar hasil flip vertical
plt.title("Flip Vertical") # memberikan judul pada gambar
plt.show() # menampilkan gambar