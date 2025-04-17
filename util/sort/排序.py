import os
import glob
from pathlib import Path
from datetime import datetime

current_time = datetime.now()
prefix = f"{current_time.month}-{current_time.day}-";

def print_usage():
    print("\n=== 工具使用说明 ===")
    print("1. 本程序用于重命名当前目录下的所有图片文件")
    print("2. 支持的图片格式：jpg、jpeg、png、gif、bmp")
    print("3. 重命名规则：当前月日 + 数字序号 + 原扩展名")
    print("   例如：当前是2025/4/17, 会生成4-17-1.jpg, 4-17-2.png 等")
    print("4. 重命名过程不可逆，请谨慎操作")
    print("=============================\n")

def rename_images():
    # 获取当前目录下的所有图片文件
    image_extensions = ('*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp')
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob.glob(ext))
    
    # 按文件名排序
    image_files.sort()
    
    # 重命名文件
    for i, old_name in enumerate(image_files, 1):
        # 获取文件扩展名
        ext = os.path.splitext(old_name)[1]
        # 构建新文件名
        new_name = f"{prefix}{i}{ext}"
        print(new_name)
        try:
            os.rename(old_name, new_name)
            print(f"Renamed: {old_name} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {old_name}: {str(e)}")

if __name__ == "__main__":
    print_usage()
    
    confirm = input("是否开始重命名操作？(Y/N): ").strip().upper()
    if confirm != 'Y':
        print("已取消操作，程序退出。")
        exit()
    rename_images()
    print("\n重命名完成！")