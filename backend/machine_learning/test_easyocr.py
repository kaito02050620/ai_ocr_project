import easyocr
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import sys
import os

# 文字化け対策
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['LANG'] = 'ja_JP.UTF-8'
os.environ['LC_ALL'] = 'ja_JP.UTF-8'

reader = easyocr.Reader(['ja', 'en'], gpu=True)

# 画像読み込み
# img_path = "/app/machine_learning/test/test.png"
img_path = "/app/machine_learning/test/test_0001.jpg"
img = cv2.imread(img_path)

if img is None:
    print(f"画像読み込みエラー: {img_path}")
    exit(1)

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

results = reader.readtext(rgb_img)

img_pil = Image.fromarray(rgb_img)
draw = ImageDraw.Draw(img_pil)

# 日本語対応フォントを探す
font = None
try:
    font_paths = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    ]
    
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                font = ImageFont.truetype(font_path, 24)
                print(f"使用フォント: {font_path}")
                break
            except Exception as e:
                print(f"フォント読み込み失敗 {font_path}: {e}")
                continue
    
    if font is None:
        font = ImageFont.load_default()
        print("デフォルトフォントを使用")
        
except Exception as e:
    font = ImageFont.load_default()
    print(f"フォント読み込み警告: {e}")

for i, (bbox, text, prob) in enumerate(results):
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple([int(x) for x in top_left])
    bottom_right = tuple([int(x) for x in bottom_right])
    
    try:
        print(f"{i+1}. text: '{text}', accuracy: {prob:.3f}")
    except UnicodeEncodeError:
        text_bytes = text.encode('utf-8', errors='replace')
        print(f"{i+1}. text: {text_bytes}, accuracy: {prob:.3f}")

    if prob > 0.8:
        box_color = "lime" 
        bg_color = "lightgreen"
    elif prob > 0.5:
        box_color = "yellow"
        bg_color = "lightyellow"
    else:
        box_color = "red"
        bg_color = "lightcoral"

    draw.rectangle([top_left, bottom_right], outline=box_color, width=3)

    try:
        text_bbox = draw.textbbox(top_left, text, font=font)
        padding = 2
        draw.rectangle([
            (text_bbox[0] - padding, text_bbox[1] - padding), 
            (text_bbox[2] + padding, text_bbox[3] + padding)
        ], fill=bg_color, outline=box_color)
        
        # テキストを描画
        draw.text(top_left, f"{i+1}: {text}", fill="black", font=font)
        
    except Exception as e:
        print(f"テキスト描画エラー (項目{i+1}): {e}")
        try:
            draw.text(top_left, "?", fill="red", font=font)
        except:
            pass

# 結果保存
rgb_img = np.array(img_pil)
result_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)

# 正しいファイル名生成
output_path = os.path.splitext(img_path)[0] + "_overlay_result.png"
success = cv2.imwrite(output_path, result_img)

if success:
    print(f"output: {output_path}")
else:
    print("error")


# OCR実行結果をファイルに保存
try:
    with open(output_path.replace('.png', '_ocr_results.txt'), 'w', encoding='utf-8') as f:
        for i, (bbox, text, prob) in enumerate(results):
            f.write(f"{i+1}. text: '{text}', accuracy: {prob:.3f}\n")
            f.write(f"Python version: {sys.version}")
            f.write(f"Default encoding: {sys.getdefaultencoding()}")
            f.write(f"File system encoding: {sys.getfilesystemencoding()}")
            f.write(f"Font: {font}")
            f.write(f"LANG: {os.environ.get('LANG', 'Not set')}")
            f.write(f"LC_ALL: {os.environ.get('LC_ALL', 'Not set')}")
            f.write(f"PYTHONIOENCODING: {os.environ.get('PYTHONIOENCODING', 'Not set')}")
except Exception as e:
    raise e