# 导入
from DrissionPage import Chromium
from datetime import datetime
import json
import os
import sys

def print_usage():
    print("\n=== 工具使用说明 ===")
    print("1. 本程序用于获取视频和照片")
    print("2. 支持的网站有阿里巴巴站、必应")
    print("3. 需要提前准备好阿里巴巴.txt、必应.txt两个文件")
    print("4. 如果文件不存在，程序会创建空文件并继续运行")
    print("=============================\n")

def ensure_file_exists(filename):
    if not os.path.exists(filename):
        print(f"文件 {filename} 不存在，将创建空文件")
        with open(filename, 'w', encoding='utf-8') as f:
            pass
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def get():
    current_time = datetime.now()
    prefix = f"{current_time.month}-{current_time.day}-"
    # 优化导入，只导入必要的模块
    if getattr(sys, 'frozen', False):
        import pyi_splash
        pyi_splash.close()
    
    # 确保文件存在并读取内容
    urls = ensure_file_exists('阿里巴巴站.txt')
    searchs = ensure_file_exists('必应.txt')
    
    if not urls and not searchs:
        print("警告：两个输入文件都为空，程序将退出")
        return
    
    browser = Chromium() 
    # 创建页面对象
    page = browser.latest_tab
    download = page.download
    download.set.if_file_exists('rename')
    save_path = r'阿里巴巴'
    save_path2 = r'必应'
    imgcount = 1
    videoName = searchs[0] + '-' if searchs else 'default-'
    videocount = 1
    if urls:  
        # 确保保存目录存在
        os.makedirs(save_path, exist_ok=True)
        for url in urls:
            try:
                page.get(url)
                imgs = page.eles('t:img@class=id-h-full id-w-full id-object-contain')
                for i, img in enumerate(imgs, 1):
                    img_url = img.attr('src')
                    if img_url:
                        download.add(img_url, save_path, f"{prefix}{imgcount}")
                        imgcount += 1
                video = page.ele('t:video')
                if video and video.attr('src'):
                    download.add(video.attr('src'), save_path, f"maya-{videoName}-{prefix}{videocount}")
                    videocount += 1
            except Exception as e:
                print(f"处理URL {url} 时出错: {str(e)}")
                continue

    if searchs:
        # 确保保存目录存在
        os.makedirs(save_path2, exist_ok=True)
        for search in searchs:    
            try:
                biying = f"https://cn.bing.com/images/search?q={search}&go=Search&qs=ds&form=QBIR&first=1"
                page.get(biying)
                hrefs = page.eles('tag:a@@class=iusc')
                for i, href in enumerate(hrefs, 1):
                    m = href.attr('m')
                    if m:
                        json_m = json.loads(m)
                        img_url = json_m['murl']
                        download.add(img_url, save_path2, f"{prefix}{imgcount}")
                        imgcount += 1
            except Exception as e:
                print(f"处理搜索词 {search} 时出错: {str(e)}")
                continue

if __name__ == "__main__":
    print_usage()
    confirm = input("是否开始获取图片和视频操作？(Y/N): ").strip().upper()
    if confirm != 'Y':
        print("已取消操作，程序退出。")
        exit()
    get()
    print("\n获取完成")