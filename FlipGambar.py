import numpy as np      # menginport library numpy dengan variabel np
import imageio.v3 as iio    # mengimport library imageio dengan variabel iio
# mengimport library matplotlib.pyplot dengan variabel plt
import matplotlib.pyplot as plt

# membuat variabel img dengan fungsi iio.imread untuk membaca file jpg
img = iio.imread("rei.jpg")

# membuat variabel img_height dengan fungsi img.shape untuk mengukur height
img_height = img.shape[0]
# membuat variabel img_width dengan fungsi img.shape untuk mengukur width
img_width = img.shape[1]
# membuat variabel img_channel dengan fungsi img.shape untuk mengukur channel
img_channel = img.shape[2]
# membuat variabel img_type dengan fungsi img.dtype untuk melihat type dari gambar
img_type = img.dtype


# Memubat variabel dengan array bernilai kosong
img_flip_horizontal = np.zeros(img.shape, img_type)
img_flip_vertical = np.zeros(img.shape, img_type)

for y in range(0, img_height):
    # memberi nilai pada x mulai dari 0 karena akan diisi pada array kosong sampai ukuran lebar citra yang dipaka
    for x in range(0, img_width):
        # Varibel img flip ini mengisi nilai pixel baru y dan c tetap sesuai citra asli
        for c in range(0, img_channel):
            # [img_width-1-x] ini yang membuat gambar membalik secara horizontal
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]

# Membalik gambar secara vertical

for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            # Varibel img flip ini mengisi nilai pixel baru x dan c tetap sesuai citra asli
            # [img_height-1-y] ini yang membuat gambar membalik secara vertikal
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]


# Menampilkan hasil balik gambar
plt.imshow(img_flip_horizontal)
plt.title("Flip Horizontal")
plt.show()
plt.imshow(img_flip_vertical)
plt.title("Flip Vertical")
plt.show()
