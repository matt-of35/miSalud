from PIL import Image, ImageDraw, ImageFont
import os

sizes = [72, 96, 128, 144, 152, 192, 384, 512]

for size in sizes:
    img = Image.new('RGB', (size, size), color='#1D9E75')
    draw = ImageDraw.Draw(img)
    
    # Rounded feel via circle background
    margin = int(size * 0.12)
    draw.rounded_rectangle([margin, margin, size-margin, size-margin], 
                           radius=int(size*0.22), fill='#085041')
    
    # Cross / medical symbol
    cx, cy = size // 2, size // 2
    arm = int(size * 0.22)
    thick = int(size * 0.10)
    draw.rounded_rectangle([cx-thick, cy-arm, cx+thick, cy+arm], radius=thick//2, fill='white')
    draw.rounded_rectangle([cx-arm, cy-thick, cx+arm, cy+thick], radius=thick//2, fill='white')
    
    img.save(f'/home/claude/miSalud/icons/icon-{size}x{size}.png')
    print(f'Created icon-{size}x{size}.png')

print('All icons generated')
