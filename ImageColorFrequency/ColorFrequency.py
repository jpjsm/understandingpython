import cv2 as cv
import matplotlib.pyplot as plt 

img_path = 'images/thalia-fullcolor.jpg'
img_8bitchannel = cv.imread(img_path)
img_3bitchannel = img_8bitchannel.copy()
img_2bitchannel = img_8bitchannel.copy()

img_width= img_8bitchannel.shape[1]
img_height= img_8bitchannel.shape[0]

colors_in_3bits = {}
colors_in_2bits = {}

for rows_index in range(img_height):
    for cols_index in range(img_width):
        (r,g,b) = img_8bitchannel[rows_index][cols_index]
        r_3bit = r & 0b11100000 if r != 255 else r
        g_3bit = g & 0b11100000 if g != 255 else g
        b_3bit = b & 0b11100000 if b != 255 else b

        r_2bit = r & 0b11000000 if r != 255 else r
        g_2bit = g & 0b11000000 if g != 255 else g
        b_2bit = b & 0b11000000 if b != 255 else b

        img_3bitchannel[rows_index][cols_index] = [r_3bit,g_3bit,b_3bit]
        img_2bitchannel[rows_index][cols_index] = [r_2bit,g_2bit,b_2bit]


        if (r_3bit,g_3bit,b_3bit) not in colors_in_3bits:
            colors_in_3bits[(r_3bit,g_3bit,b_3bit)] = 0

        colors_in_3bits[(r_3bit,g_3bit,b_3bit)] = colors_in_3bits[(r_3bit,g_3bit,b_3bit)] + 1

        if (r_2bit,g_2bit,b_2bit) not in colors_in_2bits:
            colors_in_2bits[(r_2bit,g_2bit,b_2bit)] = 0

        colors_in_2bits[(r_2bit,g_2bit,b_2bit)] = colors_in_2bits[(r_2bit,g_2bit,b_2bit)] + 1
        

cv.imwrite("images/thalia-3bit-color.png", img_3bitchannel)         
cv.imwrite("images/thalia-2bit-color.png", img_2bitchannel) 

print(f"{len(colors_in_3bits)=}")
print(f"{len(colors_in_2bits)=}")

colors_3bit = [f"#{kr:02X}{kg:02X}{kb:02X}" for kr, kg, kb in colors_in_3bits.keys()]
colors_2bit = [f"#{kr:02X}{kg:02X}{kb:02X}" for kr, kg, kb in colors_in_2bits.keys()]

print(f"{colors_3bit=}")
print(f"{colors_2bit=}")
