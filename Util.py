# -*- coding:utf-8 -*-
import Log      # Logファイル
import os.path
import datetime # datetimeモジュールのインポート

# 文字列操作クラス
class String:
	def __init__(self):
		pass

	# ファイル名取得関数
	def getFileName(self, path):
		return os.path.basename(path)

	# ディレクトリ名取得関数
	def getPathName(self, path):
		return os.path.dirname(path)

	# ファイル名から拡張子を除いた名称を取り出す
	def getName(self, filename):
		sep = filename.split('.')
		return sep[0]

# 時間操作
class Date:
	def __init__(self):
		self.d = datetime.datetime.today()

	def getYM(self):
		return str(self.d.strftime("%Y%m"))

	def getYMD(self):
		return str(self.d.strftime("%Y%m%d"))

if __name__ == "__main__":
	log = Log.Log()
	log.output(log.INFO, 'Dateクラステスト')
	date = Date()
	log.output(log.INFO, date.getYM())
	log.output(log.INFO, date.getYMD())
