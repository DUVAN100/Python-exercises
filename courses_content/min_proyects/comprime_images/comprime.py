from PIL import Image 
import os
downloadsFolder = "./images/name.jpg"
"""
if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)
        if extension in [".jpg", ".jpeg", ".png"]:
            print("enter", downloadsFolder + filename)
            picture = Image.open(downloadsFolder + filename)
            print("picture ",picture)
            picture.save(downloadsFolder + "compressed_"+filename, optimize=True, quality=60)"""

def compress_image(input_file, output_file, format, quality):
    try:
        image = Image.open(input_file)
        image.save(output_file, format=format, quality=quality)
    except Exception as ex:
        print("ERROR", ex)
compress_image(downloadsFolder, "compressed_image.jpg", "JPEG", 50)