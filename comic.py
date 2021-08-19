import imgkit

print("Usage:")
print("if a link looks like:\nhttps://tw.manhuagui.com/comic/19430/219425.html#p=2\n")
print("Then just paste\nhttps://tw.manhuagui.com/comic/19430/219425.html#p=\n")
print("And the program will loop the number and download the website screenshots\n")

ori_url = input("Feed me the link: ")
num = input("How many pages u want: ")

path_wkhtmltoimage = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe"
config = imgkit.config(wkhtmltoimage=path_wkhtmltoimage)

for i in range(int(num)):
    url = ori_url
    url += str(i+1)
    imgkit.from_url(url, 'out' + str(i+1) + '.jpg', config=config)