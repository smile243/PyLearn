import os
import cv2
import numpy as np
from PIL import Image
import argparse

def remove_watermark(image_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"无法读取图片: {image_path}")
        return None
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply threshold to create a mask
    _, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    
    # Invert the mask
    mask_inv = cv2.bitwise_not(mask)
    
    # Apply inpainting to remove watermark
    result = cv2.inpaint(img, mask_inv, 3, cv2.INPAINT_TELEA)
    
    return result

def process_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get all image files
    image_extensions = ('.jpg', '.jpeg', '.png')
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(image_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"processed_{filename}")
            
            # Process the image
            result = remove_watermark(input_path)
            if result is not None:
                # Save the processed image
                cv2.imwrite(output_path, result)
                print(f"已处理并保存: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='去除图片水印')
    parser.add_argument('--input', type=str, default='images', help='输入文件夹路径')
    parser.add_argument('--output', type=str, default='new_img', help='输出文件夹路径')
    
    args = parser.parse_args()
    
    process_images(args.input, args.output)

if __name__ == "__main__":
    main()
