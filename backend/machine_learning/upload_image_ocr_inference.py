# torchをまずインストール。GPUありの場合は適宜、自分の環境にあったバージョンを入れる
# !pip3 install torch torchvision torchaudio
# !pip install easyocr pillow opencv-python

import easyocr
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# EasyOCR初期化（日本語(ja)と英語(en)を指定するとよい）
# options -> https://www.jaided.ai/easyocr/documentation/
reader = easyocr.Reader(['ja', 'en'])

# 画像を読み込む(今回用意した画像を読み込む、使わないほうをコメントアウト)
img_path = "/app/machine_learning/test/test.png"
#img_path = "ocr_test_sample_handwritten.png"
img = cv2.imread(img_path)
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# OCRの実行
results = reader.readtext(rgb_img)

# 日本語フォントのパスを指定
# Windowsは下記、他OSは適宜設定
# font_path = 'C:/Windows/Fonts/msgothic.ttc'
# font = ImageFont.truetype(font_path, 20)  # 日本語フォントを指定

# 画像に(バウンディングボックスと)テキストを描画(見やすさのため白画像に文字を置いていく感じで実装)
#img_pil = Image.fromarray(rgb_img) # 上書きしたい場合
img_pil = Image.fromarray(np.full_like(rgb_img, 255))  # rgb_img
draw = ImageDraw.Draw(img_pil)
for (bbox, text, prob) in results:
    # バウンディングボックスの座標を取得
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple([int(x) for x in top_left])
    bottom_right = tuple([int(x) for x in bottom_right])
    # check
    #print(text, bbox)
    # バウンディングボックス + テキストの描画(日本語OK)
    #draw.rectangle([top_left, bottom_right], outline="green", width=2)
    draw.text(top_left, text,  fill=(255, 0, 0))  # テキストを描画

# 結果画像を保存(Pillow -> cv2)
rgb_img = np.array(img_pil)
result_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR) #RGB2BGR
cv2.imwrite(img_path.split(".")[0] + "_easyocr_result.png", result_img)
