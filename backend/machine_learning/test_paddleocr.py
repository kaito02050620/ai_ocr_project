#!/usr/bin/env python3
import os
import sys

# バージョン確認
try:
    from paddleocr import PaddleOCR
    import paddleocr
    print(f"PaddleOCR version: {paddleocr.__version__}")
except ImportError as e:
    print(f"PaddleOCR import error: {e}")
    sys.exit(1)

# 画像パスの確認
# img_path = "/app/machine_learning/test/general_ocr_002.png"
img_path = "/app/machine_learning/test/test_0001.jpg"
if not os.path.exists(img_path):
    print(f"画像ファイルが見つかりません: {img_path}")
    print("利用可能なファイル:")
    test_dir = "/app/machine_learning/test/"
    if os.path.exists(test_dir):
        for f in os.listdir(test_dir):
            if f.endswith(('.png', '.jpg', '.jpeg')):
                print(f"  - {f}")
    sys.exit(1)

print(f"処理対象画像: {img_path}")

try:
    # PaddleOCR初期化（日本語対応 + 軽量設定）
    print("PaddleOCR初期化中...")
    
    # バージョンに応じた初期化
    try:
        # 新しいバージョン (v3.0+) の記法
        ocr = PaddleOCR(
            use_doc_orientation_classify=False,
            use_doc_unwarping=False, 
            use_textline_orientation=False,
            lang='japan',  # 日本語指定
        )
        print("新しいPaddleOCR v3.0+で初期化完了")
        
        # 新しい記法で実行
        print("OCR処理実行中（新形式）...")
        result = ocr.predict(input=img_path)
        
        print(f"\n=== OCR結果 ===")
        for i, res in enumerate(result):
            print(f"結果 {i+1}:")
            res.print()
            
            # 出力ディレクトリ作成
            output_dir = "/app/machine_learning/output"
            os.makedirs(output_dir, exist_ok=True)
            
            # 結果保存
            res.save_to_img(output_dir)
            res.save_to_json(output_dir)
        
    except (TypeError, AttributeError) as e:
        raise e

except Exception as e:
    raise e