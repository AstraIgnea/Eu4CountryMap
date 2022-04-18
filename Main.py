from PIL import Image
import numpy as np
#5632 x 2048
print("Paradox uses odd names for some countries internally. \nMuscowy rather than Muscovy. \nPlease bare this in mind.")
New = input("Edit existing file \ny/n\n>>>")
if New.lower() == "y":
    original = np.array(Image.open("Done.png"))
else:
    original = np.array(Image.open("Blank.png"))
mapcolours = original.reshape(int(original.size/3),1,3)
def update(nation):
    countries = open("Combination","r")
    nations = [line.split(",") for line in countries.read().split("\n")]
    info = []
    for name in nations:
        if name[0] == nation.upper():
            info = name
            break
    if info == []:
        print("Not a recognised nation")
        return()
    colour = np.array([int(info[1]),int(info[2]),int(info[3])])
    print(colour)
    for pixel in info[4:]:
        mapcolours[int(pixel)] = colour

while True:
    a = input("INPUT COUNTRY OR ENTER DONE TO FINISH\n>>>")
    if a == "DONE":
        break
    update(a)
blank = mapcolours.reshape(original.shape)
newImage = Image.fromarray(blank)
newImage.show()
newImage = newImage.save("Done.png")


