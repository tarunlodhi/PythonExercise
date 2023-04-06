import PIL
from PIL import Image
img = PIL.Image.open("C:/Users/Msft/Downloads/1.jpg") # type: ignore
width,height=img.size
print(width,"x",height)