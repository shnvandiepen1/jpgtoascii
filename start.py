from PIL import Image
from PIL import ImageSequence

im = Image.open("psv.png").convert("L")

txt_list = []

def ascinize(image_to_transform):
    for x in range(image_to_transform.width):
        row_list = []
        txt_list.append(row_list)
        for y in range(image_to_transform.height):
            zz = image_to_transform.getpixel((x,y))
            if zz < 25:
                row_list.append("@")
            if zz < 50 and zz >= 25:
                row_list.append("%")
            if zz >= 50 and zz < 75:
                row_list.append("#")
            if zz >= 75 and zz < 100:
                row_list.append("*")
            if zz >= 100 and zz < 125:
                row_list.append("+")
            if zz >= 125 and zz < 150:
                row_list.append("=")
            if zz >= 150 and zz < 175:
                row_list.append("-")
            if zz >= 175 and zz < 200:
                row_list.append(":")
            if zz >= 200 and zz < 225:
                row_list.append(".")
            if zz >= 225:
                row_list.append(" ")

ascinize(im)

print(im.width)
print(im.height)

def to_txt(listie):
    f = open("out.txt", "w+")
    for i in range(len(listie)):
        for j in range(len(listie[i])):
            f.write(listie[i][j])
        f.write("\n")


to_txt(txt_list)
