import imgkit

ori_url = input("比條link我: ")
num = input("想要幾多頁： ")

for i in range(num):
    url = ori_url
    url += str(i+1)
    imgkit.from_url(url, 'out' + str(i+1) + '.jpg')