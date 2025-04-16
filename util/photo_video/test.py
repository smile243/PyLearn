# 导入
from DrissionPage import Chromium
import json

with open('阿里巴巴站.txt', 'r', encoding='utf-8') as f:
    urls = [line.strip() for line in f.readlines()]

browser = Chromium() 
# 创建页面对象
page = browser.latest_tab
download = page.download
download.set.if_file_exists('rename')
save_path = r'阿里巴巴'
save_path2 = r'必应'
imgcount = 1
videoName = 'maya-die casting-'
videocount = 1
for url in urls:
    page.get(url)
    imgs = page.eles('t:img@class=id-h-full id-w-full id-object-contain')
    for i, img in enumerate(imgs, 1):
        img_url = img.attr('src')
        if img_url:
            download.add(img_url,save_path,f"{imgcount}")
            imgcount+=1
    video = page.ele('t:video')
    if video:
         download.add(video.attr('src'),save_path,f"{videoName}{videocount}")
         videocount+=1;

with open('必应.txt', 'r', encoding='utf-8') as f:
    searchs = [line.strip() for line in f.readlines()]
for search in searchs:    
    biying = f"https://cn.bing.com/images/search?q={search}&go=Search&qs=ds&form=QBIR&first=1"
    page.get(biying)
    hrefs = page.eles('tag:a@@class=iusc')
    for i,href in enumerate(hrefs, 1):
        m = href.attr('m')
        json_m =json.loads(m);
        img_url = json_m['murl'];
        download.add(img_url,save_path2,f"{imgcount}")
        imgcount+=1     