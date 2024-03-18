# AutoDistribute

# 結論
画像認識で使うOCRエンジン Tesseract の精度が悪く、無理だった。学習させれば精度が上がるかもだけど、そこまでする気力は無い
# やろうとしたこと
それぞれの解答画像ファイル（.png or .jpg）について
1. 学籍番号の領域だけ切り取って、拡大、白黒に二値化
2. Tesseract で学籍番号を読み取って、学籍番号に対応するフォルダのパスに画像をコピー

# メモ
1. Tesseract-OCR を別途ダウンロード必要。"python-Package.txt"にある python パッケージのインストールも必要
2. Tesseract をダウンロードしても、無理にPCの環境変数"Path"に加える必要はない。python のコードにTesseract のパスを書けばOK

# 参考にしたURLページ
1. 画像を切り抜いて英字を読み取る - https://qiita.com/d_m/items/4690aa9f03bb13bf1d21
2. Tesseract エンジンの精度を高める - https://qiita.com/ku_a_i/items/93fdbd75edacb34ec610
3. Tesseract エンジンのインストール方法 - https://gammasoft.jp/blog/tesseract-ocr-install-on-windows/
4. ミリ → ピクセルの変換 - https://www.graphic.jp/comic/user_guide/px_mm_converter
5. 画像の拡大、画質向上もできるっぽい - https://note.nkmk.me/python-pillow-image-resize/
6. 

# これから参考になりそうなURL
1. DropBox のAPIの取得 - https://zerofromlight.com/blogs/detail/121/
2. DropBox へのアップロードの仕方 - https://zerofromlight.com/blogs/detail/122/ 
