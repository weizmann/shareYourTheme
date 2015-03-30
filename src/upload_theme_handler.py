import tornado.web
import os

class ThemeInfoBundle(object):
	def __init__(self, user_account_info, bg_image_file, theme_config):


class UploadThemeManager(object):
	def uploadTheme(self, theme_info_bundle):

	def saveFile(self, theme_file):
		
	def recordAccountInfo(self, account_info)

	def recordUploadOperation(self, upload_operation_info):

	#TODO:
	def checkFile(self, file_name):

class UploadThemeHandler(tornado.web.RequestHandler):
	def __init__(self):
		super(self)
		_uploadThemeManager = UploadThemeManager()

	def post(self):
		bg_image_file = self.request.files['file'][0]
		theme_config = self.request.argument['theme_config']
		user_account_info = self.request.argument['user_account_info']
		_uploadThemeManager.uploadTheme(ThemeInfoBundle(user_account_info, 
					bg_image_file, theme_config))
