import re
from PIL import Image, ImageOps
import pyocr
import pyocr.builders
import sys
from glob import glob
import os

# Tesseract実行ファイルのパス
# pyocr.tesseract.TESSERACT_CMD = r'C:\Users\Amano\Documents\home\Python\AutoDistribute\Tesseract-OCR\tesseract.exe'
pyocr.tesseract.TESSERACT_CMD = r'C:\Users\dmura\Documents\home\Programming\AutoDistribute\Tesseract-OCR\tesseract.exe'

i = 1
file_path = 'Tesseract-testMaterials/'
# 読み込むファイルリスト作成
file_list = [file for file in glob(f'{file_path}*.png')] # 拡張子に注意。jpgも出来た
for file_path in file_list:
    # ツール読み込み
    tools = pyocr.get_available_tools()
    # ツールが見付からない場合
    if len(tools) == 0:
        print('pyocrが見付かりません。pyocrをインストールして下さい。')
        sys.exit(1)
    tool = tools[0]
    # 画像読み込み
    max_medals_img = Image.open(file_path)

    # 画像を拡大
    k = 3 # 拡大率
    max_medals_img = max_medals_img.resize((max_medals_img.width * k, max_medals_img.height * k), Image.LANCZOS)
    # 画像を二値化
    max_medals_img = max_medals_img.convert("L") # グレイスケールに変換
    threshold = 220 # 二値化の閾値
    binary_image = max_medals_img.point(lambda x: 255 if x > threshold else 0, '1')
    max_medals_img = binary_image

    # デバッグ用
    max_medals_img.save("hoge" + str(i) + ".png")
    print("hoge" + str(i) + " - ")
    i += 1

    # OCR
    max_medals = tool.image_to_string(max_medals_img, lang='eng', builder=pyocr.builders.DigitBuilder(tesseract_layout=8))
    # 数値以外の文字を除去
    max_medals = re.sub(r'\D', '', max_medals)
    print(f'{max_medals}')