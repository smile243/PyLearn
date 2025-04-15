# 导入
from DrissionPage import ChromiumPage  

with open('网址.txt', 'r', encoding='utf-8') as f:
    urls = [line.strip() for line in f.readlines()]

# 创建页面对象
page = ChromiumPage()
download = page.download
download.set.if_file_exists('rename')
save_path = r'video'
imgName = 'maya-decanting-'
imgcount = 1
videoName = 'video-'
videocount = 1

for url in urls:
    page.get(url)
    imgs = page.eles('t:img@class=id-h-full id-w-full id-object-contain')
    for i, img in enumerate(imgs, 1):
        img_url = img.attr('src')
        if img_url:
            download.add(img_url,save_path,f"{imgName}{imgcount}")
            imgcount+=1
    video = page.ele('t:video')
    if video:
         download.add(video.attr('src'),save_path,f"{videoName}{videocount}")
         videocount+=1;
