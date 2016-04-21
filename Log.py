# -*- coding:utf-8 -*-

# ログ出力クラス
class Log:
	# コンストラクタ
	def __init__(self):
		self.WARNING = 'WARNING'
		self.INFO = 'INFO'

	# メッセージ出力
	def output(self, prefix, message):
		print ("{0:<10}".format('[' + prefix + ']') + message)

if __name__ == '__main__':
	log = Log()
	log.output(log.INFO, 'Hello World')
	log.output(log.WARNING, 'Danger is dangerous')