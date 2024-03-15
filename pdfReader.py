# このコード例は、Python でスキャンされた PDF ドキュメントからテキストを認識して抽出する方法を示します。
import aspose.ocr as ocr

# OCRエンジンの初期化
api = ocr.AsposeOcr()

# 認識設定の初期化
settings = ocr.RecognitionSettings()
settings.auto_denoising = True
settings.auto_contrast = True

# ファイルを認識バッチに追加します
files = ocr.OcrInput(ocr.InputType.PDF)

# スキャンした PDF にアクセスし、ページ番号と総ページ数を設定します
files.add("C:\\Files\\sample.pdf", 0, 1)

# テキストを認識する
result = api.recognize(files , settings)

# 認識結果を印刷する
print(result[0].recognition_text)
