import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img1 = cv2.imread("sample1.jpg")
img2 = cv2.imread("sample2.jpg")

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img1 is None:
    sys.exit("Could not read the image.")

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img2 is None:
    sys.exit("Could not read the image.")

# addWeighted関数 : 2つの画像を、1つの画像へ合成するための関数。

# 第一引数(必須) : 多次元配列(numpy.ndarray)
# 第二引数(必須) : alpha。第一引数の画像へ掛け合わせる係数。
# 第三引数(必須) : 多次元配列(numpy.ndarray)
# 第四引数(必須) : beta。第三引数の画像へ掛け合わせる係数。
# 第五引数(必須) : gamma。画素の値を微調整するために利用する。
output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
cv2.imwrite('output.jpg', output)
