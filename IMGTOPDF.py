import PIL
from PIL import Image
img=PIL.Image.open(r"C:/Users/LENOVO/Desktop/h.jpg")
pdf=img.convert('RGB')
pdf.save('p1.pdf')