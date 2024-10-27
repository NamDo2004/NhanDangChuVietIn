import numpy as np
import pytesseract
import cv2
from PIL import ImageFont, ImageDraw, Image

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("1.4.JPG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Dùng tesseract để nhận diện văn bản, trả về thông tin chi tiết văn bản
custom_config = r'--oem 3 --psm 6'
boxes = pytesseract.image_to_data(img, lang="vie", config=custom_config)
#In ra thong tin van ban
print(boxes)

#Khởi tạo chuỗi text
text = pytesseract.image_to_string(img, lang="vie")

#Chuyển chữ trên văn bản thành định dạng Unicode
pil_img = Image.fromarray(img)
draw = ImageDraw.Draw(pil_img)

#Dùng font tiếng việt
font_path = "arial.ttf"
font = ImageFont.truetype(font_path, 20)

for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        #Tại những dòng có len = 12 mới có ký tự
        if len(b) == 12:
            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            #Vẽ hcn quanh văn bản
            draw.rectangle(((x,y), (x+w,y+h)), outline="red",width=2)
            #Hiển thị văn bản lên hình ảnh, trên hình chữ nhật
            draw.text((x, y-20), b[11], font=font, fill=(50, 50, 255))

#Chuyển lại về opencv format
img_result = cv2.cvtColor(np.array(pil_img), cv2.COLOR_BGR2RGB)

# Hiển thị hình ảnh
cv2.imshow("Nhan dien", img_result)
cv2.waitKey()


# Ghi văn bản vào file
with open("dich.txt", "a", encoding="utf-8") as f:
    f.writelines(text)



# Đóng tất cả các cửa sổ
cv2.destroyAllWindows()