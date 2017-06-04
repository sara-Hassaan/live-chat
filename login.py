from tornado import web,ioloop
import os
from pymongo import *
#from handlers.ajax import APIHandler

class loginHandler(web.RequestHandler):
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.render("templates/login.html")
class check_userHandler(web.RequestHandler):
	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
		username =  str(self.get_query_arguments("username")[0])
		password = 	str(self.get_query_arguments("password")[0])
		client = MongoClient()
		db_livechat = client.livechat

		query  = db_livechat.login.find_one({"username":username,"password":password},{"userId":1,"_id":0})
		query  = db_livechat.user.find_one({"_id":int(query["userId"])},{"_id":1,"image":1,"userName":1})
		print(query)
		try:
			self.write(query)
		except TypeError:
			self.write("null")
class update_userHandler(web.RequestHandler):
	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
		username = self.get_query_arguments("username")
		password = self.get_query_arguments("password")
		pic      = self.get_query_arguments("pic")

		client = MongoClient()
		db_livechat = client.livechat
		collec_user= db_livechat.user
		max_id  = int(collec_user.find_one({"$query":{},"$orderby":{"_id":-1}},{"_id":1})["_id"])
		username = self.get_query_arguments("username")[0]
		password = self.get_query_arguments("password")[0]
		pic      = self.get_query_arguments("pic")[0]
		user_id = max_id+1


		dict_user={}
		dict_user["_id"] = user_id;
		dict_user["userName"] = username;
		dict_user["image"] = pic;
		dict_user["friend"] = [];
		print(dict_user)

		dict_login={}
		dict_login["userId"] = user_id
		dict_login["username"] = username
		dict_login["password"] = password

		print(dict_login)

		dict_stat ={}
		dict_stat["userId"] = user_id
		dict_stat["stat"] = 1

		print(dict_stat)

		res1 = db_livechat.user.insert_one(dict_user)
		res2 = db_livechat.login.insert_one(dict_login)
		res3 = db_livechat.stat.insert_one(dict_stat)

		self.write(str(user_id)+":success")



app = web.Application(
    [(r"/update_user",update_userHandler),(r"/", loginHandler) , (r"/check_user" , check_userHandler) , 	],
    static_path='static',
    debug=True
    )

app.listen(9888)
ioloop.IOLoop.current().start()
