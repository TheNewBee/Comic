import imgkit

ori_url = input("比條link我: ")
num = input("想要幾多頁： ")

path_wkhtmltoimage = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe"
config = imgkit.config(wkhtmltoimage=path_wkhtmltoimage)

for i in range(int(num)):
    url = ori_url
    url += str(i+1)
    imgkit.from_url(url, 'out' + str(i+1) + '.jpg', config=config)