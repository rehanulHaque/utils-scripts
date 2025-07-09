import sys
from PIL import Image

image_path = sys.argv[1]
quality = int(sys.argv[2])

if(quality > 100 or quality < 1):
    print("Quality should be between 1 and 100")
    exit(1)

def compressImage(image, quality):
    img = Image.open(image)
    img.save(f"{image_path.split('.')[0]}_compressed.jpg", optimize=True, quality=quality)
    print("Image Compressed")


compressImage(image_path, quality)