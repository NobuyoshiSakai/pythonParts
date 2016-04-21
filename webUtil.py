# -*- coding:utf-8 -*-
# -----------------------------
# parts読み込み
# -----------------------------
import sys
import os
sys.path.append("C:\pythonLab\save\Parts")

# -----------------------------
# import
# -----------------------------
import FileOperation
import Log

# ライブラリの読込
from selenium import webdriver

# Back_Space用
from selenium.webdriver.common.keys import Keys

# 待つためのライブラリ
import time

class webUtil:
	# コンストラクタ
	def __init__(self):
		# ドライバの生成
		self.driver = webdriver.Firefox()
		# driver = webdriver.Ie()

		# ログクラス
		self.log = Log.Log()

	# -----------------------------
	# サーバーファイルを読み込む
	# @filename ファイル名
	# -----------------------------
	def readFile(self, filename):
		# サーバーファイルの読込
		fopServer = FileOperation.FileOperation()	# サーバー設定ファイル
		fopServer.setFileName(filename)
		fopServer.doContentsOfTheFile()
		serverMap = fopServer.getContentsOfThMap('=')
		return serverMap

	# -----------------------------
	# 読み込んだファイルを表示する
	# @filename ファイル名
	# -----------------------------
	def readFilePrint(self, setupmap, filename):
		self.log.output(self.log.INFO, 'The contents display of loaded setup file :' + filename)
		for name, value in setupmap.items():
			self.log.output(self.log.INFO, name + ' = ' + value)

	# -----------------------------
	# imgファイル保存ディレクトリ作成処理
	# @folder フォルダ名称
	# -----------------------------
	def checkMsgDir(self, folder='img'):
		# img保存用のディレクトリの存在チェクを実施する
		# 存在しない場合は、作成する
		if os.path.exists(folder) == False:
			os.mkdir(folder)
			self.log.output(self.log.INFO, 'create folder :' + folder)

	# -----------------------------
	# urlへアクセスする
	# @url      アクセスURL
	# @time_    タイムアウト秒
	# @filename スクリーンショットファイル番号
	# -----------------------------
	def access(self, url, time_=1, filename= -1):
		self.driver.get(url)
		self.screen(time_=time_, filename=filename, msg='access:' + url)
		return self.driver
	
	# -----------------------------
	# WEB業務へログインする
	# @url      アクセスURL
	# @time_    タイムアウト秒
	# @filename スクリーンショットファイル番号
	# -----------------------------
	def login(self, url='http://localhost:8080/webtops2/', userName='j_username', userValue='44902', passName='j_password', passValue='KN500630', time_=1, filename= -1):

		# ログインページへアクセスする
		self.access(url=url)

		# ---------------------------------------------------------------------------
		# 社員コードを指定
		self.inputName(name=userName, value=userValue)

		# パスワードを指定
		self.inputName(name=passName, value=passValue)

		# ---------------------------------------------------------------------------
		# ログイン
		self.submitName('login', time_=time_, filename=filename)

	# -----------------------------
	# nameに該当するテキストボックスにvalueを設定する
	# @name     タグのname
	# @value    文字列
	# @length   文字列の長さ
	# @script   実行Javascript
	# @time_    タイムアウト秒
	# @filename スクリーンショットファイル番号
	# -----------------------------
	def inputName(self, name, value, length=0, script='', time_=1, filename= -1):
		idElem = self.driver.find_element_by_name(name)

		# lengthに入力がある場合は、length分BSしてからvalueを入力する
		if length > 0:
			idElem.send_keys(Keys.BACK_SPACE * length) # 15文字削除
		idElem.send_keys(value)

		# スクリプトに入力がある場合は、実行する
		if script:
			self.driver.execute_script(script)

		# SSを撮影する
		self.screen(time_=time_, filename=filename, msg= name + ' = ' + value)
	
	# -----------------------------
	# nameに該当するチェックボックスをクリックする
	# @name     タグのname
	# @time_    タイムアウト秒
	# @filename スクリーンショットファイル番号
	# -----------------------------
	def checkName(self, name, time_=1, filename = -1):
		elem = self.driver.find_element_by_name(name)
		elem.click()

		# SSを撮影する
		self.screen(time_=time_, filename=filename, msg= name + ' = click()')

	# -----------------------------
	# コンボボックスの内容を変更する
	# @name     タグのname
	# @value    タグの値
	# @script   実行Javascript
	# @time_    タイムアウト秒
	# @filename スクリーンショットファイル番号
	# -----------------------------
	def combName(self, name, value, script='', time_=1, filename= -1):
		from selenium.webdriver.support.ui import Select
		Select(self.driver.find_element_by_name(name)).select_by_visible_text(value)

		# スクリプトに入力がある場合は、実行する
		if script:
			self.driver.execute_script(script)

		# SSを撮影する
		self.screen(time_=time_, filename=filename, msg='change conbobox')

	# -----------------------------
	# スクリプトを実行する
	# @script   実行Javascript
	# @time_    タイムアウト秒
	# @filename スクリーンショットファイル番号
	# -----------------------------
	def execScript(self, script, time_=1, filename= -1):
		if script:
			self.driver.execute_script(script)

			# SSを撮影する
			self.screen(time_=time_, filename=filename, msg='exec ' + script)

	# -----------------------------
	# valueに該当するリンクをクリックする
	# @script   実行Javascript
	# @time_    タイムアウト秒
	# @filename スクリーンショットファイル番号
	# -----------------------------
	def clickLink(self, value='', time_=1, filename= -1):
		if value:
			self.driver.find_element_by_link_text(value).click()

			# SSを撮影する
			self.screen(time_=time_, filename=filename, msg='click ' + value)

	# -----------------------------
	# サブミット処理を行う
	# @time_    タイムアウト秒
	# @filename スクリーンショットファイル番号
	# @name     タグのname
	# -----------------------------
	def submitName(self, name, time_=1, filename= -1):
		btElem = self.driver.find_element_by_name(name)
		btElem.submit()

		# SSを撮影する
		self.screen(time_=time_, filename=filename, msg='submit ' + name)
	# -----------------------------
	# SS撮影処理
	# @folder   SS保存場所
	# @time_    タイムアウト秒
	# @filename スクリーンショットファイル番号
	# -----------------------------
	def screen(self, folder='img\\', time_=1, filename= -1, msg=''):
		if filename >= 0:
			time.sleep(time_)
			self.driver.save_screenshot(folder + str(filename) + ".jpg")
			self.log.output(self.log.INFO, 'create ss is ' + str(filename) + ".jpg" + " :"+msg)

	# -----------------------------
	# SS保存場所名称変更
	# -----------------------------
	def changeFolder(self, folder='img\\'):
		import dircache
		file_list=dircache.listdir('.')
		maxcnt = 0
		for file in file_list:
			if file.find('img_') >= 0:
				cnt = file.strip('img_')
				if int(cnt) > maxcnt :
					maxcnt = int(cnt)
		maxcnt = maxcnt + 1
		os.rename(folder, 'img_' + str(maxcnt))
		self.log.output(self.log.INFO, 'change folder name img_' + str(maxcnt))

	def closeDriver(self):
		self.driver.close()
		self.log.output(self.log.INFO, 'driver close')
