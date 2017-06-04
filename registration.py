from tornado import web,ioloop
import os
from pymongo import *


class user_checkHandler(web.RequestHandler):
	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
		username = self.get_query_arguments("username")[0]
		client = MongoClient()
		db_livechat = client.livechat
		collec_login = db_livechat.login
		query  = collec_login.find_one({"username":username},{"username":1,"_id":0})
		print(query)
		if query is None:
			self.write("avaliable")
		else:
			self.write("notavaliable")


app = web.Application(
    [ (r"/register/user_check" , user_checkHandler)	],
    static_path='../static',
    debug=True
    )

app.listen(7888)
ioloop.IOLoop.current().start()
