import tesserocr
from PIL import Image
image=Image.open('/home/tarena/1904/word007/word007/img_code/full/e3c8a581cceb896c8298fb56ff1b73f25bfab19c.jpg')
image=image.convert("L")
threshold=80
table=[]
for i in range(256):
    if i <threshold:
        table.append(0)
    else:
        table.append(1)
image=image.point(table,'1')
image.show()
print(tesserocr.image_to_text(image))