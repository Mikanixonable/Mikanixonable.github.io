import glob
import os
import codecs
from PIL import Image
# import pandas as pd
import csv
import extcolors

# deskPath = "./Mikanixonable.github.io/"
deskPath = "./"


nums = [int(os.path.splitext(os.path.basename(png))[0]) for png in glob.glob(deskPath + "illusts/*.png")]
def makeCSV(filename,nums):
    illustRange = (min(nums), max(nums))
    csvPath = deskPath + "json/" + filename
    with open(csvPath, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(illustRange[0],illustRange[1]+1):
            imgPath = deskPath + "illusts/" + str(i) + ".png"
            img = Image.open(imgPath)

            limit = 15
            colors, pixelCount = extcolors.extract_from_image(img.resize((256,256)), tolerance = 12, limit = limit)
            colorCodes = ['#{:02x}{:02x}{:02x}'.format(*rgb[0]) for rgb in colors]
            colorRates = [rgb[1] for rgb in colors]
            while len(colorCodes)<limit:
                colorCodes.append(colorCodes[len(colorCodes)-1])

           #meta
            writer.writerow([
                i,
                img.height,
                img.width,
                os.path.getsize(imgPath),
                colorCodes,
                [colorRate/pixelCount for colorRate in colorRates]
                ])
            print(i)

makeCSV("yy2.csv",nums)