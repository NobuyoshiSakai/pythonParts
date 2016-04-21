# -*- coding:utf-8 -*-

import Log

class FileOperation:

	# コンストラクタ
	def __init__(self):
		# ファイル名称
		self.fileName = ''
		# ファイルの内容
		self.contents = []
		# ファイル取得フラグ
		self.isReadFile = False
		# ログクラス
		self.log = Log.Log()
		# 行数
		self.rowCount = 0

	# ファイル名設定処理
	def setFileName(self, fileName):
		self.fileName = fileName

	# ファイルから文字列を文字配列に取得する処理
	# ファイル名が空白の場合はエラーメッセージを表示し終了する
	def doContentsOfTheFile(self):
		if not self.fileName:
			self.log.output(self.log.WARNING, 'File name is Empty')
			return
		try:
			fileObj = open(self.fileName, 'r')

			for line in fileObj:
				self.contents.append(line.rstrip('\n'))
			
			fileObj.close
		except IOError:
			self.log.output(self.log.WARNING, '"IOError" It failed to read the file: ' + self.fileName)
			return

		self.isReadFile = True
		self.rowCount = len(self.contents)
		self.log.output(self.log.INFO, 'Successful reading of the file: ' + self.fileName )
		return

	# ファイルの内容を1行取得する
	def get(self, line):
		if self.isReadFile:
			return self.contents[line]
		self.log.output(self.log.WARNING, 'You do not read the file')
		return

	# ファイルの内容をキー:値の形式に変換してディクショナリで返す
	def getContentsOfThMap(self, Separator):
		dic = {}
		rowCnt = 0
		while rowCnt < self.rowCount:
			line = self.get(rowCnt)
			lines = line.split(Separator)
			dic[lines[0]] = lines[1]

			rowCnt = rowCnt + 1
		return dic

	# 行数の出力
	def getRowCount(self):
		return self.rowCount

# test code
if __name__=="__main__":
	# ログクラス
	log = Log.Log()

	# クラス生成
	fileOpe = FileOperation()

	# ファイルから文字列を取得し文字配列に設定する
	# fileOpe.doContentsOfTheFile()

	# ファイルから1行読み込む
	# fileOpe.get(0)

	# ファイル名設定
	fileOpe.setFileName('C:\pythonLab\Parts\config.txt')

	# ファイルから文字列を取得し文字配列に設定する
	# fileOpe.doContentsOfTheFile()

	# ファイル名設定
	fileOpe.setFileName('config.txt')

	# ファイルから文字列を取得し文字配列に設定する
	fileOpe.doContentsOfTheFile()

	# ファイルの内容を出力する
	log.output(log.INFO, '------------------------------')
	rowCnt = 0
	while rowCnt < fileOpe.getRowCount():
		line = fileOpe.get(rowCnt)
		log.output(log.INFO, "{0:<3}".format(rowCnt) + ':' + line)
		rowCnt = rowCnt + 1
	config = fileOpe.getContentsOfThMap('=')
	print(config.get('sarverroot'))
	log.output(log.INFO, '------------------------------')
