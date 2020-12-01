from PIL import Image
import image_slicer
import os

# crop2()
# crop('tessttt', 'test.jpg', 100, 1260, 1, 1, '/')
def imgcrop(input, xPieces, yPieces):
    filename, file_extension = os.path.splitext(input)
    im = Image.open(input)
    imgwidth, imgheight = im.size
    height = imgheight // yPieces
    width = imgwidth // xPieces
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)
            try:
                a.save("./" + filename + "-" + str(i) + "-" + str(j) + file_extension)
            except:
                pass
imgcrop("test.jpg", 1, 82);