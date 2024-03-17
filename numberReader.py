import re
from PIL import Image, ImageOps
import pyocr
import pyocr.builders
import sys
from glob import glob

# Tesseract実行ファイルのパス
pyocr.tesseract.TESSERACT_CMD = r'C:\Users\Amano\Documents\home\Python\AutoDistribute\Tesseract-OCR\tesseract.exe'
# 切り抜く長方形の座標。左上が原点で、左、上、右、下の順。単位はミリ
kirinuki = [99, 21, 127, 33]
# ミリからピクセルへ変換する用の比例定数
dpi = 200 # スキャナによって変える
left, upper, right, lowwer = [dpi * i / 25.4 for i in kirinuki]

file_path = 'Materials/'
# 読み込むファイルリスト作成
file_list = [file for file in glob(f'{file_path}*.png')] # 拡張子に注意
for file_path in file_list:
    # ツール読み込み
    tools = pyocr.get_available_tools()
    # ツールが見付からない場合
    if len(tools) == 0:
        print('pyocrが見付かりません。pyocrをインストールして下さい。')
        sys.exit(1)
    tool = tools[0]
    # 画像読み込み
    img_org = Image.open(file_path)
    # 枚数表記部分を切り取り。座標の指定は紙の左上を原点とし、（左, 上, 右, 下）
    max_medals_img = img_org.crop((left, upper, right, lowwer))

    # 画像を拡大
    k = 3 # 拡大率
    max_medals_img = max_medals_img.resize((max_medals_img.width * k, max_medals_img.height * k), Image.LANCZOS)
    # デバッグ用
    max_medals_img.save("numHoge.png")

    # 背景色と文字色を反転（白文字→黒文字へ変換）
    # max_medals_img = ImageOps.invert(max_medals_img.convert('RGB'))
    # OCR
    max_medals = tool.image_to_string(max_medals_img, lang='eng', builder=pyocr.builders.DigitBuilder(tesseract_layout=8))
    # 数値以外の文字を除去
    max_medals = re.sub(r'\D', '', max_medals)
    print(f'{max_medals}')